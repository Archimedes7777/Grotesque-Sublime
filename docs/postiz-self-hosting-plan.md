# Self-hosted Postiz: plan

**Goal:** schedule drafts for Instagram, TikTok, YouTube, and X from a Postiz instance you control, so no third party holds the access tokens for your accounts. Humans still review and publish; the repository's guard keeps agents drafts-only (`SECURITY.md` section 6).

**Status:** plan only. Nothing has been installed or connected. Facts come from the official Postiz docs (links at the bottom), fetched 2026-10-29. Claims the docs do not cover are tagged **[Unverified]**; my estimates are tagged **[Estimate]**.

## 1. Recommendation

**Stage it. Do not self-host this month.**

- The two-week calendar (`docs/content-calendar-2wk.md`) is 10 masters across 4 platforms, about 40 posts. Native schedulers and manual posting handle that at no cost and with zero new token holders.
- Self-hosting reduces risk **only if the server is kept hardened and patched**. A neglected VPS holding four accounts' tokens is a worse single point of failure than a well-run hosted service.
- Revisit when all of these are true:
  1. The hardening checklist (`docs/account-hardening-checklist.md`) is done on every account.
  2. You post more than about 10 times a week and manual posting is the bottleneck.
  3. You can spend roughly 15 to 25 hours on setup and 1 to 2 hours a month on upkeep **[Estimate]**.
  4. The incident runbook (`docs/incident-response.md`) is printed and the contact card is filled in.

## 2. What self-hosting changes

| | Native schedulers (Meta, TikTok, YouTube Studio, X) | Hosted Postiz | Self-hosted Postiz |
|---|---|---|---|
| Who holds your tokens | Each platform only | Postiz company, plus each platform | You, plus each platform |
| Cross-posting in one place | No | Yes | Yes |
| Setup effort | None | Low | High (servers plus 4 developer apps) |
| Ongoing upkeep | None | None | Patching, backups, upgrades |
| Cost | Free | Subscription | Server and domain **[Estimate]** below |
| Main failure mode | Four logins to manage | Vendor breach | Your own misconfiguration |

## 3. Architecture

```
Internet
   |
   v 443 (TLS, automatic certificates)
Caddy reverse proxy (host)
   |
   v 127.0.0.1 only
Postiz container (internal port 5000; compose maps host 4007)
   |  private Docker network only
   +--> PostgreSQL (14+)     no published port
   +--> Redis (6+)           no published port
   +--> Temporal (7233 gRPC) no published port; Temporal UI (8080) bound to 127.0.0.1 or removed
Media: Cloudflare R2 bucket on a public custom domain (platforms must fetch media over HTTPS)
```

Why media is public: TikTok's docs say TikTok fetches media itself, so files must be publicly reachable over HTTPS and `localhost` or private paths such as `/uploads` fail. Instagram's content API also needs a public media URL **[Moderate]**. Keep the app UI and API behind the proxy; keep only the media bucket public.

## 4. Requirements (from the docs)

| Item | Docs say |
|---|---|
| Hardware tested | Ubuntu 24.04 VM, 2 vCPU, 2 GB RAM |
| Hardware recommended | 4 vCPU, 8 GB RAM, 50 GB disk plus a persistent volume for uploads; "4 GB or more" for multiple users or scheduled workflows |
| Software | Docker and Docker Compose; official compose repo `gitroomhq/postiz-docker-compose` |
| Services | PostgreSQL 14+, Redis 6+, Temporal (required since v2.12.0, bundled in the compose repo) |
| Storage | `STORAGE_PROVIDER=local` or `cloudflare` (R2) |
| Domain | A real HTTPS domain; TikTok rejects `http://` redirect URIs |

## 5. Hardening checklist

### Host
- [ ] Ubuntu LTS, `unattended-upgrades` on, reboot window set
- [ ] SSH: key-only, root login off, password login off; ideally reachable only over a VPN or from an allowlist
- [ ] Firewall: allow 80 and 443 (and SSH from your allowlist only); deny everything else
- [ ] `fail2ban` or equivalent on SSH
- [ ] Separate non-root user for operations

