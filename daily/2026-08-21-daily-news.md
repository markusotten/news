# Daily News
*Covering Friday 2026-08-21*

## Citrix

### Security Bulletin

**NetScaler ADC and NetScaler Gateway — CVE-2026-19489 and CVE-2026-19490.** Two vulnerabilities affect customer-managed NetScaler ADC and NetScaler Gateway (including FIPS and FIPS/NDcPP builds); Citrix-managed cloud services and Adaptive Authentication are patched by Cloud Software Group directly. CVE-2026-19490 (CWE-288, Authentication bypass using an alternate path, CVSS 9.3, Critical) lets a remote, unauthenticated attacker bypass authentication on an appliance configured as a Gateway (SSL VPN, ICA Proxy, CVPN, or RDP Proxy) or as an AAA virtual server, with the exact precondition depending on firmware version and whether a SAML action is configured; admins can check exposure by looking for `add authentication samlAction .*`, `add authentication vserver .*`, or `add vpn vserver .*` in their running configuration. CVE-2026-19489 (CWE-119, Memory overflow, CVSS 8.8, Critical) allows a remote, unauthenticated attacker to trigger unpredictable behavior or a denial of service on appliances with SIP ALG enabled inside a Large Scale NAT group configuration (`add lsn group.*sipalg.*`). Affected: NetScaler ADC/Gateway 14.1 before 14.1-73.32, 13.1 before 13.1-63.21, ADC FIPS before 14.1-73.32 FIPS, and ADC FIPS/NDcPP before 13.1-37.277. Fixed: 14.1-73.32+, 13.1-63.21+, 14.1-73.32 FIPS+, and 13.1-37.277+ respectively. No workaround is available for either flaw — Citrix's only remediation is to install the fixed build immediately. As of publication and as of 2026-08-20, no public proof-of-concept or evidence of active exploitation had been reported for either CVE, though researchers note NetScaler authentication-bypass flaws are historically fast-followed by exploitation given the product's perimeter-facing deployment footprint. Reported by Samarth Vashisht of JPMorgan Chase's penetration-testing team. ([CTX696939](https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html))

### Products

#### Releases

**NetScaler ADC/Gateway 14.1 Build 73.33 and 13.1 Build 63.21/37.277 (Maintenance Phase).** New maintenance-release builds across the 14.1 and 13.1 branches — VPX, VPX FIPS, CPX, BLX and appliance firmware, plus matching Citrix Gateway 14.1/13.1 builds — superseding the minimum fixed versions named in the CVE-2026-19489/CVE-2026-19490 bulletin above. (2026-08-19, [NetScaler 14.1 firmware](http://www.citrix.com/downloads/citrix-adc/firmware/release-14-1-build-73-33.html), [NetScaler 13.1 firmware](http://www.citrix.com/downloads/citrix-adc/firmware/release-13-1-build-63-21.html), [NetScaler VPX FIPS 14.1](http://www.citrix.com/downloads/citrix-adc/virtual-appliances/netscaler-vpx-release-141-73-33-fips.html), [NetScaler VPX FIPS 13.1](http://www.citrix.com/downloads/citrix-adc/virtual-appliances/netscaler-vpx-release-131-FIPS.html), [Citrix Gateway 14.1](http://www.citrix.com/downloads/citrix-gateway/product-software/citrix-gateway-14-1-build-73-33.html), [Citrix Gateway 13.1](http://www.citrix.com/downloads/citrix-gateway/product-software/citrix-gateway-13-1-build-63-21.html))

**Citrix Virtual Apps and Desktops 7 2607 Current Release wave.** New 2607 current-release builds shipped together for the CVAD stack: Citrix Virtual Apps and Desktops 7 2607 (All Editions), Citrix Probe Agent 2607, Workspace Environment Management 2607, Citrix Provisioning 2607 LTSR, Federated Authentication Service 10.24 (for CVAD 2607), and Citrix Workspace app 2607 for Mac. (2026-08-18/2026-08-19, [CVAD 2607](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/product-software/citrix-virtual-apps-and-desktops-alleditions-2607.html), [Probe Agent](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/components/app-probe-agent.html), [WEM 2607](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/components/workspace-environment-management-2607.html), [Provisioning 2607 LTSR](http://www.citrix.com/downloads/provisioning-services/product-software/provisioning-services-2607.html), [FAS 10.24](http://www.citrix.com/downloads/federated-authentication-service/product-software/fas-2607.html), [Workspace app for Mac 2607](http://www.citrix.com/downloads/workspace-app/mac/workspace-app-for-mac-latest.html))

**Citrix Virtual Apps and Desktops 7 2507 LTSR, Cumulative Update 2.** New LTSR cumulative update covering the 2507 branch, released alongside a matching Linux Virtual Delivery Agent 2507 LTSR CU2 and StoreFront 2507 LTSR CU2. (2026-08-18, [CVAD 2507 LTSR CU2](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/product-software/citrix-virtual-apps-and-desktops-2507ltsr-cu2.html), [Linux VDA 2507 LTSR CU2](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/components/linux-vda-2507-ltsr-cu2.html), [StoreFront 2507 LTSR CU2](http://www.citrix.com/downloads/storefront/product-software/storefront-2507-CU2.html))

**StoreFront 2607 LTSR.** New LTSR release of StoreFront. (2026-08-18, [Download](http://www.citrix.com/downloads/storefront/product-software/storefront-2607.html))

**uberAgent 8.1.** New release of the uberAgent endpoint-monitoring product, distributed through Citrix Observability downloads. (2026-08-18, [Download](http://www.citrix.com/downloads/citrix-monitoring-observability/uberAgent-Product-Software/8-1.html))

**License Server for Windows 11.17.2.0 (Build 56200).** New build of the Citrix Licensing server for Windows. (2026-08-17, [Download](http://www.citrix.com/downloads/licensing/license-server/license-server-version-111720-56200-for-windows.html))

**Citrix Workspace app for Windows LTSR 2607 Technical Preview.** New LTSR technical-preview build of Workspace app for Windows. (2026-08-18, [Download](http://www.citrix.com/downloads/workspace-app/betas-and-tech-previews/workspace-app-for-windows-tech-preview.html))

**Browser Content Redirection files for Workspace app (Mac).** Updated Browser Content Redirection component files for Citrix Workspace app on macOS. (2026-08-19, [Download](http://www.citrix.com/downloads/workspace-app/browser-content-redirection-mac/bcr-files.html))

**Unicon eLux Scout software packages — LTSR and CR.** New UniconOS (eLux) software package releases for both the LTSR and Current Release (CR) branches. (2026-08-19 LTSR / 2026-08-18 CR, [LTSR packages](http://www.citrix.com/downloads/Elux-Download-Pages/Elux-Software-Packages/eLux-Software-Packages-LTSR.html), [CR packages](http://www.citrix.com/downloads/Elux-Download-Pages/Elux-Software-Packages/eLux-Software-Packages-CR.html))

### Community

---

## Metadata

<sub>
Window: 2026-08-17T02:22:53Z → 2026-08-21T02:10:02Z · Last successful run: 2026-08-17T02:22:53Z<br>
Phases run: security<br>
Open defects: 0 — see <code>.skill-bugs.md</code>
</sub>
