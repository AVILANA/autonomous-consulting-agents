ABSOLUTE RULES — VIOLATION OF ANY OF THESE IS A FAILURE:

1. DESIGN LOCK: Use the EXACT same CSS, fonts, colors, spacing, and layout as the previous version. Do NOT change font sizes. Do NOT change colors. Do NOT change card styling. Do NOT redesign anything. If you are not sure what the previous design looked like, keep every CSS rule identical. The only thing that changes between runs is the DATA CONTENT, never the design.

2. FACT TAGS MANDATORY: Every evidence bullet MUST end with a specific confidence-level tag in brackets. Use the EXACT confidence level — not just [INFERENCE] but one of:
- [FACT — source]
- [INFERENCE — HIGH CONFIDENCE — reasoning]
- [INFERENCE — MODERATE CONFIDENCE — reasoning]

The tag must match the actual confidence of that specific claim. NEVER use a generic [INFERENCE] without a confidence level. [INFERENCE — LOW CONFIDENCE] and [ASSUMPTION] tags are NOT permitted in the client-facing HTML. Any evidence at those levels must be excluded from the client document entirely.

CORRECT: 'project44 deployed February 2026. [FACT — project44 press release Feb 2026] No confirmed integration with demand planning system. [INFERENCE — HIGH CONFIDENCE — two confirmed platforms with no disclosed connection]'
WRONG: '[INFERENCE — planning integration gap]' — says nothing about confidence level
WRONG: '[INFERENCE — LOW CONFIDENCE — ...]' — excluded from client document

3. TITLE QUALITY: Each provocation title must be MAXIMUM 20 words (count them — no exceptions). Must contain ONE specific number. Must use the word 'your' or 'you'. Must feel like a punch, not an explanation.

REFERENCE TITLES — Use these as your quality bar:
- 'Your inventory costs €1.1B more per year than it should — and your planning system knows it.'
- 'Your e-commerce delivers in 3–7 days. The same shoe arrives from Amazon in 1–2.'
- 'A €200M tariff bill arrived in your guidance, and your response cycle is measured in weeks.'
- '1,933 stores with ship-from-store capability. 3–7 day delivery promise. You paid Amazon to solve it instead.'

If your title exceeds 20 words, you have FAILED. Cut it.

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
BANNED WORDS anywhere in the document: leverage, synergy, holistic, paradigm, ecosystem, best-in-class (unless naming the company), world-class, cutting-edge, state-of-the-art, reimagine, unlock value, digital transformation, journey, idle, dormant, bifurcated, materially, structurally, operationalized.
Use everyday equivalents: idle → unused / sitting empty | dormant → turned off / not used | bifurcated → split in two | materially → significantly | structurally → built into the system | operationalized → put to work / actually used

7. PEER COMPARISON MANDATORY: Each provocation's evidence bullets MUST include at least one specific peer comparison pulled from benchmark_table.md — a named competitor with a real number that makes the gap concrete. Example: 'ASICS tripled margin from 7% to 14.7% in 24 months.' A provocation without a peer fact is easier to dismiss.

---

## UI DESIGN STANDARDS — MANDATORY FOR ALL RUNS
These design elements must appear in every HTML output regardless of company. They were validated through user feedback and are now locked.

