# Citrix Product Update - Weekly Rollup
*Covering Monday 2026-08-24 to Sunday 2026-08-30*

## Security Bulletin

**2026-08-28**

**NetScaler ADC and NetScaler Gateway — CVE-2026-8452 confirmed under active exploitation.** A previously patched heap-based buffer overflow (CWE-122, CVSS 8.8 High) in SAML `SignedInfo`/`PrefixList` canonicalization parsing inside the `nsppe` packet-processing engine, on appliances configured as a SAML Service Provider or Identity Provider. An unauthenticated, remote attacker can send a single crafted SAML message to overflow a fixed-size global buffer, corrupt adjacent heap chunk metadata, hijack a function pointer, and execute shellcode as root — a materially worse outcome than Citrix's original "denial of service" classification. Affected: NetScaler ADC/Gateway 13.1 before 13.1-63.18 and 13.1-37.272, and 14.1 before 14.1-72.61 (fix originally shipped 2026-06-30). Remediation: upgrade to 13.1-63.18, 13.1-37.272, or 14.1-72.61 or later; no workaround is available. Exploitation status: actively exploited — following watchTowr Labs' technical write-up and proof-of-concept release on 2026-08-14, security firms observed 36 exploitation attempts from 12 attacker IP addresses across ten countries over 12 days, dropping PHP web shells (`x.php`, `z.php`) and running reconnaissance commands; CISA added the flaw to its Known Exploited Vulnerabilities catalog and ordered federal agencies to remediate by 2026-08-29. ([CTX696604](https://support.citrix.com/external/article/CTX696604/netscaler-adc-and-netscaler-gateway-secu.html))

## Products

### Releases

**2026-08-25**

**Citrix Secure Access Client for macOS 26.08.1.1.** New macOS client build for Citrix Secure Access. (2026-08-24, [Download](http://www.citrix.com/downloads/citrix-secure-access/plug-ins/citrix-secure-access-client-for-macOS.html))

**Citrix Workspace app 2603.50 for ChromeOS.** New ChromeOS build of Citrix Workspace app. (2026-08-24, [Download](http://www.citrix.com/downloads/workspace-app/chrome/workspace-app-for-chrome-latest.html))

**Citrix Workspace app 2603.50 for ChromeOS SDK.** New ChromeOS SDK build accompanying the 2603.50 ChromeOS client release. (2026-08-24, [Download](http://www.citrix.com/downloads/workspace-app/chrome/workspace-app-for-chrome-sdk-latest.html))

**2026-08-26**

**Citrix Remote Browser Isolation - NAT Gateway built into catalog creation.** Network Address Translation (NAT) Gateway is now built directly into the catalog creation flow, removing the previously required separate switch and simplifying setup for administrators provisioning isolated browsing catalogs. (2026-08-25, [What's New](https://docs.citrix.com/en-us/citrix-remote-browser-isolation/whats-new.html))

**Citrix Workspace app - ChromeOS and HTML5 2603.10.** Maintenance releases for the ChromeOS and HTML5 clients focused on overall performance and stability improvements, with no new user-facing features. (2026-08-25, [What's New](https://docs.citrix.com/en-us/citrix-workspace-app/whats-new.html))

**Citrix Workspace app - ChromeOS and HTML5 2603.** Adds keyboard input mode refinement, audio quality improvements with reliable transport protocols, and AOT log content enhancements shared across both clients; the ChromeOS build also gains Service Continuity for connectorless workloads and a loss-tolerant graphics mode, while the HTML5 build adds support for single-tenant Microsoft Entra ID. (2026-08-25, [What's New](https://docs.citrix.com/en-us/citrix-workspace-app/whats-new.html))

### Changes

**2026-08-25**

Added **NetScaler Automation Toolkit** to the product catalog — a new tile on the docs.netscaler.com landing page unifying APIs, IaC templates, SDKs and AI integrations for Day 0–N automation; its documentation lives on GitHub rather than docs.netscaler.com. ([docs.netscaler.com](https://docs.netscaler.com/), [GitHub](https://github.com/netscaler/automation-toolkit))

**2026-08-28**

Added **NetScaler Hardware Platforms** to the product catalog — a standalone docs.netscaler.com doc-set covering NetScaler MPX/SDX physical appliance hardware, distinct from the NetScaler (ADC) software product already tracked. It carries no What's New page. ([docs.netscaler.com](https://docs.netscaler.com/en-us/netscaler-hardware-platforms))

## Press

**2026-08-26**

**Citrix UniconOS dual boot builds business resilience into Windows endpoints.** Citrix announced UniconOS dual boot, available now as part of UniconOS Release 7 2607, which runs a second, hardened UniconOS environment side-by-side with Windows on compatible endpoints — isolated via Secure Boot and independent of the Windows filesystem. If Windows is compromised, corrupted, or unavailable, users can boot into UniconOS and reconnect to their applications through Citrix DaaS and Citrix Secure Access with Chrome Enterprise within minutes, without spare hardware or central reimaging, while security teams investigate the affected Windows environment. Citrix is targeting healthcare, financial services, retail, public sector, and infrastructure customers where downtime carries outsized cost. (2026-08-25, [BusinessWire](https://www.businesswire.com/news/home/20260825838646/en/Citrix-UniconOS-Dual-Boot-Builds-Business-Resilience-Into-Windows-Endpoints-Helping-Enterprises-Recover-Within-Minutes-When-Downtime-Hits))

## Community

**2026-08-26**

**How Citrix UniconOS dual boot turns every Windows endpoint into its own recovery device.** A Tech Zone technical deep dive on the same UniconOS dual boot capability announced today, covering the architecture behind the isolated recovery environment and how it integrates with Citrix DaaS and Secure Access for reconnecting users during a Windows outage. (2026-08-25, [Tech Zone](https://community.citrix.com/techzone-blogs/citrix-unicon/uniconos-dual-boot/))

**2026-08-28**

**How Do I: Automate the deployment of TLS certificates on NetScaler?** A Tech Zone how-to on Zero Touch Certificate deployment, covering why shrinking certificate lifetimes (398 days today, heading to 47 by 2029) make manual create/chain/bind/verify rotation on every NetScaler appliance unsustainable, and how to automate the sequence instead of discovering a missed renewal as a failed handshake in production. (2026-08-27, [Tech Zone](https://community.citrix.com/techzone-blogs/netscaler/how-do-i-automate-the-deployment-of-tls-certificates-on-netscaler-r1605/))

**How St. Luke's University Health Network accelerates patient care with Citrix.** A customer-story video on how the healthcare network uses Citrix to speed clinician access to patient information. (2026-08-27, [YouTube — Citrix](https://www.youtube.com/watch?v=jen6T1Ax_JA))

## Deep Dives

**Citrix UniconOS Dual Boot.** A new endpoint-resiliency capability in UniconOS Release 7 2607 that installs a second, hardened UniconOS environment side-by-side with the primary Windows installation on a compatible endpoint. The two operating environments are isolated from one another via Secure Boot, and the UniconOS side is independent of the Windows filesystem, so corruption, ransomware, or a bad patch affecting Windows cannot touch it. When Windows becomes unavailable, a user selects UniconOS from the boot menu, signs in, and reconnects to their applications through Citrix DaaS and Citrix Secure Access with Chrome Enterprise — all from the same physical device, within minutes.

- *Use cases:* Ransomware or malware incidents that take a Windows fleet offline while forensics is underway; failed OS or driver updates that leave endpoints unbootable; branch or field locations without local IT to swap hardware; regulated industries (healthcare, financial services, public sector) where extended downtime carries SLA, compliance, or safety consequences.
- *Pros:* Recovery measured in minutes rather than the hours-to-days typical of central reimaging or hardware replacement; no spare-hardware inventory required since the recovery environment lives on the same device; security teams can continue investigating the compromised Windows install without pressure to restore it immediately, since users are already productive on the UniconOS side.
- *Cons:* Requires the endpoint to already be enrolled in UniconOS Release 7 2607 and be hardware-compatible with dual boot; UniconOS-side productivity is limited to what's reachable through Citrix DaaS and Secure Access with Chrome Enterprise, not a full local Windows replacement; adds a second OS image to manage and keep current on every covered endpoint.
- *What it changes:* Extends UniconOS — until now primarily a thin, hardened client OS for accessing virtual desktops — into an active business-continuity role for the Windows endpoints it runs alongside, rather than only replacing Windows outright on thin clients.

(2026-08-25, [BusinessWire](https://www.businesswire.com/news/home/20260825838646/en/Citrix-UniconOS-Dual-Boot-Builds-Business-Resilience-Into-Windows-Endpoints-Helping-Enterprises-Recover-Within-Minutes-When-Downtime-Hits), [Tech Zone](https://community.citrix.com/techzone-blogs/citrix-unicon/uniconos-dual-boot/))

---

## Metadata

<sub>
Covering dailies 2026-08-25 → 2026-08-28 · Generated 2026-08-28<br>
Phases run: security, downloads, catalog, whatsnew, press, community, weekly<br>
Open defects: 4 — see <code>.skill-bugs.md</code>
</sub>
