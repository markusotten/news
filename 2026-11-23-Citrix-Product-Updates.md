# Citrix Product Updates
*Last 24 hours — 2026-11-23*

## Citrix

### Unicon eLux Scout — UniconOS & UniconOS Management 2611 LTSR (released 2026-11-20, docs published 2026-11-22)

**Important upgrade notes**
- **Breaking change: new Microsoft Entra app for AVD and Entra ID sign-in:** The AVD client and device sign-in now use a different Entra application (ID 491bb6b0-…). A tenant admin must grant consent and update Conditional Access, assignments and allowlists before devices are updated. Otherwise sign-ins can fail. The old app will be retired. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **License Server 2607 or later required:** UniconOS Management 2611 needs Citrix License Server 2607 (build 56200) or later. With an older server, Scout runs on its grace period and stops serving devices when the grace period ends. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))

**Authentication & SSO**
- **AVD client on the new Entra application:** The new `OauthClientId` setting (terminal.ini, section AVD) can keep devices on the old app during a staged rollout or point them at your own app registration. Users sign in once more after the update. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Imprivata XenDesktop automation with a desktop chooser:** After an Imprivata tap-in, UniconOS reads the user's desktops from the StoreFront stores in the Imprivata policy. It starts the desktop, or shows a chooser if the user has several. Users with different desktops can now share one boot-to-VDI device. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Imprivata log-off on tap-out or inactivity:** If the Imprivata policy is set to log off, a tap-out, the hot key or inactivity now logs the user off UniconOS and disconnects the Citrix session. The Windows session stays signed in for a later reconnect. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Imprivata web applications open automatically:** UniconOS follows the Local Web Applications policies of Imprivata EAM 26.3 and later. After sign-in, Chrome opens the user's web apps and the Imprivata extension signs the user in to them. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))

**Input, accessibility & localization**
- **On-screen keyboard that can't be closed:** A new setting removes the close button of the on-screen keyboard on touch-only devices. A matching user right keeps users from turning the setting back off. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **More languages in Management Board:** Hebrew and Korean can now be set as desktop languages and German (Neo 2) as a keyboard layout centrally, also through the REST API. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))

**Connectivity & hardware**
- **Parallel network connections:** Ethernet, Wi-Fi and mobile connections can stay up at the same time. Traffic uses a preferred link (Ethernet by default) and fails over to the others, for example when a laptop is undocked. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **MAC address passthrough on the HP USB-C Dock G5:** Selected Lenovo ThinkPad L15/L16 AMD models keep their own MAC address when docked. This needs a BIOS setting and the new MAPT package. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **eSIM profile management on the device:** Users can add an eSIM profile by QR code or activation code, and delete it again. UniconOS switches the SIM slot and profile automatically, and this also works through a proxy. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Lenovo Smartcard Keyboard 5000 reader support:** UniconOS detects the built-in smart card reader without a custom driver bundle. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **CUPS driver, PPD model and printer options centrally:** Administrators can set the CUPS driver, PPD model and options such as PageSize in the device configuration or through the REST API. Label printers no longer need advanced file entries. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))

**Deployment, VDI & migration**
- **USB recovery image in the AllPackages ZIP:** The recovery .dd image is now in the ZIP and is imported together with the packages. A recovery stick can be exported right away. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))

**Device management & provisioning**
- **Image management in UniconOS Management Board:** The new Software section replaces ELIAS. It provides containers, image builds with automatic dependency solving, signing, certificate management and per-container rights. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Images held back after a package change:** If a package file changes after an image was saved, Software withdraws the image until a signer accepts the change. Devices keep their installed image in the meantime. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Export a package from the Software library:** A package version can be downloaded as one .zip with its features and signatures, ready to import into another container. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Firmware settings of an image:** A saved image now shows the protocol, server, path and file to enter in the device firmware configuration, each with a copy button. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Boot to VDI start scenario in Management Board:** Boot to VDI, the Citrix store and the target desktop or app can now be set centrally, with no advanced file entries. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Configuration templates:** Ready-made templates are available for Boot to VDI, Boot to apps and kiosk mode (Workspace app or built-in browser). You can copy, adapt, export and link them to rules. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Kiosk Mode section removed:** The unused Kiosk Mode section of the device configuration is gone. Kiosk mode through KioskMode/kioskmode.ini continues to work. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Central browser prompt suppression:** Password-save prompts can be turned off and trusted origins set centrally. With UniconOS 2609 or later, Workspace app then opens without browser prompts. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Server-side OU password check:** Scout Server now enforces access passwords for protected or hidden OUs. By default it rejects devices that send no password, so check your OU filter rules after the upgrade. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))

