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
