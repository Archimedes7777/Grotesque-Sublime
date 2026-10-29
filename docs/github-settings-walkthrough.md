# GitHub settings walkthrough (phone friendly)

These are the repository settings that no file in the repository can set. They turn the CI check from "reports a problem" into "blocks a bad merge". Total time: about 15 minutes. Do them in this order.

## Which app?

Use **github.com in a web browser**, not the GitHub mobile app. Repository settings pages (rulesets, code security, Actions permissions) live on the website. I could not confirm that the current mobile app exposes them **[Moderate]**, so the browser is the reliable path.

On an iPhone: open Safari, go to `github.com/Archimedes7777/Grotesque-Sublime/settings`, then tap the **aA** icon in the address bar and choose **Request Desktop Website**. The settings sidebar is easier to use that way.

## 1. Protect `main` (most important)

Settings > **Rules** > **Rulesets** > **New ruleset** > **New branch ruleset**

| Field | Set it to |
|---|---|
| Ruleset name | `protect-main` |
| Enforcement status | **Active** |
| Bypass list | Leave empty |
| Target branches | **Add target** > **Include default branch** |
| Restrict deletions | On |
| Block force pushes | On |
| Require a pull request before merging | On. Set **Required approvals** to **0** (GitHub does not let you approve your own pull request, and you are the only collaborator) |
| Require status checks to pass | On. **Add checks** > search `verify` > select it. It appears because it has already run |

Tap **Create**.

What changes: nobody, including you, can push straight to `main` any more. All changes go through a pull request, and the merge button stays disabled until `verify` is green.

**Note:** the leftover "Introduction to GitHub" course workflows, which would have conflicted with blocked direct pushes, were removed in the same pull request as this guide. No course files remain.

## 2. Secret scanning and push protection

Settings > **Code security** (labelled **Advanced Security** on some accounts)

- Turn on **Secret scanning** (called Secret Protection on some plans).
- Turn on **Push protection**. It blocks a push that contains a recognizable key or token.
- Turn on **Private vulnerability reporting** (`SECURITY.md` section 8 points to it).
- Turn on **Dependabot alerts**.

Availability depends on whether the repository is public or private and on your plan **[Moderate]**. If an option shows a price or is greyed out, tell me what it says and I will adjust the plan.

## 3. Make Actions read-only by default

Settings > **Actions** > **General**

- **Workflow permissions:** choose **Read repository contents and packages permissions**.
- Leave **Allow GitHub Actions to create and approve pull requests** off.

The workflows in this repository declare the extra permissions they need themselves, so this setting does not break them.

## 4. Restrict which actions may run (optional, stricter)

Same page > **Actions permissions**

- Choose **Allow Archimedes7777, and select non-Archimedes7777, actions and reusable workflows**.
- Tick **Allow actions created by GitHub**.
- No extra allow-list entries are needed: the remaining workflows use only `actions/checkout`, which is GitHub-created.
- If you see **Require actions to be pinned to a full-length commit SHA**, turn it on. Every workflow here is already pinned **[Moderate]** on the setting's exact name.

## 5. Protect the account itself

Profile photo > **Settings** > **Password and authentication**

- Add a **passkey** and both hardware security keys.
- Remove SMS as a recovery or two-factor method once the keys work.
- Save the recovery codes offline.

## Check that it worked

1. Settings > Rules > Rulesets shows `protect-main` as **Active**.
2. Open any pull request: the merge area shows "Required" next to `verify`.
3. Try to push to `main` from a local copy: it should be refused.

## If something goes wrong

- Locked yourself out of merging: Settings > Rules > Rulesets > `protect-main` > set **Enforcement status** to **Disabled**, fix the problem, then set it back to **Active**.
- A required check never appears: run the workflow once (Actions tab > Skills integrity > Run workflow), then add it again.