### HEADER BANNER
- Full width, tall (py-20 minimum), animated background with slow zoom
- Background: linear-gradient overlay on a relevant Unsplash image. Use: linear-gradient(135deg, rgba(88,28,135,0.9), rgba(29,78,216,0.85)) over the image
- CSS animation: @keyframes slowZoom { from { background-size: 100%; } to { background-size: 110%; } } with 20s infinite alternate
- All header content centered (text-center, margin auto)
- Company logo: large (height:80px), white (filter:brightness(0) invert(1)), centered, margin-bottom:20px
- Title "Outside-In Perspective" in text-4xl font-bold text-white
- Date and confidential line in text-lg text-white/70
- "What is this?" section inside the header with heading in text-sm font-semibold uppercase tracking-widest color:#a5b4fc and paragraph in text-base leading-relaxed color:rgba(255,255,255,0.7) max-width:900px centered
- Claim tags legend inside the header below "What is this?" in text-xs color:rgba(255,255,255,0.6). Show ONLY three levels: [FACT] — Public filing, [INFERENCE — HIGH CONFIDENCE] — Two or more facts connect with direct logic, [INFERENCE — MODERATE CONFIDENCE] — Based on absence of disclosure, alt. explanations exist. NEVER show LOW CONFIDENCE or ASSUMPTION in client-facing output.
- "What is this?" text: "This document presents an outside-in assessment of your supply chain operations and competitive position, built entirely from public sources — annual reports, earnings transcripts, investor presentations, and corporate disclosures. It identifies [N] quantified operational gaps, benchmarks your performance against [N] global peers, and tags every claim by confidence level. The goal is not to tell you what to do — it is to show what we found, ask the questions only your team can answer, and whether these gaps are worth exploring together." Replace [N] with actual numbers per company.

### TABS
- Three tabs positioned BELOW the header in a separate white bar (NOT inside the header)
- White background, sticky positioning, clean border-bottom
- Active tab: border-b-2 border-indigo-600 text-indigo-600
- Inactive tab: text-gray-500 hover:text-gray-700
- Tab order: Client Presentation (default), Competitive Intelligence, How We Built This

