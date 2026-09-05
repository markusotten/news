# Citrix Product Update - Weekly Rollup
*Covering Monday 2026-08-31 to Sunday 2026-09-06*

## Security Bulletin

**2026-09-05**

**NetScaler ADC and NetScaler Gateway — CVE-2026-19490 exploitation attempts observed.** Vulnerability-intelligence firm Previdian reported that, following publication of a credible proof-of-concept, its NetScaler sensors recorded exploitation attempts against CVE-2026-19490 (the critical authentication-bypass flaw disclosed 2026-08-19, CVSS 9.3) from three distinct source IPs on 2026-09-03; Previdian assesses this as evidence of exploitation attempts, not confirmed compromise. Belgium's national cybersecurity centre (NCC-BE) separately warned of exploitation attempts the same day and urged prioritized patching. The flaw affects NetScaler ADC/Gateway configured as a Gateway (SSL VPN/ICA Proxy/CVPN/RDP Proxy) or AAA virtual server; fixed in 14.1-73.32+ and 13.1-63.21+, with no workaround available. Not yet added to CISA's Known Exploited Vulnerabilities catalog as of this report. ([CTX696939](https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html), [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-target-critical-citrix-netscaler-auth-bypass-in-attacks/))

## Products

### Releases

**2026-09-03**

