# Incident response runbook: suspected account takeover

For the Bob Frapples Universe accounts (Instagram, TikTok, YouTube, X) and the systems behind them. Print this or save it somewhere you can reach **without** the accounts it protects (an offline copy, or a note on a different device).

> **Rule 1:** Work from a device and network you trust (not the one you suspect is infected, not public Wi-Fi). If your phone itself may be compromised, use a different computer.
> **Rule 2:** Never click a link in a message about a hacked account. Go to the official app or type the address yourself.
> **Rule 3:** Fix the identity root (brand email) first if there is any sign it is affected. Every platform recovers through it.

Menu names change. Steps marked **[Unverified]** describe where options usually live; confirm in the app.

## 1. Decide what happened (2 minutes)

| What you see | Most likely | Go to |
|---|---|---|
| Login alert or password-reset email you did not request | Someone is attempting access | Section 3, platform step only |
| Logged out, password no longer works, or email on the account changed | Takeover in progress | Section 2, then Section 4 |
| Posts, DMs, or follows you did not make | Active takeover | Section 2 first, fast |
| A DM or email about a "copyright strike", "verification", or "brand deal" | Phishing attempt | Section 7 |
| Brand email shows sent mail you did not send, or new forwarding rules | Identity root compromised | Section 3, brand email first |
| An API key, token, or secret appeared in chat, a repo, or a log | Secret exposure | Section 6 |

## 2. Contain (first 15 minutes)

1. **From a clean device,** open the brand email provider and change its password to a new unique one from your password manager.
2. In the email security settings: sign out of all other sessions; remove any recovery email or phone you do not recognize; remove any 2FA method you did not add; review forwarding and filter rules and delete unknown ones.
3. Re-enroll your hardware keys or passkey on the email account if the attacker could have removed them.
4. Generate **new backup codes** for every account (the old set is void once you do).
5. Write down the time you started and what you saw. Do not delete anything yet (evidence).

## 3. Platform steps

For each platform: change the password, sign out all sessions, review connected apps, review the 2FA methods, then confirm the email and phone on file are yours.

### Google and YouTube
- Open the official Google account recovery page (`g.co/recover`) and follow it if you are locked out.
- Security checkup: remove unknown devices, review third-party access, review recovery info.
- YouTube Studio: Settings > Permissions. Remove any manager or editor you do not recognize. If the channel is under a Brand Account, check its managers too. **[Unverified]** exact menu path.

### Instagram
- If locked out, use Instagram's official "hacked account" help flow (`instagram.com/hacked`). **[Moderate]** address.
- Accounts Center > Password and security: review "Where you're logged in", two-factor methods, and saved login info. **[Unverified]** menu names.
- Settings: remove unknown apps and websites that have account access.
- Check that email, phone, and linked Facebook accounts are yours.

### TikTok
- Settings and privacy > Security and login: change the password, review devices, review passkeys and 2-step verification methods. **[Unverified]** menu names.
- If locked out, search TikTok's official help center for "hacked account" and use the form there.
- Remove unknown connected apps. Check that the business or developer account (if any) is secure too.

### X
- Settings and privacy > Security and account access > Security: review two-factor methods and security keys, then Apps and sessions to revoke unknown ones. **[Unverified]** menu names.
- If locked out, search X's official help center for "hacked account".
- Revoke every third-party app you do not use today.

### Other places the attacker may have reached
- **Scheduling or posting tools:** revoke the app's access on each platform, then rotate its keys (Section 6).
- **Shop and print-on-demand accounts:** change passwords and check payout details, shipping addresses, and connected stores.
- **Payment and bank accounts:** if any card or payout account was reachable from a compromised device, review recent activity and call the provider.

## 4. If you are locked out

1. Use each platform's official recovery flow from a trusted device, ideally one you have used to sign in before.
2. Expect identity checks (selfie video, ID, a code to the original email). Keep proof of ownership ready: the original signup email, receipts, screenshots of the account with your name, a post only the owner would know.
3. Do not pay anyone offering to "recover" an account. These are scams. Do not pass codes, passwords, or screenshots of codes to anyone.
4. Keep a log of each request, ticket number, and date.

## 5. Tell your audience (when contained)

- Post from a different, still-safe account or channel: "Our [platform] account was compromised. Ignore any links or offers sent from it between [time] and [time]. We are recovering it."
- Do not give details that help the attacker. Do not accuse anyone.
- If a shop is linked, pause the shop's promotions until accounts are back.

## 6. Leaked secret or API key

1. **Rotate first.** Revoke the exposed key at the provider and create a new one. Deleting the message, commit, or file does not make a leaked key safe.
2. Put the new key only where the system reads it from (an environment variable or the platform's secret store). Never paste it into chat, an issue, a pull request, or a repository file.
3. Check the provider's usage log for activity you did not cause.
4. If the key was in a GitHub repository, also remove it from the files, and remember it stays in history: rotation is what protects you.
5. If it was a scheduling-tool key, review the posts and drafts that tool created.

## 7. Phishing triage

Typical lures: "copyright strike", "your account will be disabled in 24 hours", "verified badge approved", "brand deal, please sign in to view the contract", fake support accounts in DMs.

- Do not click. Do not sign in through the link. Do not reply with codes.
- Open the official app directly and check the in-app inbox or the Account Status area.
- Report the message inside the platform. Delete it afterward.
- If you did enter a password on a suspicious page, treat it as a takeover: Section 2 immediately.

## 8. After the incident (within a week)

- [ ] Write what happened, how it got in, and what stopped it
- [ ] Close the gap (for example, replace SMS with an authenticator app or key)
- [ ] Update `docs/account-hardening-checklist.md` if a step was missing
- [ ] Re-check connected apps and sessions on every platform
- [ ] Re-test that your backup codes and recovery contacts work

## 9. Contact card (fill in and keep offline)

| Item | Value |
|---|---|
| Brand email provider and recovery method | |
| Where hardware keys and backup keys are stored | |
| Password manager emergency access holder | |
| Instagram, TikTok, YouTube, X support ticket logs | |
| Trusted second device | |
| Person who can post the "we were compromised" notice | |
