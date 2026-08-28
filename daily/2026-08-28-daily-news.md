# Daily News
*Covering Friday 2026-08-28*

## Citrix

### Security Bulletin

**NetScaler ADC and NetScaler Gateway — CVE-2026-8452 confirmed under active exploitation.** A previously patched heap-based buffer overflow (CWE-122, CVSS 8.8 High) in SAML `SignedInfo`/`PrefixList` canonicalization parsing inside the `nsppe` packet-processing engine, on appliances configured as a SAML Service Provider or Identity Provider. An unauthenticated, remote attacker can send a single crafted SAML message to overflow a fixed-size global buffer, corrupt adjacent heap chunk metadata, hijack a function pointer, and execute shellcode as root — a materially worse outcome than Citrix's original "denial of service" classification. Affected: NetScaler ADC/Gateway 13.1 before 13.1-63.18 and 13.1-37.272, and 14.1 before 14.1-72.61 (fix originally shipped 2026-06-30). Remediation: upgrade to 13.1-63.18, 13.1-37.272, or 14.1-72.61 or later; no workaround is available. Exploitation status: actively exploited — following watchTowr Labs' technical write-up and proof-of-concept release on 2026-08-14, security firms observed 36 exploitation attempts from 12 attacker IP addresses across ten countries over 12 days, dropping PHP web shells (`x.php`, `z.php`) and running reconnaissance commands; CISA added the flaw to its Known Exploited Vulnerabilities catalog and ordered federal agencies to remediate by 2026-08-29. ([CTX696604](https://support.citrix.com/external/article/CTX696604/netscaler-adc-and-netscaler-gateway-secu.html))

### Products

#### Changes

**NetScaler Hardware Platforms added to the catalog.** A standalone docs.netscaler.com doc-set covering NetScaler MPX/SDX physical appliance hardware, distinct from the NetScaler (ADC) software product already tracked. It carries no What's New page. ([docs.netscaler.com](https://docs.netscaler.com/en-us/netscaler-hardware-platforms))

---

## Metadata

<sub>
Window: 2026-08-27T02:06:46Z → (in progress)<br>
Phases run: security<br>
Open defects: 4 — see <code>.skill-bugs.md</code>
</sub>
