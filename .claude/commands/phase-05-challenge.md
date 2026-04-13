# Phase 5: CHALLENGE — Due Diligence + Provocations
DO NOT use web search. Read ALL files in the output folder. Read memory.md.

## DATA FRESHNESS RULE — MANDATORY
For every KPI and every data point used in any output:

1. Always use the most recent available figure. If FY2025 data exists for a metric (even from a press release or earnings transcript), use FY2025. Only fall back to FY2024 if the specific metric was not disclosed in any FY2025 source.
2. Every number must show its fiscal year in parentheses. Not just "21.0%" but "21.0% (FY2024)" or "€24.8B (FY2025)". The year is mandatory. No exceptions.
3. If a KPI uses an older fiscal year than the most recent results, add a small note explaining why: "(FY2024 — FY2025 breakdown not yet published)". This tells the reader you looked for newer data and it wasn't available, not that you were lazy.
4. Never mix fiscal years within a single calculation without flagging it. If you must cross years, state it explicitly as a cross-year estimate.
5. A provocation based on old data that the client has already fixed is worse than no provocation. Before finalising each provocation, check: is there a more recent number in any output file? If yes, use it. If the most recent data shows the gap has closed, either update the provocation or replace it.

## Execute these 4 jobs IN ORDER:

### Job 1: Conditional Routing
Read company_snapshot.md for CONDITION flags. Read benchmark_table.md for STANDOUT PEER flags. Read body_brain_diagnosis.md for body vs brain results.
Document routing decisions:
- If FINANCIAL DISTRESS: provocations must weight cost reduction
- If HIGH GROWTH: provocations must weight scalability
- If STANDOUT PEER found: make that peer central to at least 2 provocations
- If body is primary constraint in 2+ areas: flag network optimization as Phase Two priority
Save as: routing_decisions.md

### Job 2: Due Diligence
Challenge the entire thesis. 5 counterarguments with evidence. Validation tests. Confidence assessment (Low/Medium/High).
Save as: due_diligence.md

### Job 3A: Company Supply Chain Model Identification — MANDATORY BEFORE ANY PROVOCATION
Before writing a single title, write this at the top of raw_provocations.md:
(1) What makes this company's supply chain unique? (2) What is the core operational differentiator? (3) What are the 3 most critical supply chain decisions this company makes every day? (4) What supply chain processes handle the most money?
RULE: Every provocation MUST connect to at least one of items 2, 3, or 4. If it does not, it is WRONG and must be replaced.

### Job 3B: Write Raw Provocations (creative mode)
Read routing_decisions.md. Write 5 provocations as if you were a senior partner who just spent 48 hours reading everything about this company and now needs to write 5 sentences that will make the COO lose sleep tonight.

Only 3 rules:
1. Each title is one short sentence with one number that hurts
2. Focus on supply chain operations
3. Use the most recent data available

Write freely. Do not think about lever tags, buyer personas, word counts, or formatting. Just write the most uncomfortable truths you found.

PROVOCATION FRESHNESS RULE: A provocation must be about a CURRENT or FUTURE problem, not a past one. The 2022 Adidas overstock crisis is HISTORY — do not build a provocation around it. Use it only as a one-line evidence bullet that shows what happens when the problem is ignored.

BAD: 'The same structural lag that built the 2022 overstock crisis is still in place.' — This tells the client you are looking backward. They already lived through 2022. They know.

GOOD: 'Your €5B inventory depends on a demand plan that refreshes every 3 weeks — and the Samba cycle is peaking now.' — This is about TODAY and what happens NEXT.

If the company has already deployed a tool (like o9 for demand planning), do NOT provoke about not having the tool. Provoke about the GAP in how the tool is connected or used. The question is never 'you need this tool' — it is 'the tool you already bought is not doing what it could because X is missing.'

SIMPLE LANGUAGE RULE — MANDATORY: Write for a 16-year-old who understands business. No complex vocabulary. No words like 'dormant', 'bifurcated', 'materially', 'structurally', 'operationalized'. Use the simplest word that works.

BAD: 'Its AI scenario planning is dormant while air freight costs 4x ocean'
GOOD: 'You have real-time tracking but nobody uses it to avoid €50M in emergency air freight'

BAD: 'The structural lag that built the overstock crisis remains operationally embedded'
GOOD: 'Your planning team still takes 3 weeks to react when a product goes viral'

If a sentence needs a second read to understand, rewrite it. A COO reads 200 emails a day. Your sentence gets 3 seconds.

BANNED WORDS LIST — never use these in titles: idle, dormant, bifurcated, materially, structurally, operationalized, leveraged, synergy, paradigm, holistic, ecosystem, optimize, utilize. Use the everyday equivalent instead.

idle → unused / sitting empty
dormant → turned off / not used
bifurcated → split in two
materially → significantly
structurally → built into the system
operationalized → put to work / actually used

Example fix:
BAD: 'Your 1,933 stores sit idle while customers wait 3-7 days'
GOOD: 'Your 1,933 stores could deliver in hours. Instead, customers wait 3-7 days.'

APPROVED EXAMPLES — use these as your quality benchmark. Your titles must reach this standard:
- 'Every shipment is tracked in real time. Your planning team may still be working with data that is weeks old — and if so, the gap could cost €50M a year in avoidable air freight.'
- 'Your warehouse packs an order in 2 hours. Customers wait 3–7 days for delivery. Amazon delivers in 1–2.'
- '€200M in tariffs hit your guidance. The next bill arrives July 24 — is anyone modelling it?'
- 'Your carriers may be overcharging you €60M a year. When was the last time someone checked?'
- 'Transport speed, warehouse delivery, tariff response and freight invoices — four gaps worth €300M that sit between you and your 2028 target.' (synthesis)

