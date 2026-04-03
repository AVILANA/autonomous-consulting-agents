FIRST: Read memory.md in the project root. This contains accumulated quality standards and learnings from previous executions. Apply all quality standards listed there throughout this step.

# Step 8: Final Executive Memo + Visuals

Read all prior outputs before completing this step.

## Outputs
- `outputs/{company}/final_memo.md`
- `outputs/{company}/visuals_data.md`

## Memo Sections
0. Executive Summary — Multi-Agent Analysis Overview. This section summarizes the key findings from each analytical step as a CLEAN table. Replace the prior format with this mandatory format:

The executive summary table must use these column headers: Agent | Role | Top 3 Findings
Do NOT include Source Collection as an agent — it is infrastructure, not analysis.

Number the agents as Agent 1 through Agent 7. The table should look like:

| Agent | Role | Top 3 Findings |
|---|---|---|
| Agent 1 | Company Research Analyst | • **finding 1** • **finding 2** • **finding 3** |
| Agent 2 | Peer Benchmark Analyst | • ... |
| Agent 3 | Operating Model Analyst | • ... |
| Agent 4 | AI Value Analyst | • ... |
| Agent 5 | Current Signals Analyst | • ... |
| Agent 6 | Due Diligence Analyst | • ... |
| Agent 7 | Executive Memo Composer | • **Overall thesis confidence** • **Primary recommendation** • **Biggest risk** |

Agent 7 is the memo composer itself — it summarizes its own conclusion as the final row. This shows that even the synthesis layer is an agent with a defined role.

Format requirements:
- Each row has EXACTLY 3 bullet points.
- Each bullet max 15 words.
- Key insight in each bullet must be in bold.
- No paragraphs, no prose.
- SUPPLY CHAIN PRIORITY: In the executive summary agent table, each agent's 3 bullet points should prioritize supply chain related findings over other findings. If an agent has both supply chain and non-supply-chain findings, lead with supply chain. Supply chain findings include: procurement, demand planning, sourcing, inventory, warehousing, transportation, freight audit, returns, logistics, and network design.
- CRITICAL: Agent 4 (AI Value Analyst) bullet points in the executive summary MUST focus on the top 3 SUPPLY CHAIN opportunities specifically (e.g., demand sensing, tariff scenario intelligence, warehouse optimization). Do NOT list marketing or generic AI opportunities for Agent 4.

Keep it scannable. An executive should understand the entire analysis in 60 seconds by reading this table.

CRITICAL: These findings must reflect the POST-due-diligence view. Before writing each step top 3, cross-reference against due_diligence.md. If due diligence challenged a finding, show the adjusted position, not the original optimistic claim.

Keep it scannable. An executive should understand the entire analysis in 60 seconds by reading this table.

CRITICAL: These findings must reflect the POST-due-diligence view. Before writing each step top 3, cross-reference against due_diligence.md. If due diligence challenged a finding, show the adjusted position, not the original optimistic claim.

## Instructions
Write the final executive pursuit memo. IMPORTANT RULES:
- Use SIMPLE language. Write so any business executive can understand, not just consultants or analysts.
- When you use an acronym, write it in full the first time with the acronym in parentheses. Example: Selling, General and Administrative expenses (SG&A).
- Avoid jargon. If a technical term is necessary, explain it briefly.
- Do NOT include a 12-week entry roadmap.

MEMO STRUCTURE:
1. Why Now — what has changed and why it matters for this company now. Keep it brief and sharp.
2. Company at a Glance — key financials, market position, operating model summary. Include a comparative table with ALL peers.
3. What We Believe Matters Most — the primary and secondary value lever (from our 5: Productivity, Efficiency, Quality, Velocity, Growth), with evidence.
4. Supply Chain AI Opportunities (DEEP DIVE) — for each supply chain area (procurement, planning, sourcing, warehousing, transportation, freight audit, returns), describe: the opportunity, expected benefit, and what we need to validate. Include a table summarizing all opportunities with estimated benefit potential (High/Medium/Low).
5. Other Opportunities (EXECUTIVE SUMMARY) — brief overview of non-supply-chain AI opportunities, grouped and concise.
6. Body or Brain First — is the first bottleneck in the physical operations or in the decision-making layer? What does that mean for where to start?
7. Reinforcing and Challenging Management Strategy — what we agree with vs what we would challenge.
8. Key Questions for Discovery — the 15 most important questions we need the client to answer, ranked by priority, with who we should ask.
9. Current Signals — recent developments creating urgency or opportunity.

BEFORE writing conclusions, read due_diligence.md. Let it inform your judgment without mentioning it explicitly.

---

CLIENT VERSION GUIDANCE. After the main memo, add a section separated by --- titled 'Client-Facing Preview Version'. Rewrite the key findings as if presenting TO the client, not about the client. Change tone from 'we believe Adidas should...' to 'based on public analysis, here are insights about your business that may be valuable...'. Remove any internal pursuit language, pricing, or engagement framing. Keep it as a demonstration of analytical capability — a preview of what deeper engagement could uncover.

visuals_data.md must include structured data for these charts:
- Spider chart: company vs peer average vs best-in-class across 6 metrics (all peers must be included, with normalized 0-100 scores)
- Value lever heatmap: 5 levers x supply chain areas, scored H/M/L
- Body vs Brain diagnosis per supply chain area
- Opportunity summary table: supply chain area, opportunity description, value lever, benefit potential, key validation question
