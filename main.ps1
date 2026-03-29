# made by kysonlol

while ($true) {
 $process = Get-Process -Name "PanGPA" -ErrorAction SilentlyContinue
 
 if ($process) {
 Stop-Process -Name "PanGPA" -Force
 Write-Host "Terminated PanGPA.exe at $(Get-Date)" -ForegroundColor Yellow
 }
 
 Start-Sleep -Seconds 5
}s 
