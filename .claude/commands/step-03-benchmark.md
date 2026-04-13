FIRST: Read memory.md in the project root. This contains accumulated quality standards and learnings from previous executions. Apply all quality standards listed there throughout this step.

# Step 3: Peer & Benchmark Analyst

Read `company_snapshot.md` and `sector_context.md` before completing this step.

## Outputs
- `outputs/{company}/peer_set.md`
- `outputs/{company}/benchmark_table.md`

## Instructions
1. CRITICAL: Ensure geographic diversity — include competitors from at least 2 of 3 major regions (Americas, Europe, Asia-Pacific). Before finalizing, run a web search for top publicly listed competitors to verify no major player is missing. If you exclude one, explain why.
2. Construct a relevant benchmark peer set with rationale.
3. The benchmark_table.md must include a FULL comparative table with ALL peers side by side showing: Revenue, Revenue Growth, Gross Margin, Operating Margin, EBITDA Margin, SG&A % Revenue, Total Operating Cost % Revenue (or SG&A + identified COGS operational components). Note: for companies with outsourced manufacturing, logistics and fulfillment costs often sit in COGS. In the comparative table, include BOTH SG&A % Revenue AND Total Operating Cost % Revenue. Note explicitly for each company whether logistics and fulfillment costs are reported within COGS or SG&A — this varies by company and makes SG&A-only comparisons misleading. Add a footnote explaining where supply chain costs sit in each company P&L structure. This is critical because a company can have low SG&A but high total OPEX if warehousing, freight, and fulfillment costs sit in COGS. The benchmark must compare like-for-like operating cost structures, not just SG&A line items., CapEx Intensity, and any available service/quality metrics. Every peer must appear in the table — do not compare only a subset.
4. Produce a P&L benchmark analysis that compares the company to peers.
5. Highlight where the company outperforms, lags, and what gaps AI/automation can address.
6. Include structured data for visual comparison: a table with normalized scores (0-100) for each peer across 6 key metrics, ready to be used for a spider/radar chart.
7. Label findings as [OBSERVABLE] or [ESTIMATED].

## DATA FRESHNESS RULE — MANDATORY
For every KPI and every data point used in any output:

1. Always use the most recent available figure. If FY2025 data exists for a metric (even from a press release or earnings transcript), use FY2025. Only fall back to FY2024 if the specific metric was not disclosed in any FY2025 source.
2. Every number must show its fiscal year in parentheses. Not just "21.0%" but "21.0% (FY2024)" or "€24.8B (FY2025)". The year is mandatory. No exceptions.
3. If a KPI uses an older fiscal year than the most recent results, add a small note explaining why: "(FY2024 — FY2025 breakdown not yet published)". This tells the reader you looked for newer data and it wasn't available, not that you were lazy.
4. Never mix fiscal years within a single calculation without flagging it. Either use consistent fiscal years across numerator and denominator, or flag it explicitly as a cross-year estimate.
5. For peer companies, each company has its own fiscal year end. Note each peer's fiscal year explicitly in the benchmark table: e.g., "Nike FY2025 (ends May 2025)", "ASICS FY2024 (ends Dec 2024)". Use the most recent published annual for each peer. Add a footnote to the benchmark table listing the fiscal year reference for every company in the peer set.