**Platform & administration**
- **Management Board is the only console:** Scout Console, Scout Report Generator, legacy ELIAS and scmd.exe are removed on upgrade. Web-based ELIAS 18 is discontinued, and from UniconOS 2612 images can only be built in Software. ([Deprecation](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new/deprecation.html))
- **Citrix branding and the UniconOS Management name:** Management Board adopts Citrix colors, fonts and logos, and most eLux/Scout labels are renamed. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Collapsible side panel:** The side panel can be hidden on the Devices, Security, Preferences and Software pages, so lists get the full width. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **New REST API endpoints:** You can list the devices of an OU page by page with selected fields, and read or change device preferences such as the default OU and the name template. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Restored or copied databases start without an unlock code:** Scout binds the license data to a restored or copied database by itself, and entitlement is still checked through the License Server. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Per-installation data key for stored passwords:** Stored passwords are encrypted with an installation-specific key. The key is kept in the database, or optionally in a key file on each server. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Stored passwords are never returned:** The UI, the REST API and configuration exports only show whether a password is set. Label passwords sent through the REST API are now encrypted. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Configuration files protected:** Standard Windows users can no longer read or change eluxd.ini, install.ini and other Scout configuration files. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Sign-in rate limiting:** After 10 failed sign-ins within 15 minutes, further attempts are blocked for up to 15 minutes (HTTP 429 in the API). Device passwords are limited the same way. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Session timeouts:** Sessions end after 30 minutes of inactivity and 12 hours at the latest. Both limits are configurable in .env.custom. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **More label settings reach devices:** Wi-Fi, mobile and VPN profiles, drives, printers, SAML, user rights and other label settings now apply to devices. Devices may change behavior after the upgrade. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Input validation for file destinations and text files:** Invalid paths and INI entries are rejected on save, and Windows line endings, BOMs and typographic quotes are flagged. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Database Layer client check on by default:** Ports 22150 and 22151 accept only the Scout server and the listed hosts. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Self-configuring Scout Server clusters:** Servers that share a database keep a common key and find each other automatically. A new Node health view shows the event flow for each server. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Safer AD/LDAPS sign-in:** The Windows certificate store is trusted for LDAPS, and domain controllers found through DNS must prove that they belong to the domain. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))

**Licensing**
- **Clearer License Server status:** Management Board now reports "too old" and "gives no license" instead of a generic "not reachable". ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **License Server certificate pinning:** Scout remembers the License Server certificate and rejects an untrusted replacement. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Citrix License Server is the only on-premises model:** The MSP, Enterprise Subscription and Software Maintenance models are retired. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Activation keys and per-device licenses removed:** Temporary licenses and threshold alerts are gone too, and devices with eLux RP 5 or earlier get no license. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **"Automatically request licenses" OU setting removed:** Fluendo licenses are now always assigned. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))
- **Health check reports the license state:** The check returns license details instead of HTTP 423/402, so monitoring must be adjusted. ([What's new](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new.html))

**Fixes & known issues**
- **Fixed issues in UniconOS Management 2611:** This release fixes installation, upgrade and database problems, including a setup path that could drop database tables. It also fixes a licensing bug that blocked firmware updates after 12 months, plus sign-in issues in Management Board. ([Fixed issues](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new/fixed_issues.html))
- **Known issues in UniconOS Management 2611:** These cover multi-server clusters (allowed hosts, Software Management on one server only), silent upgrade password handling and License Server certificate updates. ([Known issues](https://docs.citrix.com/us/en/unicon-elux-scout/2611/whats_new/known_issues.html))

---

<sub>
Window: 2026-11-22 ~02:15 UTC → 2026-11-23 · Sources: 86 per-product sitemaps of docs.citrix.com, docs.netscaler.com and docs.xenserver.com (38,703 pages)<br>
The only pages with a modification date in the window are the new Unicon eLux Scout 2611 doc set (590 pages, dated 2026-11-22). No changes were found on docs.netscaler.com or docs.xenserver.com.
</sub>
