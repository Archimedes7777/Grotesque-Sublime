# PC hardening from the 2026-11-01 network audit

Source: `NetAudit_20261101_011605` on the Desktop (machine CHUMPERS, Windows 11 Pro 25H2). This document re-reads the script's findings, corrects the ones it got wrong, adds one it missed, and gives a fix for each in priority order. Written 2026-11-07.

Why this lives in this repository: CHUMPERS is the machine that runs the agents, holds the skills, and has the `Z:` drive with this repo. `SECURITY.md` assumes breach and layers controls; a weak host undercuts every one of them.

**How to run the fixes.** Each fix is a PowerShell command. Open PowerShell **as administrator** for these (Windows key, type `PowerShell`, right-click, **Run as administrator**). You run them, not Claude. Do them in the order below; each has a check. If a check does not match, stop and ask.

---

## Part 0: Words used below

**BitLocker.** Windows' disk encryption. When it is *on*, a thief who pulls the drive out sees scrambled data. When it is *suspended*, the drive is still scrambled but the unlock key sits in the clear on the disk, so the scrambling protects nothing.

**SMB share.** A folder this PC offers to other computers over the network. `C$`, `ADMIN$`, `Z$`, `Q$` and `IPC$` are Windows defaults, only reachable by administrators. `Users` is not a default; someone made it.

**Binding.** Which network features are switched on for which network adapter. "File and Printer Sharing" bound to an adapter means that adapter answers file-share requests.

**Firewall profile.** Windows treats each network as Domain, Private or Public. Public is the strictest. Both your Wi-Fi and your VPN are set to Public, which is good.

**Listener.** A program waiting for incoming connections on a port. One that listens on `127.0.0.1` or `::1` accepts connections only from this PC itself.

**Print Spooler.** The Windows printing service. It has had serious remote bugs ("PrintNightmare"). Letting it accept remote connections is a risk if you do not share a printer.

**NetBIOS, LLMNR, mDNS, WPAD.** Four old or chatty "find things on the local network" protocols. Each has been used for attacks on local networks. Turning them off costs little on a home network.

**LmCompatibilityLevel.** How Windows proves who you are to other Windows machines. Level 5 means "only the modern, hard-to-forge way." Below 5 allows older, forgeable methods.

**PasswordRequired = False.** A flag on an account saying "a blank password is acceptable." It does not prove the password *is* blank, but it allows it, and the audit cannot tell the difference.

---

## Part 1: Corrections to the script's findings

| Script said | Reality | Severity after review |
|---|---|---|
| HIGH: Defender real-time protection is OFF | **Expected.** Bitdefender is installed and reports as the active, enabled, up-to-date antivirus (product state `0x041000`). Windows Defender turns itself off when another antivirus is active (`0x060100` = disabled). The `Get-MpPreference` error (`0x800106ba`, "service not running") says the same thing. | **Verify, do not fix.** Open Bitdefender and confirm every shield is on and signatures updated today. |
| REVIEW: Defender signatures more than 7 days old | Same cause as above. | None, once Bitdefender is confirmed current. |
| HIGH: 2 listeners run from AppData | Both are `github.exe`, the GitHub Copilot desktop app, listening on `127.0.0.1` only. That is loopback: unreachable from the network. `AppData\Local\Programs` is the normal home for per-user apps (Notion and Discord live there too). | **Low.** Keep only if you use GitHub Copilot's desktop app; uninstall it otherwise. |
| REVIEW: MDM enrollment found | Report shows `AzureAdJoined: NO`, `DomainJoined: NO`, `WorkplaceJoined: NO`, and the three enrollment rows have no UPN or URL. Those rows are built-in placeholders, not a real manager. | **Low.** Confirm in Settings > Accounts > Access work or school that nothing is listed. |
| (not flagged) | **BitLocker on `C:` is FullyEncrypted but ProtectionStatus is Off.** The drive is encrypted and the key is exposed. This is the state BitLocker is in after someone chose "suspend protection" (often for a firmware update) and it never resumed. `Z:` and `Q:` are not encrypted at all; `Z:` holds this repo. | **HIGH.** Fix first. |
| HIGH: accounts with no password required | Correct as far as the flag goes. `Bob` and `Grandma Frapples` are **administrators**. `Bob` last signed in May 2026. `Goopy Gus GutStuffer` signed in 2026-10-29. `CodexSandboxOffline/Online` are created by the OpenAI Codex app for its sandbox and are expected. | **HIGH.** Fix second. |

---

## Part 2: Fixes, in order

### Fix 1: Resume BitLocker on C:

**Why first:** everything else protects the running PC. This protects the data when the PC is off or stolen.

