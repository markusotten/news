# Citrix Product Updates
*Last 24 hours — 2026-11-18*

## Citrix

### Citrix DaaS

- **Citrix DaaS MCP Server Cloud – Preview (November 2026, first seen Nov 18, 2026):** A Citrix-hosted MCP server is now in preview. AI clients that support MCP, such as Claude Code or Codex CLI, can use it to query and troubleshoot a DaaS environment in plain language. It offers only read and diagnostic tools, and access is controlled through a Citrix Cloud service principal. ([What's new in Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/whats-new.html))
- **Automated actions for Monitor alerts (November 2026, first seen Nov 18, 2026):** Admins can attach remediation actions to Monitor alert policies, such as machine management actions. These run automatically when a critical alert fires. Monitor tracks each action and includes the result in the alert notification. ([What's new in Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/whats-new.html))

### Citrix DaaS Flex

- **Initial release of Citrix DaaS Profiles Flex (November 2026, first seen Nov 18, 2026):** This is a new cloud-native Windows user profile management service, managed by Citrix, that keeps user profiles consistent across a Flex deployment. In this first release it is available only for Citrix DaaS Flex for Azure. ([What's new in Citrix DaaS Profiles Flex](https://docs.citrix.com/en-us/citrix-daas-flex/citrix-daas-flex-overview/profiles-flex/whats-new.html))

### Device Posture

- **EPA client 2607 supports macOS 27 (Nov 17, 2026):** Devices running macOS 27 can now use EPA client 2607 with full device posture checks and continuous scanning. ([What's new in Device Posture](https://docs.citrix.com/en-us/device-posture/device-posture-whats-new.html))

### Citrix SecurAccess (Android)

- **26.10.2 – Push-notification password-token fix (Nov 16, 2026, published Nov 17):** Fixes a 26.10.1 bug that stopped some users from authenticating SecurAccess sessions when they used password tokens through the app's push notifications. ([SecurAccess for Android release notes](https://docs.citrix.com/en-us/citrix-secure-access/citrix-sso-for-android-devices/citrix-sso-release-notes-android.html))

### Citrix SecurSpaces

- **2026.9.8 – Browser IDE WebViews served through the platform proxy domain (Nov 17, 2026):** If the IDE build supports it, the startup files for browser IDE WebViews (previews and extension views) are now served through the platform's own proxy domain. They no longer have to come from the public VS Code CDN. ([SecurSpaces fixed issues](https://docs.citrix.com/en-us/securspaces/release-notes/fixed-issues.html))
- **2026.9.8 – Security fix for project workspace management (Nov 17, 2026):** Fixes a flaw where workspace management requests could read or personalize workspaces outside the caller's project, or change their state, without the required access. ([SecurSpaces fixed issues](https://docs.citrix.com/en-us/securspaces/release-notes/fixed-issues.html))
- **2026.9.8 – General fixes (Nov 17, 2026):** Fixes include:
  - Private Bitbucket and GitLab repositories were missing from search for users with limited roles.
  - Connections to self-hosted GitLab on a custom port failed.
  - The People page did not refresh after a group was added.
  - Workspaces and image builds could start in the wrong region.
  - Rootless Docker builds failed on Ubuntu 24.04 nodes with AppArmor restrictions.

  ([SecurSpaces fixed issues](https://docs.citrix.com/en-us/securspaces/release-notes/fixed-issues.html))

## XenServer

### XenServer 9

- **Normal channel update – OpenSSH 10.6p2 and zlib 1.4 (Nov 17, 2026):** The Normal update channel updates OpenSSH to 10.6p2 and zlib to 1.4. ([Normal channel updates](https://docs.xenserver.com/en-us/xenserver/9/whats-new/normal.html))

### XenServer 8.4

- **Normal channel update – OpenSSH 10.6p2 and zlib 1.4 (Nov 17, 2026):** The same OpenSSH 10.6p2 and zlib 1.4 updates are now on the Normal channel for XenServer 8.4. ([Normal channel updates](https://docs.xenserver.com/en-us/xenserver/8/whats-new/normal.html))
- **Normal channel update – storage coalesce data-loss fix (Nov 17, 2026):** The fix for a rare coalesce problem, where a coalesce finished but did not relink and a later coalesce could cause data loss, has moved from Early Access to the Normal channel. ([Normal channel updates](https://docs.xenserver.com/en-us/xenserver/8/whats-new/normal.html))

---

<sub>
Window: 2026-11-17 ~02:15 UTC → 2026-11-18 ~02:15 UTC · Sources: per-product sitemaps (86) and the What's New, release-notes and document-history pages of docs.citrix.com, docs.netscaler.com and docs.xenserver.com that changed in the window<br>
"First seen" = the entry is grouped by month with no exact date and was not in any earlier report. NetScaler: Console and VPX docs were republished on Nov 17, but they have no entries dated in the window (newest: Console 14.1-74.34 on Nov 12, already reported).
</sub>
