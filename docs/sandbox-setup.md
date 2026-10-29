# Claude Code sandbox for your local machine

The project settings (`.claude/settings.json`) control what Claude may *try*. The sandbox controls what a command *can physically reach*: files outside the project, and network hosts outside an allowlist. It is the backstop for the guard's known limitation (obfuscated commands).

This belongs in **user settings** on your own machine, not in the repository:

- The strict network allowlist is honored only from user or managed settings; project settings cannot set it.
- Cloud sessions run in an already isolated container whose network policy is set in the environment settings.

## Install

1. Prerequisites: macOS works out of the box. On Linux or WSL, install `bubblewrap` and `socat` (for example `sudo apt install bubblewrap socat`). On native Windows, run `/sandbox install` inside Claude Code.
2. Merge the JSON below into `~/.claude/settings.json` (create the file if it does not exist; keep any existing keys).
3. Restart Claude Code and run `/sandbox` to confirm it is active.

```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "autoAllowBashIfSandboxed": false,
    "allowUnsandboxedCommands": false,
    "network": {
      "strictAllowlist": true,
      "allowedDomains": [
        "github.com",
        "*.github.com",
        "*.githubusercontent.com",
        "registry.npmjs.org",
        "skills.sh"
      ]
    },
    "filesystem": {
      "denyRead": [
        "~/.ssh",
        "~/.aws",
        "~/.config/gh",
        "~/.netrc",
        "~/.git-credentials",
        "~/.docker/config.json"
      ]
    }
  }
}
```

## What each setting does

| Setting | Effect |
|---|---|
| `disableBypassPermissionsMode` | Removes the "skip all permission prompts" mode entirely |
| `enabled` + `failIfUnavailable` | Every Bash command runs sandboxed; if the sandbox cannot start, Claude Code refuses to start instead of silently running unsandboxed (fail-closed) |
| `autoAllowBashIfSandboxed: false` | Sandboxed commands still go through normal permission prompts |
| `allowUnsandboxedCommands: false` | The agent cannot request an escape from the sandbox |
| `network.strictAllowlist` | Hosts not on the list are denied outright, not prompted; this blocks data exfiltration to unknown servers |
| `filesystem.denyRead` | Credential stores are unreadable to sandboxed commands even if the guard is evaded |

## Expected friction

- A command that needs a new host fails with a network error. Add the host to `allowedDomains` deliberately; never use a wildcard like `*`.
- If you adopt Postiz or another API, add only its API host (for example `api.postiz.com`).