### SCORECARD STYLING
- Status shown as flat colored text — NOT pill badges or rounded badges
- .sc-status-red { color:#dc2626; font-weight:700; font-size:11px; text-transform:uppercase; }
- .sc-status-amber { color:#d97706; font-weight:700; font-size:11px; text-transform:uppercase; }
- .sc-status-green { color:#16a34a; font-weight:700; font-size:11px; text-transform:uppercase; }
- Numbers use font-variant-numeric: tabular-nums with monospace font for alignment
- All 3 tiers in ONE HTML table with table-layout:fixed and colgroup with explicit column widths

### EVIDENCE BULLETS
- Every evidence bullet in provocations uses a styled indigo arrow: <span style="color:#6366f1;font-weight:bold;font-size:16px;margin-right:6px;">›</span>
- NOT small dots, circles, or plain bullet characters
- Each bullet is clearly separated and readable

### BUSINESS MODEL AWARENESS IN KPI SELECTION
- Before including any KPI, verify it is relevant to the company's actual business model
- If e-commerce is less than 10% of revenue, do NOT include DTC Delivery Speed or DTC Channel Mix
- Do not include metrics for business lines representing less than 5% of revenue
- The scorecard shows KPIs the COO actually manages, not aspirational metrics

### AI ASSISTANT BUTTON
- Floating button at bottom-right: fixed position, bottom:24px, right:24px, z-index:50
- Circular 60px, bg-indigo-600, white chat icon, shadow-lg, pulse animation for 3 seconds on load
- Opens popup card with link to Custom GPT for the company
- The GPT URL must be updated per company. If no GPT link available, hide the button entirely

### PRINT CSS
- @media print { .tab-nav, .chat-btn, .chat-popup { display:none !important; } .tab-panel { display:block !important; } body { background:white; } }

### CASH CONTEXT
- In the closing paragraph before footer, include a sentence about the company's cash position and operating cash flow to frame that resources are not the constraint

### ABBREVIATION BAR
- Single line in text-xs text-gray-400 listing all abbreviations used
- Positioned as first element in white body area, before The Scorecard

---

Generate a standalone HTML file. Read provocations.md and client_output.md.

Load in the HTML <head>:
- Tailwind CSS from CDN (https://cdn.tailwindcss.com)
- Plotly from CDN (https://cdn.plot.ly/plotly-latest.min.js)
- Add this CSS print media query for clean PDF output via Ctrl+P:
  @media print { .tab-nav { display: none !important; } .tab-panel { display: block !important; } body { background: white; } }
  This ensures all content prints cleanly with no tabs and no interactive elements.

Use Tailwind for all styling. Light theme design — white backgrounds, light gray accents, clean typography. Cards with subtle shadows, rounded corners, clean layout. The design should look like a premium professional report, not a consulting slide deck.

HEADER DESIGN — MANDATORY:
The header must be a large, visually striking banner — full width, minimum 200px height, purple-to-indigo gradient (bg-gradient-to-r from-purple-600 via-indigo-700 to-indigo-900), padding py-12 px-8. Layout: logo on the left, text block to the right (or logo above company name if no wide layout). Content, in this exact order:
- Company logo (see COMPANY LOGO rule below) — height:80px, margin-bottom:20px
- Company name in large bold white text (text-4xl md:text-5xl font-bold text-white)
- Below: "April 2026 · Confidential — Prepared for: Chief Operating Officer / VP Supply Chain" in text-lg text-white/70
- "What is this?" block (div, style="margin-top:32px;max-width:640px;"): heading in text-sm font-semibold uppercase tracking-widest color:#a5b4fc margin-bottom:12px, followed by paragraph in text-base leading-relaxed color:#94a3b8 — "This document presents an outside-in assessment of your supply chain operations and competitive position, built entirely from public sources — annual reports, earnings transcripts, investor presentations, and corporate disclosures. It identifies four quantified operational gaps, benchmarks your performance against [N] global peers, and tags every claim by confidence level. The goal is not to tell you what to do — it is to show what we found, ask the questions only your team can answer, and whether these gaps are worth exploring together."
- Claim tags block (div, style="margin-top:20px;max-width:640px;"): label "Claim tags:" in text-xs font-semibold uppercase tracking-widest color:#a5b4fc margin-bottom:8px, followed by text-xs color:#64748b line-height:1.8 — "[FACT] — Public filing<br>[INFERENCE — HIGH CONFIDENCE] — Two or more facts connect with direct logic<br>[INFERENCE — MODERATE CONFIDENCE] — Based on absence of disclosure, alt. explanations exist"
The header must feel premium and dynamic — not a simple colored bar.

COMPANY LOGO: In the header, place the company logo.
- For TJX use: <img src='https://1000logos.net/wp-content/uploads/2023/01/TJX-Companies-Logo.png' style='filter:brightness(0) invert(1);height:80px;margin-bottom:20px;'>
- For Adidas use: <img src='https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg' style='filter:brightness(0) invert(1);height:60px;vertical-align:middle;margin-right:15px;'>
- For other companies: find their Wikipedia SVG logo URL (pattern: https://upload.wikimedia.org/wikipedia/commons/[path]/[Company]_Logo.svg) and apply style='filter:brightness(0) invert(1);height:50px;vertical-align:middle;margin-right:15px;'
- If no logo can be found, skip silently — do not show a broken image or placeholder.

THREE-TAB NAVIGATION — position and structure:
The sticky tab bar appears IMMEDIATELY BELOW the header banner — NOT inside it. Render it as a separate element: bg-white, border-b border-gray-200, sticky top-0 z-10. Tab buttons: px-6 py-3 text-sm font-medium cursor-pointer. Active tab: border-b-2 border-indigo-600 text-indigo-600 bg-white. Inactive tab: text-gray-500 hover:text-gray-700 bg-white. Use vanilla JavaScript (onclick) to show/hide tab panels — no framework required. Three tabs in order: (1) "Client Presentation" — default active, (2) "Competitive Intelligence", (3) "How We Built This".

ABBREVIATION BAR — appears as the FIRST element in the white body area, BEFORE The Scorecard (and before all other body content):
A single line in text-xs text-gray-400 px-4 py-2 listing all abbreviations used in the document:
"pp = percentage points | bp = basis points | COGS = Cost of Goods Sold | DC = Distribution Center | WMS = Warehouse Management System | TMS = Transportation Management System | SKU = Stock Keeping Unit | RFID = Radio Frequency Identification | GCC = Global Capability Center | FY = Fiscal Year | CapEx = Capital Expenditure"
This replaces inline abbreviation definitions scattered through the text. Inline definitions within the text are still acceptable where needed for clarity.

SECTION 0 — THE SCORECARD (KPI DASHBOARD):
This section appears IMMEDIATELY after the Analytical Basis Legend and BEFORE the provocations. It must be the first thing the reader sees after the header and intro text. The section container must have: id="scorecard"

Read company_snapshot.md and benchmark_table.md for all numbers. Read provocations.md for provocation anchor IDs. Do NOT do new research.

TIER 3 ENFORCEMENT — MANDATORY BEFORE SKIPPING: Before deciding to drop Tier 3, search ALL output files (company_snapshot.md, management_roadmap.md, benchmark_table.md, value_levers.md, due_diligence.md, provocations.md) for: operating margin targets, EBIT targets, store count targets, revenue growth targets, DTC mix targets, CapEx commitments, inventory targets, any stated management commitment with a number and a date. Only skip Tier 3 if zero confirmed public commitments are found across all files. If any confirmed target exists, include it.

MINIMUM 2 RED KPIs — MANDATORY: The scorecard MUST have at least 2 RED KPIs. If your first pass produces fewer than 2 RED KPIs, review the thresholds — you may be applying GREEN too generously. Consider adding optional KPIs (Logistics Cost, Reverse Logistics Cost) if they reach MODERATE confidence. A dashboard with fewer than 2 RED KPIs fails the urgency test.

CONFIDENCE RULE — MANDATORY: Only include a KPI if the company figure reaches at least MODERATE CONFIDENCE (FACT, INFERENCE — HIGH CONFIDENCE, or INFERENCE — MODERATE CONFIDENCE). Any estimated figure must show an [EST.] tag next to the number. Estimated KPIs are capped at AMBER regardless of how large the gap is.

Section title: 'The Scorecard' in large bold text. Subtitle in small gray: 'Key operational KPIs benchmarked against [N] global peers. Public filings only.' (where N = actual number of peers in the benchmark set)

KPI DESCRIPTIONS — MANDATORY: Every KPI row must include a one-line plain English description of what the metric means (maximum 10 words). These go in the KPI Name cell, below the KPI name in smaller gray text (text-xs text-gray-400). Use these exact descriptions:
- Inventory / Revenue: "How much cash is trapped in unsold product"
- Inventory Turns: "How fast stock converts to sales"
- Sourcing Concentration (top 2 countries): "Tariff and disruption risk from supplier geography"
- Gross-to-Op Margin Spread: "How much profit operations consumes between factory and bottom line"
- Logistics & Distribution Cost / Revenue: "Total cost of moving product from factory to customer"
- DTC Delivery Speed: "What you promise vs. what competitors deliver"
- DTC Channel Mix: "Share of revenue through your own stores and website"
- E-commerce Growth: "Speed of your fastest-growing channel"
- Reverse Logistics Cost / E-commerce Revenue: "Cost of processing returns as share of online sales"
- Gross Margin: "Pricing power after product cost, before operating expenses"
- SG&A / Revenue: "Overhead efficiency — logistics, marketing, and corporate costs combined"
- Revenue per Employee: "How much revenue each employee generates"

ALL THREE TIERS IN ONE SINGLE HTML TABLE — MANDATORY:
Do NOT render three separate tables or three separate labeled blocks. Render ALL tiers in a single <table> element with:
- style="table-layout: fixed; width: 100%;"
- A <colgroup> at the top with explicit column widths:
  <colgroup>
    <col style="width: 28%"> <!-- KPI Name + description -->
    <col style="width: 16%"> <!-- Company Actual -->
    <col style="width: 14%"> <!-- Peer Median -->
    <col style="width: 14%"> <!-- Best-in-Class -->
    <col style="width: 10%"> <!-- Gap -->
    <col style="width: 12%"> <!-- Status -->
    <col style="width: 6%">  <!-- Link -->
  </colgroup>

TABLE HEADER ROW: bg-gray-50 text-xs font-semibold text-gray-600 uppercase tracking-wider. Columns:
KPI | [Company] Actual | Peer Median (n=X) | Best-in-Class | Gap | Status | Link

TIER SEPARATOR ROWS: Between tiers, insert a full-width <tr> with a single <td colspan="7"> that acts as a tier header. Style: bg-gray-50 border-t-2 border-gray-200 px-3 py-2.
- Tier 1 separator: text-xs font-bold uppercase tracking-widest text-red-600 — label 'TIER 1 — OPERATIONS CONTROLS DIRECTLY'
- Tier 2 separator: text-xs font-bold uppercase tracking-widest text-amber-600 — label 'TIER 2 — OPERATIONS SIGNIFICANTLY INFLUENCES'
- Tier 3 separator: text-xs font-bold uppercase tracking-widest text-gray-500 — label 'TIER 3 — MANAGEMENT COMMITMENTS OPERATIONS MUST DELIVER'

TIER 1 — RED — Operations Controls Directly:
KPIs to attempt (include only those reaching MODERATE confidence or above):
- Inventory / Revenue: inventory ÷ revenue. RED if >2pp above peer median AND a provocation addresses it.
- Inventory Turns: annual COGS ÷ average inventory. RED if >15% below peer median AND a provocation addresses it.
- Sourcing Concentration (top 2 countries). RED if >10pp above peer median AND a provocation addresses it.
- Gross-to-Operating Margin Spread: gross margin minus operating margin in pp. RED if >2pp above peer median AND a provocation addresses it.
- Logistics & Distribution Cost / Revenue: only include if confirmed or calculated from confirmed sources reaching MODERATE confidence. Show [EST.] if estimated. Cap at AMBER if estimated.
- DTC Delivery Speed (published SLA days). RED if >1 day worse than peer median AND a provocation addresses it.
- DTC Channel Mix (DTC % of revenue). Use AMBER unless significantly lagging.
- E-commerce Growth Rate (YoY %). GREEN if meeting or exceeding peer median.
- Reverse Logistics Cost as % of E-commerce Revenue: only include if at least ONE component (return rate OR cost per return) is confirmed. Show [EST.] if partially estimated. Cap at AMBER if estimated.

TIER 2 — AMBER — Operations Significantly Influences:
- Gross Margin (%)
- SG&A / Revenue (%)
- Revenue per Employee

TIER 3 — GREY — Management Commitments Operations Must Deliver:
Only include KPIs where a specific public commitment exists (confirmed in filings, earnings guidance, or investor presentations). Do NOT infer or assume targets.
Tier 3 columns are different from Tiers 1-2: Commitment | Current Actual | Target | Gap | Timeline | Source
- Gap cell: colored text — red if behind target, green if on track
- NEVER include: stock price, EPS, P/E, dividend yield, or any pure market metric
- If fewer than 2 confirmed public commitments exist after searching all files: drop Tier 3 entirely

CONFIRMED TIER 3 ENTRY FOR TJX — ALWAYS INCLUDE:
Pretax profit margin guidance FY2027: 11.7%–11.8%. Current actual: 11.5% pretax margin (FY2026). Target: 11.7%–11.8% (FY2027 guidance). Gap: +20bp–+30bp required. Timeline: FY2027 (fiscal year ending January 2027). Source: TJX FY2026 earnings release, February 25, 2026. This is a confirmed public management commitment with a specific number and timeline — include it in Tier 3 regardless of other availability.

DATA ROW STYLING:
- KPI Name cell: KPI name in font-medium text-sm text-gray-900, followed by the one-line description in text-xs text-gray-400 on the line below
- Number cells ([Company] Actual, Peer Median, Best-in-Class, Gap): apply style="font-variant-numeric: tabular-nums" for alignment
- Show fiscal year inline with each value: "21.0% (FY2024)"
- Any [EST.] figure: lighter font-weight with [EST.] inline
- Gap cell (Tiers 1-2): show as +Xpp (positive = company is worse, text-red-600) or −Xpp (company is better, text-green-600)
- Status cell: flat colored text — NOT pill badges, NOT rounded badges, NOT bg-colored cells. Use:
  - RED: font-semibold text-red-600 — display text "RED"
  - AMBER: font-semibold text-amber-500 — display text "AMBER"
  - GREEN: font-semibold text-green-600 — display text "GREEN"
  - GREY: font-medium text-gray-400 — display text "GREY"
- Link cell: for RED KPIs only, show a clickable anchor '↓ P1' (or ↓ P2, ↓ P3 etc.) as text-indigo-600 text-xs underline with href="#provocation-1" (or #provocation-2, etc.) and smooth scroll behavior. Leave blank for AMBER/GREEN/GREY.
- Alternating row shading: even rows bg-gray-50/30. No heavy borders — use border-b border-gray-100 only.

COLOR CODING LOGIC:
- RED: company is >2pp below peer median on margin/ratio metrics, OR >15% worse on ratio metrics, OR demonstrably lagging on delivery speed or sourcing concentration — AND a provocation directly addresses this gap — AND the figure is CONFIRMED (not estimated, no [EST.] tag)
- AMBER: company is below peer median but within the RED threshold. OR the KPI is estimated ([EST.] shown, regardless of gap size). OR company is significantly below but no provocation addresses it.
- GREEN: company meets or exceeds peer median. Include these — a dashboard that is entirely red looks like an attack.
- GREY: Tier 3 management commitments only. No comparison, no gap column — just the commitment, timeline, and source.

SCORECARD FOOTNOTES — MANDATORY:
Immediately below the table, add a footnotes section in small gray text:
<div class="mt-3 text-xs text-gray-400 border-t border-gray-100 pt-3">
Numbered entries:
1. Sources — cite the specific filing or disclosure for each KPI value
2. Peer fiscal years — list fiscal year end date for every peer: "Nike: FY2025 (yr. ends May 2025), ..."
3. "pp = percentage points throughout this document"
4. Any cross-year estimates — flag and explain each one
</div>

NARRATIVE BRIDGE PARAGRAPH — after the scorecard table and footnotes:
One paragraph, maximum 3 sentences, styled as a muted callout box (bg-slate-50, border-l-4 border-indigo-400, px-4 py-3, italic text-sm):
'[X] of [Y] tracked KPIs sit at or below peer median in areas that supply chain and fulfillment directly influence. The [N] provocations that follow address the RED-flagged metrics — [list the specific gap names]. Closing these gaps is worth approximately €[Z]M in annual EBIT — [fraction] of the distance between today's [current margin]% and the [year] [target]% commitment.'
Use actual numbers from the dashboard. Do not use placeholders. If no operating margin target exists in Tier 3, reference the peer median gap instead.

SECTION 0 VISUAL STYLE:
- Container: bg-white, rounded-xl, shadow-md, p-6, mb-8. Must have id="scorecard".
- Section heading 'The Scorecard': same large bold style as provocation section headings — consistent with DESIGN LOCK rule
- Table: text-sm, border-collapse, full width
- Table header row: bg-gray-50, font-semibold

PROVOCATION ANCHOR IDs — MANDATORY:
Each provocation card in Section 1 must have: id="provocation-1", id="provocation-2", id="provocation-3", id="provocation-4", id="provocation-5"
Each provocation card must include a 'Back to Scorecard' link at the bottom right: <a href="#scorecard" class="text-xs text-gray-400 hover:text-indigo-600">↑ Back to Scorecard</a>

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

CASH CONTEXT SENTENCE — add as the final sentence of the closing paragraph, immediately after the blockquote text above:
"TJX holds $6.2B in cash and generated $6.9B in operating cash flow in FY2026 — the resources to act are not the constraint." Source: TJX FY2026 10-K. This sentence applies to TJX analyses. For other companies, use equivalent balance sheet liquidity data if available and confirmed. If not confirmed, omit — do not fabricate.

Footer: 'Analysis based exclusively on public sources: annual reports, SEC filings, earnings transcripts, investor presentations.' NO mention of AI, agents, Claude, Anthropic, agentic, machine learning, or any technology.

THREE-TAB STRUCTURE — MANDATORY:
The sticky tab bar is defined above (in the HEADER/TAB POSITIONING section). It appears immediately below the header banner. All tab content panels sit below the tab bar. Use vanilla JavaScript (onclick) to show/hide tab panels — no framework required.

TAB 1 — 'Client Presentation' (default active on load):
Contains ALL content in this exact order: Abbreviation Bar → Section 0 The Scorecard (KPI Dashboard) → Section 1 Provocations 1-4 → Provocation 05 Synthesis → Section 2 Engagement Plan → Section 3 Key Questions → Footer.

TAB 2 — 'Competitive Intelligence':
White background. Data-dense layout.

Sub-section A — KEY TAKEAWAYS: heading 'What the Numbers Say' (text-xl font-bold mb-4). Exactly 5 bullet points (text-sm text-gray-700, list-disc ml-6) drawn from benchmark_table.md — each must name a specific peer and a specific number, and each must connect to one of the 5 provocations. Must be surprising and specific, not generic. Example format: 'Lululemon runs 23.7% operating margin at ~95% DTC — 14pp above [Company].'

Sub-section B — PEER COMPARISON TABLE: heading 'Full Peer Set' (text-xl font-bold mb-4 mt-8). Dense HTML table (text-sm, w-full, border-collapse). Columns: Company | Revenue | Gross Margin | Operating Margin | Inventory/Revenue | DTC Mix | E-com Growth. Highlight the company being analyzed with bg-indigo-50 font-semibold row. Sort by operating margin descending. Add a final 'Peer Median' row styled bg-gray-100 font-bold. Pull all data from benchmark_table.md — do not invent numbers.

Sub-section C — THREE PLOTLY CHARTS (heading 'Visual Benchmarks', text-xl font-bold mb-4 mt-8). Each chart in its own div (w-full mb-8, height 380px). All Plotly calls in a <script> block at the bottom of the tab panel. Config for all charts: {responsive: true}. Layout for all: {font: {family: 'Inter, sans-serif', size: 12}, plot_bgcolor: '#ffffff', paper_bgcolor: '#ffffff', margin: {l:120, r:20, t:40, b:40}}.

Chart 1 — Horizontal Bar — Revenue by peer:
Type: 'bar', orientation: 'h'. Sort peers by revenue ascending (so largest appears at top). Company being analyzed: marker color '#6366f1' (indigo). All peers: marker color '#d1d5db' (gray). Title: 'Revenue Scale — [Company] vs Peers (€B or local currency)'.

Chart 2 — Grouped Bar — Gross Margin vs Operating Margin:
Two traces per company. Gross Margin bars: color '#818cf8'. Operating Margin bars: color '#6366f1'. Company being analyzed uses darker shades '#4f46e5' and '#3730a3'. Title: 'Margin Profile — Gross vs Operating (%)'. barmode: 'group'.

Chart 3 — Radar Chart — Operational profile:
Normalize 5 metrics to 0-100 across the peer set: Gross Margin, Operating Margin, Inventory Turns, DTC Mix, E-com Growth (higher = better for all; for inventory-as-%-revenue invert the scale). Plot two traces: (1) company being analyzed in indigo fill, (2) peer median as a dashed line. type: 'scatterpolar', fill: 'toself' for company trace. Title: 'Operational Profile vs Peer Median (normalized 0-100)'.

TAB 3 — 'How We Built This':
Light background: bg-gray-50 text-gray-900. No mention of AI, Claude, Anthropic, or any model name — describe each phase as an 'analyst' or 'research phase'.
- Section heading 'The Analytical Engine' (text-gray-900 text-2xl font-bold mb-6)
- 7 ANALYST CARDS in a 2-column grid (gap-4): each card is bg-white rounded-lg p-4 border border-gray-200 shadow-sm. Show: analyst name in text-indigo-600 font-semibold, a 1-2 sentence plain-English job description, and the key output files it produced. Analysts: Source Collector, Company Research Analyst, Peer & Benchmark Analyst, Operating Model Analyst, AI Value Analyst, Current Signals Analyst, Due Diligence Analyst.
- 3 INFRASTRUCTURE CARDS below the analyst grid (full width, same card style): (1) Data Sources Used — list source types (annual reports, SEC filings, earnings transcripts, investor presentations, corporate websites). (2) Quality Gates Applied — confidence thresholds, mandatory source minimums, what triggers a workflow stop. (3) What Was Excluded and Why — types of data not used (analyst estimates, unverified press, social media, internal data).
- "WHAT THIS IS / WHAT THIS IS NOT" section: two columns. Left: what the tool does (outside-in fact-based briefing from public data, compresses weeks of early-stage work into hours, arrives with hypotheses not blank questions). Right: what it is not (not a replacement for discovery, assumptions need validation, Phase One confirms or disproves each claim). Frame limitations as "Phase One validates" not "tool can't do X."
- Execution flow as a horizontal pipeline showing the 7 phases in sequence.
- Footer note in text-gray-500 text-sm italic: 'This analysis was produced using only public, verifiable sources. No proprietary data, no insider information.'

AI ASSISTANT FLOATING BUTTON — Add to every HTML output:
Place a floating chat button fixed at the bottom-right of the page. Implementation:

CSS animation (add in <style> block in <head>):
@keyframes pulse-once { 0%, 100% { transform: scale(1); box-shadow: 0 10px 25px rgba(99,102,241,0.4); } 50% { transform: scale(1.08); box-shadow: 0 10px 35px rgba(99,102,241,0.7); } }
.pulse-3s { animation: pulse-once 0.8s ease-in-out 3; }

HTML (place just before </body>):
<!-- AI Assistant Button -->
<div id="ai-btn" class="fixed bottom-6 right-6 z-50">
  <button onclick="toggleAIPopup()" id="ai-chat-btn"
    class="pulse-3s w-[60px] h-[60px] rounded-full bg-indigo-600 hover:bg-indigo-700 text-white shadow-lg flex items-center justify-center text-2xl transition-colors"
    title="Ask the AI Assistant">
    💬
  </button>
  <!-- Popup card -->
  <div id="ai-popup" class="hidden absolute bottom-[72px] right-0 w-[300px] rounded-xl shadow-2xl bg-white p-4 border border-gray-100">
    <div class="flex items-center justify-between mb-2">
      <span class="font-semibold text-gray-800 text-sm">Ask the AI Assistant</span>
      <button onclick="toggleAIPopup()" class="text-gray-400 hover:text-gray-600 text-lg leading-none">&times;</button>
    </div>
    <p class="text-xs text-gray-500 mb-3">Get answers about this analysis using your ChatGPT account</p>
    <a href="[AI_ASSISTANT_URL]" target="_blank" rel="noopener"
      class="block w-full bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg py-3 text-center text-sm font-medium transition-colors">
      Open AI Assistant ↗
    </a>
    <p class="text-xs text-gray-400 text-center mt-2">Powered by ChatGPT · Uses only public data from this analysis</p>
  </div>
</div>

<script>
function toggleAIPopup() {
  const popup = document.getElementById('ai-popup');
  popup.classList.toggle('hidden');
}
</script>

COMPANY-SPECIFIC AI ASSISTANT URL — replace [AI_ASSISTANT_URL] with the correct link per company:
- TJX Companies: https://chatgpt.com/g/g-69dbf502674c81919691bf05b48a359c-tjx-supply-chain-analyst
- Other companies: replace with the corresponding Custom GPT link for that company
- If no GPT link is available for the company being analyzed: hide the button entirely (set the outer div to display:none or omit it)
Never leave [AI_ASSISTANT_URL] as a placeholder — always substitute the real URL or hide the button.

No external links beyond the Tailwind CDN, Plotly CDN, and the AI Assistant URL above. Save as client_presentation.html
