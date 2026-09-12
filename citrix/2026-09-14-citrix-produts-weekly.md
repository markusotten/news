# Citrix Product Update - Weekly Rollup
*Covering Monday 2026-09-07 to Sunday 2026-09-13*

## Security Bulletin

**NetScaler ADC and NetScaler Gateway — CVE-2026-19490 added to CISA KEV.** CISA added CVE-2026-19490 (CWE-288, authentication bypass using an alternate path, CVSS 9.3, critical) to its Known Exploited Vulnerabilities catalog, requiring Federal Civilian Executive Branch agencies to remediate by 2026-09-12. The flaw affects NetScaler ADC and Gateway appliances configured as a Gateway (SSL VPN/ICA Proxy/CVPN/RDP Proxy) or AAA virtual server, letting an unauthenticated remote attacker bypass login and reach functionality that normally requires valid credentials; exploitation attempts were first reported on 2026-09-04. No fix beyond upgrading to 14.1-73.32+ / 13.1-63.21+ is available. (2026-09-10, [source](https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html))

## Products

### Releases

**2026-09-09**

**Citrix Workspace app for Linux - Version 2608 (Technology Preview).** New technology-preview build of the Linux Workspace app, available for testing ahead of general availability. (2026-09-08, [download](http://www.citrix.com/downloads/workspace-app/betas-and-tech-previews/workspace-app-tp-for-linux.html))

**2026-09-11**

**Citrix Endpoint Analysis — Latest EPA Libraries.** Updated Endpoint Analysis Plug-in scan libraries for NetScaler Gateway, refreshing the signature set used to check device posture (antivirus, firewall, OS patch level) before granting access. (2026-09-10, [download](http://www.citrix.com/downloads/citrix-endpoint-analysis/epa-libraries/epa-libraries-for-netscaler-gateway.html))

**Citrix Workspace app — Isolated Web Apps (Tech Preview).** A new tech-preview build of Citrix Workspace app for Windows adding support for isolated web apps, letting admins deliver web-based apps in their own sandboxed browser context alongside virtualized apps. (2026-09-10, [download](http://www.citrix.com/downloads/workspace-app/betas-and-tech-previews/workspace-app-tp-iwa.html))

**Citrix Endpoint Management - Fixed issues in CEM 26.8.0.** Fixes an issue where users could not install optional Volume Purchase Program apps through Secure Hub once more than 2,100 licenses were assigned to an app, with installations wrongly redirected to the App Store instead of completing. (2026-09-11, first seen, [what's new](https://docs.citrix.com/en-us/citrix-endpoint-management/whats-new.html))

**2026-09-12**

**Citrix DaaS - Citrix Advisor: Scheduled runs and Home page widget.** Advisor can now run its site health checks automatically on a recurring weekly schedule, keeping each report on file for up to 90 days instead of requiring a manual run. A new Advisor widget on the Home page also surfaces recommendations grouped by impact and filterable by category, so admins can spot and act on critical items without opening the full Advisor view. (2026-09-12, first seen, [what's new](https://docs.citrix.com/en-us/citrix-daas/whats-new.html))

### Changes

**2026-09-12**

**Citrix SD-WAN added to the catalog.** Reconciliation against `docs.netscaler.com`'s product index found the whole Citrix SD-WAN product line (main product plus Center, Orchestrator, Orchestrator for On-premises, Platforms and WANOP sub-components) documented but never tracked in the product catalog, despite already having its own download RSS feed. Added as a single catalog row (sub-components roll up under it, matching how other multi-component product lines are tracked); it has no dedicated what's-new page. ([docs](https://docs.netscaler.com/en-us/citrix-sd-wan))

## Community

**2026-09-08**

**Citrix Connect Pulse Sydney.** One-day customer event covering infrastructure, cloud, security and end-user-computing topics through keynotes, customer case studies and Birds-of-a-Feather discussions aimed at modernizing and securing Citrix environments. (2026-09-08, Sydney, [event](https://community.citrix.com/events/event/150-citrix-connect-pulse-sydney/))

**2026-09-09**

**Citrix Connect Pulse Toronto.** Regional edition of Citrix Connect focused on Citrix vision and strategy, practical guidance for stabilizing and upgrading environments, and ways for admins to reduce infrastructure complexity. (2026-09-09, Toronto, [event](https://community.citrix.com/events/event/147-citrix-connect-pulse-toronto/))

**2026-09-10**

**Learn how to configure NetScaler Gateway with SAML Service Provider Authentication for Secure Citrix Remote Access.** A new Tech Zone deployment guide walking through configuring NetScaler Gateway as a SAML service provider for secure remote access to Citrix resources, provided as a customizable implementation template. (2026-09-09, [article](https://community.citrix.com/tech-zone/build/deployment-guides/learn-how-to-configure-netscaler-gateway-with-saml-service-provider-authentication-for-secure-citrix-remote-access-r381/))

**Managing TLS at enterprise scale in a world of short-lived certificates.** A Tech Zone blog post on why certificate lifetimes are shrinking industry-wide and how NetScaler administrators can move from manual renewal tracking to ACME-based automated certificate management at scale. (2026-09-10, [blog](https://community.citrix.com/techzone-blogs/netscaler/managing-tls-at-enterprise-scale-in-a-world-of-short-lived-certificates-r1611/))

**2026-09-11**

**NetScaler WAF Signatures Update v181.** A new NetScaler Web App Firewall signature release covering actively-exploited, CISA KEV-listed vulnerabilities including a critical unauthenticated deserialization flaw in Microsoft SharePoint Server (CVSS 9.8) and a critical SQL injection flaw in WordPress Core (CVSS 9.1), plus Joomla and Langflow issues; signatures are compatible with NetScaler 12.1–14.1. (2026-09-10, [blog](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-waf-signatures-update-v181%C2%A0-r1612/))

**NetScaler WAF Signatures Update v182.** A follow-up NetScaler Web App Firewall signature release covering a critical, CISA KEV-listed unauthenticated remote-code-execution flaw in JetBrains TeamCity (CVSS 9.8) and a critical unauthenticated PHP-upload flaw in the Joomla Content Editor (JCE) extension (CVSS 10.0), alongside additional Joomla and WordPress signatures; compatible with NetScaler 12.1–14.1. (2026-09-10, [blog](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-waf-signatures-update-v182%C2%A0-r1613/))

**2026-09-12**

**How Do I: Get started with NetScaler AI Gateway for enterprise LLM deployments?** A Tech Zone walkthrough on placing a NetScaler in front of AI applications talking to Azure OpenAI and other OpenAI-compatible backends, giving platform teams token-aware load balancing, per-user rate limiting and AI-specific observability, all configured from the NetScaler CLI. (2026-09-11, [blog](https://community.citrix.com/techzone-blogs/netscaler/how-do-i-get-started-with-netscaler-ai-gateway-for-enterprise-llm-deployments-r1615/))

**Citrix NetScaler AI Gateway + Protecto: Securing Enterprise LLM Traffic.** Webinar on pairing NetScaler AI Gateway with Protecto to secure AI/LLM traffic at the infrastructure layer — NetScaler handles routing, authentication, policy enforcement and observability for LLM/MCP traffic, while Protecto applies semantic-aware masking/tokenization to sensitive data (PII/PHI) in prompts and agent workflows without breaking model context. First announced as an upcoming online session; the recorded replay is now published. (2026-09-11, [video](https://www.youtube.com/watch?v=k4BgwH1BkYA), Citrix)

**Citrix Connect Pulse Arlington.** Regional edition of Citrix Connect focused on Citrix vision and strategy, practical guidance for stabilizing and upgrading environments, and ways for admins to reduce infrastructure complexity. (2026-09-15, Arlington, [event](https://community.citrix.com/events/event/148-citrix-connect-pulse-arlington/))

---

## Metadata

<sub>
Covering dailies 2026-09-07 → 2026-09-12 · Generated 2026-09-12<br>
Phases run: security, downloads, catalog, whatsnew, press, community, weekly<br>
Open defects: 5 — see <code>.skill-bugs.md</code>
</sub>
