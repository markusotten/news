# Citrix / NetScaler / XenServer Security Bulletins

Cumulative list of every security bulletin currently listed on Citrix's public trending page (`support-home/topic-article-list?trendingCategory=20&trendingTopicName=Security%20Bulletin`). Source per entry: the corresponding CTX article page (`support-home/kbsearch/article`). For the full CVE/CWE/CVSS/preconditions/remediation breakdown, see [`citrix-CVE.md`](./citrix-CVE.md).

**Coverage note:** the source page is a "trending" widget with no pagination, currently showing 34 entries reaching back to October 2023 (CVE-2023-4966, "Citrix Bleed" — likely kept listed indefinitely given its significance). It is **not a full historical archive** of every Citrix bulletin ever published, just Citrix's own current/relevant selection.

As of: 2026-08-14, plus bulletins added incrementally by the daily skill run as found in each run's window (most recently 2026-08-30). Not a fresh full re-scrape of the trending page on every run.

---

### NetScaler ADC and NetScaler Gateway Security Bulletin for CVE-2026-19489 and CVE-2026-19490
2026-08-19 · Critical · [CTX696939](https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html)

Two vulnerabilities affect NetScaler ADC and Gateway. CVE-2026-19490 is a critical authentication-bypass-using-an-alternate-path flaw letting an unauthenticated remote attacker reach authenticated functionality without valid credentials, on appliances configured as a Gateway (SSL VPN/ICA Proxy/CVPN/RDP Proxy) or AAA virtual server; exact exposure depends on firmware branch/build and, on newer builds, whether a SAML action is configured. CVE-2026-19489 is a memory-overflow bug causing unpredictable behavior or denial-of-service, but only when SIP ALG is enabled on a Large Scale NAT (LSN) group. No exploitation had been reported as of this bulletin.

### XenServer Security Update for Multiple Issues
2026-07-28 · High · [CTX696836](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696836)

Several issues in XenServer 8.4 and XenServer 9 could collectively let a malicious privileged user inside a guest VM compromise or crash the host. Citrix has not broken these out into individual CWE/CVSS scores; seven CVEs are tracked under this bulletin.

### Citrix Secure Access Client for Windows and Citrix Endpoint Analysis Client for Windows Security Bulletin for CVE-2026-53565 and CVE-2026-53566
2026-07-14 · High · [CTX696734](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696734)

Two flaws affect the Windows builds of Citrix Secure Access Client and the Endpoint Analysis Client. A standard local user can escalate to SYSTEM, and a separate issue permits an out-of-bounds memory read under certain conditions.

### XenServer Security Update for CVE-2026-42491
2026-07-10 · Medium · [CTX696811](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696811)

A flaw in the XenServer management API SDK lets an attacker on the management network who can intercept specific HTTPS requests within a higher-level operation act with the intercepted administrator's privileges. It affects the XenCenter management agent and third-party PowerShell/C# SDK clients, independent of the XenServer host version.

