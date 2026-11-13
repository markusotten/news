# Citrix Product Updates
*Last 24 hours — 2026-11-13*

## Citrix

### Adaptive Authentication Service

- **November 2026 security update (Nov 12, 2026):** Adaptive Authentication instances are automatically upgraded to NetScaler build 14.1-73.57 or later, which fixes the vulnerabilities in security bulletin [CTX697305](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697305). Customers do not need to do anything. ([Adaptive Authentication release notes](https://docs.citrix.com/en-us/adaptive-authentication/adaptive-authentication-release-notes.html))

### Citrix SecurAccess client for Windows (formerly Citrix Secure Access)

- **26.11.1.6 – Product renamed (Nov 12, 2026):** The Citrix Secure Access client is now called Citrix SecurAccess. The same rename applies to the Linux, macOS/iOS and Android clients below. ([Windows release notes](https://docs.citrix.com/en-us/citrix-secure-access/citrix-secure-access-for-windows/windows-plug-in-release-notes.html))
- **26.11.1.6 – PAC-file proxy settings follow split tunneling (Nov 12, 2026):** When you use a proxy auto-config (PAC) file, SecurAccess now moves its changed proxy settings to the Windows web proxy. As a result, Chrome, Edge and other apps that use the Windows proxy settings follow the VPN split-tunnel rules. This is on by default and you don't need to change the PAC file. ([Windows release notes](https://docs.citrix.com/en-us/citrix-secure-access/citrix-secure-access-for-windows/windows-plug-in-release-notes.html))
- **26.11.1.6 – One installer for SecurAccess and the device posture client (Nov 12, 2026):** `AGEE_setup.exe` can now install the device posture client in the same step. Use `INSTALLDPC=1` on the command line, or set the `InstallDPC` registry value. ([Windows release notes](https://docs.citrix.com/en-us/citrix-secure-access/citrix-secure-access-for-windows/windows-plug-in-release-notes.html))
- **26.11.1.6 – Full disconnect on Log Out in Always On mode (Nov 12, 2026):** If both machine and user tunnels are configured, Log Out can now close both tunnels. The device then stays off the corporate network until the user signs in again. This needs client control and the `EnableLogoutFullDisconnect` registry value. ([Windows release notes](https://docs.citrix.com/en-us/citrix-secure-access/citrix-secure-access-for-windows/windows-plug-in-release-notes.html))
- **26.11.1.6 – Fixed issues (Nov 12, 2026):** Fixes include DNS failures when Zscaler Client Connector is also installed (now handled with the `EnableDnsProxy` and `DnsExcludeApps` registry settings), smart cards that use a legacy CryptoAPI provider, disconnects caused by periodic EPA scans, and intermittent DNS/TCP failures during long VPN sessions. ([Windows release notes](https://docs.citrix.com/en-us/citrix-secure-access/citrix-secure-access-for-windows/windows-plug-in-release-notes.html))

### Citrix SecurAccess client for Linux

- **26.10.4 – Network latency in Citrix Monitor (Nov 12, 2026):** In cloud and hybrid SecurAccess ZTNA deployments, the Linux client now reports round-trip latency to the ZTNA service or NetScaler Gateway, and admins can view it in Citrix Monitor. ([Linux release notes](https://docs.citrix.com/en-us/citrix-secure-access/secure-access-client-linux/linux-plug-in-release-notes.html))
- **26.10.4 – New notification center and connection management (Nov 12, 2026):** The client UI adds a notification center that collects alerts in one place and makes it easier to manage several connections. ([Linux release notes](https://docs.citrix.com/en-us/citrix-secure-access/secure-access-client-linux/linux-plug-in-release-notes.html))
- **26.10.4 – eLux OS support (Nov 12, 2026):** The Linux client is now supported on eLux OS 7, image 2609 or later. ([Linux release notes](https://docs.citrix.com/en-us/citrix-secure-access/secure-access-client-linux/linux-plug-in-release-notes.html))
- **26.10.4 – Fixed issues (Nov 12, 2026):** Fixes ZTNA sign-in failures. Intranet apps with addresses in the carrier-grade NAT range are reachable again. ([Linux release notes](https://docs.citrix.com/en-us/citrix-secure-access/secure-access-client-linux/linux-plug-in-release-notes.html))

### Citrix SecurAccess for macOS/iOS

- **V26.10.1 / V26.10.1.1 – Rebranded release (Nov 12, 2026):** These releases rename the app to Citrix SecurAccess. No other functional changes are listed. ([macOS/iOS release notes](https://docs.citrix.com/en-us/citrix-secure-access/citrix-sso-for-ios-macos-devices/citrix-sso-release-notes-ios-macos.html))

### Citrix SecurAccess for Android

- **V26.10.1 – Legacy device administrator VPN provisioning deprecated (Nov 12, 2026):** Provisioning VPN profiles through MDM in Android device administrator mode is deprecated and will be removed in a later release. MDM admins should move to Android Enterprise-based configurations. This release also includes the rename to SecurAccess. ([Android release notes](https://docs.citrix.com/en-us/citrix-secure-access/citrix-sso-for-android-devices/citrix-sso-release-notes-android.html))

### Citrix SecurSpaces

- **26.9.7 – Traefik routing for central deployments and external regions (released Nov 11, docs published Nov 12, 2026):** Traefik routes now cover HTTPS, SSH and proxy traffic for central deployments and external regions. ([SecurSpaces release notes](https://docs.citrix.com/en-us/securspaces/release-notes/fixed-issues.html))
- **26.9.7 – More SCIM group operations (released Nov 11, docs published Nov 12, 2026):** SCIM now supports removing filtered group members, replacing the whole membership list, and updating groups without a PATCH path. ([SecurSpaces release notes](https://docs.citrix.com/en-us/securspaces/release-notes/fixed-issues.html))
- **26.9.7 – Security fixes (released Nov 11, docs published Nov 12, 2026):** Workspace resume links can no longer redirect to addresses outside the platform. Removing members or groups through SCIM now also removes shared-workspace access. ([SecurSpaces release notes](https://docs.citrix.com/en-us/securspaces/release-notes/fixed-issues.html))
- **26.9.7 – General fixes (released Nov 11, docs published Nov 12, 2026):** Fixes include DaaS session-expiry prompts and repeated reauthentication notices, partial or conflicting SCIM group updates, and several workspace-from-template and creation-wizard issues. ([SecurSpaces release notes](https://docs.citrix.com/en-us/securspaces/release-notes/fixed-issues.html))

## NetScaler

### NetScaler ADC / NetScaler Gateway 14.1 (Build 14.1-73.58)

- **New build 14.1-73.58 (Nov 12, 2026):** This build replaces 14.1-73.49 and fixes GOPHDX-9751, NSHELP-42791, NSHELP-44589, NSHELP-44985, NSHELP-45059, NSHELP-44524 and NSHELP-45833. Builds 14.1-73.57 and later fix the vulnerabilities in [CTX697305](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697305). ([NetScaler 14.1 release notes](https://docs.netscaler.com/en-us/citrix-adc/current-release/citrix-adc-release-notes.html), [Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20ADC%20(includes%20NetScaler%20Gateway)&version=14.1&build=73.58))
- **Connection pooling for the ExtraHop integration (Nov 12, 2026):** NetScaler now reuses connections when it sends TLS session secrets to ExtraHop, which lowers latency at the start of each session. You set it up with a WASM-module service and a `warmup_connection_count` setting (1–8 per packet engine). ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20ADC%20(includes%20NetScaler%20Gateway)&version=14.1&build=73.58))
- **NetScaler VPX on Google Cloud C4 and C4D instances (Nov 12, 2026):** VPX is now qualified on GCP C4 and C4D machine families, with validated gVNIC/GVE driver support, so you can run it on newer high-performance instance types. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20ADC%20(includes%20NetScaler%20Gateway)&version=14.1&build=73.58))
- **Higher API session token limits (Nov 12, 2026):** The limit on concurrent API session tokens is raised, which helps automation-heavy environments. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20ADC%20(includes%20NetScaler%20Gateway)&version=14.1&build=73.58))
- **Warning on untagged VLAN assignment (Nov 12, 2026):** NetScaler now warns when you assign an untagged VLAN, to help prevent accidental network misconfiguration. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20ADC%20(includes%20NetScaler%20Gateway)&version=14.1&build=73.58))
- **GSLB context in OAuth grant tokens (Nov 12, 2026):** OAuth grant tokens can now carry GSLB context, so OAuth authentication works across GSLB sites. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20ADC%20(includes%20NetScaler%20Gateway)&version=14.1&build=73.58))

### NetScaler ADC / NetScaler Gateway 13.1 (Build 13.1-64.39)

- **New build 13.1-64.39 (Nov 12, 2026):** This is a new 13.1 release build, the first since 13.1-63.21 (Aug 19). ([NetScaler 13.1 release notes](https://docs.netscaler.com/en-us/citrix-adc/13-1/citrix-adc-release-notes.html), [Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20ADC%20(includes%20NetScaler%20Gateway)&version=13.1&build=64.39))
- **URL normalization (Nov 12, 2026):** HTTP profiles can now normalize incoming URLs (case, percent-encoding, path segments, duplicate slashes) before any other module evaluates them. This closes off filter-bypass tricks that rely on non-normalized URLs. You enable it with `set httpprofile <name> -normalizeURL ENABLED`, and you can also send the normalized URL to the origin with `-normalizeURLtoOrigin ENABLED`. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20ADC%20(includes%20NetScaler%20Gateway)&version=13.1&build=64.39))
- **Time-window log collection for tech support bundles (Nov 12, 2026):** The new `-period` parameter of `show techsupport -time` collects newnslog, text logs and non-PE cores only for a set number of hours around a given time. The GUI offers this through a Custom option. Bundles are smaller and contain more relevant data. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20ADC%20(includes%20NetScaler%20Gateway)&version=13.1&build=64.39))
- **New global TCP parameter for enhanced ISN generation (Nov 12, 2026):** A new global TCP setting improves how TCP initial sequence numbers are generated. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20ADC%20(includes%20NetScaler%20Gateway)&version=13.1&build=64.39))
- **Better out-of-order packet handling with enhanced ISN (Nov 12, 2026):** Out-of-order packets are handled better when enhanced ISN generation is in use. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20ADC%20(includes%20NetScaler%20Gateway)&version=13.1&build=64.39))

### NetScaler FIPS

- **New FIPS builds 14.1-73.58 and 13.1-37.293 (Nov 12, 2026):** New FIPS release builds are available for 14.1 and 13.1. ([FIPS 14.1 release notes](https://docs.netscaler.com/en-us/citrix-adc/current-release/fips/netscaler-fips-release-notes.html), [FIPS 13.1 release notes](https://docs.netscaler.com/en-us/citrix-adc/13-1/fips/netscaler-fips-release-notes.html))

### NetScaler Console on-prem (ADM) 14.1 (Build 14.1-74.34)

- **New build 14.1-74.34 (Nov 12, 2026):** This build fixes the vulnerabilities in [CTX697320](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697320). ([Console on-prem release notes](https://docs.netscaler.com/en-us/netscaler-application-delivery-management-software/current-release/release-notes.html), [Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20Console%20on-prem%20(ADM)&version=14.1&build=74.34))
- **RADIUS Message-Authenticator for admin authentication (Nov 12, 2026):** RADIUS admin logins now support the Message-Authenticator attribute, which protects them against RADIUS response-forgery attacks. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20Console%20on-prem%20(ADM)&version=14.1&build=74.34))
- **CVE scan support for FIPS instances (Nov 12, 2026):** Security Advisory can now scan NetScaler FIPS instances for CVEs. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20Console%20on-prem%20(ADM)&version=14.1&build=74.34))
- **Custom CA support for ACME-based certificate renewal (Nov 12, 2026):** ACME renewal can now use a custom or private certificate authority, not only public ACME CAs. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20Console%20on-prem%20(ADM)&version=14.1&build=74.34))
- **Unified certificate source experience and import pre-checks (Nov 12, 2026):** SSL certificate management now has one consistent way to choose the certificate source, and it checks certificates before import. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20Console%20on-prem%20(ADM)&version=14.1&build=74.34))
- **Certificate source visibility and bound certificate protection (Nov 12, 2026):** The Console now shows where each certificate came from and protects certificates that are bound to entities from accidental changes. ([Build details](https://docs.netscaler.com/en-us/updates.html?product=NetScaler%20Console%20on-prem%20(ADM)&version=14.1&build=74.34))

### NetScaler Console service

- **Security Advisory detects 28 more CVEs (Nov 12, 2026):** Security Advisory can now find and help remediate CVE-2026-107407 to -107415, CVE-2026-111340 to -111349 and CVE-2026-120860 to -120868. Detection needs a version scan, and remediation means upgrading affected instances to a fixed build. ([NetScaler Console service – What's new](https://docs.netscaler.com/en-us/netscaler-console-service/release-notes/whats-new.html))

---

<sub>
Window: 2026-11-12 ~02:20 UTC → 2026-11-13 ~02:20 UTC · Sources: page "last-modified" metadata and entry dates on the What's New / release-notes pages of docs.citrix.com, docs.netscaler.com, docs.xenserver.com<br>
XenServer: pages republished Nov 12 but no new entries since the previous report. CVAD LTSR, WEM, Citrix Cloud, RBI and SecurAccess ZTNA pages were republished without new entries in the window. Title-only NetScaler items are summarized from their release-note titles.
</sub>
