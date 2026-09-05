# Daily News
*Covering Saturday 2026-09-05*

## Citrix

### Security Bulletin

**NetScaler ADC and NetScaler Gateway — CVE-2026-19490 exploitation attempts observed.** Vulnerability-intelligence firm Previdian reported that, following publication of a credible proof-of-concept, its NetScaler sensors recorded exploitation attempts against CVE-2026-19490 (the critical authentication-bypass flaw disclosed 2026-08-19, CVSS 9.3) from three distinct source IPs on 2026-09-03; Previdian assesses this as evidence of exploitation attempts, not confirmed compromise. Belgium's national cybersecurity centre (NCC-BE) separately warned of exploitation attempts the same day and urged prioritized patching. The flaw affects NetScaler ADC/Gateway configured as a Gateway (SSL VPN/ICA Proxy/CVPN/RDP Proxy) or AAA virtual server; fixed in 14.1-73.32+ and 13.1-63.21+, with no workaround available. Not yet added to CISA's Known Exploited Vulnerabilities catalog as of this report. ([CTX696939](https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html), [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-target-critical-citrix-netscaler-auth-bypass-in-attacks/))

### Products

#### Releases

**Citrix Virtual Delivery Agent for macOS - VDA for macOS 2607 migrates to .NET 10 and adds Day-0 macOS 27 support.** The 2607 release moves the macOS VDA from .NET 8 to .NET 10, Microsoft's current LTS runtime; the Arm64 .NET 10 runtime must be installed on the Mac before installing or upgrading, and the installer now fails fast with an actionable message if it is missing. The release also adds TCP BBR support for improved throughput and latency handling, Apple Intelligence-based webcam frame interpolation/upscaling under constrained networks, Day-0 support for macOS 27, and Gateway information in Director for troubleshooting. (2026-09-04, [What's new](https://docs.citrix.com/en-us/mac-vda/whats-new.html), [Download](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/components/mac-vda-2607.html))

### Community

---

## Metadata

<sub>
Window: 2026-09-04T02:10:39Z → 2026-09-05T02:10:39Z · Last successful run: 2026-09-04T02:10:39Z<br>
Phases run: security, downloads, catalog, whatsnew, press<br>
Open defects: 4 — see <code>.skill-bugs.md</code>
</sub>