```powershell
Resume-BitLocker -MountPoint C:
```

**Check:**

```powershell
Get-BitLockerVolume -MountPoint C: | Select-Object VolumeStatus, ProtectionStatus
```

Expect `FullyEncrypted` and `On`.

Then **save the recovery key** somewhere that is not this PC: Settings > Privacy & security > Device encryption > BitLocker drive encryption > Back up your recovery key. A password manager entry or a printed sheet in a drawer both work.

Optional but recommended: encrypt `Z:` too, since it holds the repo and the skills. In the same BitLocker window choose **Turn on BitLocker** for `Z:`. It runs in the background and can take an hour or more; the PC stays usable.

### Fix 2: Accounts

**2a. Decide what each account is for.**

| Account | Admin? | Last sign-in | Action |
|---|---|---|---|
| `Grandma Frapples` | Yes | 2026-11-01 | Your account. Give it a real password and require it. |
| `Bob` | Yes | 2026-05-31 | If you do not use it, disable it. If you do, require a password. |
| `Goopy Gus GutStuffer` | No | 2026-10-29 | **Do you recognize this account?** If yes, require a password. If no, disable it now and ask Claude to help look at what it did. |
| `CodexSandboxOffline`, `CodexSandboxOnline` | No | never | Created by the Codex app. Leave them. |

**2b. Require a password on every enabled account** (the flag only; this does not set the password):

```powershell
net user "Grandma Frapples" /passwordreq:yes
```

```powershell
net user "Bob" /passwordreq:yes
```

```powershell
net user "Goopy Gus GutStuffer" /passwordreq:yes
```

**2c. Set the password itself** on each account you keep. Settings > Accounts > Sign-in options for your own account; for others, Control Panel > User Accounts > Manage another account. Use a password manager to generate them. A Windows Hello PIN on top is fine; the password is still what protects the account over the network.

**2d. Disable accounts you do not use:**

```powershell
Disable-LocalUser -Name "Bob"
```

**Check:**

```powershell
Get-LocalUser | Where-Object Enabled | Select-Object Name, PasswordRequired
```

Every row should say `True`.

### Fix 3: Stop sharing C:\Users with the network

The `Users` share exposes every profile folder on this PC to anyone who can log in over the network. Nothing on a home PC needs it.

```powershell
Remove-SmbShare -Name "Users" -Force
```

**Check:**

```powershell
Get-SmbShare | Select-Object Name, Path
```

`Users` should be gone. `C$`, `ADMIN$`, `IPC$`, `Q$`, `Z$` staying is normal.

### Fix 4: Stop answering file-share requests on the VPN and Wi-Fi

File and Printer Sharing is bound to the Bitdefender VPN tunnel. Inside a VPN you share an address range (`100.64.0.0/10`) with other customers of that VPN. You do not want to answer their file-share requests. Same for a Wi-Fi network you do not share files on.

```powershell
Disable-NetAdapterBinding -Name "bdvpnservice_1" -ComponentID ms_server
```

```powershell
Disable-NetAdapterBinding -Name "Wi-Fi" -ComponentID ms_server
```

If you never share files or printers from this PC at all, you can stop the Server service entirely instead; ask before doing that, because it also removes the admin shares some backup tools use.

**Check:**

```powershell
Get-NetAdapterBinding -ComponentID ms_server | Where-Object Enabled | Select-Object Name
```

Neither `bdvpnservice_1` nor `Wi-Fi` should be listed.

### Fix 5: Remove the hand-made firewall holes

Two identical rules named **WSL2 Port 3000** allow any computer, on any network profile, to reach port 3000 on this PC, for any program. Someone created them to show a dev server running in WSL. Remove them; recreate with `-RemoteAddress LocalSubnet` only if you need it again.

```powershell
Get-NetFirewallRule -DisplayName "WSL2 Port 3000" | Remove-NetFirewallRule
```

The **Microsoft Office Outlook** rule (UDP 6004, Public, any remote) is a legacy Exchange rule. Remove it unless Outlook stops working, in which case Outlook will offer to re-add it:

```powershell
Get-NetFirewallRule -DisplayName "Microsoft Office Outlook" | Remove-NetFirewallRule
```

The two **HNS Container Networking** rules are Hyper-V/WSL internal DNS. Leave them.

**Check:**

```powershell
Get-NetFirewallRule -Enabled True -Direction Inbound -Action Allow | Where-Object { -not $_.Group } | Select-Object DisplayName, Profile
```

Only the two HNS rules should remain.

### Fix 6: Print Spooler and Remote Assistance

If you have **no printer**, stop the Spooler entirely:

