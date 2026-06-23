# GlobalProtect VPN Disabler

> [!CAUTION]
> This is purely for educational purposes. Do not use on educational devices or devices that enforce VPN entries.


# Description

This is a PowerShell script for Windows that forcefully stops GlobalProtect VPN service by eliminating `PanGPA.exe`, etc. All without administrator.

Useful for devices who have a VPN installed via GlobalProtect that is configured as `Always-On` and wants to disable it temporaily.

# GlobalProtect

GlobalProtect is a VPN-service used by enterprise's, companies or businesses. The main goal is to ensure that a firewall is always active no matter what internet your connected to. For example: a school laptop connected to the school Wifi will have the same internet restrictions as if the school laptop was connected to your home Wifi. Thats the power of a VPN.

By default, GlobalProtect, the app itself, has the ability to add VPN entries. These VPN entires can be removed by default. You can also add VPN entries, remove VPN entries and edit them. However, GlobalProtect has one enforcement policy. (A VPN entry is esssentially just the VPN portal domain (vpn.example.com), or an IP address).

Enterprises, etc, can force a VPN to enabled at all times and cannot be removed as an entry. This means that your administrator can ensure that no more VPN portals are removed, added, or edited. This script tries to disable the VPN entirely, even if your administrator prevents it from being disabled.

Additionally, on Windows, someone might think to clear the app data to clear local VPN entries. It's unknown whether it was like that before in older versions, but in newer versions, local user data are stored somewhere else. The script will attempt too clear it, but it won't work most of the time.

# Usage

Run `main.ps1`, or `main.py`.

`main.py` is more reliable. Use if possible. Otherwise, use `main.ps1`.

It may take more than one minute for the VPN to be fully disabled.

# Disclaimer

Palo Alto Networks is aware of this script (as I submitted it as a vulnerability) and it does not qualify as a vulnerability due to the nature of how the bypass is executed.

**Works as of:` 06/22/26*` **

