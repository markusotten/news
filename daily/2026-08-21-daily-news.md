# Daily News
*Covering Friday 2026-08-21*

## Citrix

### Security Bulletin

**NetScaler ADC and NetScaler Gateway — CVE-2026-19489 and CVE-2026-19490.** Two vulnerabilities affect customer-managed NetScaler ADC and NetScaler Gateway (including FIPS and FIPS/NDcPP builds); Citrix-managed cloud services and Adaptive Authentication are patched by Cloud Software Group directly. CVE-2026-19490 (CWE-288, Authentication bypass using an alternate path, CVSS 9.3, Critical) lets a remote, unauthenticated attacker bypass authentication on an appliance configured as a Gateway (SSL VPN, ICA Proxy, CVPN, or RDP Proxy) or as an AAA virtual server, with the exact precondition depending on firmware version and whether a SAML action is configured; admins can check exposure by looking for `add authentication samlAction .*`, `add authentication vserver .*`, or `add vpn vserver .*` in their running configuration. CVE-2026-19489 (CWE-119, Memory overflow, CVSS 8.8, Critical) allows a remote, unauthenticated attacker to trigger unpredictable behavior or a denial of service on appliances with SIP ALG enabled inside a Large Scale NAT group configuration (`add lsn group.*sipalg.*`). Affected: NetScaler ADC/Gateway 14.1 before 14.1-73.32, 13.1 before 13.1-63.21, ADC FIPS before 14.1-73.32 FIPS, and ADC FIPS/NDcPP before 13.1-37.277. Fixed: 14.1-73.32+, 13.1-63.21+, 14.1-73.32 FIPS+, and 13.1-37.277+ respectively. No workaround is available for either flaw — Citrix's only remediation is to install the fixed build immediately. As of publication and as of 2026-08-20, no public proof-of-concept or evidence of active exploitation had been reported for either CVE, though researchers note NetScaler authentication-bypass flaws are historically fast-followed by exploitation given the product's perimeter-facing deployment footprint. Reported by Samarth Vashisht of JPMorgan Chase's penetration-testing team. ([CTX696939](https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html))

### Products

#### Releases

### Community

---

## Metadata

<sub>
Window: 2026-08-17T02:22:53Z → 2026-08-21T02:10:02Z · Last successful run: 2026-08-17T02:22:53Z<br>
Phases run: security<br>
Open defects: 0 — see <code>.skill-bugs.md</code>
</sub>
