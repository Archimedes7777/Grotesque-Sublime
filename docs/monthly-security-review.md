# Monthly security review (one page, about 20 minutes)

Do this on the **first weekend of each month**, from your own trusted device. Write the date and any findings in the log at the bottom. If anything looks wrong, stop and follow `docs/incident-response.md`.

## 1. Brand email (identity root): 4 minutes

- [ ] Recent security activity: no sign-ins you do not recognize
- [ ] Recovery email and phone are still yours
- [ ] Passkey and both hardware keys still listed; no SMS
- [ ] No unknown forwarding rules or filters
- [ ] Third-party connections: remove anything unused

## 2. Each social account: 2 minutes each (8 minutes)

For Instagram (`activelypsychotic`), YouTube (`activelypsychotic`), X (`realbobfrapples`), TikTok (`bobfrapplesgns`):

- [ ] Active sessions and devices: log out anything unknown
- [ ] Two-factor methods unchanged; backup codes still stored offline
- [ ] Connected apps: remove anything you no longer use
- [ ] YouTube only: Studio permissions list shows only people you added
- [ ] Profile details (name, bio, links) are exactly as you set them

## 3. Impersonation check: 2 minutes

- [ ] Search each platform for `activelypsychotic`, `bobfrapples`, and close spellings
- [ ] Report impersonating accounts inside the official app

## 4. Repository and GitHub: 4 minutes

- [ ] Open the repository's **Issues** tab: any "Upstream skill drift detected" issue is a review task (see `SECURITY.md` section 4.3). Do not update a skill without the review
- [ ] **Actions** tab: the latest "Skills integrity" run on `main` is green; the monthly "Upstream skill watch" ran on the 1st
- [ ] **Settings > Rules**: the `protect-main` ruleset is still **Active**
- [ ] **Security** tab: no open secret-scanning or Dependabot alerts
- [ ] Your GitHub account: no unknown sessions, keys, or authorized apps

## 5. Domains: 1 minute

- [ ] `activelypsychotic.com` and `bobfrapples.com`: auto-renew on, registrar lock on, expiry date more than 60 days away (`bobfrapples.com` showed 2026-12-20 when checked)

## 6. Quarterly extras (January, April, July, October)

- [ ] Test one set of backup codes on a low-risk account to confirm the stored codes work
- [ ] Rotate any API keys you use (for example a Postiz key, if adopted)
- [ ] Re-read `docs/account-hardening-checklist.md` against current platform menus

## Log

| Date | Done by | Findings | Actions taken |
|---|---|---|---|
| | | | |