**NetScaler Console Release (Maintenance Phase) 14.1 Build 73.36.** New maintenance-phase build for NetScaler Console. (2026-09-01, http://www.citrix.com/downloads/citrix-application-management/product-software/citrix-adm-14-1-build-73-36.html)

**Session Recording Agent for Endpoint Devices 2607.** New download for the Session Recording Agent for Endpoint Devices, version 2607, published under Citrix Virtual Apps and Desktops. (2026-09-01, http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/components/session-recording-agent-for-endpoint-devices-2607.html)

**XenServer 9 installation ISO (build 2026-09-01.0946).** New XenServer 9 Normal-channel ISO rolling up all updates to September 1, 2026. (2026-09-01, https://downloads.xenserver.com/xenserver/2026-09-01.0946/XenServer9_2026-09-01.iso)

**XenServer 9 source ISO (build 2026-09-01.0946).** Matching source installation ISO for the same XenServer 9 build. (2026-09-01, https://downloads.xenserver.com/xenserver/2026-09-01.0946/XenServer9_2026-09-01_source.iso)

**EPA Clients for macOS.** New download for Citrix Endpoint Analysis plug-ins on macOS. (2026-09-02, http://www.citrix.com/downloads/citrix-endpoint-analysis/plug-ins/EPA-clients-for-macOS.html)

**Linux Virtual Delivery Agent 2607.** New Linux VDA release, version 2607, published under Citrix Virtual Apps and Desktops. (2026-09-02, http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/components/linux-vda-2607.html)

**Citrix Virtual Delivery Agent for macOS 2607.** New macOS VDA release, version 2607, published under Citrix Virtual Apps and Desktops. (2026-09-03, http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/components/mac-vda-2607.html)

**2026-09-04**

**NetScaler Release (Maintenance Phase) 13.1 Build 64.22.** New maintenance-phase firmware build for NetScaler ADC. (2026-09-03, http://www.citrix.com/downloads/citrix-adc/firmware/release-13-1-build-64-22.html)

**NetScaler VPX Release (Maintenance Phase) 13.1 Build 64.22.** Matching virtual-appliance build for the same 13.1 maintenance release. (2026-09-03, http://www.citrix.com/downloads/citrix-adc/virtual-appliances/vpx-release-13-1-64-22.html)

**NetScaler CPX Release (Maintenance Phase) 13.1 Build 64.22.** Matching container-based NetScaler build for the same 13.1 maintenance release. (2026-09-03, http://www.citrix.com/downloads/citrix-adc/container-based-adc/cpx-13-1-64-22.html)

**NetScaler SDX Bundle (Maintenance Phase) 13.1-64.22.** Matching SDX service-delivery-appliance bundle for the same 13.1 maintenance release. (2026-09-03, http://www.citrix.com/downloads/citrix-adc/service-delivery-appliances/sdx-bundle-13-1-64-22.html)

**NetScaler BLX image (Maintenance Phase) 13.1 Build 64.22.** Matching bare-metal NetScaler build for the same 13.1 maintenance release. (2026-09-03, http://www.citrix.com/downloads/citrix-adc/bare-metal-adc/blx-13-1-64-22.html)

**Citrix Gateway (Maintenance Phase) 13.1 Build 64.22.** Matching Citrix Gateway build released alongside the NetScaler 13.1 maintenance-phase set. (2026-09-03, http://www.citrix.com/downloads/citrix-gateway/product-software/citrix-gateway-13-1-build-64-22.html)

**2026-09-05**

**Citrix Virtual Delivery Agent for macOS - VDA for macOS 2607 migrates to .NET 10 and adds Day-0 macOS 27 support.** The 2607 release moves the macOS VDA from .NET 8 to .NET 10, Microsoft's current LTS runtime; the Arm64 .NET 10 runtime must be installed on the Mac before installing or upgrading, and the installer now fails fast with an actionable message if it is missing. The release also adds TCP BBR support for improved throughput and latency handling, Apple Intelligence-based webcam frame interpolation/upscaling under constrained networks, Day-0 support for macOS 27, and Gateway information in Director for troubleshooting. (2026-09-04, [What's new](https://docs.citrix.com/en-us/mac-vda/whats-new.html), [Download](http://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/components/mac-vda-2607.html))

## Press

**2026-09-03**

**Citrix acquires Numecent to simplify and broaden application management and delivery capabilities across Windows environments.** Citrix, a Cloud Software Group company, completed its acquisition of Numecent, maker of Cloudpaging (application containerization for Windows apps, independent of the OS image) and Cloudpager (a cloud console to provision, update, roll back and meter those containers across physical and virtual Windows endpoints). The deal extends Citrix DaaS application-delivery capabilities beyond virtual desktops to physical Windows endpoints, building on an integration launched in April that let admins publish Cloudpaging containers through Citrix workflows; Citrix positions it as cutting image-management overhead and speeding recovery from ransomware or image failures. (2026-09-01, by Sridhar Mullapudi, Co-President of Citrix, https://www.citrix.com/news/announcements/sep-2026/citrix-acquires-numecent-to-simplify-and-broaden-application-management-and-delivery-capabilities-across-windows-environments.html; companion post: https://www.citrix.com/blogs/2026/09/01/citrix-acquires-numecent/)

## Community

**2026-08-31**

**Migrating PVS Images from VMware to XenServer.** A Citrix YouTube walkthrough covering the steps to migrate Provisioning Services (PVS) images from a VMware environment to XenServer, aimed at admins planning a hypervisor migration. (2026-08-30, [YouTube](https://www.youtube.com/watch?v=j6mJ6iEKEuY))

**Citrix workload-aware XenCenter.** A Citrix YouTube demo of workload-aware XenCenter, which surfaces the impact on Citrix users when an admin makes changes to XenServer hosts, reducing the risk of errors and enabling faster, more confident host administration. (2026-08-30, [YouTube](https://www.youtube.com/watch?v=cuM0hqugqtc))

**2026-09-01**

**XenServer Automated Updates simplifies updating XenServer hosts.** A Citrix YouTube demo of the automated-updates capability in XenServer, walking through how it streamlines applying host updates across a pool with less manual intervention. (2026-08-31, [YouTube](https://www.youtube.com/watch?v=QLAZhI29g4o))

**XenServer 8 simplifies migrating Citrix PVS catalogs from VMware to XenServer.** A Citrix YouTube walkthrough of migrating Provisioning Services catalogs from VMware to XenServer 8, aimed at admins consolidating PVS-based deployments onto XenServer. (2026-08-31, [YouTube](https://www.youtube.com/watch?v=N4x6oFDCxnA))

**2026-09-03**

**Rethinking end-user computing (EUC) design.** A Citrix Tech Zone blog post argues that persona-based EUC design — matching Citrix delivery models (DaaS Cloud, DaaS Local, secure tunneling, etc.) to how specific user groups actually work rather than to assumptions made when an environment was first built — improves user experience and can cut unnecessary cloud and infrastructure spend as workloads drift from their original design. (2026-09-01, https://community.citrix.com/techzone-blogs/platform-services/rethinking-euc-design/)

**2026-09-05**

**How Do I: Enable secure management (Management Plane Isolation) on a live NetScaler HA pair?** Tech Zone deployment guide walking through moving SSH, GUI, SNMP and HA-heartbeat traffic onto a dedicated management plane on a live, production HA pair, converting one node at a time so the pair stays available throughout with only a brief planned cutover interruption. Covers prerequisites (a dedicated management interface/VLAN, console/OOB access as a recovery path, a change window) and per-node considerations, since Secure Management is set per node, takes effect only after reboot, and is never synced by HA. (2026-09-04, [Tech Zone](https://community.citrix.com/techzone-blogs/netscaler/how-do-i-enable-secure-management-management-plane-isolation-on-a-live-netscaler-ha-pair-r1610/))

**August 2026 Tech Wire.** Monthly Tech Zone newsletter roundup covering the month's CVAD/DaaS what's-new items (CVAD 2607 LTSR's Virtual Desktop Assistant graphics view and proactive resource-usage/profile-storage alerts, HDX PDF Universal Print Driver enhancements) alongside links to the underlying release notes and documentation. (2026-09-04, [Tech Zone](https://community.citrix.com/techzone-blogs/newsletter/august_2026/))

**Citrix Connect Pulse Sydney.** One-day customer event for infrastructure, cloud, security and end-user-computing teams, with keynotes, customer use cases and Birds-of-a-Feather sessions on modernizing, securing and optimizing Citrix environments. (2026-09-08, Sydney, https://community.citrix.com/events/event/150-citrix-connect-pulse-sydney/)

**Citrix NetScaler AI Gateway + Protecto: Securing Enterprise LLM Traffic.** Webinar on using NetScaler AI Gateway together with Protecto to apply semantic-aware data protection to LLM traffic — user prompts, agent workflows and AI application calls — where regex- and firewall-based controls struggle to spot PII/PHI without breaking model context. (2026-09-08, online session, https://community.citrix.com/events/event/157-citrix-netscaler-ai-gateway-protecto-securing-enterprise-llm-traffic/)

**Citrix Connect Pulse Toronto.** One-day regional version of Citrix Connect covering Citrix vision and strategy, practical approaches to stabilizing and upgrading environments, and ways to reduce complexity for admins and technical teams. (2026-09-09, Toronto, https://community.citrix.com/events/event/147-citrix-connect-pulse-toronto/)

## Deep Dives

**Citrix Virtual Delivery Agent for macOS — 2607 migrates from .NET 8 to .NET 10.**

The macOS VDA's 2607 release rebases its managed runtime from .NET 8 to .NET 10, Microsoft's current long-term-support release, and makes the Arm64 .NET 10 runtime a hard prerequisite: it must be installed on the Mac before the VDA is installed or upgraded. Both the `.pkg` installer and the `ctxinstall.sh` command-line installer now fail fast with an actionable error if the runtime is not found under `/usr/local/share/dotnet`, and `xdping` validates the runtime as part of its pre-checks, so a mismatched or missing runtime surfaces in a support bundle rather than as a failed session launch at connect time. The release bundles several capability additions alongside the runtime change: TCP BBR for improved throughput and latency handling in HDX sessions over lossy or high-latency networks, Apple Intelligence-based webcam frame interpolation and upscaling to keep webcam video usable under constrained bandwidth, Day-0 support for macOS 27, and Gateway information surfaced in Director for connection troubleshooting.

**Use cases:** organizations running Apple Silicon Mac fleets as Citrix Workspace app endpoints benefit most directly from the BBR and webcam improvements on branch or remote-worker connections with variable network quality; IT teams that image or provision Macs centrally (via MDM or manual `.pkg` deployment) are the ones who need to sequence the .NET 10 runtime installation ahead of the VDA upgrade to avoid a failed rollout.

**Pros:** aligns the client with a current, Microsoft-supported LTS runtime rather than the aging .NET 8 line, ahead of its own end-of-support; the pre-check/fail-fast behavior converts what would otherwise be a silent session-launch failure into a clear, diagnosable installer error; day-0 macOS 27 support avoids a lag between an OS upgrade and VDA compatibility.

**Cons:** the runtime dependency turns what was previously a self-contained VDA upgrade into a two-step change — any fleet using unattended or MDM-driven upgrade pipelines needs to add a .NET 10 Arm64 runtime deployment step ahead of the VDA package, or upgrades will fail at install time on machines that haven't received the runtime yet. Environments relying on manual, per-machine upgrades face the same risk without fleet-management tooling to sequence it.

**What it replaces:** the .NET 8 runtime dependency used by 2607's predecessor macOS VDA releases; any deployment automation built around installing the VDA without a preceding runtime step needs to be updated for this and future macOS VDA releases, which the release notes state will continue targeting .NET 10 going forward.

---

## Metadata

<sub>
Covering dailies 2026-08-31 → 2026-09-05 · Generated 2026-09-05<br>
Phases run: security, downloads, catalog, whatsnew, press, community, weekly<br>
Open defects: 5 — see <code>.skill-bugs.md</code>
</sub>
