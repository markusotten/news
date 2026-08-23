# Citrix Product Update - Weekly Rollup
*Covering Monday 2026-08-17 to Sunday 2026-08-23*

## Security Bulletin

**2026-08-21**

**NetScaler ADC and NetScaler Gateway — CVE-2026-19489 and CVE-2026-19490.** Two vulnerabilities affect customer-managed NetScaler ADC and NetScaler Gateway (including FIPS and FIPS/NDcPP builds); Citrix-managed cloud services and Adaptive Authentication are patched by Cloud Software Group directly. CVE-2026-19490 (CWE-288, Authentication bypass using an alternate path, CVSS 9.3, Critical) lets a remote, unauthenticated attacker bypass authentication on an appliance configured as a Gateway (SSL VPN, ICA Proxy, CVPN, or RDP Proxy) or as an AAA virtual server, with the exact precondition depending on firmware version and whether a SAML action is configured; admins can check exposure by looking for `add authentication samlAction .*`, `add authentication vserver .*`, or `add vpn vserver .*` in their running configuration. CVE-2026-19489 (CWE-119, Memory overflow, CVSS 8.8, Critical) allows a remote, unauthenticated attacker to trigger unpredictable behavior or a denial of service on appliances with SIP ALG enabled inside a Large Scale NAT group configuration (`add lsn group.*sipalg.*`). Affected: NetScaler ADC/Gateway 14.1 before 14.1-73.32, 13.1 before 13.1-63.21, ADC FIPS before 14.1-73.32 FIPS, and ADC FIPS/NDcPP before 13.1-37.277. Fixed: 14.1-73.32+, 13.1-63.21+, 14.1-73.32 FIPS+, and 13.1-37.277+ respectively. No workaround is available for either flaw — Citrix's only remediation is to install the fixed build immediately. As of 2026-08-20, no public proof-of-concept or evidence of active exploitation had been reported for either CVE, though researchers note NetScaler authentication-bypass flaws are historically fast-followed by exploitation given the product's perimeter-facing deployment footprint. Reported by Samarth Vashisht of JPMorgan Chase's penetration-testing team. ([CTX696939](https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html))

## Products

### Releases

**2026-08-21**

