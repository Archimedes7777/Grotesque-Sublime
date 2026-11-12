#!/bin/bash
# Confirms that the cloud environment setup script (docs/environments.md,
# section 3.4) ran and that its controls are in place. Read-only: it changes
# nothing and prints no environment variable values.
#
# Usage, from the repository root in a cloud session:
#   bash scripts/check-cloud-env.sh [--quiet] [--skip-skills]
#     --quiet        print only failures (the SessionStart hook uses this)
#     --skip-skills  skip check 6 when the caller already ran verify-skills
# Exit 0 means every check passed. The SessionStart hook runs it in cloud
# sessions only (CLAUDE_CODE_REMOTE=true); on a local machine most checks
# would fail by design, because the setup script never ran there.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV=/opt/lint-tools
REPO_LOCK="$ROOT/tools/lint-requirements.lock"
PROBE_URL=https://example.com/   # IANA-reserved; never on the allowlist
quiet=0; skip_skills=0
for arg in "$@"; do
  case "$arg" in
    --quiet) quiet=1 ;;
    --skip-skills) skip_skills=1 ;;
    *) echo "unknown option: $arg" >&2; exit 2 ;;
  esac
done
fails=0
pass() { [ "$quiet" -eq 1 ] || printf 'PASS  %s\n' "$1"; }
fail() { printf 'FAIL  %s\n' "$1"; fails=$((fails + 1)); }

# 1. npm install scripts are off by default
if [ "$(npm config get ignore-scripts 2>/dev/null)" = "true" ]; then
  pass "npm ignore-scripts is true"
else
  fail "npm ignore-scripts is not true"
fi

# 2. Standing security instructions are loaded for Claude
if head -1 "${HOME:-/root}/.claude/CLAUDE.md" 2>/dev/null \
    | grep -qx '# Security rules for this environment'; then
  pass "user CLAUDE.md security rules present"
else
  fail "user CLAUDE.md security rules missing"
fi

# 3. Lint tools present, at the versions the repository lock pins
pinned() { sed -n "s/^$1==\([^ ]*\) .*/\1/p" "$REPO_LOCK" 2>/dev/null; }
check_version() { # label, expected version, command...
  local label=$1 want=$2; shift 2
  local got
  got="$("$@" 2>/dev/null | head -1)"
  if [ -n "$want" ] && [[ "$got" == *"$want"* ]]; then
    pass "$label $want"
  else
    fail "$label: expected ${want:-a version from $REPO_LOCK}, got '${got:-missing}'"
  fi
}
if command -v shellcheck >/dev/null; then pass "shellcheck installed"; else fail "shellcheck missing"; fi
check_version yamllint "$(pinned yamllint)" yamllint --version
check_version pip-audit "$(pinned pip-audit)" pip-audit --version

# 4. The environment's lock is the repository's lock, and the venv holds
#    exactly those packages, nothing more or less
normalize() { # PEP 503 name normalization, version left as is
  awk -F'==' '{ n = tolower($1); gsub(/[-_.]+/, "-", n); print n "==" $2 }' | sort
}
if [ ! -f "$REPO_LOCK" ]; then
  fail "repository lock missing: $REPO_LOCK"
elif [ ! -f "$VENV/requirements.lock" ] || [ ! -x "$VENV/bin/pip" ]; then
  fail "venv or requirements.lock missing at $VENV"
else
  if cmp -s "$VENV/requirements.lock" "$REPO_LOCK"; then
    pass "environment lock matches tools/lint-requirements.lock"
  else
    fail "environment lock differs from tools/lint-requirements.lock: update the setup script (docs/environments.md 3.4)"
  fi
  want="$(cut -d' ' -f1 "$VENV/requirements.lock" | normalize)"
  have="$("$VENV/bin/pip" freeze --all 2>/dev/null | normalize)"
  if [ "$want" = "$have" ]; then
    pass "venv matches its lock ($(echo "$want" | wc -l) packages)"
  else
    fail "venv differs from its lock:"
    diff <(echo "$want") <(echo "$have") | grep '^[<>]' | sed 's/^/        /'
  fi
fi

# 5. Network policy is still Limited: a host outside the allowlist must be
#    refused by the egress proxy (CONNECT 403) before any connection leaves.
#    A success here means the environment was switched to unrestricted.
code="$(curl -sS -o /dev/null --max-time 5 -w '%{http_code}' "$PROBE_URL" 2>/dev/null)"
rc=$?
if [ "$rc" -eq 0 ] && [[ "$code" =~ ^[23] ]]; then
  fail "network: $PROBE_URL answered HTTP $code, so the environment is not Limited"
else
  pass "network: non-allowlisted host refused (curl exit $rc)"
fi

# 6. Skill integrity (same check as CI and the SessionStart hook)
if [ "$skip_skills" -eq 0 ]; then
  if node "$ROOT/scripts/verify-skills.mjs" >/dev/null 2>&1; then
    pass "skills match skills-lock.json"
  else
    fail "skill integrity check failed: run node scripts/verify-skills.mjs and do not use project skills"
  fi
fi

if [ "$fails" -eq 0 ]; then
  [ "$quiet" -eq 1 ] || printf '\nAll cloud environment checks passed.\n'
else
  printf '\n%s cloud environment check(s) failed.\n' "$fails"
  exit 1
fi
