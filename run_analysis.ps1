param(
    [Parameter(Mandatory=$true)]
    [string]$Company
)

$slug = $Company.ToLower() -replace '\s+', '-'
$out = "outputs/" + $slug
$env:ENABLE_CLAUDEAI_MCP_SERVERS = "false"
$tools = "WebSearch,Read,Write,Edit"

New-Item -Path "$out/sources" -ItemType Directory -Force | Out-Null

Write-Host "Starting analysis for $Company" -ForegroundColor Cyan

$steps = @(
    "step-01-sources",
    "step-02-research",
    "step-03-benchmark",
    "step-04-operating",
    "step-05-ai-value",
    "step-06-signals",
    "step-07-diligence",
    "step-08-memo"
)

$i = 0
foreach ($step in $steps) {
    $i++
    Write-Host "[$i/8] $step" -ForegroundColor Yellow
    $prompt = "Read CLAUDE.md, memory.md, and .claude/commands/$step.md. Read all files in $out/ for prior context. Execute the instructions for $Company. Use web search when needed. Save all outputs to $out/"
    claude -p $prompt --allowedTools $tools
    Write-Host "[$i/8] Done - Evaluating..." -ForegroundColor DarkYellow
    $evalPrompt = "Read memory.md and .claude/commands/evaluate-step.md. Evaluate the outputs just produced by $step for $Company in $out/. If any quality check fails, fix the output. Save evaluation to $out/evaluation_$step.md"
    claude -p $evalPrompt --allowedTools "Read,Write"
    Write-Host "[$i/8] Verified" -ForegroundColor Green
}

Write-Host ""
Write-Host "Updating memory..." -ForegroundColor Yellow
claude -p "Read CLAUDE.md and .claude/commands/update-memory.md. Read all files in $out/. Update memory.md with execution history and learnings from the $Company analysis." --allowedTools "Read,Write"
Write-Host "Memory updated" -ForegroundColor Green

Write-Host ""
Write-Host "Analysis complete: $Company" -ForegroundColor Cyan
Get-ChildItem -Path $out -Recurse -File | ForEach-Object { Write-Host ("  " + $_.Name) -ForegroundColor Gray }