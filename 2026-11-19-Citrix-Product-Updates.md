# Citrix Product Updates
*Last 24 hours — 2026-11-19*

## NetScaler

### NetScaler Console service

- **Fix: Microsoft Sentinel export stops with HTTP 413 (Nov 18, 2026):** Analytics exports to Microsoft Sentinel no longer fail and stop when large records make a batch bigger than Sentinel's request size limit. ([NetScaler Console service – What's new](https://docs.netscaler.com/en-us/netscaler-console-service/release-notes/whats-new.html))
- **Fix: Console key files and CSRs missing from the SSL Dashboard (Nov 18, 2026):** Admins could not find key files and CSRs stored on NetScaler Console, because the drill-down only listed SSL files from managed instances. This is now fixed. ([NetScaler Console service – What's new](https://docs.netscaler.com/en-us/netscaler-console-service/release-notes/whats-new.html))
- **Fix: AWS agent fails to boot after upgrade (Nov 18, 2026):** Upgrading a NetScaler Console agent on AWS now applies the sysid correctly, so the agent boots normally after the upgrade. ([NetScaler Console service – What's new](https://docs.netscaler.com/en-us/netscaler-console-service/release-notes/whats-new.html))
- **Fix: Analytics services run out of memory in multi-tenant deployments (Nov 18, 2026):** An agent could pull the whole tenant's application and virtual server inventory instead of only its own instances. That could exhaust memory, restart analytics services and interrupt a tenant's application visibility. Agents now retrieve only the inventory they need. ([NetScaler Console service – What's new](https://docs.netscaler.com/en-us/netscaler-console-service/release-notes/whats-new.html))
- **Fix: ACME certificate issuance fails with periods in the name or an empty SAN (Nov 18, 2026):** Automated ACME certificate requests no longer return HTTP 400 when the certificate name contains periods, such as an FQDN. Requests with an empty Subject Alternative Name are no longer rejected by the CA. ([NetScaler Console service – What's new](https://docs.netscaler.com/en-us/netscaler-console-service/release-notes/whats-new.html))
- **Fix: False "disconnected" status and license grace-period alerts for VPX instances (Nov 18, 2026):** After a short connectivity glitch, Console no longer keeps marking VPX instances as disconnected or raising grace-period alerts while they are still licensed and running. ([NetScaler Console service – What's new](https://docs.netscaler.com/en-us/netscaler-console-service/release-notes/whats-new.html))

---

<sub>
Window: 2026-11-18 ~02:15 UTC → 2026-11-19 ~02:15 UTC · Sources: 86 per-product sitemaps of docs.citrix.com, docs.netscaler.com and docs.xenserver.com, plus the What's New, release-notes and document-history pages that changed in the window<br>
Republished but nothing new in the window: Citrix Aidrien (DaaS MCP Server Cloud preview, reported 2026-11-18), Citrix Cloud (Cloud Connector items, reported 2026-11-12), Remote Browser Isolation (Okta SAML, reported 2026-11-14), SecurAccess ZTNA, XenServer 8.4/9, XenCenter, Conversion Manager and WLB.
</sub>
