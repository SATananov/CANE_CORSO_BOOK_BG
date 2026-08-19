$ErrorActionPreference = "Stop"

$ROOT = "$env:USERPROFILE\Desktop\CANE_CORSO_BOOK_BG"
Set-Location $ROOT

Write-Host "=== CANE CORSO BG - PLANNING / AGENT SYSTEM ==="

if (-not (Test-Path ".\references\PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf")) {
    throw "Italian reference missing"
}

python ".\tools\bg_phase_guard.py"
if ($LASTEXITCODE -ne 0) { throw "BG phase guard failed" }

Write-Host ""
Write-Host "Files installed:"
@(
    "AGENTS.md",
    "BG_MASTER_PLAN.md",
    "BG_STYLE_LOCK.md",
    "BG_TRANSLATION_RULES.md",
    "BG_PAGE_INVENTORY.md",
    "BG_PHASE_STATE.json",
    "agents\bg-orchestrator.md",
    "agents\translation-guardian.md",
    "agents\visual-master-guardian.md",
    "agents\image-text-guardian.md",
    "agents\final-qa-guardian.md",
    "tools\bg_phase_guard.py"
) | ForEach-Object {
    if (-not (Test-Path $_)) { throw "Missing: $_" }
    Write-Host "  PASS  $_"
}

Write-Host ""
Write-Host "BG-00 PLANNING SYSTEM: PASS"
Write-Host "ACTIVE PHASE: BG-01"
Write-Host "MODE: REPORT ONLY"
Write-Host ""
git status --short
