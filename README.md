# GlobalProtect VPN Disabler

> [!CAUTION]
> This is purely for educational purposes. Do not use on educational devices or devices that enforce VPN entries.

> [!WARNING]
> This can consume a lot of RAM and will cause battery drainage if the script is ran for too long. See more information at the bottom of this readme.

# Description

This is a Python script for Windows that forcefully stops GlobalProtect VPN service by eliminating its processes, etc. All without administrator.

Due to the nature of this script, it can cause memory consumption & battery drainage. The script should be considered a last choice, since theres still other options to go about disabling GlobalProtect if a VPN entry is configured as `Always-On`.

Useful for devices who have a VPN installed via GlobalProtect that is configured as `Always-On` and wants to disable it temporaily.

# GlobalProtect

GlobalProtect is a VPN-service used by enterprise's, companies or businesses. The main goal is to ensure that a firewall is always active no matter what internet your connected to. For example: a school laptop connected to the school Wifi will have the same internet restrictions as if the school laptop was connected to your home Wifi. Thats the power of a VPN.

By default, GlobalProtect, the app itself, has the ability to add VPN entries. These VPN entires can be removed by default. You can also add VPN entries, remove VPN entries and edit them. However, GlobalProtect has one enforcement policy. (A VPN entry is esssentially just the VPN portal domain (vpn.example.com), or an IP address).

Enterprises, etc, can force a VPN to enabled at all times and cannot be removed as an entry. This means that your administrator can ensure that no more VPN portals are removed, added, or edited. This script tries to disable the VPN entirely, even if your administrator prevents it from being disabled.

# Payload

1. Kills GlobalProtect related-userspace processes

```
$procs = "PanGPA","PanGpHip","PanGpHipMp","GlobalProtect"
foreach ($p in $procs) {
    Stop-Process -Name $p -Force -ErrorAction SilentlyContinue
}
```

**PanGPA** - GlobalProtect VPN service - unless privelleges are sufficient; this just won't work. You will most likely get an `Access is denied` error.

**PanGpHip** - Host Information profile collector

**PanGpHipMp** - HIP management process


2. Defines paths to user-level GP data

```
$localPath   = "$env:LOCALAPPDATA\Palo Alto Networks"
$roamingPath = "$env:APPDATA\Palo Alto Networks"
```

Specifies LocalAppData & AppData
  

3. Empty the PanGPA.log file

```
$logFile = Join-Path $localPath "GlobalProtect\PanGPA.log"
if (Test-Path $logFile) {
    Set-Content $logFile -Value "" -ErrorAction SilentlyContinue
}
```

The exact usage of this file is unknown, but clearing it reduces the risk of file-in-use errors when deleting the folder.


4. Delete everything in LocalAppData except locked files

```
if (Test-Path $localPath) {
    Get-ChildItem $localPath -Recurse -Force -ErrorAction SilentlyContinue |
        Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
}
```

Anything that is in-use, or locked, cannot be deleted.


5. Wipe user-related data (Disclaimer)

```
if (Test-Path $roamingPath) {
    Remove-Item $roamingPath -Recurse -Force -ErrorAction SilentlyContinue
}
```

This will wipe userdata, but this will not work on recent versions.

This means the VPN portal may be still intact after the script is finished being ran.


# How this works

Technically, this is not considered a "race-condition", but it takes advantage of a small time window when processes are eliminated.

Because we are terminating all GlobalProtect userspace processes & deleting it's related folders faster than it can recover, the VPN service can never recover, since the PowerShell script runs every 3 seconds.

This is NOT a Global Protect issue, but infact a Windows issue.

# Usage

Run `main.py`. Once the script is ran, it will automatically run a PowerShell script every 3 seconds.

You can keep it on, for as long as you like. But remember, the longer the script runs the more memory the script consumes, and will probably lag your device. Use with caution.

**During testing, we found out that stopping the Python script after a while may temporary kill the VPN until the next device reboot, or if GlobalProtect is opened manually.**

It may take more than one minute for the VPN to be fully disabled.
