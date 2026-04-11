# MEMORY — Quality Standards and Rules
Updated: April 2026
These rules are mandatory for ALL phases and ALL company analyses.

## 1. TOOL PURPOSE
This tool is a provocation machine that produces outside-in executive briefings from public data. Its purpose is to earn the right to sell a €600-800K, 20-week proof-of-value engagement. Target audience: CFO, COO, VP Supply Chain. Every design decision must serve that commercial goal.

## 2. PROVOCATION TITLE RULE

- Maximum 20 words. No exceptions. Count them.
- Formula: one number + one gap or contradiction + one twist (personal or urgent)
- The twist must imply one of: you already have what you need and are not using it, you are paying someone else to solve what you could solve yourself, or a specific deadline makes inaction more expensive every week
- NEVER include system names (o9, project44, SAP, SageMaker) in titles
- NEVER include country percentages (Vietnam 27%, Indonesia 19%) in titles
- NEVER explain the mechanism in the title — save that for evidence
- APPROVED TITLE EXAMPLES (follow this exact style):
  - "Your inventory costs €1.1B more per year than it should — and your planning system knows it."
  - "Your e-commerce delivers in 3–7 days. The same shoe arrives from Amazon in 1–2."
  - "A €200M tariff bill arrived in your guidance, and your response cycle is measured in weeks."
  - "1,933 stores with ship-from-store capability. 3–7 day delivery promise. You paid Amazon to solve it instead."

## 3. CONFIDENCE RULE — ABSOLUTE
The client document may ONLY contain these confidence levels:

- [FACT] — confirmed from public filing or disclosed source
- [INFERENCE — HIGH] — direct logical conclusion from confirmed facts
- [INFERENCE — MODERATE] — reasonable inference, alternative explanations exist, BUT the provocation must also contain at least one FACT

NEVER include in client-facing output:

- [INFERENCE — LOW] — remove entirely
- [ASSUMPTION] — remove entirely

LOW and ASSUMPTION evidence goes to the internal memo (Track B) only. If a provocation has no FACT or HIGH evidence, either kill the provocation or reframe it around structural observations rather than unverifiable numbers.
The claim tags legend in the client document should only show three levels: FACT, INFERENCE — HIGH, INFERENCE — MODERATE.

## 4. DUAL VALUE LEVER TAGS
Every provocation gets exactly two tags:

Financial lever (pick one or two):
- Working Capital Release
- Gross Margin Improvement
- OPEX Reduction
- COGS Avoidance
- Revenue Protection / Growth
- Risk Mitigation
- Operating Margin Expansion (synthesis provocation only)

Operational lever (pick exactly one):
- Planning Cycle Speed
- Response Latency
- Fulfillment Speed
- Decision Cycle Compression
- Production-to-Shelf Velocity
- Throughput / Process Efficiency

In the internal memo (Track B) only, add a buyer persona tag: CFO, COO, CSCO, CDO, CMO, CEO.
The 5 provocations must collectively cover at least 3 distinct financial levers AND at least 3 distinct operational levers. If they don't, revise.

## 5. PROVOCATION QUALITY TESTS
Each provocation must pass three tests before inclusion:

- Test 1 — CFO TEST: Can a CFO calculate ROI on first read without explanation?
- Test 2 — SPECIFICITY TEST: Does it point to a specific fixable sub-process, not a general observation?
- Test 3 — FALSIFIABILITY TEST: Could the client disprove it with one internal data point?

If any provocation fails any test, rewrite it before including.
The 5th provocation must be a SYNTHESIS tying provocations 1-4 into a margin improvement thesis with an EBIT bridge table showing each provocation's mechanism + impact summing to a total. Never a standalone comparison.

## 6. KPI SCORECARD — "THE SCORECARD"
Appears as its own section BEFORE the provocations. Called "The Scorecard" with subtitle "Key operational KPIs benchmarked against [N] global peers. Public filings only."

Three tiers in ONE single HTML table (not separate tables) with table-layout: fixed and colgroup with explicit column widths:

**Tier 1 — RED — Operations Controls Directly:**
- Inventory / Revenue ("How much cash is trapped in unsold product")
- Inventory Turns ("How fast stock converts to sales")
- Sourcing Concentration, top 2 countries ("Tariff and disruption risk from supplier geography")
- Gross-to-Op Margin Spread ("How much profit operations consumes between factory and bottom line")
- Logistics & Distribution Cost / Revenue — only if MODERATE confidence+ ("Total cost of moving product from factory to customer")
- DTC Delivery Speed ("What you promise vs. what competitors deliver")
- DTC Channel Mix ("Share of revenue through your own stores and website")
- E-commerce Growth ("Speed of your fastest-growing channel")
- Reverse Logistics Cost / E-commerce Revenue — only if MODERATE confidence+ ("Cost of processing returns as share of online sales")

**Tier 2 — AMBER — Operations Significantly Influences:**
- Gross Margin ("Pricing power after product cost, before operating expenses")
- SG&A / Revenue ("Overhead efficiency — logistics, marketing, and corporate costs combined")
- Revenue per Employee ("How much revenue each employee generates")

