param(
    [string]$Root = (Split-Path -Parent $PSScriptRoot)
)

Set-Location $Root

Write-Host "=== Money Machine Daily Run ===" -ForegroundColor Cyan

& "$Root\scripts\sync-site.ps1"

$today = Get-Date -Format "yyyy-MM-dd"
$weekDirs = Get-ChildItem -Path "$Root\content" -Directory -Filter "week-*" -ErrorAction SilentlyContinue |
    Sort-Object Name -Descending

if (-not $weekDirs) {
    Write-Host "No content week found. Generating..." -ForegroundColor Yellow
    python "$Root\generate.py"
    $weekDirs = Get-ChildItem -Path "$Root\content" -Directory -Filter "week-*" | Sort-Object Name -Descending
}

$latestWeek = $weekDirs[0].FullName
$checklist = Join-Path $latestWeek "CHECKLIST.md"
$manifest = Join-Path $latestWeek "manifest.json"

Write-Host ""
Write-Host "Latest content pack: $latestWeek"
Write-Host "Checklist: $checklist"
Write-Host ""

if (Test-Path $manifest) {
    $data = Get-Content $manifest -Raw | ConvertFrom-Json
    $todayPost = $data.posts | Where-Object { $_.schedule.date -eq $today } | Select-Object -First 1

    if ($todayPost) {
        Write-Host "TODAY'S POST ($today):" -ForegroundColor Green
        Write-Host "  Hook: $($todayPost.hook)"
        Write-Host "  Time: $($todayPost.schedule.post_time)"
        Write-Host "  Folder: $($todayPost.folder)"
        Write-Host ""
        Write-Host "  Caption:" -ForegroundColor Green
        $captionPath = Join-Path $Root (Join-Path ($todayPost.folder -replace '/', '\') "caption.txt")
        Get-Content $captionPath | Write-Host
    } else {
        Write-Host "No post scheduled for $today in current week." -ForegroundColor Yellow
        Write-Host "Run: python generate.py"
    }
}

Write-Host ""
Write-Host "Site folder ready to deploy: $Root\site"
Write-Host "Push to GitHub main branch to auto-deploy Pages."
