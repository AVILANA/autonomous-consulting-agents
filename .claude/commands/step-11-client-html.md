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

4. DATA RECENCY: Do NOT lead with 2022 data. The 2022 overstock is CONTEXT, not the provocation. The provocation is about TODAY and TOMORROW. Lead with FY2025 numbers. Reference 2022 only as supporting evidence of what happens when planning fails.

5. NO SELF-IMPROVEMENT: Do NOT add features, sections, or styling that were not explicitly requested. Do NOT reorganize sections. Do NOT change the order of elements. Produce exactly what is asked, nothing more.

---

Generate a standalone HTML file. Read provocations.md and client_output.md.

Use Tailwind CSS from CDN (https://cdn.tailwindcss.com) for all styling. Purple-to-indigo gradient theme matching modern Accenture internal portals. Cards with subtle shadows, rounded corners, badges, clean typography. The design should look like a premium SaaS product landing page, not a consulting document.

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

No external links beyond the Tailwind CDN. Save as client_presentation.html