### NetScaler ADC and NetScaler Gateway Security Bulletin for CVE-2026-8451, CVE-2026-8452, CVE-2026-8655, CVE-2026-10816, CVE-2026-10817 and CVE-2026-13474
2026-06-30 · High (CVSS up to 8.8) · [CTX696604](https://support.citrix.com/external/article/CTX696604/netscaler-adc-and-netscaler-gateway-secu.html)

Six vulnerabilities affect NetScaler ADC and Gateway across several configurations: CVE-2026-8451, an insufficient-input-validation memory overread when configured as a SAML IdP; CVE-2026-8452, a memory-overflow bug Citrix originally classified as denial-of-service on Gateway/AAA-configured virtual servers; CVE-2026-8655, multiple memory-overflow issues on an Oracle-type load balancer, DNS proxy, or DNS recursive-resolver deployment; CVE-2026-10816, an externally-controlled filename/path issue enabling unauthenticated arbitrary file read; plus CVE-2026-10817 and CVE-2026-13474. **Update (2026-08-27, reported in the 2026-08-28 daily note):** watchTowr Labs published a technical write-up and working proof-of-concept on 2026-08-14 showing CVE-2026-8452 chains into full unauthenticated remote code execution as root, a materially worse outcome than Citrix's original DoS classification — active exploitation (PHP web shells, recon commands) was confirmed shortly after, and CISA added it to its KEV catalog with a 2026-08-29 federal remediation deadline. Fixed in 13.1-63.18/13.1-37.272 and 14.1-72.61 or later; no workaround.

### XenServer Security Update for Multiple Issues
2026-04-28 · High · [CTX696527](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696527)

Multiple issues in XenServer 8.4 could let a privileged guest VM user compromise or crash the host, or let a host administrator escalate privileges beyond their assigned RBAC role. A related AMD CPU side-channel issue affecting cross-VM floating-point division is also mitigated as a convenience, though it is not a XenServer product flaw.

### NetScaler ADC and NetScaler Gateway Security Bulletin for CVE-2026-3055 and CVE-2026-4368
2026-03-23 · Critical · [CTX696300](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696300)

Two vulnerabilities affect NetScaler ADC and Gateway: a memory overread when the appliance is configured as a SAML IDP, and a race condition that can mix up user sessions on gateway- or AAA-configured virtual servers. CVE-2026-3055 was found internally during Citrix's own security review; only customer-managed appliances are affected.

### XenServer Security Update for CVE-2026-4397
2026-03-18 · Medium · [CTX696397](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696397)

Under low host memory conditions, a privileged user in a newly started VM could read leftover memory data belonging to a previously terminated VM on the same XenServer 8.4 host.

### XenServer Security Update for CVE-2026-23554
2026-03-17 · High · [CTX696350](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696350)

Privileged code running inside a guest VM on XenServer 8.4 could compromise the underlying host.

### XenServer Security Update for CVE-2025-58151 and CVE-2026-23553
2026-01-27 · Medium · [CTX695997](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX695997)

One flaw lets privileged code in a guest VM degrade the XenServer host's management responsiveness; a second, unrelated flaw lets a process in a guest VM infer in-memory data belonging to a different process on that same guest.

### XenServer Security Update for CVE-2025-62626
2025-12-08 · Medium · [CTX695797](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX695797)

A hardware flaw in AMD Zen 5 CPUs makes the random number generator return zero more often than it should, which can weaken cryptographic keys generated by software relying on that randomness. This is a CPU hardware issue rather than a XenServer software bug, and only affects AMD-based XenServer 8.4 systems.

### NetScaler ADC and NetScaler Gateway Security Bulletin for CVE-2025-12101
2025-11-11 · Medium · [CTX695486](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX695486)

A cross-site scripting flaw affects NetScaler ADC and Gateway when configured as a gateway (VPN/ICA Proxy/CVPN/RDP Proxy) or AAA virtual server. Secure Private Access on-prem or hybrid deployments using NetScaler instances are also affected.

### XenServer Security Update for CVE-2025-58147 and CVE-2025-58148
2025-10-21 · High · [CTX695405](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX695405)

Two issues in XenServer 8.4 could let privileged code inside a guest VM compromise or crash the host it runs on.

### XenServer Security Update for CVE-2025-27466, CVE-2025-58142, CVE-2025-58143 and CVE-2025-58146
2025-09-09 · High · [CTX695195](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX695195)

Four separate issues in XenServer 8.4 could collectively let an attacker with privileged code inside a guest VM break out enough to crash or take over the underlying host.

### NetScaler ADC and NetScaler Gateway Security Bulletin for CVE-2025-7775, CVE-2025-7776 and CVE-2025-8424
2025-08-26 · Critical · [CTX694938](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX694938)

Three vulnerabilities affect NetScaler ADC and Gateway: two memory-overflow bugs on Gateway/AAA-configured or IPv6-bound virtual servers that can lead to remote code execution or denial of service, and an access-control flaw on the management interface. Exploits of one of the three (CVE-2025-7775) have been observed on unmitigated appliances.

### Windows Virtual Delivery Agent for CVAD and Citrix DaaS Security Bulletin CVE-2025-6759
2025-07-08 · High · [CTX694820](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX694820)

A flaw in the Windows Virtual Delivery Agent used by Citrix Virtual Apps and Desktops / Citrix DaaS lets a low-privileged local user escalate to SYSTEM-level privileges on the machine.

### XenServer Security Update for CVE-2024-36350 and CVE-2024-36357
2025-07-03 · Medium · [CTX694846](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX694846)

AMD disclosed CPU hardware issues that could let code running in one guest VM infer memory contents belonging to a different VM on the same physical host — a cross-VM information leak at the hardware level, not a XenServer software bug.

### XenServer Security Update for CVE-2025-27465
2025-07-02 · Medium · [CTX694780](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX694780)

An issue in XenServer 8.4 could let privileged code running inside a guest VM crash the host or make it unresponsive — effectively a denial-of-service against the hypervisor host.

### NetScaler ADC and NetScaler Gateway Security Bulletin for CVE-2025-6543
2025-06-25 · Critical · [CTX694788](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX694788)

A memory overflow bug in NetScaler ADC/Gateway, when set up as a Gateway (VPN vServer, ICA Proxy, CVPN, RDP Proxy) or AAA virtual server, lets an attacker disrupt control flow and force the appliance into denial-of-service. Exploits have been observed in the wild against unmitigated appliances.

### Citrix Workspace app for Windows Security Bulletin CVE-2025-4879
2025-06-17 · High · [CTX694718](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX694718)

A local privilege escalation flaw in Citrix Workspace app for Windows lets a low-privileged local user obtain SYSTEM privileges when the App Protection service is running.

### NetScaler Console and NetScaler SDX (SVM) Security Bulletin for CVE-2025-4365
2025-06-17 · Medium · [CTX694729](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX694729)

An authenticated attacker with access to NetScaler Console or NetScaler SDX (SVM) can read arbitrary files due to improper access control. Only customer-managed NetScaler Console is affected; the Citrix-managed NetScaler Console Service is not.

### Citrix Secure Access Client for Windows Security Bulletin for CVE-2025-0320
2025-06-17 · High · [CTX694724](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX694724)

A local privilege escalation vulnerability in the Citrix Secure Access Client for Windows allows a low-privileged local user to gain SYSTEM privileges.

### XenServer and Citrix Hypervisor Security Update for CVE-2024-28956
2025-05-12 · Medium · [CTX693178](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX693178)

An Intel-disclosed CPU hardware issue could let privileged code in one guest VM infer memory content from another VM sharing the same CPU core. Deployments without Intel CPUs are unaffected.

### Citrix Secure Access Client for Mac Security Bulletin for CVE-2025-1222 and CVE-2025-1223
2025-02-18 · Medium · [CTX692679](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX692679)

Two local vulnerabilities in Citrix Secure Access Client for Mac could let an attacker with local access gain application privileges and perform limited modification or reading of arbitrary data.

### NetScaler Console and NetScaler Agent Security Bulletin for CVE-2024-12284
2025-02-18 · High · [CTX692579](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX692579)

An authenticated privilege escalation vulnerability affects NetScaler Console and NetScaler Agent when a NetScaler Console Agent is deployed. Only customer-managed deployments are affected.

### Citrix Session Recording Security Bulletin for CVE-2024-8068 and CVE-2024-8069
2024-11-12 · Medium · [CTX691941](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX691941)

Two vulnerabilities in Citrix Session Recording could let a domain- or intranet-authenticated attacker escalate to NetworkService account privileges, with the second issue also enabling limited remote code execution at that privilege level via unsafe deserialization.

### XenServer and Citrix Hypervisor Security Update for CVE-2024-45818
2024-11-12 · Medium · [CTX692065](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX692065)

An issue in XenServer 8 and Citrix Hypervisor 8.2 CU1 LTSR could let a malicious guest VM administrator crash the host or render it unresponsive.

### XenServer and Citrix Hypervisor Security Update for CVE-2024-45817
2024-09-24 · Medium · [CTX691646](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX691646)

An issue in XenServer 8 and Citrix Hypervisor 8.2 CU1 LTSR could let a malicious guest VM administrator crash the host or make it unresponsive. Two additional issues in XenServer 8's SNMP service could let a management-network attacker crash or hang that service.

### Citrix Workspace app for Windows Security Bulletin CVE-2024-6286
2024-07-09 · High · [CTX678036](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX678036)

A local privilege escalation flaw in Citrix Workspace app for Windows allows a low-privileged local user to obtain SYSTEM privileges.

### NetScaler ADC and NetScaler Gateway Security Bulletin for CVE-2024-5491 and CVE-2024-5492
2024-07-09 · High · [CTX677944](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX677944)

Two vulnerabilities affect NetScaler ADC and Gateway when SNMP is configured on the management interface: a denial-of-service flaw from a memory buffer overflow, and an unauthenticated open-redirect that can send users to attacker-controlled sites.
