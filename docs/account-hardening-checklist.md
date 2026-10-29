# Account Hardening Checklist: ActivelyPsychotic

Implements SECURITY.md section 6. Work top to bottom; the identity root comes first because every platform recovers through it. Platform menus change; verified 2026-10-28, re-check quarterly.

Legend: **[Verified]** confirmed against current sources this session. **[Unverified]** not confirmed; check in the app.

## 0. Before you start

- [ ] Install a password manager. Every account gets a unique, generated password (20+ characters).
- [ ] Buy two FIDO2 hardware security keys (primary plus a backup kept in a separate location).
- [ ] Prepare an offline place for backup codes (printed and locked away, or an encrypted vault entry).

## 1. Identity root: the brand email (Google account recommended)

This account recovers every platform, so it gets the strongest protection.

- [ ] Use a dedicated email address for the brand, not your personal or work email.
- [ ] Add a passkey and both hardware security keys. Google supports both.
- [ ] Consider enrolling in **Google Advanced Protection** (strongest takeover protection Google offers; requires passkeys or security keys).
- [ ] Remove SMS as a sign-in or recovery method once keys are enrolled.
- [ ] Review Security > Third-party connections and remove anything unused.
- [ ] Turn on sign-in alerts.

## 2. YouTube (inherits the Google account)

- [ ] Covered by section 1 if the channel lives under the brand Google account.
- [ ] Use a **Brand Account** for the channel; grant collaborators the **Manager/Editor** role, never the Owner role, and never share the login.
- [ ] YouTube Studio > Settings > Permissions: review quarterly.
- [ ] Upload flow: answer the **altered or synthetic content** question truthfully. Disclosure is required for realistic synthetic content, and YouTube auto-labels detected photorealistic AI content. **[Verified]**

## 3. Instagram (Meta Accounts Center)

- [ ] Accounts Center > Password and security > Two-factor authentication: choose **Authentication app**. Current options are SMS, authentication app, and WhatsApp. **[Verified]**
- [ ] Passkeys for Instagram: **[Unverified]** (Meta has offered passkeys for Facebook; check Accounts Center for an Instagram option and enable it if present).
- [ ] Remove SMS as a second factor after the app is set up; save the backup codes offline.
- [ ] Accounts Center > Password and security > **Where you're logged in**: log out unknown sessions.
- [ ] Settings > Website permissions > **Apps and websites**: remove unused integrations.
- [ ] Switch to a Professional (Creator) account for analytics; link it to a Facebook Page only if needed.
- [ ] AI label: Meta applies "AI info" labels, largely from C2PA metadata. Do not strip metadata to avoid labels.

## 4. TikTok

- [ ] Settings and privacy > Security > **Passkey**: create one. TikTok supports passkey login, user-initiated. **[Verified]**
- [ ] Settings and privacy > Security > **2-step verification**: enable it with an **authenticator app** plus email (TikTok requires at least two methods; avoid SMS where you can). **[Verified]**
- [ ] Run TikTok's **Security Checkup** and log out unknown devices.
- [ ] Settings > Security > Manage app permissions: remove unused apps.
- [ ] Upload flow: turn on the **AI-generated content** toggle for realistic AI content. TikTok also auto-labels from C2PA Content Credentials. **[Verified]**

## 5. X

- [ ] Settings and privacy > Security and account access > Security > Two-factor authentication: enroll **both hardware security keys**. Options are text message, authentication app, and security key. **[Verified]**
- [ ] If keys were enrolled before late 2025, confirm they are re-enrolled for the x.com domain (X required this in October to November 2025 to avoid lockout). **[Verified]**
- [ ] Add an authentication app as a fallback; remove text message.
- [ ] Save backup codes offline.
- [ ] Settings > Security and account access > **Apps and sessions**: revoke unused apps and log out unknown sessions.

## 6. Scheduling tool (Postiz, if adopted)

- [ ] Prefer **self-hosted** Postiz; the SaaS concentrates OAuth access to every account in one third party.
- [ ] Create a Postiz **public API key** only when needed; give it to the agent through an environment variable, never in chat or in the repository. Rotate it quarterly.
- [ ] Protect the Postiz account itself with the strongest MFA it offers.
- [ ] The repository's guard keeps the agent drafts-only (`-t draft`); you promote posts to the schedule.

## 7. Ongoing (put these on a calendar)

| Cadence | Task |
|---|---|
| Every post | AI-content label applied where required; human review before publishing |
| Monthly | Check login alerts and active sessions on every platform |
| Quarterly | Revoke unused connected apps; confirm recovery email and phone; rotate API keys; re-check this list against platform help pages |
| On any suspicious message | Treat "copyright strike", "verification", "brand deal", or "suspension" DMs and emails as phishing; verify only inside the official app |
| On suspected compromise | From a clean device: change the identity-root password, revoke all sessions, rotate all API keys, then each platform in order 2 to 6 |
