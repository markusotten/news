# Skill defects

Defects in the `citrix-product-update` skill and the sources it depends on. This file is the only place they are recorded — the daily and weekly notes never carry a Skill-Bug section.

Each entry has a stable id. Runs update `Last seen` for defects that still occur and move cleared ones to Resolved.

## Open

### feed-xenserver-dead — XenServer download RSS feed is dead
- First seen: 2026-08-13
- Last seen: 2026-08-13
- Expected: RSS feed for new XenServer downloads
- Actual: `citrix-links.md` lists `https://www.citrix.com/content/citrix/en_us/downloads/citrix-hypervisor.rss`, which returns HTTP 404. The "Subscribe to RSS notifications" link on https://www.citrix.com/downloads/xenserver/ points to `/content/citrix/en_us/downloads/xenserver.rss`, which itself 301-redirects back to the dead `citrix-hypervisor.rss` URL.
- Run did: skipped XenServer download coverage for this run; `citrix-links.md` row not updated to `ok`. Per skill guidance, XenServer should be covered via https://www.xenserver.com/downloads instead of this feed — needs to be fixed in the next run.

### community-cloudflare-blocked — community.citrix.com blocked by Cloudflare bot challenge
- First seen: 2026-08-13
- Last seen: 2026-08-13
- Expected: RSS/HTML access to community.citrix.com (articles, Tech Zone blogs, events)
- Actual: `https://community.citrix.com/` and `https://community.citrix.com/techzone-blogs/` return HTTP 403 with a "Just a moment..." Cloudflare interstitial, via both `web_fetch` and `curl` with a browser User-Agent.
- Run did: skipped Community coverage for featured articles, Tech Zone blog posts, and upcoming events this run.

## Resolved

_Entries are kept for 30 days after resolution, then deleted._
