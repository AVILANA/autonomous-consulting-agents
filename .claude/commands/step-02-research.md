FIRST: Read memory.md in the project root. This contains accumulated quality standards and learnings from previous executions. Apply all quality standards listed there throughout this step.

# Step 2: Company Research Analyst

Read all sources collected in Step 1 and produce the core company research outputs.

## Outputs
- `outputs/{company}/company_snapshot.md`
- `outputs/{company}/management_roadmap.md`
- `outputs/{company}/sector_context.md`

## Instructions
Perform three analyses:
1. Company strategic and financial snapshot: The financial snapshot MUST include a clear P&L structure table for each available year showing: Revenue, COGS (broken down if disclosed — including logistics, warehousing, freight-in components), Gross Profit, Total Operating Expenses (not just SG&A — many fulfillment and logistics costs sit in COGS, not SG&A), Operating Income, EBITDA, Net Income. Also include CapEx, Debt levels, and Working Capital components. If specific line items are not disclosed, state it explicitly. If the company reports supply chain or logistics costs within COGS, extract and highlight them separately. This is not optional — without operating cost structure, the analysis has no foundation.
2. Management strategy and roadmap
3. Industry context

Use the company’s public filings, investor presentations, and transcripts as evidence. Tag every claim as [FACT], [INFERENCE], or [ASSUMPTION].

## DATA FRESHNESS RULE — MANDATORY
For every KPI and every data point used in any output:

1. Always use the most recent available figure. If FY2025 data exists for a metric (even from a press release or earnings transcript), use FY2025. Only fall back to FY2024 if the specific metric was not disclosed in any FY2025 source.
2. Every number must show its fiscal year in parentheses. Not just "21.0%" but "21.0% (FY2024)" or "€24.8B (FY2025)". The year is mandatory. No exceptions.
3. If a KPI uses an older fiscal year than the most recent results, add a small note explaining why: "(FY2024 — FY2025 breakdown not yet published)". This tells the reader you looked for newer data and it wasn’t available, not that you were lazy.
4. Never mix fiscal years within a single calculation without flagging it. If you calculate inventory as % of revenue using FY2024 inventory and FY2025 revenue, that’s a mismatched calculation. Either use FY2024 inventory ÷ FY2024 revenue, or FY2025 inventory ÷ FY2025 revenue. If you must cross years, state it explicitly: "[Company] FY2024 inventory on FY2025 revenue (cross-year estimate)."
5. In the P&L table and financial snapshot, each column header must show the fiscal year explicitly: "FY2025", "FY2024", "FY2023". If the most recent year is incomplete (press release only, full annual report pending), label it "FY2025 (preliminary)" and note which line items are confirmed vs estimated.
