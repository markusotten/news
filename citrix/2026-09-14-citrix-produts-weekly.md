# Citrix Product Update - Weekly Rollup
*Covering Monday 2026-09-07 to Sunday 2026-09-13*

## Security Bulletin

**NetScaler ADC and NetScaler Gateway — CVE-2026-19490 added to CISA KEV.** CISA added CVE-2026-19490 (CWE-288, authentication bypass using an alternate path, CVSS 9.3, critical) to its Known Exploited Vulnerabilities catalog, requiring Federal Civilian Executive Branch agencies to remediate by 2026-09-12. The flaw affects NetScaler ADC and Gateway appliances configured as a Gateway (SSL VPN/ICA Proxy/CVPN/RDP Proxy) or AAA virtual server, letting an unauthenticated remote attacker bypass login and reach functionality that normally requires valid credentials; exploitation attempts were first reported on 2026-09-04. No fix beyond upgrading to 14.1-73.32+ / 13.1-63.21+ is available. (2026-09-10, [source](https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html))

## Products

### Releases

**2026-09-09**

**Citrix Workspace app for Linux - Version 2608 (Technology Preview).** New technology-preview build of the Linux Workspace app, available for testing ahead of general availability. (2026-09-08, http://www.citrix.com/downloads/workspace-app/betas-and-tech-previews/workspace-app-tp-for-linux.html)

**2026-09-11**

**Citrix Endpoint Analysis — Latest EPA Libraries.** Updated Endpoint Analysis Plug-in scan libraries for NetScaler Gateway, refreshing the signature set used to check device posture (antivirus, firewall, OS patch level) before granting access. (2026-09-10, http://www.citrix.com/downloads/citrix-endpoint-analysis/epa-libraries/epa-libraries-for-netscaler-gateway.html)

**Citrix Workspace app — Isolated Web Apps (Tech Preview).** A new tech-preview build of Citrix Workspace app for Windows adding support for isolated web apps, letting admins deliver web-based apps in their own sandboxed browser context alongside virtualized apps. (2026-09-10, http://www.citrix.com/downloads/workspace-app/betas-and-tech-previews/workspace-app-tp-iwa.html)

**Citrix Endpoint Management - Fixed issues in CEM 26.8.0.** Fixes an issue where users could not install optional Volume Purchase Program apps through Secure Hub once more than 2,100 licenses were assigned to an app, with installations wrongly redirected to the App Store instead of completing. (2026-09-11, first seen, https://docs.citrix.com/en-us/citrix-endpoint-management/whats-new.html)

## Community

**2026-09-08**

**Citrix Connect Pulse Sydney.** One-day customer event covering infrastructure, cloud, security and end-user-computing topics through keynotes, customer case studies and Birds-of-a-Feather discussions aimed at modernizing and securing Citrix environments. (2026-09-08, Sydney, https://community.citrix.com/events/event/150-citrix-connect-pulse-sydney/)

**Citrix NetScaler AI Gateway + Protecto: Securing Enterprise LLM Traffic.** Webinar demonstrating how NetScaler AI Gateway paired with Protecto secures LLM traffic at the infrastructure layer, with NetScaler handling routing, policy and observability while Protecto masks or tokenizes sensitive data in prompts and agent workflows before it reaches the model. (2026-09-08, online session, https://community.citrix.com/events/event/157-citrix-netscaler-ai-gateway-protecto-securing-enterprise-llm-traffic/)

**2026-09-09**

**Citrix Connect Pulse Toronto.** Regional edition of Citrix Connect focused on Citrix vision and strategy, practical guidance for stabilizing and upgrading environments, and ways for admins to reduce infrastructure complexity. (2026-09-09, Toronto, https://community.citrix.com/events/event/147-citrix-connect-pulse-toronto/)

**2026-09-10**

**Citrix Connect Pulse Arlington.** Regional edition of Citrix Connect focused on Citrix vision and strategy, practical guidance for stabilizing and upgrading environments, and ways for admins to reduce infrastructure complexity. (2026-09-15, Arlington, https://community.citrix.com/events/event/148-citrix-connect-pulse-arlington/)

**Learn how to configure NetScaler Gateway with SAML Service Provider Authentication for Secure Citrix Remote Access.** A new Tech Zone deployment guide walking through configuring NetScaler Gateway as a SAML service provider for secure remote access to Citrix resources, provided as a customizable implementation template. (2026-09-09, https://community.citrix.com/tech-zone/build/deployment-guides/learn-how-to-configure-netscaler-gateway-with-saml-service-provider-authentication-for-secure-citrix-remote-access-r381/)

**Managing TLS at enterprise scale in a world of short-lived certificates.** A Tech Zone blog post on why certificate lifetimes are shrinking industry-wide and how NetScaler administrators can move from manual renewal tracking to ACME-based automated certificate management at scale. (2026-09-10, https://community.citrix.com/techzone-blogs/netscaler/managing-tls-at-enterprise-scale-in-a-world-of-short-lived-certificates-r1611/)

**2026-09-11**

**NetScaler WAF Signatures Update v181.** A new NetScaler Web App Firewall signature release covering actively-exploited, CISA KEV-listed vulnerabilities including a critical unauthenticated deserialization flaw in Microsoft SharePoint Server (CVSS 9.8) and a critical SQL injection flaw in WordPress Core (CVSS 9.1), plus Joomla and Langflow issues; signatures are compatible with NetScaler 12.1–14.1. (2026-09-10, https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-waf-signatures-update-v181%C2%A0-r1612/)

**NetScaler WAF Signatures Update v182.** A follow-up NetScaler Web App Firewall signature release covering a critical, CISA KEV-listed unauthenticated remote-code-execution flaw in JetBrains TeamCity (CVSS 9.8) and a critical unauthenticated PHP-upload flaw in the Joomla Content Editor (JCE) extension (CVSS 10.0), alongside additional Joomla and WordPress signatures; compatible with NetScaler 12.1–14.1. (2026-09-10, https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-waf-signatures-update-v182%C2%A0-r1613/)

---

## Metadata

<sub>
Covering dailies 2026-09-07 → 2026-09-11 · Generated 2026-09-11<br>
Phases run: security, downloads, catalog, whatsnew, press, community, weekly<br>
Open defects: 5 — see <code>.skill-bugs.md</code>
</sub>
