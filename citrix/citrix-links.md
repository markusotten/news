# Citrix Download Feeds

Source of truth for the download RSS feeds parsed in Phase 2 of the `citrix-product-update` skill.

URL patterns:

- Download page: `https://www.citrix.com/downloads/<value>/`
- RSS feed: `https://www.citrix.com/content/citrix/en_us/downloads/<value>.rss`

`<value>` is the `value` attribute of the corresponding `<option>` in the product select box on https://www.citrix.com/downloads/. It is **not** derivable from the label — see the warnings below.

## Products in the select box

| Product | Value | Download page | RSS feed | Feed status |
| --- | --- | --- | --- | --- |
| Citrix Analytics | `citrix-analytics` | https://www.citrix.com/downloads/citrix-analytics/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-analytics.rss | ok 2026-08-13 |
| Citrix Early Access Release (EAR) | `citrix-early-access-release` | https://www.citrix.com/downloads/citrix-early-access-release/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-early-access-release.rss | ok 2026-08-13 |
| Citrix Endpoint Analysis | `citrix-endpoint-analysis` | https://www.citrix.com/downloads/citrix-endpoint-analysis/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-endpoint-analysis.rss | ok 2026-08-13 |
| Citrix Endpoint Management | `citrix-endpoint-management` | https://www.citrix.com/downloads/citrix-endpoint-management/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-endpoint-management.rss | ok 2026-08-13 |
| Citrix Enterprise Browser | `citrix-enterprise-browser` | https://www.citrix.com/downloads/citrix-enterprise-browser/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-enterprise-browser.rss | ok 2026-08-13 |
| Citrix Gateway | `citrix-gateway` | https://www.citrix.com/downloads/citrix-gateway/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-gateway.rss | ok 2026-08-13 |
| Citrix Observability | `citrix-monitoring-observability` | https://www.citrix.com/downloads/citrix-monitoring-observability/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-monitoring-observability.rss | ok 2026-08-13 |
| Citrix SD-WAN | `citrix-sd-wan` | https://www.citrix.com/downloads/citrix-sd-wan/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-sd-wan.rss | ok 2026-08-13 |
| Citrix Secure Access | `citrix-secure-access` | https://www.citrix.com/downloads/citrix-secure-access/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-secure-access.rss | ok 2026-08-13 |
| Citrix Secure Private Access | `citrix-secure-private-access` | https://www.citrix.com/downloads/citrix-secure-private-access/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-secure-private-access.rss | ok 2026-08-13 |
| Citrix Session Remote Start | `citrix-session-remote-start` | https://www.citrix.com/downloads/citrix-session-remote-start/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-session-remote-start.rss | ok 2026-08-13 |
| Citrix Virtual Apps and Desktops | `citrix-virtual-apps-and-desktops` | https://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-virtual-apps-and-desktops.rss | ok 2026-08-13 |
| Citrix Workspace app | `workspace-app` | https://www.citrix.com/downloads/workspace-app/ | https://www.citrix.com/content/citrix/en_us/downloads/workspace-app.rss | ok 2026-08-13 |
| NetScaler | `citrix-adc` | https://www.citrix.com/downloads/citrix-adc/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-adc.rss | ok 2026-08-13 |
| NetScaler Console | `citrix-application-management` | https://www.citrix.com/downloads/citrix-application-management/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-application-management.rss | ok 2026-08-13 |
| StoreFront | `storefront` | https://www.citrix.com/downloads/storefront/ | https://www.citrix.com/content/citrix/en_us/downloads/storefront.rss | ok 2026-08-13 |
| StoreFront Cloud | `citrix-workspace` | https://www.citrix.com/downloads/citrix-workspace/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-workspace.rss | ok 2026-08-13 |
| Tools and Utilities | `citrix-tools` | https://www.citrix.com/downloads/citrix-tools/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-tools.rss | ok 2026-08-13 |
| Unicon eLux Scout | `Elux-Download-Pages` | https://www.citrix.com/downloads/Elux-Download-Pages/ | https://www.citrix.com/content/citrix/en_us/downloads/Elux-Download-Pages.rss | ok 2026-08-13 |
| XenServer | `xenserver` | https://www.xenserver.com/downloads | **none — parse the download page** | n/a |