SUPPLY CHAIN COVERAGE CHECK — MANDATORY:
Before finalizing, verify ALL THREE covered:
- At least ONE on transport/freight (inbound, outbound, consolidation, freight audit, carrier management)
- At least ONE on sourcing/procurement decision-making (vendor selection, deal quality, tariff response)
- At least ONE on DC operations or inventory flow (throughput, automation, allocation, inventory positioning)
If ANY missing, replace the weakest provocation.

WHAT COUNTS AS SUPPLY CHAIN — STRICT DEFINITION:
YES: sourcing, procurement, inbound transport, freight consolidation, freight audit, DC operations, outbound transport, last mile, returns, demand/supply planning, inventory optimization, tariff/trade response, supplier management, DC-to-store allocation.
NO: store labor scheduling, store layout, marketing, e-commerce UX, international margin gaps (unless traced to specific operational cause like DC costs), HR, real estate, corporate overhead.
TEST: If it would make sense in a board presentation, too generic. If it only makes sense talking to VP Supply Chain about a specific process, it is right.

TITLE RULES FROM APPROVED EXAMPLES:
- Use conditional language when not FACT: may, could, if so, it seems, it looks like
- Use questions instead of accusations: 'is anyone modelling it?' not 'nobody is modelling it'
- Include one specific number that creates pain
- Be specific: name the gap, not the category
- The synthesis title must name all the gaps and connect them to the margin target

TITLE PROFESSIONALISM RULE: Provocation titles must sound like a senior partner wrote them, not a tech blogger.

NEVER put in a title: specific technology names (TikTok, Instagram, o9, SAP), buzzwords (AI, digital twin, GenAI), or anything that sounds trendy. The title is about MONEY and TIME, not tools.

BAD: 'Your demand system is 3 weeks behind TikTok' — a COO will laugh
BAD: 'Your o9 system is not connected to project44' — sounds like an IT audit
GOOD: 'Your demand plan refreshes every 3 weeks. Your inventory costs €5B.' — about money
GOOD: 'Your inventory costs €1.1B more per year than it should.' — about pain

Technology names go in the EVIDENCE section only. The title speaks the language of a CEO, not a solutions architect.

SUPPLY CHAIN FOCUS: At least 4 of 5 must be supply chain. Max 1 non-supply-chain labeled 'Beyond Supply Chain'. Marketing is NOT valid.
PROVOCATION 05 SPECIAL: Must be SYNTHESIS tying 1-4 together into a margin improvement thesis with arithmetic.

CONFIDENCE THRESHOLD RULE: A provocation can only be included if its TITLE CLAIM and COST OF INACTION number are supported by at least one FACT and the overall argument reaches MODERATE CONFIDENCE or higher. If every evidence bullet is LOW CONFIDENCE or ASSUMPTION, the provocation is too weak — either find stronger evidence or replace it with a different provocation. LOW CONFIDENCE evidence can appear as supporting context inside a stronger provocation, but cannot be the foundation of one.

PEER AMMUNITION RULE: Before writing each provocation, check benchmark_table.md and peer_set.md. Each provocation must include at least one specific peer comparison as evidence — a named competitor with a real number that makes the gap concrete. Example: ASICS tripled margin from 7% to 14.7% in 24 months. Lululemon runs 23.7% operating margin at 95% DTC. These peer facts are ammunition that makes the provocation harder to dismiss.

Save the 5 raw titles and a short evidence note for each as: raw_provocations.md

### Job 3C: Add Compliance Layer (formatting mode)
Take the 5 raw provocations from Job 3A and ADD to each one — WITHOUT changing the title:
- Financial lever badge and operational lever badge
- Primary buyer personas (CFO, COO, CSCO, CDO, CEO)
- Evidence bullets (2-3) with [FACT — source], [INFERENCE — reasoning], or [ASSUMPTION — basis] tags
- Cost of inaction: one specific number per year
- Discovery question: the question this earns us the right to ask
- Check lever distribution covers 3+ distinct financial AND 3+ distinct operational categories across all 5

Financial Levers (CFO): Working Capital Release, Gross Margin Improvement, OPEX Reduction, COGS Avoidance, Revenue Protection/Growth, Risk Mitigation, Operating Margin Expansion (synthesis only)
Operational Levers (COO): Planning Cycle Speed, Response Latency, Fulfillment Speed, Decision Cycle Compression, Production-to-Shelf Velocity, Throughput/Process Efficiency

Rules: 1 financial + 1 operational per provocation. Max 2 financial if truly warranted.

CRITICAL: Do NOT rewrite or 'improve' the titles from Job 3A. The titles are final. You are only ADDING metadata around them.

FORMAT per provocation: Category tag (small), Title (from Job 3A, unchanged), Lever badges, Buyer personas, Evidence bullets with tags, Cost of Inaction, Discovery Question.

Save as: provocations.md

### Job 4: Quality Self-Evaluation
Check each provocation:
Test 1 CFO Test: Can CFO calculate ROI on first read? If not, rewrite.
Test 2 Specificity: Points to specific fixable sub-process? Vague = fail.
Test 3 Falsifiability: Client could prove wrong with one data point? If too vague, rewrite.
Test 4 Supply Chain Validity: Is this about an actual supply chain process per strict definition? Store labor and international margin gap are NOT supply chain. Fail = REPLACE.
Test 5 Coverage: Do the 5 provocations collectively cover transport/freight, sourcing/procurement, AND DC operations? If any missing, REPLACE weakest.
Check lever distribution: 3+ distinct financial, 3+ distinct operational across all 5.
If any provocation fails, revise and save updated provocations.md.
Save evaluation as: quality_evaluation.md
Save clean questions as: discovery_questions.md
