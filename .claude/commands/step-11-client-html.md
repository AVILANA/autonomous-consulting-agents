ABSOLUTE RULES — VIOLATION OF ANY OF THESE IS A FAILURE:

1. DESIGN LOCK: Use the EXACT same CSS, fonts, colors, spacing, and layout as the previous version. Do NOT change font sizes. Do NOT change colors. Do NOT change card styling. Do NOT redesign anything. If you are not sure what the previous design looked like, keep every CSS rule identical. The only thing that changes between runs is the DATA CONTENT, never the design.

2. FACT TAGS MANDATORY: Every evidence bullet MUST end with a specific confidence-level tag in brackets. Use the EXACT confidence level — not just [INFERENCE] but one of:
- [FACT — source]
- [INFERENCE — HIGH CONFIDENCE — reasoning]
- [INFERENCE — MODERATE CONFIDENCE — reasoning]
- [INFERENCE — LOW CONFIDENCE — reasoning]
- [ASSUMPTION — basis]

The tag must match the actual confidence of that specific claim. NEVER use a generic [INFERENCE] without a confidence level.

CORRECT: 'project44 deployed February 2026. [FACT — project44 press release Feb 2026] No confirmed integration with demand planning system. [INFERENCE — HIGH CONFIDENCE — two confirmed platforms with no disclosed connection]'
WRONG: '[INFERENCE — planning integration gap]' — says nothing about confidence level

3. TITLE QUALITY: Each provocation title must be MAXIMUM 15 words. Must contain ONE specific number. Must use the word 'your' or 'you'. Must feel like a punch, not an explanation.

REFERENCE TITLES — Use these as your quality bar:
- 'Your inventory costs €1.1B more per year than it should.'
- 'Your e-commerce delivers in 3-7 days. Amazon delivers in 1-2.'
- 'A €200M tariff bill arrived. Your response takes weeks.'

If your title is longer than 15 words, you have FAILED. Cut it.

TITLE BENCHMARK: Before writing any title, read the APPROVED TITLE EXAMPLES section in memory.md. Those examples represent validated quality standards from prior runs — use them as an additional quality bar alongside the reference titles above.

4. DATA FRESHNESS RULE — MANDATORY: For every KPI and every data point rendered in the HTML:
   a. Always use the most recent available figure. If FY2025 data exists (even from a press release or earnings transcript), use FY2025. Only fall back to FY2024 if the specific metric was not disclosed in any FY2025 source.
   b. Every number must show its fiscal year. In the scorecard table, add the year next to each value (e.g., "21.0% (FY2024)" or "51.0% (FY2025)"). The year is mandatory. No exceptions.
   c. If a KPI uses an older fiscal year than the most recent results, add a small italic sub-note in the KPI description cell: "(FY2024 — FY2025 balance sheet not yet published)". This shows the reader you looked for newer data.
   d. Never mix fiscal years within a single calculation without flagging it. Cross-year estimates must be labeled: "(cross-year estimate)" next to the value.
   e. The column header should read "[Company] Actual" (not "[Company] Actual (FY2025)") when the dashboard mixes years across rows — individual years are shown per-value instead.
   f. Footnotes must include a "Peer fiscal years" line listing the fiscal year reference for every company in the peer set (e.g., "Nike: FY2025 (yr. ends May 2025), ASICS: FY2024 (yr. ends Dec 2024)..."). Do NOT lead with 2022 data. The 2022 overstock is CONTEXT, not the provocation. Lead with the most recent FY numbers available.

5. NO SELF-IMPROVEMENT: Do NOT add features, sections, or styling that were not explicitly requested. Do NOT reorganize sections. Do NOT change the order of elements. Produce exactly what is asked, nothing more.

