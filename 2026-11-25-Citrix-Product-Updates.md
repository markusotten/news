# Citrix Product Updates
*Last 24 hours — 2026-11-25*

## XenServer

### XenServer 9 (Early Access update channel)
- **Link Layer Discovery Protocol (LLDP) support (Nov 24, 2026):** XenServer hosts can now use LLDP (IEEE 802.1AB) to announce themselves to the physical switches they are connected to and to read switch details back. Admins can see which host NIC is plugged into which switch and port without SSH. Turn it on for the whole pool with `xe pool-set-lldp-enabled`, or per NIC with `xe pif-set-lldp-mode`. It works only on managed physical NICs, not on VLANs, bonds, tunnels or SR-IOV. Not yet available on the Normal channel. ([XenServer 9 – Early Access updates](https://docs.xenserver.com/us/en/xenserver/9/whats-new/early-access.html), [LLDP](https://docs.xenserver.com/us/en/xenserver/9/networking/lldp.html))
- **Updated Broadcom/LSI storage drivers (Nov 24, 2026):** The same update bundle moves the mpi3mr driver to 8.19.0.11.0, mpt3sas to 58.255.09.00 and megaraid_sas to 07.739.07.00. ([XenServer 9 – Early Access updates](https://docs.xenserver.com/us/en/xenserver/9/whats-new/early-access.html))

### XenCenter 2026.7.0
- **Maintenance mode wizard with HA support (Nov 24, 2026):** Putting a server into maintenance mode now opens a wizard that also works on pools with high availability (HA) turned on. It runs prechecks, such as whether VMs can be migrated, and helps fix what it finds. On the pool coordinator it turns HA off for a short time and lets you pick the next coordinator. On other servers HA stays on and failover capacity is lowered if needed. ([What's new in XenCenter](https://docs.xenserver.com/us/en/xencenter/current-release/whats-new.html))
- **Fix: VMs imported from OVF/OVA or disk images kept the template's disk layout (Nov 24, 2026):** Templates made from such VMs could fail when used to create machines, for example in the Citrix Virtual Apps and Desktops setup wizard. ([What's new in XenCenter](https://docs.xenserver.com/us/en/xencenter/current-release/whats-new.html))
- **Fix: Crash or blank console when switching to Remote Desktop (Nov 24, 2026):** XenCenter no longer crashes, and the VM console no longer stays blank, when the console switches to RDP. ([What's new in XenCenter](https://docs.xenserver.com/us/en/xencenter/current-release/whats-new.html))
- **Fix: Updates and rolling pool upgrades on GFS2 pools (Nov 24, 2026):** Installing updates or running a rolling pool upgrade no longer fails when GFS2 storage reconnects after a server reboots. ([What's new in XenCenter](https://docs.xenserver.com/us/en/xencenter/current-release/whats-new.html))
- **Fix: Crash when setting a main password after connecting (Nov 24, 2026):** XenCenter no longer crashes when a main password is set from the Save and Restore Connection State dialog. ([What's new in XenCenter](https://docs.xenserver.com/us/en/xencenter/current-release/whats-new.html))
- **Fix: Status bar replaced during Disaster Recovery failover (Nov 24, 2026):** The status bar is no longer replaced by a red cross during a DR failover. ([What's new in XenCenter](https://docs.xenserver.com/us/en/xencenter/current-release/whats-new.html))
- **Fix: Duplicate access key in the VM menu (Nov 24, 2026):** Force Reboot and Secure Boot Certificates no longer share the same keyboard access key. ([What's new in XenCenter](https://docs.xenserver.com/us/en/xencenter/current-release/whats-new.html))

---

<sub>
Window: 2026-11-24 ~02:15 UTC → 2026-11-25 ~02:17 UTC · Sources: 86 per-product sitemaps of docs.citrix.com, docs.netscaler.com and docs.xenserver.com (39,239 pages), plus the What's New, release-notes and document-history pages that changed in the window<br>
Republished without new entries: Citrix DaaS (November entries already reported 2026-11-12 to 2026-11-18), Citrix Virtual Apps and Desktops 2603 and older releases, Profile Management, Adaptive Authentication, DaaS Flex, SecurAccess, XenServer 8.4, WLB, Conversion Manager, XenServer SDK. No docs.netscaler.com page changed in the window.
</sub>
