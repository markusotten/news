# Citrix Product Catalog

Canonical list of products tracked in Phase 4 ("What's New") of the `citrix-product-update` skill, reconciled against `https://docs.citrix.com/`, `https://docs.netscaler.com/` and `https://docs.xenserver.com/`. Kept sorted alphabetically so the diff stays readable in git.

The **What's New URL** column is read by Phase 4 so it never has to rediscover a product's release-notes URL. Values: a URL (validated — 200 with what's-new content), `none` (genuinely no what's-new page, do not retry), `unverified: <url>` (resolved but not real what's-new content, skipped by Phase 4, needs a human), `unresolved` (could not be checked, retried next run).

| Product | Docs URL | What's New URL |
| --- | --- | --- |
| Citrix Adaptive Authentication Service | https://docs.citrix.com/en-us/adaptive-authentication | none |
| Citrix Aidrien | https://docs.citrix.com/en-us/citrix-aidrien | https://docs.citrix.com/en-us/citrix-aidrien/whats-new.html |
| Citrix Always On Tracing | https://docs.citrix.com/en-us/citrix-always-on-tracing | none |
| Citrix Analytics | https://docs.citrix.com/en-us/citrix-analytics | https://docs.citrix.com/en-us/citrix-analytics/whats-new.html |
| Citrix App Layering | https://docs.citrix.com/en-us/citrix-app-layering | unverified: https://docs.citrix.com/en-us/citrix-app-layering/4.html |
| Citrix Cloud | https://docs.citrix.com/en-us/citrix-cloud | https://docs.citrix.com/en-us/citrix-cloud/whats-new.html |
| Citrix Cloud Government | https://docs.citrix.com/en-us/citrix-cloud-government | https://docs.citrix.com/en-us/citrix-cloud-government/whats-new.html |
| Citrix Cloud Japan | https://docs.citrix.com/en-us/citrix-cloud-japan | https://docs.citrix.com/en-us/citrix-cloud-japan#whats-new |
| Client app management | https://docs.citrix.com/en-us/client-app-management | https://docs.citrix.com/en-us/client-app-management/whats-new.html |
| Citrix DaaS | https://docs.citrix.com/en-us/citrix-daas | https://docs.citrix.com/en-us/citrix-daas/whats-new.html |
| Citrix DaaS Flex | https://docs.citrix.com/en-us/citrix-daas-flex | https://docs.citrix.com/en-us/citrix-daas-flex#whats-new |
| Citrix DaaS Standard for Azure | https://docs.citrix.com/en-us/citrix-daas-azure | https://docs.citrix.com/en-us/citrix-daas-azure/whats-new.html |
| Device Posture | https://docs.citrix.com/en-us/device-posture | https://docs.citrix.com/en-us/device-posture#whats-new |
| deviceTRUST | https://docs.citrix.com/en-us/device-trust | https://docs.citrix.com/en-us/device-trust/current-release/whats-new.html |
| Citrix Endpoint Management | https://docs.citrix.com/en-us/citrix-endpoint-management | https://docs.citrix.com/en-us/citrix-endpoint-management/whats-new.html |
| Citrix Enterprise Browser | https://docs.citrix.com/en-us/citrix-enterprise-browser | https://docs.citrix.com/en-us/citrix-enterprise-browser/whats-new.html |
| Citrix Experience Insights Flex | https://docs.citrix.com/en-us/citrix-experience-insights-flex | none |
| Federated Authentication Service | https://docs.citrix.com/en-us/federated-authentication-service | https://docs.citrix.com/en-us/federated-authentication-service/current-release/whats-new.html |
| Citrix Gateway Service | https://docs.citrix.com/en-us/citrix-gateway-service | unverified: https://docs.citrix.com/en-us/citrix-gateway-service |
| Global App Configuration Service | https://docs.citrix.com/en-us/citrix-workspace/global-app-config-service.html | https://docs.citrix.com/en-us/citrix-workspace/whats-new.html |
| Citrix HDX Plus for Windows 365 | https://docs.citrix.com/en-us/citrix-hdxplus-w365 | https://docs.citrix.com/en-us/citrix-hdxplus-w365/whats-new.html |
| HDX RealTime Optimization Pack | https://docs.citrix.com/en-us/hdx-optimization | https://docs.citrix.com/en-us/hdx-optimization/current-release/whats-new.html |
| ITSM Adapter for ServiceNow | https://docs.citrix.com/en-us/citrix-itsm-adapter-service | https://docs.citrix.com/en-us/citrix-itsm-adapter-service/whats-new.html |
| LAS for NetScaler | https://docs.netscaler.com/en-us/citrix-adc/las-for-netscaler.html | https://docs.netscaler.com/en-us/citrix-adc/las-for-netscaler.html#whats-new |
| Licensing | https://docs.citrix.com/en-us/licensing | https://docs.citrix.com/en-us/licensing/current-release/whats-new.html |
| Linux Virtual Delivery Agent | https://docs.citrix.com/en-us/linux-virtual-delivery-agent | https://docs.citrix.com/en-us/linux-virtual-delivery-agent/current-release/whats-new.html |
| MAM SDK | https://docs.citrix.com/en-us/mam-sdk | unverified: https://docs.citrix.com/en-us/mam-sdk |
| Mobile Productivity Apps | https://docs.citrix.com/en-us/mobile-productivity-apps | unverified: https://docs.citrix.com/en-us/mobile-productivity-apps |
| NetScaler (ADC) | https://docs.netscaler.com/en-us/citrix-adc | https://docs.netscaler.com/en-us/citrix-adc#whats-new |
| NetScaler Automation Toolkit | https://github.com/netscaler/automation-toolkit | none |
| NetScaler Console | https://docs.netscaler.com/en-us/netscaler-application-delivery-management-software | https://docs.netscaler.com/en-us/netscaler-application-delivery-management-software#whats-new |
| NetScaler Console Service | https://docs.netscaler.com/en-us/netscaler-console-service/ | https://docs.netscaler.com/en-us/netscaler-console-service/#whats-new |
| NetScaler Gateway | https://docs.netscaler.com/en-us/netscaler-gateway | https://docs.netscaler.com/en-us/netscaler-gateway#whats-new |
| NetScaler SDX | https://docs.netscaler.com/en-us/sdx | https://docs.netscaler.com/en-us/sdx#whats-new |
| Profile Management | https://docs.citrix.com/en-us/profile-management | https://docs.citrix.com/en-us/profile-management/current-release/whats-new.html |
| Citrix Provisioning | https://docs.citrix.com/en-us/provisioning | https://docs.citrix.com/en-us/provisioning/current-release/whats-new.html |
| Citrix Ready Workspace Hub | https://docs.citrix.com/en-us/citrix-ready-workspace-hub | unverified: https://docs.citrix.com/en-us/citrix-ready-workspace-hub |
| Citrix Receiver | https://docs.citrix.com/en-us/receiver | none |
| Citrix Remote Browser Isolation | https://docs.citrix.com/en-us/citrix-remote-browser-isolation | https://docs.citrix.com/en-us/citrix-remote-browser-isolation/whats-new.html |
| Citrix Secure Access | https://docs.citrix.com/en-us/citrix-secure-access | unverified: https://docs.citrix.com/en-us/citrix-secure-access |
| Citrix Secure Developer Spaces | https://docs.citrix.com/en-us/secure-developer-spaces | https://docs.citrix.com/en-us/secure-developer-spaces#whats-new |
| Citrix Secure Hub | https://docs.citrix.com/en-us/citrix-secure-hub | https://docs.citrix.com/en-us/citrix-secure-hub/overview.html#whats-new-in-the-current-version |
| Citrix Secure Mail | https://docs.citrix.com/en-us/citrix-secure-mail | https://docs.citrix.com/en-us/citrix-secure-mail/whats-new.html |
| Citrix Secure Private Access | https://docs.citrix.com/en-us/citrix-secure-private-access | unverified: https://docs.citrix.com/en-us/legacy-archive/citrix-secure-private-access.html |
| Citrix Secure Web | https://docs.citrix.com/en-us/citrix-secure-web | https://docs.citrix.com/en-us/citrix-secure-web/whats-new.html |
| Self Service Password Reset | https://docs.citrix.com/en-us/self-service-password-reset | https://docs.citrix.com/en-us/self-service-password-reset/current-release/whats-new.html |
| Session Recording | https://docs.citrix.com/en-us/session-recording | https://docs.citrix.com/en-us/session-recording/current-release/whats-new.html |
| Session Recording Service | https://docs.citrix.com/en-us/session-recording-service | unverified: https://docs.citrix.com/en-us/session-recording/service |
| Session Remote Start | https://docs.citrix.com/en-us/session-remote-start | unverified: https://docs.citrix.com/en-us/session-remote-start |
| StoreFront | https://docs.citrix.com/en-us/storefront | https://docs.citrix.com/en-us/storefront/current-release/whats-new.html |
| StoreFront Cloud | https://docs.citrix.com/en-us/citrix-workspace | https://docs.citrix.com/en-us/citrix-workspace/whats-new.html |
| uberAgent | https://docs.citrix.com/en-us/uberagent | https://docs.citrix.com/en-us/uberagent/current-release/whats-new.html |
| Unicon eLux Scout | https://docs.citrix.com/en-us/unicon-elux-scout | unverified: https://docs.citrix.com/en-us/unicon-elux-scout/2607/ |
| Citrix Virtual Apps and Desktops | https://docs.citrix.com/en-us/citrix-virtual-apps-desktops | https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/whats-new.html |
| Citrix Virtual Delivery Agent for macOS | https://docs.citrix.com/en-us/mac-vda | https://docs.citrix.com/en-us/mac-vda/whats-new.html |
| Citrix Workspace app | https://docs.citrix.com/en-us/citrix-workspace-app | https://docs.citrix.com/en-us/citrix-workspace-app/whats-new.html |
| Citrix Workspace app for visionOS | https://docs.citrix.com/en-us/citrix-workspace-app-for-visionos | unverified: https://docs.citrix.com/en-us/citrix-workspace-app-for-visionos/whats-new.html |
| Workspace Environment Management | https://docs.citrix.com/en-us/workspace-environment-management | https://docs.citrix.com/en-us/workspace-environment-management/current-release/whats-new.html |
| Workspace Environment Management Service | https://docs.citrix.com/en-us/workspace-environment-management-service | https://docs.citrix.com/en-us/workspace-environment-management-service#whats-new |
| XenApp and XenDesktop (legacy) | https://docs.citrix.com/en-us/xenapp-and-xendesktop | none |
| XenCenter | https://docs.xenserver.com/en-us/xencenter | https://docs.xenserver.com/en-us/xencenter/current-release/whats-new.html |
| XenMobile (legacy) | https://docs.citrix.com/en-us/xenmobile | https://docs.citrix.com/en-us/xenmobile/server/whats-new |
| XenServer 8.4 | https://docs.xenserver.com/en-us/xenserver/8 | https://docs.xenserver.com/en-us/xenserver/8/whats-new.html |
| XenServer 9 | https://docs.xenserver.com/en-us/xenserver/9 | https://docs.xenserver.com/en-us/xenserver/9/whats-new.html |
| XenServer SDK | https://docs.xenserver.com/en-us/xenserver/developer | none |