6. SIMPLE LANGUAGE — MANDATORY: Write for a 16-year-old who understands business. No complex vocabulary. If a sentence needs a second read to understand, rewrite it. A COO reads 200 emails a day. Your sentence gets 3 seconds.
BANNED WORDS in titles: idle, dormant, bifurcated, materially, structurally, operationalized. Use everyday equivalents:
idle → unused / sitting empty | dormant → turned off / not used | bifurcated → split in two | materially → significantly | structurally → built into the system | operationalized → put to work / actually used

7. PEER COMPARISON MANDATORY: Each provocation's evidence bullets MUST include at least one specific peer comparison pulled from benchmark_table.md — a named competitor with a real number that makes the gap concrete. Example: 'ASICS tripled margin from 7% to 14.7% in 24 months.' A provocation without a peer fact is easier to dismiss.

---

Generate a standalone HTML file. Read provocations.md and client_output.md.

Load in the HTML <head>: Tailwind CSS from CDN (https://cdn.tailwindcss.com) and Plotly from CDN (https://cdn.plot.ly/plotly-latest.min.js). Use Tailwind for all styling. Purple-to-indigo gradient theme matching modern Accenture internal portals. Cards with subtle shadows, rounded corners, badges, clean typography. The design should look like a premium SaaS product landing page, not a consulting document.

Header: company name large, 'Outside-In Perspective: [COMPANY]' title, date, 'Confidential — Prepared for: Chief Operating Officer / VP Supply Chain'.

COMPANY LOGO: In the header, place the company logo inline to the left of the company name. For Adidas use: <img src='https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg' style='filter:invert(1);height:60px;vertical-align:middle;margin-right:15px;'> — the filter:invert(1) makes the black SVG logo white on the dark header. For other companies, find their Wikipedia SVG logo URL (pattern: https://upload.wikimedia.org/wikipedia/commons/[path]/[Company]_Logo.svg) and apply the same inline style. If no logo can be found, skip silently — do not show a broken image or placeholder.

ANALYTICAL BASIS LEGEND — immediately after the header, before Section 1:
Add a subtle, understated box styled with muted colors and small font (text-xs, text-gray-500, bg-gray-50, border border-gray-200, rounded, px-4 py-3). Do NOT make it prominent. Format as bullet points, each tag on its own line:

ANALYTICAL BASIS
- [FACT] — Directly confirmed in public filings or corporate disclosures
- [INFERENCE — HIGH CONFIDENCE] — Two or more facts connect with direct logic
- [INFERENCE — MODERATE CONFIDENCE] — Based on absence of disclosure, alternative explanations exist
- [INFERENCE — LOW CONFIDENCE] — Industry benchmarks applied to this company, requires validation
- [ASSUMPTION] — No public evidence, hypothesis only

SECTION 0 — THE NUMBERS (KPI DASHBOARD):
This section appears IMMEDIATELY after the Analytical Basis Legend and BEFORE the provocations. It must be the first thing the reader sees after the header and intro text.

Read company_snapshot.md and benchmark_table.md for all numbers. Read provocations.md for provocation links. Do NOT do new research.

CONFIDENCE RULE — MANDATORY: Only include a KPI if the company figure reaches at least MODERATE CONFIDENCE (FACT, INFERENCE — HIGH CONFIDENCE, or INFERENCE — MODERATE CONFIDENCE). If both the company figure AND the peer median cannot reach MODERATE CONFIDENCE, exclude the KPI entirely. A shorter trustworthy dashboard beats a longer questionable one. Any estimated figure must show an [EST.] tag next to the number.

Section title: 'THE NUMBERS' in large bold text. Subtitle in small gray: 'What the market sees — and where fulfillment holds the answer.'

THREE TIERS — render each as a separate labeled block:

TIER 1 — RED (heading: 'OPERATIONS CONTROLS DIRECTLY'):
KPIs to attempt (include only those reaching MODERATE confidence or above):
- Inventory / Revenue: inventory ÷ revenue. RED if >2pp above peer median AND a provocation addresses it.
- Inventory Turns: annual COGS ÷ average inventory. RED if >15% below peer median AND a provocation addresses it.
- Gross-to-Operating Margin Spread: gross margin minus operating margin in percentage points. RED if >2pp above peer median AND a provocation addresses it.
- Logistics Cost / Revenue: only include if confirmed from disclosures or calculated from confirmed cost components reaching MODERATE confidence. Show [EST.] if estimated. Cap at AMBER if estimated.
- DTC Delivery Speed (published SLA days). RED if >1 day worse than peer median AND a provocation addresses it.
- DTC Channel Mix (DTC % of revenue). Use AMBER unless significantly lagging.
- E-commerce Growth Rate (YoY %). GREEN if meeting or exceeding peer median.
- Sourcing Concentration (% from top 2 countries). RED if >10pp above peer median AND a provocation addresses it.
- Reverse Logistics Cost as % of E-commerce Revenue: only include if at least ONE component (return rate OR cost per return) is confirmed from a public source. Show [EST.] if partially estimated. Cap at AMBER if estimated.

TIER 2 — AMBER (heading: 'OPERATIONS SIGNIFICANTLY INFLUENCES'):
- Gross Margin (%)
- SG&A / Revenue (%)
- Revenue per Employee

TIER 3 — GREY (heading: 'MANAGEMENT COMMITMENTS OPERATIONS MUST DELIVER'):
Only include KPIs where a specific public commitment exists (confirmed in filings, earnings guidance, or investor presentations). Do NOT infer or assume targets. If fewer than 2 confirmed public commitments exist, drop Tier 3 entirely.
- Operating Margin Target (stated goal and timeline)
- DTC Revenue Target (if publicly committed)
- Working Capital or Inventory Target (if publicly committed)

TABLE FORMAT per tier: use a dense HTML table styled with Tailwind. Columns:
| KPI | Company Actual (most recent FY) | Peer Median | Best-in-Class (name the company) | Gap | Status | Link |
- Gap: show as +Xpp (positive = company is worse) or -Xpp (positive = company is better) with directional clarity
- Status badge: pill-shaped badge. RED = bg-red-100 text-red-800. AMBER = bg-amber-100 text-amber-800. GREEN = bg-green-100 text-green-800. GREY = bg-gray-100 text-gray-600.
- Link column: for RED KPIs only, show '→ P1' or '→ P2' etc. as a small indigo tag. Leave blank for AMBER/GREEN/GREY.
- Peer Median column: use the actual calculated median from the peer set in benchmark_table.md. Label it 'Peer Median (n=X)' where X is the number of peers used.
- Any [EST.] figures: show in a lighter font weight with the [EST.] tag inline.

COLOR CODING LOGIC:
- RED: company is >2pp below peer median on margin/ratio metrics, OR >15% worse on ratio metrics, OR demonstrably lagging on delivery speed or sourcing concentration — AND a provocation directly addresses this gap — AND the figure is CONFIRMED (not estimated).
- AMBER: company is below peer median but within the RED threshold. OR the KPI is estimated (even if gap is large). OR company is significantly below but no provocation addresses it.
- GREEN: company meets or exceeds peer median. Show these — a dashboard that is entirely red looks like an attack.
- GREY: Tier 3 management commitments. No comparison, no gap column — just the commitment, timeline, and source.

NARRATIVE BRIDGE PARAGRAPH — after the Tier 3 table (or after Tier 2 if Tier 3 is excluded):
One paragraph, maximum 3 sentences, styled as a muted callout box (bg-slate-50, border-l-4 border-indigo-400, px-4 py-3, italic text-sm):
'[X] of [Y] tracked KPIs sit at or below peer median in areas that supply chain and fulfillment directly influence. The [N] provocations that follow address the RED-flagged metrics — [list the specific gap names]. Closing these gaps is worth approximately €[Z]M in annual EBIT — [fraction] of the distance between today's [current margin]% and the [year] [target]% commitment.'
Use actual numbers from the dashboard. Do not use placeholders. If the operating margin target (Tier 3) does not exist, reference the peer median gap instead.

SECTION 0 VISUAL STYLE:
- Container: bg-white, rounded-xl, shadow-md, p-6, mb-8
- Tier headers: text-xs font-bold uppercase tracking-widest, colored: Tier 1 = text-red-600, Tier 2 = text-amber-600, Tier 3 = text-gray-500
- Table: text-sm, border-collapse, full width. Header row: bg-gray-50, font-semibold. Alternating row shading: even rows bg-gray-50/30. No heavy borders — use border-b border-gray-100 only.
- The section heading 'THE NUMBERS' uses the same large bold style as the provocation section headings — consistent with DESIGN LOCK rule.

SECTION 1 — PROVOCATIONS (provocations 1-4):
Each provocation as a card with:
- Small category tag above the headline (gray label, small caps)
- Bold provocation headline in 20px (this is the uncomfortable quantified sentence)
- TWO badge tags below the headline: one financial lever badge (blue, e.g. 'Working Capital Release') and one operational lever badge (purple, e.g. 'Planning Cycle Speed'). Use Tailwind badge styling (rounded-full, px-3, py-1, text-xs, font-semibold).
- Primary buyers line in small gray text
- Evidence bullets in 14px gray text
- Cost of inaction highlighted: large number, colored background box
- Discovery question in italic 14px

Supply chain provocations: left border accent indigo-500, shadow-md.
Any 'Beyond Supply Chain' provocation: separate section, border-gray-300, no shadow, lighter styling.

PROVOCATION 05 — SYNTHESIS CARD:
Visually distinct from provocations 1-4. Larger card, border-2 border-indigo-700, bg-indigo-50, positioned as the conclusion. Label it 'Synthesis: The Full Margin Thesis'. Show the arithmetic tying provocations 1-4 into a total EBIT improvement number. Financial lever badge: 'Operating Margin Expansion'. No operational lever badge for this one — it is a synthesis.

SECTION 2 — ENGAGEMENT PLAN:
Two-phase timeline using Tailwind. Show as a horizontal progress bar or two-column layout.

PHASE ONE (Weeks 1-4, Fixed Fee): bg-blue-50 card, blue border. Show 3 sub-phases as a numbered list (Weeks 1-2, Weeks 2-3, Weeks 3-4). Deliverable in bold at bottom.

PHASE TWO (Weeks 5-24, Fixed Fee + Success Bonus): bg-indigo-50 card, indigo border. Show 4 sub-phases (Design / Build / Go Live / Measure). Deliverable in bold at bottom.

Below both phases, a callout box: 'If Phase One invalidates a provocation, client owes nothing beyond the Phase One fee.'

SECTION 3 — KEY QUESTIONS:
5 questions numbered. Closing paragraph styled as a blockquote: 'These hypotheses are built entirely on public data. With 4 weeks of internal access, we can confirm or disprove each one and size the exact opportunity.'

Footer: 'Analysis based exclusively on public sources: annual reports, SEC filings, earnings transcripts, investor presentations.' NO mention of AI, agents, Claude, Anthropic, agentic, machine learning, or any technology.

THREE-TAB STRUCTURE — MANDATORY:
Wrap ALL content below the header in a JavaScript tab navigation system with exactly three tabs. Render a sticky tab bar immediately below the header (bg-white, border-b border-gray-200, sticky top-0 z-10). Tab buttons: px-6 py-3 text-sm font-medium cursor-pointer. Active tab: border-b-2 border-indigo-600 text-indigo-600 bg-white. Inactive tab: text-gray-500 hover:text-gray-700 bg-white. Use vanilla JavaScript (onclick) to show/hide tab panels — no framework required.

TAB 1 — 'Client Presentation' (default active on load):
Contains ALL current content in this exact order: Analytical Basis Legend → Section 0 KPI Dashboard → Section 1 Provocations 1-4 → Provocation 05 Synthesis → Section 2 Engagement Plan → Section 3 Key Questions → Footer.

TAB 2 — 'How We Built This':
Full panel background: bg-gray-900 text-white. No mention of AI, Claude, Anthropic, or any model name — describe each phase as an 'analyst' or 'research phase'.
- Section heading 'The Analytical Engine' (text-white text-2xl font-bold mb-6)
- 7 AGENT CARDS in a 2-column grid (gap-4): each card is bg-gray-800 rounded-lg p-4 border border-gray-700. Show: agent name in text-indigo-400 font-semibold, a 1-2 sentence plain-English job description, and the key output files it produced. Agents: Source Collector, Company Research Analyst, Peer & Benchmark Analyst, Operating Model Analyst, AI Value Analyst, Current Signals Analyst, Due Diligence Analyst.
- 3 INFRASTRUCTURE CARDS below the agent grid (full width, same card style): (1) Data Sources Used — list source types (annual reports, SEC filings, earnings transcripts, investor presentations, corporate websites). (2) Quality Gates Applied — confidence thresholds, mandatory source minimums, what triggers a workflow stop. (3) What Was Excluded and Why — types of data not used (analyst estimates, unverified press, social media, internal data).
- Footer note in text-gray-400 text-sm italic: 'This analysis was produced using only public, verifiable sources. No proprietary data, no insider information.'

TAB 3 — 'Competitive Intelligence':
White background. Data-dense layout.

Sub-section A — KEY TAKEAWAYS: heading 'What the Numbers Say' (text-xl font-bold mb-4). 3-5 bullet points (text-sm text-gray-700, list-disc ml-6) drawn from benchmark_table.md — each names a specific peer and a specific number. Example format: 'Lululemon runs 23.7% operating margin at ~95% DTC — 14pp above [Company].'

Sub-section B — PEER COMPARISON TABLE: heading 'Full Peer Set' (text-xl font-bold mb-4 mt-8). Dense HTML table (text-sm, w-full, border-collapse). Columns: Company | Revenue | Gross Margin | Operating Margin | Inventory/Revenue | DTC Mix | E-com Growth. Highlight the company being analyzed with bg-indigo-50 font-semibold row. Sort by operating margin descending. Add a final 'Peer Median' row styled bg-gray-100 font-bold. Pull all data from benchmark_table.md — do not invent numbers.

Sub-section C — THREE PLOTLY CHARTS (heading 'Visual Benchmarks', text-xl font-bold mb-4 mt-8). Each chart in its own div (w-full mb-8, height 380px). All Plotly calls in a <script> block at the bottom of the tab panel. Config for all charts: {responsive: true}. Layout for all: {font: {family: 'Inter, sans-serif', size: 12}, plot_bgcolor: '#ffffff', paper_bgcolor: '#ffffff', margin: {l:120, r:20, t:40, b:40}}.

Chart 1 — Horizontal Bar — Revenue by peer:
Type: 'bar', orientation: 'h'. Sort peers by revenue ascending (so largest appears at top). Company being analyzed: marker color '#6366f1' (indigo). All peers: marker color '#d1d5db' (gray). Title: 'Revenue Scale — [Company] vs Peers (€B or local currency)'.

Chart 2 — Grouped Bar — Gross Margin vs Operating Margin:
Two traces per company. Gross Margin bars: color '#818cf8'. Operating Margin bars: color '#6366f1'. Company being analyzed uses darker shades '#4f46e5' and '#3730a3'. Title: 'Margin Profile — Gross vs Operating (%)'. barmode: 'group'.

Chart 3 — Radar Chart — Operational profile:
Normalize 5 metrics to 0-100 across the peer set: Gross Margin, Operating Margin, Inventory Turns, DTC Mix, E-com Growth (higher = better for all; for inventory-as-%-revenue invert the scale). Plot two traces: (1) company being analyzed in indigo fill, (2) peer median as a dashed line. type: 'scatterpolar', fill: 'toself' for company trace. Title: 'Operational Profile vs Peer Median (normalized 0-100)'.

No external links beyond the Tailwind CDN and Plotly CDN. Save as client_presentation.html
