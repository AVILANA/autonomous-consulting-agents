# Phase 3: BENCHMARK — Peer Analysis
DO NOT use web search. Work exclusively with Phase 1 and Phase 2 files.

Read CLAUDE.md and memory.md. Read: peer_raw_data.md, company_snapshot.md from output folder.

## Produce 2 files:

### peer_set.md
For each peer (7-9 companies): why included, business overlap, revenue, operating model similarity, comparability caveats. Organized in tiers. Geographic diversity across Americas, Europe, Asia-Pacific verified.

CONDITIONAL FLAG: If one peer shows a dramatically superior margin trajectory, flag it: 'STANDOUT PEER: [name] — deep-dive this peer trajectory and make comparison central to provocations.'

### benchmark_table.md
Full comparative table with ALL peers side by side: Revenue (3 years), Revenue Growth, Gross Margin, Operating Margin, EBITDA Margin, SG&A % Revenue, Total Operating Cost % Revenue (note where logistics costs sit in COGS vs SG&A for each company), CapEx Intensity, Revenue per Employee, DTC %, E-commerce %.
Where company outperforms. Where it lags. Which gaps addressable by AI. Which structural.
Include normalized scores (0-100) for spider chart data.
Tag each finding as [OBSERVABLE] or [ESTIMATED].

## DATA FRESHNESS RULE — MANDATORY
For every KPI and every data point used in any output:

1. Always use the most recent available figure. If FY2025 data exists for a metric (even from a press release or earnings transcript), use FY2025. Only fall back to FY2024 if the specific metric was not disclosed in any FY2025 source.
2. Every number must show its fiscal year in parentheses. Not just "21.0%" but "21.0% (FY2024)" or "€24.8B (FY2025)". The year is mandatory. No exceptions.
3. If a KPI uses an older fiscal year than the most recent results, add a small note explaining why: "(FY2024 — FY2025 breakdown not yet published)". This tells the reader you looked for newer data and it wasn't available, not that you were lazy.
4. Never mix fiscal years within a single calculation without flagging it. Either use consistent fiscal years, or flag cross-year estimates explicitly.
5. For peer companies, each company has its own fiscal year end. Note each peer's fiscal year explicitly in the benchmark table (e.g., "Nike FY2025 (ends May 2025)", "ASICS FY2024 (ends Dec 2024)"). Use the most recent published annual for each peer. Add a footnote to the benchmark table listing the fiscal year reference for every company in the peer set.
