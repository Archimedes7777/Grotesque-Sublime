#!/bin/bash
# Confirms that the cloud environment setup script (docs/environments.md,
# section 3.4) ran and that its controls are in place. Read-only: it changes
# nothing and prints no environment variable values.
#
# Usage, from the repository root in a fresh cloud session:
#   bash scripts/check-cloud-env.sh
# Exit 0 means every check passed.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV=/opt/lint-tools
fails=0
pass() { printf 'PASS  %s\n' "$1"; }
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

# 3. Pinned tools at the expected versions
check_version() { # label, expected substring, command...
  local label=$1 want=$2; shift 2
  local got
  got="$("$@" 2>/dev/null | head -1)"
  if [[ "$got" == *"$want"* ]]; then pass "$label $want"; else fail "$label: expected $want, got '${got:-missing}'"; fi
}
if command -v shellcheck >/dev/null; then pass "shellcheck installed"; else fail "shellcheck missing"; fi
check_version yamllint "1.38.0" yamllint --version
check_version pip-audit "2.10.1" pip-audit --version
check_version markdownlint-cli2 "v0.24.0" markdownlint-cli2 --help

# 4. The venv holds exactly the hash-locked packages, nothing more or less
normalize() { # PEP 503 name normalization, version left as is
  awk -F'==' '{ n = tolower($1); gsub(/[-_.]+/, "-", n); print n "==" $2 }' | sort
}
if [ -f "$VENV/requirements.lock" ] && [ -x "$VENV/bin/pip" ]; then
  want="$(cut -d' ' -f1 "$VENV/requirements.lock" | normalize)"
  have="$("$VENV/bin/pip" freeze --all 2>/dev/null | normalize)"
  if [ "$want" = "$have" ]; then
    pass "venv matches requirements.lock ($(echo "$want" | wc -l) packages)"
  else
    fail "venv differs from requirements.lock:"
    diff <(echo "$want") <(echo "$have") | grep '^[<>]' | sed 's/^/        /'
  fi
else
  fail "venv or requirements.lock missing at $VENV"
fi

# 5. Skill integrity (same check as CI and the SessionStart hook)
if node "$ROOT/scripts/verify-skills.mjs" >/dev/null 2>&1; then
  pass "skills match skills-lock.json"
else
  fail "skill integrity check failed: run node scripts/verify-skills.mjs"
fi

echo
if [ "$fails" -eq 0 ]; then
  echo "All cloud environment checks passed."
else
  echo "$fails check(s) failed. Do not use project skills until resolved."
  exit 1
fi
