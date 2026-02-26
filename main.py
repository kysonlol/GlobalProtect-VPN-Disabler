import subprocess
import time
import shutil
import sys

pwsh = shutil.which("pwsh") or shutil.which("powershell")
if not pwsh:
    print("PowerShell not found on PATH.")
    sys.exit(1)

ps_script = r'''
$procs = "PanGPA","PanGpHip","PanGpHipMp","GlobalProtect"
foreach ($p in $procs) {
    Stop-Process -Name $p -Force -ErrorAction SilentlyContinue
}

$localPath   = "$env:LOCALAPPDATA\Palo Alto Networks"
$roamingPath = "$env:APPDATA\Palo Alto Networks"

$logFile = Join-Path $localPath "GlobalProtect\PanGPA.log"
if (Test-Path $logFile) {
    Set-Content $logFile -Value "" -ErrorAction SilentlyContinue
}

if (Test-Path $localPath) {
    Get-ChildItem $localPath -Recurse -Force -ErrorAction SilentlyContinue |
        Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
}

if (Test-Path $roamingPath) {
    Remove-Item $roamingPath -Recurse -Force -ErrorAction SilentlyContinue
}

Write-Host "User-level GlobalProtect data cleaned."

'''

def run_powershell(script):
    cmd = [pwsh, "-NoProfile", "-NonInteractive", "-Command", f"& {{ {script} }}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

try:
    while True:
        res = run_powershell(ps_script)
        print(res.stdout, end="")
        if res.stderr:
            print("ERROR:", res.stderr, file=sys.stderr)
        time.sleep(3)
except KeyboardInterrupt:
    print("\nStopped by user.")

