# Citrix Product Update — Weekly Rollup
*Covering Monday 2026-08-10 through Thursday 2026-08-13*

Built from the daily notes dated 2026-08-10 through 2026-08-13. Only one daily note exists in this range — the `citrix-product-update` skill's first two runs in this repository, both dated 2026-08-13. The first run's window fell back to the last 24 hours in the absence of prior run-state; a same-day follow-up run extended coverage through 2026-08-13T13:35Z.

## Products

### Releases

**2026-08-12**

**Citrix Virtual Apps and Desktops - HDX graphics super resolution reaches General Availability.** HDX graphics super resolution automatically engages when a session is running under constrained bandwidth and the client supports it, upscaling session graphics to keep perceived visual quality high. It moves from preview to GA in the 2603 current release, making it usable in production without an opt-in flag. (2026-08-12, https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/whats-new.html)

### Catalog Changes

**2026-08-13**

Initial catalog build — no prior `citrix-produts.md` existed in this repository. Enumerated 60 products from https://docs.citrix.com/, https://docs.netscaler.com/ and https://docs.xenserver.com/ and recorded them in `citrix/citrix-produts.md`. Future runs will report only additions, renames and removals against this baseline.

A same-day reconciliation pass against the same three docs sites found two corrections to that initial build:

- **Renamed:** "Global App Configuration Service" is now presented as "Client app management" on docs.citrix.com (https://docs.citrix.com/en-us/client-app-management) — the docs page itself states the service was "previously known as the Global App Configuration Service."
- **Added:** "LAS for NetScaler" (License Activation Service), a cloud-based licensing product for the NetScaler suite, listed on the docs.netscaler.com landing page but missing from the initial build. https://docs.netscaler.com/en-us/citrix-adc/las-for-netscaler.html

## Community

**2026-08-13**

**XenServer 9 Deep Dive Webinar.** Citrix's Tech Zone community events calendar lists a "Deep Dive Webinar Series - Inside Citrix XenServer 9: Updates, strategy, and roadmap," presented by the XenServer Product Management team, covering security, streamed updates, performance and migration considerations for XenServer 9. Thursday, 2026-08-20, 15:00 UTC, online. https://community.citrix.com/events/event/151-deep-dive-webinar-series-inside-citrix-xenserver-9-updates-strategy-and-roadmap/

## Deep Dives

**2026-08-12**

**Citrix Virtual Apps and Desktops - Delivery Controller SQL Server 2025 support.** (https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/whats-new.html)

The Delivery Controller — the core broker component of a CVAD Site — now supports Microsoft SQL Server 2025 as its backend database, joining the existing list of supported SQL Server versions. Admins can point Site configuration at a SQL Server 2025 instance (standalone or a supported HA/AlwaysOn topology) without workarounds.

*Use cases:* Organizations already upgrading their SQL estate to SQL Server 2025 for its security and performance improvements can bring CVAD along on the same timeline instead of waiting for a separate compatibility patch. New CVAD deployments can standardize on the newest SQL release from day one.

*Pros / cons:* Keeps CVAD aligned with Microsoft's current support lifecycle and avoids pinning the Site database to an aging SQL version. The tradeoff is the usual early-adopter risk of a brand-new database release — third-party backup, monitoring, or DBA tooling may not yet fully support SQL Server 2025, and LTSR customers won't see this until (if) it's backported.

*What it changes:* Purely additive — it extends the supported-database list (previously topping out at SQL Server 2022) rather than replacing anything.

---

**Citrix Virtual Apps and Desktops - Microsoft Entra ID single sign-on to VDAs (Preview).** (https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/whats-new.html)

Session hosts (VDAs) that are Microsoft Entra hybrid-joined can now participate in single sign-on using Entra ID credentials, giving CVAD an authentication path that doesn't rely solely on traditional AD-only Kerberos/NTLM logon.

*Use cases:* Enterprises moving identity infrastructure toward Entra ID as part of a broader Zero Trust or cloud-identity strategy can extend that SSO experience into CVAD sessions. Hybrid AD/Entra shops can reduce end-user logon friction without a full cutover.

*Pros / cons:* Reduces dependence on legacy AD-only auth flows and aligns session logon with modern conditional-access policies. Being a preview feature, it isn't yet supported for production-critical workloads, and it only applies to Entra hybrid-joined session hosts — pure on-prem AD-only environments see no benefit yet. It also adds a second identity path that needs to be secured and audited alongside the existing one.

*What it changes:* Additive rather than a replacement — classic AD-based authentication continues to work, but this positions Entra ID auth as CVAD's eventual primary path for Entra-centric environments.

---

**Citrix Virtual Apps and Desktops - Citrix Aidrien integration in Web Studio and Director.** (https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/whats-new.html)

Citrix's AI assistant, Aidrien, is now reachable directly from both Web Studio (the CVAD management console) and Director (the monitoring/troubleshooting console). Clicking its icon opens a Citrix Cloud-authenticated chat panel that answers questions from the Citrix knowledge base without leaving the console.

*Use cases:* An admin diagnosing a session-launch failure in Director can ask Aidrien for likely causes and relevant KB articles without switching to a browser tab. An admin configuring a new delivery group in Web Studio can get contextual guidance inline instead of searching support.citrix.com separately.

*Pros / cons:* Cuts context-switching during troubleshooting and surfaces Citrix's own knowledge base at the point of work, with sign-in via existing Citrix Cloud credentials. The tradeoff is that it requires a Citrix Cloud sign-in and outbound connectivity from the admin's browser — a consideration for air-gapped or high-security environments — and, like any AI assistant, its answers still need to be verified before being acted on in production.

*What it changes:* Doesn't replace the existing Citrix Support/KB search workflow, but shortens it by pulling the same knowledge base into the consoles where the problem is actually being worked.
