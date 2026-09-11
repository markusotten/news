# Daily News
*Covering Friday 2026-09-11*

## Citrix

### Security Bulletin

**NetScaler ADC and NetScaler Gateway — CVE-2026-19490 added to CISA KEV.** CISA added CVE-2026-19490 (CWE-288, authentication bypass using an alternate path, CVSS 9.3, critical) to its Known Exploited Vulnerabilities catalog, requiring Federal Civilian Executive Branch agencies to remediate by 2026-09-12. The flaw affects NetScaler ADC and Gateway appliances configured as a Gateway (SSL VPN/ICA Proxy/CVPN/RDP Proxy) or AAA virtual server, letting an unauthenticated remote attacker bypass login and reach functionality that normally requires valid credentials; exploitation attempts were first reported on 2026-09-04. No fix beyond upgrading to 14.1-73.32+ / 13.1-63.21+ is available. (2026-09-10, [source](https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html))

### Products

#### Releases

**Citrix Endpoint Analysis — Latest EPA Libraries.** Updated Endpoint Analysis Plug-in scan libraries for NetScaler Gateway, refreshing the signature set used to check device posture (antivirus, firewall, OS patch level) before granting access. (2026-09-10, [download](http://www.citrix.com/downloads/citrix-endpoint-analysis/epa-libraries/epa-libraries-for-netscaler-gateway.html))

**Citrix Workspace app — Isolated Web Apps (Tech Preview).** A new tech-preview build of Citrix Workspace app for Windows adding support for isolated web apps, letting admins deliver web-based apps in their own sandboxed browser context alongside virtualized apps. (2026-09-10, [download](http://www.citrix.com/downloads/workspace-app/betas-and-tech-previews/workspace-app-tp-iwa.html))

**Citrix Endpoint Management - Fixed issues in CEM 26.8.0.** Fixes an issue where users could not install optional Volume Purchase Program apps through Secure Hub once more than 2,100 licenses were assigned to an app, with installations wrongly redirected to the App Store instead of completing. (2026-09-11, first seen, [what's new](https://docs.citrix.com/en-us/citrix-endpoint-management/whats-new.html))

### Community

**NetScaler WAF Signatures Update v181.** A new NetScaler Web App Firewall signature release covering actively-exploited, CISA KEV-listed vulnerabilities including a critical unauthenticated deserialization flaw in Microsoft SharePoint Server (CVSS 9.8) and a critical SQL injection flaw in WordPress Core (CVSS 9.1), plus Joomla and Langflow issues; signatures are compatible with NetScaler 12.1–14.1. (2026-09-10, [blog](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-waf-signatures-update-v181%C2%A0-r1612/))

**NetScaler WAF Signatures Update v182.** A follow-up NetScaler Web App Firewall signature release covering a critical, CISA KEV-listed unauthenticated remote-code-execution flaw in JetBrains TeamCity (CVSS 9.8) and a critical unauthenticated PHP-upload flaw in the Joomla Content Editor (JCE) extension (CVSS 10.0), alongside additional Joomla and WordPress signatures; compatible with NetScaler 12.1–14.1. (2026-09-10, [blog](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-waf-signatures-update-v182%C2%A0-r1613/))

---

## Metadata

<sub>
Window: 2026-09-10T02:06:47Z → 2026-09-11T02:07:04Z · Last successful run: 2026-09-10T02:06:47Z<br>
Phases run: security, downloads, catalog, whatsnew, press, community<br>
Open defects: 5 — see <code>.skill-bugs.md</code>
</sub>