**NetScaler ADC/Gateway 14.1 Build 73.33 and 13.1 Build 63.21/37.277 (Maintenance Phase).** New maintenance-release builds across the 14.1 and 13.1 branches — VPX, VPX FIPS, CPX, BLX and appliance firmware, plus matching Citrix Gateway 14.1/13.1 builds — superseding the minimum fixed versions named in the CVE-2026-19489/CVE-2026-19490 bulletin above. (2026-08-19, [NetScaler 14.1 firmware](http://www.citrix.com/downloads/citrix-adc/firmware/release-14-1-build-73-33.html), [NetScaler 13.1 firmware](http://www.citrix.com/downloads/citrix-adc/firmware/release-13-1-build-63-21.html), [NetScaler VPX FIPS 14.1](http://www.citrix.com/downloads/citrix-adc/virtual-appliances/netscaler-vpx-release-141-73-33-fips.html), [NetScaler VPX FIPS 13.1](http://www.citrix.com/downloads/citrix-adc/virtual-appliances/netscaler-vpx-release-131-FIPS.html), [Citrix Gateway 14.1](http://www.citrix.com/downloads/citrix-gateway/product-software/citrix-gateway-14-1-build-73-33.html), [Citrix Gateway 13.1](http://www.citrix.com/downloads/citrix-gateway/product-software/citrix-gateway-13-1-build-63-21.html))

**Citrix Virtual Apps and Desktops 7 2607 Current Release wave.** New 2607 current-release builds shipped together for the CVAD stack: Citrix Virtual Apps and Desktops 7 2607 (All Editions), Citrix Probe Agent 2607, Workspace Environment Management 2607, Citrix Provisioning 2607 LTSR, Federated Authentication Service 10.24 (for CVAD 2607), and Citrix Workspace app 2607 for Mac. The Mac client adds a generally-available Microsoft Teams VDI plugin (installed by default), version-rollback support and faster side-by-side silent updates, session pre-launch, improved Point-of-Presence selection, and several Technical Preview items (DNS caching, EDT MTU rediscovery, streaming Client Drive Mapping, HDX Direct for connectorless Service Continuity, HDX graphics super resolution, virtual-session location redirection, and resilient third-party plugin execution). (2026-08-18/2026-08-19, [CVAD 2607](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/product-software/citrix-virtual-apps-and-desktops-alleditions-2607.html), [Probe Agent](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/components/app-probe-agent.html), [WEM 2607](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/components/workspace-environment-management-2607.html), [Provisioning 2607 LTSR](http://www.citrix.com/downloads/provisioning-services/product-software/provisioning-services-2607.html), [FAS 10.24](http://www.citrix.com/downloads/federated-authentication-service/product-software/fas-2607.html), [Workspace app for Mac 2607](http://www.citrix.com/downloads/workspace-app/mac/workspace-app-for-mac-latest.html), [Mac what's new](https://docs.citrix.com/en-us/citrix-workspace-app/whats-new.html))

**Citrix Virtual Apps and Desktops 7 2507 LTSR, Cumulative Update 2.** New LTSR cumulative update covering the 2507 branch, released alongside a matching Linux Virtual Delivery Agent 2507 LTSR CU2 and StoreFront 2507 LTSR CU2. (2026-08-18, [CVAD 2507 LTSR CU2](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/product-software/citrix-virtual-apps-and-desktops-2507ltsr-cu2.html), [Linux VDA 2507 LTSR CU2](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/components/linux-vda-2507-ltsr-cu2.html), [StoreFront 2507 LTSR CU2](http://www.citrix.com/downloads/storefront/product-software/storefront-2507-CU2.html))

**StoreFront 2607 LTSR.** New LTSR release of StoreFront, adding an optional detailed desktop tile for the modern experience (thumbnail, OS, power status including new Under maintenance/Unavailable states, last-connected time, active session duration) and PowerShell control over which power actions are exposed to end users for persistent desktops. (2026-08-18, [Download](http://www.citrix.com/downloads/storefront/product-software/storefront-2607.html), [What's new](https://docs.citrix.com/en-us/storefront/current-release/whats-new.html))

**uberAgent 8.1.** New release of the uberAgent endpoint-monitoring product: adds an IGEL OS 12 app for Linux endpoints (deployable via the IGEL Universal Management Suite, requiring IGEL OS 12.8.0+; manual install only until it reaches the IGEL App Portal), discontinues the Azure Monitor output backend ahead of Microsoft's September 2026 retirement of the HTTP Data Collector API, improves Citrix VDA detection, and updates the bundled Splunk dashboard's licensing-status visualization. (2026-08-18/2026-08-19, [Download](http://www.citrix.com/downloads/citrix-monitoring-observability/uberAgent-Product-Software/8-1.html), [What's new](https://docs.citrix.com/en-us/uberagent/8-x/whats-new/8-1))

**License Server for Windows 11.17.2.0 (Build 56200).** New build of the Citrix Licensing server for Windows. (2026-08-17, [Download](http://www.citrix.com/downloads/licensing/license-server/license-server-version-111720-56200-for-windows.html))

**Citrix Workspace app for Windows LTSR 2607 Technical Preview.** New LTSR technical-preview build of Workspace app for Windows. (2026-08-18, [Download](http://www.citrix.com/downloads/workspace-app/betas-and-tech-previews/workspace-app-for-windows-tech-preview.html))

**Browser Content Redirection files for Workspace app (Mac).** Updated Browser Content Redirection component files for Citrix Workspace app on macOS. (2026-08-19, [Download](http://www.citrix.com/downloads/workspace-app/browser-content-redirection-mac/bcr-files.html))

**Unicon eLux Scout software packages — LTSR and CR.** New UniconOS (eLux) software package releases for both the LTSR and Current Release (CR) branches. (2026-08-19 LTSR / 2026-08-18 CR, [LTSR packages](http://www.citrix.com/downloads/Elux-Download-Pages/Elux-Software-Packages/eLux-Software-Packages-LTSR.html), [CR packages](http://www.citrix.com/downloads/Elux-Download-Pages/Elux-Software-Packages/eLux-Software-Packages-CR.html))

### Changes

**2026-08-17**

- **Added:** "XenServer SDK" — the docs.xenserver.com landing page lists a "Develop for XenServer" section (PowerShell, Python, C, Go and Java client libraries) as a peer navigation entry alongside XenCenter, XenServer 8 and XenServer 9, previously untracked. It has no what's-new page. https://docs.xenserver.com/en-us/xenserver/developer

**2026-08-21**

- **Added:** "Citrix Always On Tracing" (AOT), a diagnostic framework that continuously captures Citrix Diagnostic Facility (CDF) traces and other component logs across a Citrix Virtual Apps and Desktops environment for troubleshooting common failures — a peer navigation entry on the docs.citrix.com landing page, previously untracked. It has no what's-new page. https://docs.citrix.com/en-us/citrix-always-on-tracing

## Press

**2026-08-21**

**Citrix Virtual Apps and Desktops 2607 LTSR: Why standing still costs more than upgrading.** Shawn Bass previews the CVAD 2607 LTSR release, citing internal testing showing roughly a 14% reduction in bandwidth consumption versus the prior version, Azure VM cost estimation built into provisioning workflows, AI-assisted analysis that surfaces security findings from session recordings automatically, faster logons via enhanced Workspace Environment Management, and HDX graphics super resolution offloaded to endpoint GPUs instead of server resources. (2026-08-19, [Citrix Blog](https://www.citrix.com/blogs/2026/08/19/citrix-virtual-apps-and-desktops-2607-ltsr/))

## Community

**2026-08-17**

**XenServer 9 Deep Dive Webinar.** Citrix's Tech Zone community events calendar lists a "Deep Dive Webinar Series - Inside Citrix XenServer 9: Updates, strategy, and roadmap," presented by the XenServer Product Management team (Jose Augustin and Marshall Wu), covering security, streamed updates, performance and migration considerations for XenServer 9. Thursday, 2026-08-20, 15:00 UTC, online. https://community.citrix.com/events/event/151-deep-dive-webinar-series-inside-citrix-xenserver-9-updates-strategy-and-roadmap/

**2026-08-21**

**CVAD 2607 LTSR: What's worth your attention in this release.** A Tech Zone blog walks admins through the operationally significant parts of CVAD 2607 LTSR beyond the headline features: a new Service Window lets teams schedule OS disk resets, hardware changes, AD account repair, and Entra Hybrid Join conversion through Web Studio or PowerShell on a controlled schedule; existing AD-joined MCS catalogs can now convert to Entra Hybrid Join in place, for both persistent and non-persistent VMs, without a rebuild; and Citrix Director gains real-time machine diagnostic insights (refreshed every 15 minutes) integrated with Always On Tracing across Windows, Mac and Linux VDAs plus FAS and Session Recording. (2026-08-20, [Tech Zone](https://community.citrix.com/techzone-blogs/app-and-desktop-virtualization/2607-ltsr-tech/))

**Indicators of Compromise detection in NetScaler Console: Did they get in?** A Tech Zone blog explains NetScaler Console's IoC detection capability, which is aimed at the harder follow-up question after a critical CVE ships: not just "are we vulnerable" but "were we compromised before we patched." It frames the feature as reducing the manual log-collection and artifact review that answering that question has historically required. (2026-08-20, [Tech Zone](https://community.citrix.com/techzone-blogs/netscaler/indicators-of-compromise-detection-in-netscaler-console-did-they-get-in-r1604/))

**Why clinician logon feels slow, and how to get it under 5 seconds.** A Tech Zone blog previews a new configuration guide, *Optimizing EHR Logon with Citrix*, arguing that slow EHR access in healthcare is usually a Windows logon and session-initialization problem — profile loading, Group Policy processing, logon scripts — rather than a fault of the EHR application itself, and breaks the logon path into five measurable phases that can each be shortened. (2026-08-20, [Tech Zone](https://community.citrix.com/techzone-blogs/app-and-desktop-virtualization/optimizing-ehr-logon/))

**Citrix SecurAccess ZTNA: Security in your control.** New video on the Citrix YouTube channel covering Citrix SecurAccess's zero-trust network access approach. (2026-08-19, [YouTube](https://www.youtube.com/watch?v=A1NDWNK2O58))

## Deep Dives

**2026-08-21**

**NetScaler ADC/Gateway 14.1 Build 73.33 and 13.1 Build 63.21/37.277 — security maintenance releases.** ([CTX696939](https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html))

These maintenance builds ship the fix for CVE-2026-19489 (a critical memory-overflow/denial-of-service flaw triggered via SIP ALG inside a Large Scale NAT group configuration) and CVE-2026-19490 (a critical unauthenticated authentication bypass on appliances configured as a Gateway or AAA virtual server), across the VPX, VPX FIPS, CPX and BLX form factors on both the 14.1 and 13.1 branches, plus matching Citrix Gateway builds.

*Use cases:* Any customer-managed NetScaler ADC or Gateway appliance configured as a Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or AAA virtual server, or with SIP ALG enabled under a Large Scale NAT group, needs this build regardless of deployment size — the affected configurations are common perimeter-access patterns, not edge cases.

*Pros / cons:* Closes an unauthenticated remote authentication-bypass flaw — the exact class of vulnerability that has repeatedly been mass-exploited against NetScaler in prior years (CitrixBleed and its successors). No workaround exists for either CVE, so the only mitigation is the upgrade itself, which means an unplanned maintenance window for anyone who can't apply it immediately; FIPS/NDcPP-certified environments in particular tend to lag behind general releases in adopting new certified builds.

*What it changes:* Supersedes the bulletin's stated minimum fixed versions (14.1-73.32 / 13.1-63.21) with maintenance builds one point higher; no architectural change, but it closes a critical unauthenticated attack surface on internet-facing appliances.

---

**Citrix Virtual Apps and Desktops 7 2607 Current Release wave.** ([What's new](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/whats-new.html))

CVAD 2607 ships together with matching Probe Agent, Workspace Environment Management, Provisioning LTSR, Federated Authentication Service and Workspace app for Mac builds. The Mac client's Microsoft Teams VDI plugin reaches general availability and is installed by default. On the operations side, a new Service Window lets admins schedule OS disk resets, hardware configuration changes, AD account repair, and Entra Hybrid Join conversion through Web Studio or PowerShell on a controlled schedule; existing AD-joined MCS catalogs (persistent and non-persistent) can convert to Entra Hybrid Join in place, without a rebuild; and Citrix Director gains real-time machine diagnostic insights refreshed every 15 minutes, integrated with Always On Tracing across Windows, Mac and Linux VDAs plus FAS and Session Recording.

*Use cases:* Organizations mid-way through an identity-modernization project that stalled because rebuilding AD-joined catalogs for Entra Hybrid Join was too costly now have an in-place conversion path. Teams currently running disk resets, hardware changes or account repair through custom scripts or manual coordination can move that work into a repeatable, platform-managed Service Window. Mac-heavy deployments get a production-ready (GA), default-installed Teams optimization instead of a manual add-on.

*Pros / cons:* Meaningful operational and identity-modernization capability delivered without an infrastructure rebuild, and GA status for the Teams plugin removes a prior workaround requirement. On the downside, several of the release's other headline client capabilities remain Technical Preview (DNS caching, EDT MTU rediscovery, streaming Client Drive Mapping, HDX Direct for connectorless Service Continuity, HDX graphics super resolution, virtual-session location redirection, resilient third-party plugin execution) and aren't yet production-ready everywhere; and because 2607 is a Current Release rather than an LTSR, it carries a shorter support lifecycle than the 2507 LTSR CU2 released alongside it.

*What it changes:* Additive to 2507, not a replacement — but Entra Hybrid Join in-place conversion replaces the previous "must rebuild the catalog" path for identity modernization.

---

**uberAgent 8.1 — Azure Monitor output backend discontinued.** ([What's new](https://docs.citrix.com/en-us/uberagent/8-x/whats-new/8-1))

Alongside adding an IGEL OS 12 app for Linux endpoints (deployable via the IGEL Universal Management Suite), uberAgent 8.1 discontinues its Azure Monitor output backend ahead of Microsoft's September 14, 2026 retirement of the HTTP Data Collector API that backend relies on.

*Use cases:* Any uberAgent customer currently routing endpoint or session telemetry to Azure Monitor needs to plan a migration to a remaining supported backend — the release's updated Splunk dashboard (clearer licensing-status visualization) points at Splunk as one such destination — before the September cutoff breaks that pipeline.

*Pros / cons:* Removing the backend proactively avoids a hard, uncontrolled telemetry outage when Microsoft retires the underlying API out from under it. The cost falls on customers currently depending on the integration, who now face an unplanned migration project against an external deadline they don't control.

*What it changes:* Removes the Azure Monitor backend entirely rather than deprecating it gradually; there is no in-place migration path, so affected customers must reconfigure output to a different backend.

---

## Metadata

<sub>
Covering dailies 2026-08-17 → 2026-08-23 · Generated 2026-08-23<br>
Phases run: security, downloads, catalog, whatsnew, press, community, weekly<br>
Open defects: 1 — see <code>.skill-bugs.md</code>
</sub>