### Containers
- [ ] Only the proxy listens publicly. Change the compose port mapping to `127.0.0.1:4007:5000` **[Unverified: confirm the mapping in the current compose file]**
- [ ] Postgres and Redis publish no ports
- [ ] Temporal UI (8080) bound to `127.0.0.1` or removed; reach it through an SSH tunnel when needed
- [ ] Pin image versions (by digest where possible); upgrade deliberately, never with an auto-updater
- [ ] Run `docker compose down` then `up` after any variable change (the docs warn variable changes apply only after recreate)

### Application
- [ ] `JWT_SECRET`: 48+ random bytes (`openssl rand -base64 48`), set once, never in version control (rotating it logs everyone out)
- [ ] `NOT_SECURED`: never set (the docs call it dev-only; it disables security checks)
- [ ] `DISABLE_SSRF_PROTECTION`: never set (it removes the guard against requests to private IPs)
- [ ] `DISABLE_REGISTRATION=true` after you create your one admin account. Then **test it**: try to sign up in a private browser window. One forum report says the flag may be checked for presence only, and the docs describe one-signup behavior, so verify rather than trust
- [ ] Strong unique admin password from the password manager. Whether Postiz supports 2FA on its own login is **[Unverified]**; check the account settings at install. If it does not, restrict the admin UI at the network level (VPN or IP allowlist)
- [ ] URLs must match the browser exactly, protocol and port included: `MAIN_URL`, `FRONTEND_URL`, `NEXT_PUBLIC_BACKEND_URL` (`https://postiz.example.com/api`). Serve frontend and backend from the same parent domain or the OAuth "Invalid state" error appears

### Proxy (public domain)
```
postiz.example.com {
    encode zstd gzip
    reverse_proxy 127.0.0.1:4007
}
```
Caddy obtains and renews certificates for a public domain on its own; the docs' sample uses `tls internal`, which is only for private networks.

## 6. Secrets

- Platform app secrets live only in the deployment's `.env` on the server (`chmod 600`, owned by the operations user). They never enter this repository, a chat, or an agent's context.
- If an agent needs the Postiz API, give it a dedicated key through an environment variable it cannot print. Scope granularity of that key is **[Unverified]**, so treat it as full power. The repository guard blocks non-draft creation and asks before scheduling or deleting (`SECURITY.md` section 4.4).
- Rotate the Postiz API key and each platform app secret every 90 days and after any incident (`docs/incident-response.md` section 6).
- Every developer account (Meta, TikTok, X, Google Cloud) is one more credential. Give each a hardware key or passkey.

## 7. Connecting the four platforms

Single-owner setups can skip the heaviest reviews because the docs let the app's own developer or tester accounts post without full approval.

