# Citrix Download Feeds

Source of truth for the download RSS feeds parsed in Phase 2 of the `citrix-product-update` skill.

URL patterns:

- Download page: `https://www.citrix.com/downloads/<value>/`
- RSS feed: `https://www.citrix.com/content/citrix/en_us/downloads/<value>.rss`

`<value>` is the `value` attribute of the corresponding `<option>` in the product select box on https://www.citrix.com/downloads/. It is **not** derivable from the label — see the warnings below.

## Products in the select box

| Product | Value | Download page | RSS feed | Feed verified |
| --- | --- | --- | --- | --- |
| Citrix Analytics | `citrix-analytics` | https://www.citrix.com/downloads/citrix-analytics/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-analytics.rss | — |
| Citrix Early Access Release (EAR) | `citrix-early-access-release` | https://www.citrix.com/downloads/citrix-early-access-release/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-early-access-release.rss | — |
| Citrix Endpoint Analysis | `citrix-endpoint-analysis` | https://www.citrix.com/downloads/citrix-endpoint-analysis/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-endpoint-analysis.rss | — |
| Citrix Endpoint Management | `citrix-endpoint-management` | https://www.citrix.com/downloads/citrix-endpoint-management/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-endpoint-management.rss | yes |
| Citrix Enterprise Browser | `citrix-enterprise-browser` | https://www.citrix.com/downloads/citrix-enterprise-browser/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-enterprise-browser.rss | — |
| Citrix Gateway | `citrix-gateway` | https://www.citrix.com/downloads/citrix-gateway/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-gateway.rss | — |
| Citrix Observability | `citrix-monitoring-observability` | https://www.citrix.com/downloads/citrix-monitoring-observability/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-monitoring-observability.rss | — |
| Citrix SD-WAN | `citrix-sd-wan` | https://www.citrix.com/downloads/citrix-sd-wan/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-sd-wan.rss | — |
| Citrix Secure Access | `citrix-secure-access` | https://www.citrix.com/downloads/citrix-secure-access/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-secure-access.rss | — |
| Citrix Secure Private Access | `citrix-secure-private-access` | https://www.citrix.com/downloads/citrix-secure-private-access/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-secure-private-access.rss | — |
| Citrix Session Remote Start | `citrix-session-remote-start` | https://www.citrix.com/downloads/citrix-session-remote-start/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-session-remote-start.rss | — |
| Citrix Virtual Apps and Desktops | `citrix-virtual-apps-and-desktops` | https://www.citrix.com/downloads/citrix-virtual-apps-and-desktops/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-virtual-apps-and-desktops.rss | — |
| Citrix Workspace app | `workspace-app` | https://www.citrix.com/downloads/workspace-app/ | https://www.citrix.com/content/citrix/en_us/downloads/workspace-app.rss | — |
| NetScaler | `citrix-adc` | https://www.citrix.com/downloads/citrix-adc/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-adc.rss | yes |
| NetScaler Console | `citrix-application-management` | https://www.citrix.com/downloads/citrix-application-management/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-application-management.rss | — |
| StoreFront | `storefront` | https://www.citrix.com/downloads/storefront/ | https://www.citrix.com/content/citrix/en_us/downloads/storefront.rss | — |
| StoreFront Cloud | `citrix-workspace` | https://www.citrix.com/downloads/citrix-workspace/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-workspace.rss | — |
| Tools and Utilities | `citrix-tools` | https://www.citrix.com/downloads/citrix-tools/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-tools.rss | — |
| Unicon eLux Scout | `Elux-Download-Pages` | https://www.citrix.com/downloads/Elux-Download-Pages/ | https://www.citrix.com/content/citrix/en_us/downloads/Elux-Download-Pages.rss | — |
| XenServer | `xenserver` | https://www.citrix.com/downloads/xenserver/ | https://www.citrix.com/content/citrix/en_us/downloads/xenserver.rss | — |

## Additional products

Reachable via "View additional downloads" rather than the select box. Not covered by the daily select-box drift check.

| Product | Value | Download page | RSS feed | Feed verified |
| --- | --- | --- | --- | --- |
| Citrix App Layering | `citrix-app-layering` | https://www.citrix.com/downloads/citrix-app-layering/ | https://www.citrix.com/content/citrix/en_us/downloads/citrix-app-layering.rss | — |
| Citrix Licensing | `licensing` | https://www.citrix.com/downloads/licensing/ | https://www.citrix.com/content/citrix/en_us/downloads/licensing.rss | — |
| Citrix Provisioning Services | `provisioning-services` | https://www.citrix.com/downloads/provisioning-services/ | https://www.citrix.com/content/citrix/en_us/downloads/provisioning-services.rss | — |
| Citrix FAS | `federated-authentication-service` | https://www.citrix.com/downloads/federated-authentication-service/ | https://www.citrix.com/content/citrix/en_us/downloads/federated-authentication-service.rss | — |

## Warnings

- **Never derive a value from the label.** Several diverge sharply: NetScaler is `citrix-adc`, NetScaler Console is `citrix-application-management`, StoreFront Cloud is `citrix-workspace`, Citrix Observability is `citrix-monitoring-observability`, Citrix Workspace app is `workspace-app`.
- **`Elux-Download-Pages` is mixed case.** Preserve it exactly; do not lowercase it.
- **Ignore these select-box entries** — they are not products: `Select a Product`, `Additional Products and Services`, `View Additional Downloads`.
- The `Feed verified` column records feeds confirmed to return valid RSS. Update it as the skill confirms others.

## Maintenance

The daily run compares the live select box against the "Products in the select box" table and reports any drift under **Skill-Bug**. Update this file when a product is added, removed, or renamed, then clear the corresponding Skill-Bug entry.
