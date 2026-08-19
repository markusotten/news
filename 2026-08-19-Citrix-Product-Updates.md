# Citrix Product Updates
*Last 24 hours — 2026-08-19*

Covering "What's New" documentation updates published 2026-08-18 through 2026-08-19 across docs.citrix.com, docs.netscaler.com, and docs.xenserver.com.

## Citrix

### Citrix DaaS
- Added a Microsoft Entra single sign-on machine policy setting for VDAs, letting admins control Entra ID SSO behavior at the machine level instead of only per session.
- Introduced a preview web sign-in flow for Entra-joined and hybrid-joined desktops, letting users authenticate through a browser-based flow instead of the standard domain sign-in.
- Added Connector Appliance-to-backend-application latency metrics to the Application Topology view, making it easier to troubleshoot performance issues.

([docs.citrix.com](https://docs.citrix.com/en-us/citrix-daas/whats-new.html))

### deviceTRUST
- Enhanced Smart Card support: reader properties now update in real time, verifying ATR data against ISO 7816 compliance and identifying the card vendor; a new session template can automatically deny access if a smart card is removed mid-session.
- Added dynamic control of App Protection's anti-screen-capture feature, letting admins toggle screen-capture blocking for Windows endpoints on the fly, with configurable fallback actions (deny access, log off, disconnect) when a platform can't support it.
- The Client Extension now runs natively on Windows ARM64 devices, currently in technical preview.
- Registry-based property lookups can now reference values under paths keyed by the current user's SID or session ID, enabling more dynamic per-user and per-session configuration.
- The deviceTRUST Client Extension is now built directly into the Citrix Workspace app for iOS and Android, removing the need for a separate install.

([docs.citrix.com](https://docs.citrix.com/en-us/device-trust/current-release/whats-new.html))

### StoreFront
- Version 2607 adds a richer desktop tile showing a thumbnail, OS info, power status (including new "Under maintenance" and "Unavailable" states), last connection time, and active session duration; administrators can also use PowerShell to control which power-management actions are exposed to end users for persistent desktops.

([docs.citrix.com](https://docs.citrix.com/en-us/storefront/current-release/whats-new.html))

---

No NetScaler or XenServer product updates were found in the "What's New" documentation in the last 24 hours (2026-08-18 through 2026-08-19).