| Platform | Setup per the docs | Friction and constraints |
|---|---|---|
| **X** | Developer account; app type **Native App** (other types fail with error 32); permissions **Read and Write**; OAuth 1.0a with X API v1 for image upload | Access tier, cost, and rate limits are **[Unverified]**; check X's current developer pricing before committing |
| **Instagram** | Meta developer app ("Other" type) under a business portfolio; Facebook Business option needs the Instagram account linked to a Facebook Page; permissions include `instagram_basic`, `instagram_content_publish`, `pages_show_list`, `pages_read_engagement`, `business_management`, `instagram_manage_comments`, `instagram_manage_insights` | Public apps need business verification and advanced-permission approval; the app's own developer or tester accounts can post without it. Reels audio only works with the Facebook Business option |
| **TikTok** | Developer app with Login Kit and Content Posting API (Direct Post); scopes `user.info.basic`, `video.create`, `video.publish`, `video.upload`, `user.info.profile`; verified domain; public HTTPS terms and privacy pages | **Unaudited apps can only post privately (`SELF_ONLY`) and are limited to 5 users per 24 hours.** The "Upload without posting" mode sends media to your TikTok inbox as a draft you publish within 24 hours, which fits the drafts-only policy |
| **YouTube** | Google Cloud project; OAuth web client; enable YouTube Data API v3, YouTube Analytics API, and YouTube Reporting API; add yourself as a test user | The docs do not mention that refresh tokens for apps left in "Testing" status expire after about 7 days, which would force repeated reconnecting **[Moderate: Google's rule, not in the Postiz docs]**. Publishing the app moves you into Google's verification process. Brand Accounts need an extra Workspace admin step and up to 5+ hours to propagate |

## 8. Backups and recovery

| What | How | Frequency |
|---|---|---|
| PostgreSQL | `pg_dump` from the database container, encrypted (for example with `age`), copied to a different provider | Nightly |
| Uploads | R2 bucket versioning on; or volume snapshot if local | Continuous or weekly |
| Server | Provider snapshot before every upgrade; weekly otherwise | Weekly |
| Configuration | Private repository containing compose file and a `.env.example` with no secrets; real `.env` in the password manager | On change |
| Restore test | Rebuild the instance from backup on a throwaway VPS and log in | Quarterly |

Targets **[Estimate]:** recovery point 24 hours, recovery time 4 hours. Redis holds queues and caches; treat it as rebuildable. Scheduled-post state lives in Temporal and Postgres, so the restore test must prove scheduled posts survive.

## 9. Operations

- Monthly: read Postiz release notes, snapshot the server, upgrade one version, verify logins and one test draft. v2.12.0 and later need the Temporal migration guide.
- Weekly: check disk space, container health, and failed posts.
- Always: watch the proxy and application logs for repeated failed logins.
- After any suspected incident: follow `docs/incident-response.md`.

## 10. Phased rollout with gates

| Phase | What | Gate to continue | Time **[Estimate]** |
|---|---|---|---|
| 0 | Native schedulers and manual posting; finish hardening checklist | Checklist complete on all accounts | Now to 2 weeks |
| 1 | Provision VPS and domain, harden, install Postiz **with no accounts connected**, test backups and restore | Restore test passes; registration confirmed closed | 6 to 10 h |
| 2 | Create X and Instagram developer apps (developer-mode access), connect those two accounts, publish one test draft each | Test draft works; no extra permissions granted | 4 to 6 h |
| 3 | TikTok app, using inbox-draft mode; apply for audit only if you need public Direct Post. YouTube app in testing mode, then decide whether to publish | Drafts reach TikTok inbox; YouTube reconnect cadence understood | 4 to 8 h plus review wait |
| 4 | Optional agent integration (CLI or API key) under guard rules | Guard tests pass; key stored outside the repository | 1 to 2 h |

## 11. Exit and rollback

1. On each platform, revoke the Postiz app's access (Connected apps / Apps and sessions).
2. Delete the developer apps or rotate their secrets.
3. Export anything you need (media, analytics), then destroy the VPS and snapshots.
4. Rotate the brand email password and review sessions (`docs/incident-response.md` section 2).

## 12. Cost **[Estimate]**

| Item | Rough monthly |
|---|---|
| VPS, 4 vCPU and 8 GB class | about $20 to $40 |
| Domain | about $1 |
| R2 storage and backups | under $5 at small volume |
| **Total** | **about $25 to $45 per month, plus your time** |

Prices vary by provider and change; confirm before committing.

## 13. Risks

- **Neglect:** unpatched server or stale images. Mitigation: monthly upgrade routine and unattended OS updates.
- **Misconfiguration exposing the admin UI or Temporal UI.** Mitigation: the container and firewall checklist above, plus an external port scan after install.
- **Platform policy change:** X pricing, TikTok audit rules, Google verification. Mitigation: do not build the posting workflow so it cannot fall back to manual.
- **Single operator:** if you are unavailable, scheduling stops. Mitigation: native schedulers remain a working fallback.

## 14. Open questions to settle at install

1. Does Postiz offer 2FA for its own login?
2. How granular are API key permissions?
3. Is the registration lock enforced as documented?
4. Which X access tier and price applies to your usage?
5. Do you want YouTube published (verification) or kept in testing (reconnect weekly)?

## Sources

- [System requirements](https://docs.postiz.com/installation/system-requirements)
- [Docker Compose install](https://docs.postiz.com/installation/docker-compose.md)
- [Configuration reference](https://docs.postiz.com/configuration/reference)
- [Self-host gotchas](https://docs.postiz.com/self-host/troubleshooting.md)
- [Caddy reverse proxy](https://docs.postiz.com/self-host/reverse-proxies/caddy.md)
- Provider setup: [X](https://docs.postiz.com/self-host/providers/x-twitter.md), [Instagram](https://docs.postiz.com/self-host/providers/instagram.md), [TikTok](https://docs.postiz.com/self-host/providers/tiktok.md), [YouTube](https://docs.postiz.com/self-host/providers/youtube.md)
