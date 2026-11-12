# Citrix Product Updates
*Last 24 hours — 2026-11-12*

## Citrix

### Citrix DaaS

- **Connect WEM agents to the cloud service from Studio (first seen Nov 12, 2026):** Admins can now link Workspace Environment Management agents to the WEM service in Citrix Cloud from Studio > Settings. That way the connection is in place before a WEM configuration set is applied for experience optimization. ([What's new in Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/whats-new.html))
- **Run WEM scripted tasks from Studio (first seen Nov 12, 2026):** In Studio > Search, admins can select one or more machines and run a built-in or custom WEM scripted task without opening a separate console. The WEM service must be provisioned, and target machines need WEM agent 2110 or later. ([What's new in Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/whats-new.html))
- **Delivery group restart schedules in Task Center (first seen Nov 12, 2026):** Task Center now lists delivery group restart schedules next to other tasks, with timing, run status, name and frequency, for better visibility and auditing. ([What's new in Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/whats-new.html))
- **Citrix Advisor: new reliability check (first seen Nov 12, 2026):** Citrix Advisor adds a check that flags outdated VDA registration configurations and recommends fixes. ([What's new in Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/whats-new.html))
- **Last boot time and session idle time in Studio > Search (first seen Nov 12, 2026):** Optional, sortable and filterable "Last Boot Time (UTC)" (Machines) and "Idle Time" (Sessions) columns help spot inactive sessions and stale MCS machines. ([What's new in Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/whats-new.html))

### Citrix Cloud

- **Register Cloud Connectors with a registration code (first seen Nov 12, 2026; page updated Nov 11):** The Cloud Connector installer now shows a code that you enter in the new Add Cloud Connector wizard, from any computer, instead of signing in from the installer. Silent installs can also use a registration code instead of a service principal. ([What's new in Citrix Cloud](https://docs.citrix.com/en-us/citrix-cloud/citrix-cloud-overview/whats-new.html))
- **Cloud Connector services on .NET 10 (first seen Nov 12, 2026; page updated Nov 11):** Some Cloud Connector services now run on Microsoft .NET 10. The installer deploys the .NET Desktop Runtime 10 and ASP.NET Core Runtime 10 automatically from the same Citrix site, so no firewall or proxy changes are needed. .NET 8 is no longer required, but .NET Framework 4.7.2 still is. ([What's new in Citrix Cloud](https://docs.citrix.com/en-us/citrix-cloud/citrix-cloud-overview/whats-new.html))

## XenServer

### XenServer 8.4

- **Early Access update – storage coalesce fix (Nov 11, 2026):** Fixes a very rare problem where a storage coalesce completed but did not relink properly, so a later coalesce could cause data loss. ([Early Access channel updates](https://docs.xenserver.com/en-us/xenserver/8/whats-new/early-access.html))

### XenCenter

- **XenCenter 2026.6.0 – CVAD 2607 integration fix (first seen Nov 12, 2026; page updated Nov 11):** Citrix Integration again shows CVAD machine and session information when XenCenter is connected to Citrix Virtual Apps and Desktops 2607. ([What's new in XenCenter](https://docs.xenserver.com/en-us/xencenter/current-release/whats-new.html))
- **XenCenter 2026.6.0 – UI fixes (first seen Nov 12, 2026):** The remote-access configuration dialog can be dismissed again. Docked VM consoles no longer appear scaled when scaling is disabled. ([What's new in XenCenter](https://docs.xenserver.com/en-us/xencenter/current-release/whats-new.html))

### XenServer SDK

- **SDK 26.22.0 – PowerShell 7 module on .NET 10 (first seen Nov 12, 2026; page updated Nov 11):** The PowerShell 7 module is now built on .NET 10 and requires PowerShell 7.6 or later. The Windows PowerShell 5.1 module is unchanged. ([What's new in the XenServer SDK](https://docs.xenserver.com/en-us/xenserver/developer/sdk-guide/whats-new.html))
- **SDK 26.22.0 – Full Get-Help content (first seen Nov 12, 2026):** Every cmdlet in both PowerShell modules now has full help (synopsis, description, parameters, examples), which is also published online. ([What's new in the XenServer SDK](https://docs.xenserver.com/en-us/xenserver/developer/sdk-guide/whats-new.html))
- **SDK 26.22.0 – Optional parameters only sent when specified (first seen Nov 12, 2026):** Cmdlets like Invoke-XenHost/VM/Pool/SR no longer send optional parameters you didn't specify, so they now work against older 8.4 hosts that lack newer API parameters (for example `Invoke-XenHost -XenAction Disable`). ([What's new in the XenServer SDK](https://docs.xenserver.com/en-us/xenserver/developer/sdk-guide/whats-new.html))
- **SDK 26.22.0 – Go SDK uses int64 (first seen Nov 12, 2026):** All XenAPI integers are now `int64`, which fixes wrong values above 2^31 (memory and disk sizes) in 32-bit builds. Go 1.27.1 or later is now required. ([What's new in the XenServer SDK](https://docs.xenserver.com/en-us/xenserver/developer/sdk-guide/whats-new.html))
- **SDK 26.22.0 – Java dependency security updates (first seen Nov 12, 2026):** The Java SDK now depends on Apache HttpClient 5.6.4 and Jackson Databind 2.22.4, which fix security vulnerabilities. ([What's new in the XenServer SDK](https://docs.xenserver.com/en-us/xenserver/developer/sdk-guide/whats-new.html))

---

<sub>
Window: 2026-11-11 → 2026-11-12 · Sources: per-product sitemaps and What's New pages of docs.citrix.com, docs.netscaler.com, docs.xenserver.com<br>
"First seen" = entry has no exact publish date (month-grouped or versioned), was not in any earlier report, and its page was republished Nov 11–12. NetScaler: release notes republished Nov 11, but the newest build (14.1-73.49) is dated Oct 27, so no update is listed.
</sub>
