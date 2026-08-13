# Citrix Product Update — 2026-08-13
*Covering 2026-08-12T11:48Z to 2026-08-13T11:48Z (no prior run-state found; window fell back to the last 24 hours)*

## Products

### Catalog Changes

Initial catalog build — no prior `citrix-produts.md` existed in this repository. Enumerated 60 products from https://docs.citrix.com/, https://docs.netscaler.com/ and https://docs.xenserver.com/ and recorded them in `citrix/citrix-produts.md`. Future runs will report only additions, renames and removals against this baseline.

## Skill-Bug

- **XenServer download RSS feed is dead.** `citrix-links.md` lists the XenServer feed as `https://www.citrix.com/content/citrix/en_us/downloads/citrix-hypervisor.rss`, which returns HTTP 404. The "Subscribe to RSS notifications" link on https://www.citrix.com/downloads/xenserver/ points to `/content/citrix/en_us/downloads/xenserver.rss`, which itself 301-redirects back to the dead `citrix-hypervisor.rss` URL. No working RSS feed could be found for XenServer downloads; the download page was not scraped as a fallback per skill guidance. XenServer download announcements are not covered until this is fixed.
