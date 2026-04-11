param(
    [Parameter(Mandatory=$true)]
    [string]$Company
)
 
$slug = $Company.ToLower() -replace '\s+', '-'
$out = "outputs/" + $slug
$env:ENABLE_CLAUDEAI_MCP_SERVERS = "false"
 
New-Item -Path "$out/sources" -ItemType Directory -Force | Out-Null
 
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " AUTONOMOUS CONSULTING AGENTS v3" -ForegroundColor Cyan
Write-Host " Company: $Company" -ForegroundColor Cyan
Write-Host " Architecture: 7-Phase Pipeline" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
 
$start = Get-Date
 
# PHASE 1: GATHER (ONLY phase with web search)
Write-Host "[1/7] GATHER - Collecting all data..." -ForegroundColor Yellow
$p1 = "Read CLAUDE.md, memory.md, and .claude/commands/phase-01-gather.md. Execute comprehensive data gathering for $Company. This is the ONLY phase that uses web search. Collect financial filings, technology data, current signals, and peer data. Save all to $out/"
claude -p $p1 --allowedTools "WebSearch,Read,Write,Edit"
Write-Host "[1/7] GATHER complete." -ForegroundColor Green
 
# Check source gate
if (Test-Path "$out/source_gate_report.md") {
    $gate = Get-Content "$out/source_gate_report.md" -Raw
    if ($gate -match "FAIL") {
        Write-Host "[STOPPED] Source gate FAILED." -ForegroundColor Red
        Write-Host "Check: $out/source_gate_report.md" -ForegroundColor Red
        Write-Host "Place missing files in: inputs/$slug/manual/" -ForegroundColor Yellow
        exit 1
    }
}
 
# PHASE 2: RESEARCH (no web search)
Write-Host "[2/7] RESEARCH - Company analysis..." -ForegroundColor Yellow
$p2 = "Read CLAUDE.md, memory.md, and .claude/commands/phase-02-research.md. Read source_gate_report.md, sources/financial_data.md, tech_ops_raw.md, current_signals.md, sources/source_index.md from $out/. DO NOT use web search. Produce company_snapshot.md, management_roadmap.md, sector_context.md in $out/"
claude -p $p2 --allowedTools "Read,Write,Edit"
Write-Host "[2/7] RESEARCH complete." -ForegroundColor Green
 
# PHASE 3: BENCHMARK (no web search)
Write-Host "[3/7] BENCHMARK - Peer analysis..." -ForegroundColor Yellow
$p3 = "Read CLAUDE.md, memory.md, and .claude/commands/phase-03-benchmark.md. Read peer_raw_data.md and company_snapshot.md from $out/. DO NOT use web search. Produce peer_set.md and benchmark_table.md in $out/"
claude -p $p3 --allowedTools "Read,Write,Edit"
Write-Host "[3/7] BENCHMARK complete." -ForegroundColor Green
 
# PHASE 4: DEEP ANALYSIS (no web search)
Write-Host "[4/7] DEEP ANALYSIS - Operating model + AI value..." -ForegroundColor Yellow
$p4 = "Read CLAUDE.md, memory.md, and .claude/commands/phase-04-deep-analysis.md. Read company_snapshot.md, sector_context.md, management_roadmap.md, benchmark_table.md, tech_ops_raw.md, current_signals.md from $out/. DO NOT use web search. Execute Sub-section A fully and save files, THEN execute Sub-section B. Produce tech_ops_footprint.md, transformation_capacity.md, value_levers.md, stream_ranking.md, body_brain_diagnosis.md, moat_analysis.md in $out/"
claude -p $p4 --allowedTools "Read,Write,Edit"
Write-Host "[4/7] DEEP ANALYSIS complete." -ForegroundColor Green
 
# PHASE 5: CHALLENGE (no web search)
Write-Host "[5/7] CHALLENGE - Due diligence + provocations..." -ForegroundColor Yellow
$p5 = "Read CLAUDE.md, memory.md, and .claude/commands/phase-05-challenge.md. Read ALL files in $out/. Execute four jobs in order: conditional routing, due diligence, provocation generation with dual lever tags, quality self-evaluation. Produce routing_decisions.md, due_diligence.md, provocations.md, quality_evaluation.md, discovery_questions.md in $out/"
claude -p $p5 --allowedTools "Read,Write,Edit"
Write-Host "[5/7] CHALLENGE complete." -ForegroundColor Green
 
# PHASE 6: PRODUCE (no web search)
Write-Host "[6/7] PRODUCE - Final documents..." -ForegroundColor Yellow
$p6 = "Read CLAUDE.md, memory.md, and .claude/commands/phase-06-produce.md. Read ALL files in $out/. Produce client_document.md, internal_memo.md, visuals_data.md in $out/"
claude -p $p6 --allowedTools "Read,Write,Edit"
Write-Host "[6/7] PRODUCE complete." -ForegroundColor Green
 
# PHASE 7: CLIENT HTML PRESENTATION (no web search)
Write-Host "[7/7] PRESENT - Client HTML presentation..." -ForegroundColor Yellow
$p7 = "Read CLAUDE.md, memory.md, and .claude/commands/phase-07-client-html.md. Read ALL files in $out/ for context. Execute for $Company. Include Section 0 KPI Dashboard before provocations. Use Tailwind CSS and Plotly CDN. Keep all 3 tabs. Save to $out/client_presentation.html"
claude -p $p7 --allowedTools "Read,Write,Edit"
Write-Host "[7/7] PRESENT complete." -ForegroundColor Green
 
# UPDATE MEMORY
Write-Host "Updating memory..." -ForegroundColor Yellow
claude -p "Read CLAUDE.md and .claude/commands/update-memory.md. Read all files in $out/. Update memory.md with execution history and learnings from the $Company analysis." --allowedTools "Read,Write"
Write-Host "Memory updated." -ForegroundColor Green
 
$elapsed = ((Get-Date) - $start).TotalMinutes
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " COMPLETE: $Company" -ForegroundColor Cyan
Write-Host " Time: $([math]::Round($elapsed,1)) minutes" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Files:" -ForegroundColor White
Get-ChildItem -Path $out -Recurse -File | ForEach-Object { Write-Host ("  " + $_.Name) -ForegroundColor Gray }