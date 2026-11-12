#!/usr/bin/env bash
# SessionStart: re-verify every installed skill against skills-lock.json before
# the agent can act on it. On failure, warn the user and instruct the agent not
# to invoke project skills. In cloud sessions, also confirm the environment's
# setup controls (scripts/check-cloud-env.sh). Never blocks startup (a broken
# check must not lock the user out); it reports instead. Silent when all pass.

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

clean() { printf '%s' "$1" | tr '\n' ' ' | tr -d '\\"' | cut -c1-700; }
skills_msg=""
env_msg=""

if ! command -v node >/dev/null 2>&1; then
  echo '{"systemMessage":"zero-trust: node not found, so skill integrity was NOT verified this session."}'
  exit 0
fi

if ! out="$(node scripts/verify-skills.mjs --quiet 2>&1)"; then
  skills_msg="$(clean "$out")"
fi

# Cloud only: the setup script never runs on a local machine.
if [ "${CLAUDE_CODE_REMOTE:-}" = "true" ] && [ -f scripts/check-cloud-env.sh ]; then
  if ! out="$(bash scripts/check-cloud-env.sh --quiet --skip-skills 2>&1)"; then
    env_msg="$(clean "$out")"
  fi
fi

[ -z "$skills_msg" ] && [ -z "$env_msg" ] && exit 0

system=""; context=""
if [ -n "$skills_msg" ]; then
  system="SKILL INTEGRITY CHECK FAILED: $skills_msg "
  context="SECURITY ALERT: skill integrity verification failed at session start ($skills_msg). Do not invoke any project skill until the user reviews the change and re-locks it. Tell the user about this before doing anything else. "
fi
if [ -n "$env_msg" ]; then
  system="${system}CLOUD ENVIRONMENT CHECK FAILED: $env_msg"
  context="${context}The cloud environment check (scripts/check-cloud-env.sh) failed: $env_msg Tell the user which checks failed before starting other work, and do not change the environment to fix it without their approval."
fi
printf '{"systemMessage":"%s","hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}\n' "$system" "$context"
exit 0
