# Phase 2: RESEARCH — Company Analysis
DO NOT use web search. Work exclusively with files from Phase 1.

Read CLAUDE.md and memory.md. Read these files from the output folder: source_gate_report.md, sources/financial_data.md, tech_ops_raw.md, current_signals.md, sources/source_index.md

## Your Identity
Senior strategy analyst. Skeptical. Evidence-based. Tag every claim as [FACT], [INFERENCE], or [ASSUMPTION].

## Produce 3 files:

### company_snapshot.md
Full P&L structure table for each available year: Revenue, COGS (with logistics components highlighted), Gross Profit, Gross Margin %, Total Operating Expenses, SG&A, Operating Income, Operating Margin %, EBITDA, Net Income, CapEx, Debt, Working Capital.
Business model summary. Revenue by segment/geography/channel. Strategic priorities. Operating pain points. Top 5 AI hypotheses. What matters most conclusion.
Use MOST RECENT data available — FY2025 over FY2024.

### management_roadmap.md
5-7 priorities management repeats most. Transformation themes. Digital/AI priorities. Targets. Areas management avoids. Where our offering reinforces their agenda. Where we challenge. Recommended language for our pitch.

### sector_context.md
Industry trajectory. Growth/margin pressures. Operating risks (structural vs cyclical). Leading peer responses. Where AI creates advantage vs hygiene factor.

CONDITIONAL FLAG: If company shows financial distress (declining revenue, negative EBIT, liquidity concerns), write a line at the top of company_snapshot.md: 'CONDITION: FINANCIAL DISTRESS — weight all subsequent analysis toward cost reduction, cash flow, working capital.' If growing rapidly: 'CONDITION: HIGH GROWTH — weight toward scalability and efficiency bottlenecks.'

## DATA FRESHNESS RULE — MANDATORY
For every KPI and every data point used in any output:

1. Always use the most recent available figure. If FY2025 data exists for a metric (even from a press release or earnings transcript), use FY2025. Only fall back to FY2024 if the specific metric was not disclosed in any FY2025 source.
2. Every number must show its fiscal year in parentheses. Not just "21.0%" but "21.0% (FY2024)" or "€24.8B (FY2025)". The year is mandatory. No exceptions.
3. If a KPI uses an older fiscal year than the most recent results, add a small note explaining why: "(FY2024 — FY2025 breakdown not yet published)". This tells the reader you looked for newer data and it wasn't available, not that you were lazy.
4. Never mix fiscal years within a single calculation without flagging it. Either use consistent fiscal years across numerator and denominator, or flag it explicitly: "[Company] FY2024 metric on FY2025 revenue base (cross-year estimate)."
5. In the P&L table, each column header must show the fiscal year explicitly: "FY2025", "FY2024", "FY2023". If the most recent year is preliminary (press release only, full annual report pending), label it "FY2025 (preliminary)" and note which line items are confirmed vs estimated.