## Additional products

Reachable via "View additional downloads" rather than the select box. Not covered by the daily select-box drift check.

| Product | Value | Download page | RSS feed | Feed status |
| --- | --- | --- | --- | --- |
| Citrix App Layering | `citrix-app-layering` | https://www.citrix.com/downloads/citrix-app-layering/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-app-layering.rss | ok 2026-08-13 |
| Citrix Licensing | `licensing` | https://www.citrix.com/downloads/licensing/ | https://www.citrix.com/content/citrix/en_us/downloads/licensing.rss | ok 2026-08-13 |
| Citrix Provisioning Services | `provisioning-services` | https://www.citrix.com/downloads/provisioning-services/ | https://www.citrix.com/content/citrix/en_us/downloads/provisioning-services.rss | ok 2026-08-13 |
| Citrix FAS | `federated-authentication-service` | https://www.citrix.com/downloads/federated-authentication-service/ | https://www.citrix.com/content/citrix/en_us/downloads/federated-authentication-service.rss | ok 2026-08-13 |

## Community feeds

Used by Phase 6 instead of parsing the community pages. These require `curl` — the hosts below must be in the network egress allowlist.

| Feed | URL | Host | Feed status |
| --- | --- | --- | --- |
| Tech Zone articles (document history) | https://community.citrix.com/rss/1-citrix-tech-zone-document-history.xml/ | `community.citrix.com` | ok 2026-08-13 |
| Tech Zone blogs | https://community.citrix.com/rss/3-citrix-tech-zone-blogs.xml/ | `community.citrix.com` | ok 2026-08-13 |
| Community events | https://community.citrix.com/events/events.xml/ | `community.citrix.com` | ok 2026-08-13 |
| YouTube — Citrix | https://www.youtube.com/feeds/videos.xml?channel_id=UCBnEJLbLEPoP_6lIZU5_qQA | `www.youtube.com` | ok 2026-08-13 |
| YouTube — NetScaler | https://www.youtube.com/feeds/videos.xml?channel_id=UCT2QIrhHsy_NGC8yMnfQOEw | `www.youtube.com` | ok 2026-08-13 |

**Do not fall back to the community HTML pages.** `community.citrix.com/`, `/techzone-blogs/` and `/tech-zone-home/` sit behind a Cloudflare bot challenge and return 403 to both `curl` and `web_fetch`. Only the feed URLs above are usable; if one fails, record it and skip.

The YouTube feeds have **no `web_fetch` fallback** — that tool refuses youtube.com under `ROBOTS_DISALLOWED`. Without the allowlist entry these channels cannot be covered at all. The three `community.citrix.com` feeds can fall back to parsing their HTML pages.


## GitHub watchlist

Used by Phase 6. **Static list — maintained by hand.** Org-level discovery is impossible: `https://github.com/<org>.atom` returns an empty document unauthenticated, and `api.github.com` is unusable (repo-scoped sessions reject cross-repo calls; unauthenticated requests are capped at 60/hour per shared IP). A repo created after this list was written will not be seen until it is added here.

As of 2026-08-13, all eight return HTTP 403 — the session's GitHub proxy scopes github.com access to `markusotten/news` only, blocking both `releases.atom` and `tags.atom` for every watchlist repo. See `.skill-bugs.md` (`github-org-repos-scoped`). Note `xenserver/xenadmin` and `xenserver/xen-api` last tagged in 2023 and 2017 respectively — kept for completeness, but they rarely move.

