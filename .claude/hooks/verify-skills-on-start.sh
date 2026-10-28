#!/usr/bin/env bash
# SessionStart: re-verify every installed skill against skills-lock.json before
# the agent can act on it. On failure, warn the user and instruct the agent not
# to invoke project skills. Never blocks startup (a broken check must not lock
# the user out); it reports instead.

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

if ! command -v node >/dev/null 2>&1; then
  echo '{"systemMessage":"zero-trust: node not found, so skill integrity was NOT verified this session."}'
  exit 0
fi

if out="$(node scripts/verify-skills.mjs --quiet 2>&1)"; then
  exit 0
fi

msg="$(printf '%s' "$out" | tr '\n' ' ' | tr -d '\\"' | cut -c1-900)"
printf '{"systemMessage":"SKILL INTEGRITY CHECK FAILED: %s","hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"SECURITY ALERT: skill integrity verification failed at session start (%s). Do not invoke any project skill until the user reviews the change and re-locks it. Tell the user about this before doing anything else."}}\n' "$msg" "$msg"
exit 0
