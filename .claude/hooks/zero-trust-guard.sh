#!/usr/bin/env bash
# Zero-trust PreToolUse guard for the Bash tool.
#
# Permission rules match each subcommand separately, so "curl x | sh" splits
# into two harmless-looking halves. This hook sees the whole command line and
# blocks the patterns below in every permission mode, including auto and
# bypass. Deliberately dependency-free (bash + grep only) so it cannot fail
# open on a machine without jq; settings.json runs it with onFailure: block.
#
# Input:  PreToolUse JSON on stdin (we grep the raw text; the command string
#         sits inside it with only quotes and backslashes escaped).
# Output: a permissionDecision JSON on stdout when a rule matches, else nothing.

set -u
input="$(cat)"

decide() { # $1 = deny|ask, $2 = reason (no double quotes)
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"%s","permissionDecisionReason":"zero-trust-guard: %s"}}\n' "$1" "$2"
  exit 0
}
has() { printf '%s' "$input" | grep -Eqi -- "$1"; }

# --- DENY: remote code execution without review -----------------------------
# curl/wget/iwr piped or substituted into an interpreter.
fetch='(curl|wget|iwr|invoke-webrequest|irm|invoke-restmethod)'
interp='(sudo[[:space:]]+)?(ba|z|da|k|fi)?sh|python[0-9.]*|node|perl|ruby|php|iex|invoke-expression'
if has "${fetch}[^|;&]*\\|[[:space:]]*(${interp})([[:space:]]|\\\\?\"|$|;|&)" \
  || has "(${interp})[[:space:]]+(-c[[:space:]]+)?(\\\\?\")?(<\\(|\\\$\\()[[:space:]]*${fetch}"; then
  decide deny "piping a downloaded script into an interpreter is blocked. Download it, read it, pin its hash, then run it as a file."
fi

# --- DENY: history rewriting on shared branches ------------------------------
# Blocks --force and -f and +refspec; --force-with-lease stays allowed.
if has 'git[[:space:]]+push([[:space:]][^|;&]*)?[[:space:]](--force([[:space:]]|\\?"|$)|-[a-zA-Z]*f[a-zA-Z]*([[:space:]]|\\?"|$)|\+[^[:space:]]+)'; then
  decide deny "force push is blocked. Use --force-with-lease on a branch you own, after confirming with the user."
fi

# --- DENY: tampering with git hooks or guard-rails ---------------------------
if has '\.git/hooks/|core\.hooksPath'; then
  decide deny "writing git hooks or changing core.hooksPath is blocked (persistent code execution vector)."
fi

# --- DENY: catastrophic deletes ----------------------------------------------
if has 'rm[[:space:]]+(-[a-zA-Z]*[rR][a-zA-Z]*[[:space:]]+)+(--no-preserve-root[[:space:]]+)?(/|~|\$HOME|/\*)([[:space:]]|\\?"|$)'; then
  decide deny "recursive delete of / or the home directory is blocked."
fi

# --- DENY: reading secrets through the shell ---------------------------------
# Mirrors the Read() deny rules in settings.json, which the shell would bypass.
secret='(^|[[:space:]/=<"'"'"'])(\.env(\.[a-z0-9_-]+)?|id_(rsa|ed25519|ecdsa|dsa)|\.netrc|\.git-credentials|\.pgpass)([[:space:]"'"'"';|&)]|\\\\|$)|\.ssh/|\.aws/credentials|\.config/gh/hosts|\.docker/config\.json|[a-z0-9_-]+\.(pem|key|p12|pfx)([[:space:]"'"'"';|&)]|\\\\|$)'
if has "$secret" && ! has '\.env\.(example|sample|template|dist)([[:space:]"]|\\\\|$)'; then
  decide deny "commands that touch secret files (.env, private keys, cloud or git credentials) are blocked for the agent."
fi

# --- ASK: actions that weaken the controls themselves ------------------------
# Reading control files is fine; modifying them needs a human.
controls='\.claude/(settings(\.local)?\.json|hooks/|skills/)|skills-lock\.json|\.agents/skills/|\.github/workflows/|scripts/(verify-skills\.mjs|test-guard\.sh)|\.mcp\.json|(^|[^a-z])(CLAUDE|AGENTS|SECURITY)\.md'
writes='(^|[[:space:];&|"(])(rm|mv|cp|ln|chmod|chown|tee|truncate|install|sed[[:space:]]+-i|perl[[:space:]]+-pi|git[[:space:]]+(add|rm|mv|checkout|restore|reset|stash|apply|am)|npx[[:space:]]+(-y[[:space:]]+)?skills[[:space:]]+(add|remove|update))([[:space:]]|$)|(^|[^0-9&])>'
if { has "$controls" && has "$writes"; } || has '--no-verify|disableAllHooks'; then
  decide ask "this command modifies security controls (settings, hooks, skill files) or skips verification. A human must approve."
fi

# --- ASK: new agent capabilities (skills, MCP servers, plugins) --------------
# These run with the agent's full permissions; SECURITY.md requires review first.
if has '(npx|bunx|pnpm[[:space:]]+dlx|uvx)[[:space:]]+(-y[[:space:]]+)?skills[[:space:]]+(add|a|update|upgrade|remove|experimental_install)([[:space:]]|\\?"|$)|claude[[:space:]]+(mcp[[:space:]]+add|plugin[[:space:]]+(install|add)|plugins?[[:space:]]+marketplace[[:space:]]+add)'; then
  decide ask "installing or changing skills, MCP servers or plugins requires human review per SECURITY.md."
fi

# --- ASK: dumping the environment (tokens often live there) ------------------
if has '(^|"|[;&|][[:space:]]*)(printenv|env|set|export[[:space:]]+-p)[[:space:]]*($|\\?"|[;&|])'; then
  decide ask "dumping environment variables can expose tokens. A human must approve."
fi

exit 0