**Tier 3 — GREY — Management Commitments Operations Must Deliver:**
- Must show: Commitment name, Current Actual, Target, Gap (red/green colored), Timeline, Source
- Only include targets explicitly stated as public commitments by management
- NEVER include: stock price, EPS, P/E, dividend yield, or any pure market metric
- If fewer than 2 Tier 3 KPIs confirmed from public sources, drop Tier 3 entirely

**Scorecard Rules:**
- Every RED KPI must link to a provocation via clickable anchor with smooth scroll
- Estimated KPIs capped at AMBER regardless of gap size
- Each KPI has a one-line plain English description (max 10 words)
- Numbers use font-variant-numeric: tabular-nums for alignment
- Status as flat colored text (RED/AMBER/GREEN), not pill badges or rounded badges
- Footnotes section below table with numbered source references in small text
- Narrative paragraph below table bridging scorecard to provocations: "[X] of [Y] tracked KPIs sit at or below peer median..."
- Light theme matching rest of page — NOT dark/Bloomberg

## 7. ENGAGEMENT PLAN
**Phase One: Validate & Scope — Weeks 1-4, fixed fee.**
- Stress-test provocations against internal data
- Optional body-vs-brain network diagnostic (2-3 days, NOT a separate workstream)
- Deliverable: go/no-go with confirmed Phase Two scope, measurable outcome target, measured baseline
- Zero-risk: if provocations are wrong, client owes nothing beyond Phase One fee

**Phase Two: Design, Build, Test, Deploy — Weeks 5-24, fixed fee + success bonus.**
- Weeks 5-8: Design target process, map integrations, start security/governance
- Weeks 9-16: Build in client environment, connect live data, run parallel operations
- Weeks 17-20: Go live on bounded scope, measure against baseline
- Weeks 21-24: Measure, document before/after, build business case for scale

This is a real production deployment, NOT a 90-day consulting discovery.

## 8. DUAL TRACK OUTPUT
- **Track A — Client-facing:** ZERO mention of AI, agents, architecture, methodology, or Accenture platforms. Reads like a senior partner wrote it.
- **Track B — Internal Accenture:** Full architecture, all agent outputs, accelerator mapping per provocation, buyer persona tags, routing decisions, quality evaluation, competitive intelligence.

## 9. HTML OUTPUT FORMAT
- Single HTML file with Tailwind CSS CDN + Plotly CDN (for competitive intelligence charts)
- Three tabs: Tab 1 Client Presentation (default), Tab 2 Competitive Intelligence, Tab 3 How We Built This
- Tabs 2 and 3 are internal only — never show to client
- Light theme design — NOT dark/Bloomberg
- CSS print media query for clean PDF output via Ctrl+P (no tabs, no interactive in print)
- Provocation links as clickable anchors with smooth scroll + "Back to Scorecard" links

## 10. DATA FRESHNESS RULE
- Always use most recent fiscal year available
- Every number must show its fiscal year: "21.0% (FY2024)" not just "21.0%"
- Never mix fiscal years within a calculation without flagging: "(FY2024 inventory on FY2025 revenue — cross-year estimate)"
- If using older data: add "(FY2024 — FY2025 breakdown not yet published)"
- For peers: note each peer's fiscal year end date

## 11. LANGUAGE RULES
- Spell out ALL abbreviations on first use: DTC (Direct-to-Consumer), SG&A (Selling, General & Administrative), EBIT (Earnings Before Interest & Tax), COGS (Cost of Goods Sold), 3PL (third-party logistics), CN = Currency-Neutral (NEVER use "CN" alone)
- Add "pp = percentage points" once in footnotes
- BANNED WORDS: leverage, synergy, holistic, paradigm, ecosystem, best-in-class (unless naming the company), world-class, cutting-edge, state-of-the-art, reimagine, unlock value, digital transformation, journey
- Maximum 25 words per sentence
- No passive hedging ("there may be an opportunity to potentially explore" — either there's a gap or there isn't)

## 12. CONDITIONAL ROUTING
- After Phase 1 (company research): check financial health → distress → weight toward cost reduction
- After body-vs-brain diagnosis: physical network is constraint → lead with network optimization before AI
- After peer benchmarking: outlier peer with >5pp margin improvement in 2 years → make that peer central to provocations

## 13. PEER AMMUNITION RULE
Every provocation needs one peer data point proving the gap is closable — a named company that demonstrated the improvement. The competitive intelligence tab provides the deep-dive backup, but provocations must carry enough peer evidence to stand alone.

## 14. BRITTAIN LADD BODY VS BRAIN
Before recommending AI/process improvements, diagnose whether the physical supply chain (network, warehouses, transportation) is the constraint. If body is broken, fix network first. Body diagnostic = 2-3 days within Phase One, explicitly optional in proposals.