```powershell
Stop-Service Spooler; Set-Service Spooler -StartupType Disabled
```

If you **do print locally**, keep it running but refuse remote connections (the audit's "SpoolerRemote" step):

```powershell
New-Item -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\Printers" -Force | Out-Null; Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\Printers" -Name RegisterSpoolerRemoteRpcEndPoint -Type DWord -Value 2; Restart-Service Spooler
```

Turn off Remote Assistance (lets a remote person control your screen after an invite; you do not need it):

```powershell
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Remote Assistance" -Name fAllowToGetHelp -Type DWord -Value 0
```

**Check:**

```powershell
Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Remote Assistance" | Select-Object fAllowToGetHelp
```

Expect `0`.

### Fix 7: Quiet the local-network discovery protocols

LLMNR is already off (good). The rest:

NetBIOS off on every interface (two still had it on):

```powershell
Get-ChildItem "HKLM:\SYSTEM\CurrentControlSet\Services\NetBT\Parameters\Interfaces" | ForEach-Object { Set-ItemProperty -Path $_.PSPath -Name NetbiosOptions -Type DWord -Value 2 }
```

WPAD off (stops Windows from asking the network "where is my proxy?", a classic trick for intercepting traffic):

```powershell
New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp" -Force | Out-Null; Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp" -Name DisableWpad -Type DWord -Value 1; Stop-Service WinHttpAutoProxySvc -Force -ErrorAction SilentlyContinue
```

mDNS off in the Windows resolver (**skip this one if you cast to a Chromecast or similar from this PC**; Chrome has its own mDNS and will keep working for most casting, but some devices need the Windows one):

```powershell
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters" -Name EnableMDNS -Type DWord -Value 0
```

**Check:**

```powershell
Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters" | Select-Object EnableMulticast, EnableMDNS
```

Expect `0` for both (if you skipped mDNS, `EnableMDNS` will be blank).

### Fix 8: Modern authentication only

```powershell
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name LmCompatibilityLevel -Type DWord -Value 5
```

```powershell
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name RestrictAnonymous -Type DWord -Value 1
```

**Check:**

```powershell
Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" | Select-Object LmCompatibilityLevel, RestrictAnonymous
```

Expect `5` and `1`. **Restart the PC** after this fix; these take effect at boot.

### Fix 9 (optional): turn off features you do not use

These each come with a Windows firewall rule open to any address on the Public profile. Off switches, all in Settings:

| Feature | Rules it opens | Where to turn off |
|---|---|---|
| Delivery Optimization from other PCs | TCP/UDP 7680 | Settings > Windows Update > Advanced options > Delivery Optimization > **Allow downloads from other devices: Off** |
| Cast to Device / Wireless Display / Wi-Fi Direct | ~15 rules | Settings > Apps > Optional features > remove **Wireless Display** if present; Settings > System > Projecting to this PC > **Always Off** |
| Nearby sharing (Proximity sharing) | 1 rule, any port | Settings > System > Nearby sharing > **Off** |
| Game Bar, Xbox | 2 rules | Settings > Gaming > Game Bar > Off; uninstall Xbox app if unused |

---

## Part 3: What is already good (leave alone)

- Firewall on for all three profiles, default inbound Block, logging on.
- Both active networks classified **Public**.
- SMB1 disabled; SMB signing required; unencrypted SMB access rejected.
- RDP denied, WinRM disabled, Remote Registry disabled, SSDP and UPnP disabled.
- Secure Boot on, TPM ready.
- LLMNR already off.
- Every established outbound connection in the capture is to an expected owner: Anthropic (Claude), Bitdefender, Google (Drive, Chrome), GitHub, Microsoft. Nothing unexplained.
- Startup programs and scheduled tasks are all recognizable (Bitdefender, OneDrive, Notion, Google Drive, Discord, Edge, Chrome, Brave, Adobe, Windows). `AutorunsMonitor` is a Sysinternals task; if you did not set it up, ask.

---

## Part 4: Re-audit

After Fix 8's restart, run the audit script again (it lives at `Z:\AP BF GNS\6-6999\Audit-Network.ps1`). Expected changes in the findings summary:

- The two account and listener HIGHs: gone or reduced (the Copilot listener will remain if you kept the app; it is fine).
- Defender HIGH: still there, and still a false positive while Bitdefender is active. Ignore it, or edit the script to check `productState` of all registered antivirus products.
- Users share, NetBIOS, LmCompatibilityLevel, Remote Assistance, Spooler, no-group firewall rules: gone.

Keep the before and after folders side by side on the Desktop. If any finding comes **back** on its own later, something is reverting settings and that is worth investigating.
