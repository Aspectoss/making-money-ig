# Injects today's money-machine task when a Cursor session starts in this project.
$inputJson = [Console]::In.ReadToEnd() | ConvertFrom-Json
$root = if ($inputJson.workspace_roots) { $inputJson.workspace_roots[0] } else { (Get-Location).Path }

$dailyScript = Join-Path $root "scripts\daily.ps1"
$context = "Money Machine project active. Run scripts/daily.ps1 and report today's Instagram reel to post."

if (Test-Path $dailyScript) {
    $output = & powershell -NoProfile -ExecutionPolicy Bypass -File $dailyScript 2>&1 | Out-String
    if ($output.Length -gt 2000) { $output = $output.Substring(0, 2000) + "..." }
    $context = "Money Machine autopilot context:`n$output"
}

@{ additional_context = $context } | ConvertTo-Json -Compress
exit 0