## 15. LOW-CONFIDENCE REFRAME PATTERN
When a provocation has strong structural facts but weak numbers: keep the provocation, reframe around the structural observation, NOT the unverifiable number. Example: don't assert "€60M in freight overcharges" (LOW), instead assert "60+ DCs, 15+ carriers, no confirmed centralised reconciliation" (HIGH). Make the sizing a Phase One discovery question.

## 16. SYNTHESIS ARITHMETIC
The 5th provocation shows an EBIT bridge table: each preceding provocation's mechanism + EBIT impact summing to total. Must connect to management commitment in Tier 3 (e.g., "€419M closes the gap from 8.3% to 10%+"). If a provocation is removed or its number can't be defended, recalculate the total. Never include LOW CONFIDENCE numbers in synthesis arithmetic.

## 17. WHY NOW FRAMING
Never frame urgency around AI capability timelines (ANI/AGI). Instead:
- Competitive data accumulation: "Every month you delay, competitors accumulate proprietary operational data you can't replicate"
- Client-specific deadlines: tariff expiry dates, World Cup windows, earnings dates
- "AI models are commoditizing. The data you train them on is not."

## 18. ACCELERATOR MAPPING (Track B only)
Each provocation in the internal memo must identify the specific Accenture capability, AI Refinery agent, or pre-built accelerator that addresses it. If none exists: "custom build required — estimate X weeks within Phase Two." NEVER mention accelerators in client document.

## 19. COMPETITIVE INTELLIGENCE TAB
- 5 key takeaways — each must be surprising and specific, not generic
- Full peer comparison table with interactive Plotly charts (radar + bar)
- Takeaways must connect to provocations

## 20. HOW WE BUILT THIS TAB (internal)
- 7 specialist agents as numbered cards with name, role, capabilities
- Infrastructure section: orchestration, web search, source library, claim tagging
- Execution flow as horizontal pipeline
- "What This Is / What This Is Not" section
- Reframe limitations as "Phase One validates" not "tool can't do X"

## 21. ARCHITECTURE
6-phase optimized pipeline:
1. Phase 1 GATHER: ONLY phase with web search — collects everything
2. Phase 2 RESEARCH: no web — company analysis
3. Phase 3 BENCHMARK: no web — peer analysis
4. Phase 4 DEEP ANALYSIS: no web — merged operating model + AI value (sub-sections with firewall)
5. Phase 5 CHALLENGE: no web — due diligence + routing + provocations + quality tests
6. Phase 6 PRODUCE: no web — dual track outputs + KPI scorecard + HTML generation

## 22. DOCUMENT STRUCTURE (client-facing)
Header → "What is this?" intro → The Scorecard (KPI dashboard) → Provocations (4-5 with dual levers, evidence, cost of inaction, discovery question) → Engagement Plan (Phase One + Phase Two) → Discovery Questions → Closing paragraph.

## 23. AUGER COMPETITIVE AWARENESS
Auger (Dave Clark, ex-Amazon CEO, $100M funding) is the key AI-native competitor in supply chain. Autonomous operating system for supply chains. First customer: Meta Reality Labs (Feb 2026). Microsoft Fabric partnership. Study their deployments as market intelligence.

## 24. ACCENTURE POSITIONING
Right to win is NOT the platform — it is the integration gap startups cannot fill: enterprise infrastructure, security, data governance, change management, organizational redesign. Trojan horse: inject AI into existing managed service contracts where trust and data access already exist.

## 25. GEOGRAPHIC COVERAGE RULE
For any company that operates across multiple major regions (US, Europe, Asia-Pacific), operational KPIs must be captured and compared per region, not just globally or for one market. Specifically:

- **DTC Delivery Speed:** Show SLAs for BOTH the company's home market AND its largest international market (e.g., US + EU for adidas, US + China for Nike). Compare against the relevant Amazon benchmark in each region (Amazon US = 1-2 days, Amazon DE = next-day, etc.)
- **Fulfillment infrastructure:** Describe the major DC or fulfillment hub in each region separately (e.g., Wilkes-Barre for US, Mantova for EU) with per-region capabilities and constraints
- **Carrier structure:** List the primary 3PL/carrier partners per region — the fragmentation and audit complexity differs by geography
- **Tariff and trade exposure:** Cover trade policy risks for each major sourcing-to-destination corridor, not just US tariffs — EU has its own trade dynamics
- **E-commerce metrics:** If per-region e-commerce data is available, split it. The fulfillment challenge in the US (long distances, one major DC) is different from Europe (shorter distances, more borders, more carriers)
- **In the KPI dashboard:** if a KPI is only available for one region, label it explicitly: "DTC Delivery Speed (US)" not just "DTC Delivery Speed." If both regions are available, show both rows or show the global figure with a footnote noting regional variation.

The goal: a European COO should never feel the analysis only covered the US. A US COO should never feel it only covered Europe. The document must demonstrate global awareness.

## Execution History
(This section is updated automatically after each run)

## Company-Specific Learnings
(This section stores learnings per company for future re-runs)
