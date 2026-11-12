#!/bin/bash
# Lints the files that enforce security in this repository. Used by CI (the
# required "verify" check) and by Claude before committing changes to hooks,
# scripts, workflows or the tool lock. Read-only.
#
# Usage: bash scripts/lint.sh
# Needs shellcheck and yamllint on PATH (installed by the cloud setup script,
# and in CI from tools/lint-requirements.lock). Exit 0 means clean.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 2
fails=0
step() { printf '== %s\n' "$1"; }
bad() { printf 'FAIL  %s\n' "$1"; fails=$((fails + 1)); }

# A bug in a hook can make it fail open, so warnings count as failures.
step "shellcheck (hooks and scripts)"
if command -v shellcheck >/dev/null; then
  shellcheck -S warning .claude/hooks/*.sh scripts/*.sh || bad "shellcheck reported problems"
else
  bad "shellcheck not installed"
fi

step "yamllint (workflows and Dependabot config)"
if command -v yamllint >/dev/null; then
  yamllint --strict -c .yamllint.yml .github/ || bad "yamllint reported problems"
else
  bad "yamllint not installed"
fi

# Every line pins one exact version and at least one SHA-256 digest, so
# pip --require-hashes cannot fall back to an unpinned download.
step "tools/lint-requirements.lock format"
if [ ! -s tools/lint-requirements.lock ]; then
  bad "tools/lint-requirements.lock missing or empty"
elif grep -nvE '^[a-z0-9][a-z0-9._-]*==[A-Za-z0-9.+!-]+( --hash=sha256:[0-9a-f]{64})+$' tools/lint-requirements.lock; then
  bad "lock lines above are not 'name==version --hash=sha256:<64 hex>'"
fi

if [ "$fails" -eq 0 ]; then echo "Lint passed."; else echo "$fails lint step(s) failed."; exit 1; fi
