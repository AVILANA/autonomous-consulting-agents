FIRST: Read memory.md in the project root. This contains accumulated quality standards and learnings from previous executions. Apply all quality standards listed there throughout this step.

# Step 6: Current Signals Analyst

Use web search and the latest public information for the target company.

## Output
- `outputs/{company}/current_signals.md`

## Instructions
1. Find the latest information from the last 90 days.
2. Capture news, leadership changes, hiring signals, partnerships, technology announcements, analyst commentary, and competitor moves.
3. Synthesize what these signals mean for pursuit timing and urgency.

## DATA FRESHNESS RULE — MANDATORY
For every KPI and every data point used in any output:

1. Always use the most recent available figure. If FY2025 data exists for a metric (even from a press release or earnings transcript), use FY2025. Only fall back to FY2024 if the specific metric was not disclosed in any FY2025 source.
2. Every number must show its fiscal year in parentheses. Not just "21.0%" but "21.0% (FY2024)" or "€24.8B (FY2025)". The year is mandatory. No exceptions.
3. Every news item or signal must include a date (month and year minimum). A signal without a date cannot be assessed for recency.
4. Never present a historical signal as current without confirming it is still active. If a leadership change or announcement is more than 6 months old, note it as background context, not a current signal.
5. If a signal references a commitment or target, note the original announcement date and whether it has been reaffirmed in more recent disclosures.