| Repository | What it is | Releases feed | Tags feed | Feed status |
| --- | --- | --- | --- | --- |
| `citrix/terraform-provider-citrix` | Terraform provider for Citrix DaaS | https://github.com/citrix/terraform-provider-citrix/releases.atom | https://github.com/citrix/terraform-provider-citrix/tags.atom | fail 2026-08-13 (403 - session GitHub proxy scoped to markusotten/news) |
| `citrix/citrix-k8s-ingress-controller` | Kubernetes ingress controller | https://github.com/citrix/citrix-k8s-ingress-controller/releases.atom | https://github.com/citrix/citrix-k8s-ingress-controller/tags.atom | fail 2026-08-13 (403 - session GitHub proxy scoped to markusotten/news) |
| `citrix/citrix-helm-charts` | Helm charts | https://github.com/citrix/citrix-helm-charts/releases.atom | https://github.com/citrix/citrix-helm-charts/tags.atom | fail 2026-08-13 (403 - session GitHub proxy scoped to markusotten/news) |
| `citrix/citrix-adc-ansible-modules` | Ansible modules for NetScaler | https://github.com/citrix/citrix-adc-ansible-modules/releases.atom | https://github.com/citrix/citrix-adc-ansible-modules/tags.atom | fail 2026-08-13 (403 - session GitHub proxy scoped to markusotten/news) |
| `netscaler/netscaler-k8s-ingress-controller` | NetScaler ingress controller | https://github.com/netscaler/netscaler-k8s-ingress-controller/releases.atom | https://github.com/netscaler/netscaler-k8s-ingress-controller/tags.atom | fail 2026-08-13 (403 - session GitHub proxy scoped to markusotten/news) |
| `netscaler/netscaler-helm-charts` | NetScaler Helm charts | https://github.com/netscaler/netscaler-helm-charts/releases.atom | https://github.com/netscaler/netscaler-helm-charts/tags.atom | fail 2026-08-13 (403 - session GitHub proxy scoped to markusotten/news) |
| `xenserver/xenadmin` | XenCenter source | https://github.com/xenserver/xenadmin/releases.atom | https://github.com/xenserver/xenadmin/tags.atom | fail 2026-08-13 (403 - session GitHub proxy scoped to markusotten/news) |
| `xenserver/xen-api` | XenServer management API | https://github.com/xenserver/xen-api/releases.atom | https://github.com/xenserver/xen-api/tags.atom | fail 2026-08-13 (403 - session GitHub proxy scoped to markusotten/news) |

If an entry starts returning 404 the repo was renamed or removed — record it in `.skill-bugs.md` rather than guessing a replacement.


## Warnings

- **Never derive a value from the label.** Several diverge sharply: NetScaler is `citrix-adc`, NetScaler Console is `citrix-application-management`, StoreFront Cloud is `citrix-workspace`, Citrix Observability is `citrix-monitoring-observability`, Citrix Workspace app is `workspace-app`.
- **`Elux-Download-Pages` is mixed case.** Preserve it exactly; do not lowercase it.
- **Ignore these select-box entries** — they are not products: `Select a Product`, `Additional Products and Services`, `View Additional Downloads`.
- **`n/a` means there is no feed — parse the Download page column instead.** Never construct a `.rss` URL for such a row, and never follow a product page's own "Subscribe to RSS notifications" link: Citrix's XenServer page still advertises a feed that 301-redirects to the long-dead `citrix-hypervisor.rss`.
- **XenServer does not use a Citrix feed.** The Citrix download page is a stub pointing at https://www.xenserver.com/downloads, which is server-rendered and dated and covers XenServer 9, 8.4, XenCenter, VM Tools and the optional components. Phase 2 parses that page directly; the row is marked `n/a`.
- **Validate download URLs.** The date in a download path should match the item's stated date. The XenServer 9 source ISO link is malformed upstream (`/xenserver/026-07-16.0907/`, missing the leading `2`) — record such links in `.skill-bugs.md` rather than passing them on silently.

## Feed status values

| Value | Meaning |
| --- | --- |
| `ok YYYY-MM-DD` | Returned 200 and parseable XML on that date |
| `fail YYYY-MM-DD (reason)` | Failed on that date; an open entry in `.skill-bugs.md` should exist |
| `unverified` | Never yet returned a valid feed |
| `n/a` | No Citrix feed for this product (see notes) |

The daily run updates this column for every feed it actually fetches and commits the change with Phase 2. Rows reading `unverified` are fetched first.

## Maintenance

The daily run compares the live select box against the "Products in the select box" table and records any drift in `.skill-bugs.md`. Update this file when a product is added, removed, or renamed, then resolve the corresponding entry in `.skill-bugs.md`.
