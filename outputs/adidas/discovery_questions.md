# Adidas AG — Prioritized Discovery Questions
**Step 7: Due Diligence | Date: 2026-04-03 (v2 — post Step 6 integration)**
**Company:** adidas AG | XETRA: ADS | OTC ADR: ADDYY
**Sources:** All prior step outputs (Steps 1–6); due_diligence.md (Step 7 v2); adidas Annual Reports 2023–2025; FY2025 results press release; current_signals.md; Databricks Data + AI Summit 2025/2026 session catalog

---

## RANKING METHODOLOGY

Questions are ranked by **decision impact** — the degree to which the answer will change what we propose, how we scope it, and whether we should pursue the engagement at all. Questions that can kill or radically reshape the thesis rank highest.

**Impact scale:**
- **CRITICAL:** Answer changes whether and how we engage. Pursuing without this answer means scoping blind.
- **HIGH:** Answer shapes the scope, entry point, or financial case materially.
- **MEDIUM:** Answer refines a specific opportunity or identifies an execution risk.

**Tags on each question:**
- [ASSUMPTION]: We have made an explicit assumption that this question validates or invalidates.
- [INFERENCE]: Our analytical inference needs grounding in facts from the company.
- [FACT GAP]: A specific fact that our public analysis could not determine but is material.

---

## TIER 1 — CRITICAL (Must answer before scoping the engagement)

---

### Q1 — What does the Databricks Agent Digital Twin fleet actually govern today?

**Impact:** CRITICAL
**Counterargument addressed:** CA-1 (Technology house more advanced than assumed)

"We reviewed your Databricks Data + AI Summit 2026 session — 'Beyond the Trace: adidas' Agent Digital Twin for Governance, Cost, and ROI.' This describes a production lakehouse control plane managing an agent fleet across governance, cost, and ROI. Can you walk us through what that agent fleet does today — specifically: which business decisions does it influence or make autonomously? Is its scope currently limited to analytics and customer insights, or does it extend to supply chain decisions, marketing automation, or procurement? And who owns and operates this architecture day-to-day?"

**What a good answer sounds like:** The fleet is currently scoped to analytics, product review intelligence, and engineering workflows — not yet cross-functional business decisions. A named internal team owns it but it operates as a pocketed capability, not an enterprise-wide platform. This confirms the white space for an integration and strategy engagement.

**What a worrying answer sounds like:** "The agent fleet already governs demand planning and supply chain allocation" — which would mean our #1 ranked value stream is already being addressed internally.

**Why it matters:** This is the single most important fact to establish. If the agent fleet is purely analytics-scoped, our enterprise AI integration opportunity is confirmed and significant. If it already spans supply chain or marketing decisions, our opportunity set narrows dramatically. Everything we propose about AI integration and strategy rests on understanding the actual current state of adidas's most sophisticated AI asset. [FACT — Databricks 2026 session confirmed; FACT GAP — scope of fleet not publicly disclosed]

---

### Q2 — Who owns the enterprise AI strategy and integration architecture?

**Impact:** CRITICAL
**Counterargument addressed:** CA-1, CA-5 (AI governance gap)

"With five distinct AI and data platforms running in production — Databricks for GenAI and analytics, AWS SageMaker for seasonal forecasting, o9 Solutions for supply planning, project44 for supply chain visibility, and AWS Bedrock for GenAI knowledge management — who is responsible for the integration strategy that connects them? Is there a named internal owner (a Head of AI, Chief Data Officer, or enterprise architect) with a mandate to design the unified AI architecture? And is there a funded roadmap for integrating these systems, or is each platform managed by a separate functional team?"

**What a good answer sounds like:** A named owner exists below CFO level; there is a funded integration roadmap; the work is structured. Our role is acceleration and external perspective.

**What a worrying answer sounds like:** "Each platform has its own team; there's no single owner for the integrated architecture." This confirms the governance gap — and confirms our opportunity.

**Why it matters:** The entire premise of our engagement (enterprise AI integration strategy) depends on whether this gap is real and unfilled. If adidas already has a strong internal AI architecture team with a clear mandate, our engagement design must align to their roadmap rather than lead it. If the gap is confirmed, we have a clear entry point above the existing SI landscape. [FACT GAP — not determinable from public sources; critical to scope]

---

### Q3 — What is the TRANS4RM go-live status and which areas are in process design freeze?

**Impact:** CRITICAL
**Counterargument addressed:** CA-3 (TRANS4RM bandwidth)

"Central Finance went live on S/4HANA in November 2023. Finance and Purchasing modules were planned for 2024. As of today, what percentage of adidas's transactional volume is now running on S/4HANA? Which modules are currently in active design and deployment? And specifically — are supply planning, demand planning, commercial/sales, and order management processes currently in design freeze, meaning the process definition is locked and cannot be changed until the relevant module goes live?"

**What a good answer sounds like:** A clear module sequencing map with confirmed go-live dates and explicit list of areas in design freeze. This lets us scope our engagement precisely around the frozen zones.

**What a worrying answer sounds like:** "Most of supply chain and commercial processes are in design phase right now" — which would mean our top two value streams (demand planning, procurement intelligence) are effectively locked for 12–18 months.

**Why it matters:** The design freeze map determines which AI opportunities are available to engage now vs. which must wait for TRANS4RM module go-lives. It is the most important structural constraint on engagement sequencing. [INFERENCE — standard ERP program practice; specifics unknown; FACT — no completion announcement exists in public record as of April 2026]

---

### Q4 — What is EPAM's and Infosys's scope boundary relative to AI and analytics work?

**Impact:** CRITICAL
**Counterargument addressed:** CA-2 (Delivery partners own the relationship)

"EPAM has been your primary systems integrator on TRANS4RM since the program began, and Infosys manages your IT infrastructure. Can you describe precisely where each partner's scope ends — specifically: does EPAM have any mandate in the Databricks analytics stack, the o9 integration layer, the Agent Digital Twin governance architecture, or the project44 implementation? And separately — do either EPAM or Infosys have a role in your AI and data strategy work, or is that entirely led by your internal team?"

**What a good answer sounds like:** EPAM owns SAP delivery. Infosys owns infrastructure and managed services. The AI/analytics and agent governance layer is designed and owned by adidas's internal engineering team with no SI in the driver's seat. This confirms our differentiated lane.

**What a worrying answer sounds like:** "EPAM also supports our data and analytics work" — meaning the territory we want to occupy is already allocated to an incumbent with a 15-year relationship.

**Why it matters:** Our engagement model depends entirely on a gap between the ERP delivery lane (EPAM) and the enterprise AI strategy lane (our opportunity). If EPAM has claimed the AI/analytics space, we are entering a crowded room with an entrenched competitor. This must be resolved before scoping. [FACT GAP — SI scope boundary not determinable from public sources]

---

## TIER 2 — HIGH IMPACT (Shapes scope and financial case materially)

---

### Q5 — What is your World Cup data and DTC activation strategy for North America?

**Impact:** HIGH
**Counterargument addressed:** CA-9 (World Cup window); CA-7 (North America)

"The FIFA World Cup begins in June — approximately 10–12 weeks from now. You are the exclusive sporting goods partner; you have 13 national team kits in market; and the tournament is hosted across your weakest-performing region. Can you describe what specific DTC and data strategy you have designed for the World Cup window: Is there a dedicated North America consumer acquisition and adiClub activation program for the tournament period? Do you have data capture mechanisms in place to understand how World Cup consumers interact with adidas.com, in-store, and adiClub — and to convert that interaction into long-term loyalty relationships? And who owns the post-World Cup analysis of whether the brand moment converted into durable market share?"

**What a good answer sounds like:** A structured World Cup data and DTC activation plan exists with clear objectives and measurement frameworks. There is a named team responsible for post-World Cup analysis and capability retention.

**What a worrying answer sounds like:** "We have the marketing campaign ready" without a specific data capture and loyalty conversion strategy — suggesting the World Cup will generate sales but not lasting DTC capability uplift.

**Why it matters:** Our repositioned thesis frames the World Cup as a data collection event that requires architectural readiness NOW. If adidas already has a robust World Cup data strategy, our engagement aligns to it and accelerates it. If the strategy is marketing-only (campaign, inventory), the data and DTC architecture gap is confirmed and urgent. [INFERENCE — no World Cup data strategy evidenced in public sources; FACT on World Cup commercial calendar]

---

### Q6 — What is your current tariff scenario modeling process and timeline?

**Impact:** HIGH
**Counterargument addressed:** CA-1; SC-1 validation

"When a new tariff event occurs — like the US Section 122 tariff signed February 22, 2026, or the scheduled July 24, 2026 expiry of that tariff — what is the actual process for modeling the landed-cost impact across your active sourcing lanes and re-ranking supplier options? Who is involved, what tools do they use, and how long does it take to go from 'tariff announced' to 'sourcing decision made'? And separately: do you have a scenario model already built for the July 24 tariff expiry?"

**What a good answer sounds like:** The process takes weeks, involves multiple teams (procurement, finance, supply chain), and relies on manual spreadsheet analysis supplemented by Coupa and o9 outputs. No automated tariff scenario tool exists.

**What a worrying answer sounds like:** "We already have an automated scenario modeling tool that gives us options in hours" — which would shrink or eliminate this opportunity.

**Why it matters:** The €200M tariff headwind in 2026 guidance is our most time-sensitive financial hook. The July 24, 2026 Section 122 expiry creates a second inflection point that is exactly the kind of scenario where AI-powered tariff intelligence has immediate, quantifiable value. If adidas already has this capability, the opportunity does not exist. If the process is manual, the value is immediate and concrete. [ASSUMPTION — no AI-powered tariff modeling confirmed; FACT on tariff policy timeline]

---

### Q7 — How does your demand planning system handle a viral product moment today?

**Impact:** HIGH
**Value lever:** SC-2 (demand planning) validation

"When a product like the Samba or Gazelle starts to accelerate beyond forecast — driven by social media, celebrity wear, or a cultural moment — how quickly does your current planning system detect and respond? Does o9 or SageMaker automatically pick up social acceleration signals, or does a human planner identify the trend and manually revise the forecast? What is the typical lag between a product going viral and the production order revision being issued?"

**What a good answer sounds like:** Detection is largely human-driven and backward-looking; social signals are not integrated into o9 or SageMaker; the planning cycle revision happens monthly. This confirms the demand sensing gap.

**What a worrying answer sounds like:** "We have real-time social signal feeds integrated into o9" — which would mean the highest-value demand sensing opportunity is already being addressed.

**Why it matters:** The demand planning opportunity (Ranked #1 by weighted value at €250M+ working capital potential) depends on the gap between adidas's current social signal detection speed (weeks) and AI-enabled detection speed (24–48 hours). Whether this gap exists and how large it is determines the core financial case for our #1 ranked value stream. [INFERENCE — backward-looking assumption based on TRANS4RM incompleteness; FACT on o9 and SageMaker deployment]

---

### Q8 — What is the actual deployment and adoption depth of o9 Solutions?

**Impact:** HIGH
**Counterargument addressed:** CA-1 (Technology house already full)

"o9 Solutions is live for in-season planning and demand management. Can you walk us through what percentage of o9's functionality is actively used in production vs. licensed but not yet fully operationalized? Specifically: are o9's AI-driven recommendations being acted on autonomously by the planning system, or are they recommendations that human planners review and accept or override? And is o9 integrated with real-time store sell-through data from GK OmniPOS, or does the store sell-through feed arrive as a batch upload?"

**What a good answer sounds like:** A frank account of which modules are active, what percentage of planning decisions are AI-influenced, and what the known gaps are between the tool's capability and current use — particularly on data integration gaps.

**What a worrying answer sounds like:** "We have it deployed" with no specifics on usage depth — which typically means licensed but underutilized.

**Why it matters:** If o9 is fully operationalized and integrated with real-time store data, our demand planning opportunity is narrower (enhancement work). If it is partially deployed or operating on batch data, the opportunity is much larger (operationalization and real-time integration). This directly sizes the addressable opportunity for our #1 ranked value stream. [ASSUMPTION — prior analysis assumes partial operationalization based on TRANS4RM incompleteness and absence of confirmed real-time store integration]

---

### Q9 — Is ship-from-store operationally live, and what is the obstacle to scaling it?

**Impact:** HIGH
**Value lever:** SC-3 (ship-from-store) validation

"You have GK OmniPOS deployed at 1,300+ stores with RFID inventory accuracy above 99% — that is exceptional infrastructure. Are you currently using stores as fulfillment nodes for e-commerce orders? If yes, at what scale and in which markets? If not, what is the specific obstacle — a technology gap in AI routing, a contractual issue with franchise stores, labor cost concerns in the fulfilment process, or a strategic decision to route all e-commerce through distribution centers? And how does the Amazon Buy with Prime and MCF partnership affect your internal thinking about ship-from-store economics?"

**What a good answer sounds like:** "We have the infrastructure but haven't built the central AI routing layer" — confirming the opportunity is available.

**What a worrying answer sounds like:** "We evaluated ship-from-store and decided against it because [strategic reason]" — meaning the opportunity is closed for non-technical reasons.

**Why it matters:** Ship-from-store is a top-3 value stream. If it is already operational at scale, the opportunity is smaller. If there is a deliberate strategic decision against it (driven by the Amazon partnership posture), we need to understand that reasoning before proposing it. The answer also determines whether we frame this as "build the AI routing layer" or "rethink the omnichannel economics model." [ASSUMPTION — routing AI not confirmed at scale; FACT on GK RFID and Amazon Buy with Prime infrastructure]

---

### Q10 — What is the depth of adiClub data and how is it used in personalization today?

**Impact:** HIGH
**Value lever:** Marketing personalization / DTC growth

"adiClub has millions of members with a confirmed 3× conversion rate lift. Can you describe what behavioral data you have on members beyond purchase history? Do you capture browsing behavior on adidas.com, in-store behavior connected through GK OmniPOS and RFID, fitness activity data, or lifestyle preference signals? And how is that data currently used in marketing personalization — are you doing individual-level recommendations, segment-based targeting, or primarily campaign-level audience selection? And how is the MosaicML product review intelligence connected to adiClub personalization, if at all?"

**What a good answer sounds like:** Rich data exists but personalization is segment-based rather than individual-level; the MosaicML pipeline and adiClub data are not yet connected; a clear gap exists between available data and personalization depth.

**What a worrying answer sounds like:** "We only have purchase history and email" — meaning the personalization upside is limited by data poverty, not capability gaps.

**Why it matters:** The marketing personalization opportunity (Ranked #2 value stream, €300M potential) depends on the richness of the underlying consumer data and the gap between available data and deployed personalization depth. The combination of adiClub behavioral data + MosaicML review intelligence + AI Archive is potentially a uniquely powerful personalization foundation — but only if connected. [FACT GAP — adiClub behavioral data depth not publicly disclosed]

---

### Q11 — What is the root cause of North America's underperformance relative to all other regions?

**Impact:** HIGH
**Counterargument addressed:** CA-7 (North America)

"North America grew only +4% constant currency in FY2025 while every other region grew double digits. Management cited conservative wholesale sell-in. But below that explanation — what is driving the conservatism? Is it excess retail inventory at wholesale partners like Foot Locker and Dick's Sporting Goods? Brand positioning weakness relative to Nike and On in running and performance? DTC digital infrastructure gaps that reduce conversion relative to European or Asian markets? Or something specific to how you manage the wholesale-DTC balance in that market? And has the recent Nike turnaround signal (Q1 FY2026: first positive quarter in multiple quarters) changed your North America competitive assessment?"

**What a good answer sounds like:** A specific root cause diagnosis — either wholesale inventory overhang, brand positioning, DTC capability gap, or competitive pressure — with a clear internal plan for each.

**What a worrying answer sounds like:** "It's a combination of everything" without prioritization — meaning no one has a clear plan to fix it, and the World Cup is being relied on as an external recovery catalyst rather than an internal capability investment.

**Why it matters:** Our North America AI opportunity (DTC data activation, personalization, demand sensing) is strongest if the gap is a technology and data problem. If the root cause is brand positioning or wholesale channel dynamics, our engagement has less direct leverage on the outcome. [INFERENCE — multiple possible root causes; definitive cause not publicly stated by management]

---

## TIER 3 — MEDIUM IMPACT (Refines specific opportunities or execution risks)

---

### Q12 — How is the Databricks MosaicML pipeline governed for brand voice?

**Impact:** MEDIUM
**Value lever:** Marketing content AI / GenAI brand governance

"Your MosaicML GenAI pipeline processes 2 million+ product reviews annually at production scale. As you consider extending GenAI to external marketing content — campaign materials, product descriptions, social content, World Cup activation — what governance framework do you have for ensuring AI-generated output maintains adidas brand voice and quality standards? Who has authority to approve AI-generated content before it goes live? And has the AI Archive been integrated into the GenAI content workflow, or does it operate as a separate design research tool?"

**What a good answer sounds like:** A brand governance framework exists or is being built; the bottleneck to scaling GenAI marketing is defined and manageable.

**What a worrying answer sounds like:** "We haven't figured out governance yet" — which is simultaneously a risk and an engagement entry point.

**Why it matters:** GenAI marketing content is our #2 value opportunity by financial size, but brand governance is the primary execution risk. Understanding the governance starting point determines whether we help build the framework or accelerate an existing one. The AI Archive integration question matters because the design archive is a differentiating AI asset that most competitors cannot replicate — and its connection (or disconnection) to the content generation pipeline is the difference between commodity GenAI and brand-authentic AI content. [INFERENCE — governance depth not publicly documented]

---

### Q13 — What second-tier supplier visibility do you have below your 124 direct partners?

**Impact:** MEDIUM
**Value lever:** SC-1 (tariff intelligence) — multi-tier risk

"You source from 124 supplier partners operating 283 factories across 32 countries, with Vietnam (27%) and Indonesia (19%) as top sourcing countries. Do you have visibility into where those factories source their critical materials — fabrics, foams, soles, hardware? Specifically: if a Vietnamese factory uses Chinese-sourced foam for US-bound footwear, does that material-origin exposure appear in your tariff risk model? And does your SAP Business Technology Platform supplier portal extend beyond first-tier factories into materials sourcing?"

**What a good answer sounds like:** Second-tier visibility exists for critical materials in key markets; a risk mapping has been done.

**What a worrying answer sounds like:** "Our visibility stops at the contract manufacturer" — meaning the AI opportunity includes multi-tier supply chain mapping, not just first-tier tariff modeling.

**Why it matters:** Multi-tier visibility is a materially more valuable and differentiated AI capability than first-tier tariff modeling. If adidas has no second-tier visibility, the opportunity scope is substantially larger than our current hypothesis. The July 24, 2026 tariff expiry makes this question urgent — if Vietnam and Indonesia sourcing exposure has hidden Chinese material content, the tariff liability may be larger than adidas currently models. [ASSUMPTION — second-tier visibility unlikely given standard industry practice; FACT on sourcing country concentration]

---

### Q14 — What performance milestones are embedded in Gulden's extended contract?

**Impact:** MEDIUM
**Value lever:** Executive alignment and engagement sponsorship

"Bjørn Gulden's contract was extended to December 31, 2030 — announced simultaneously with the FY2025 record results and the share buyback. The public announcement does not detail what performance conditions are attached to the extension. Can you share what financial and strategic milestones are embedded in the CEO's extended mandate? Specifically: is the >10% EBIT margin by 2028 a formal performance condition, or an aspirational target? Are there DTC penetration targets, North America recovery milestones, or transformation program completion milestones that would constitute underperformance relative to the board's expectations?"

**What a good answer sounds like:** Clear financial conditions tied to compensation; the >10% EBIT margin and North America recovery are formally embedded performance expectations.

**What a worrying answer sounds like:** "The extension is unconditional" — which removes the urgency lever from our financial case, though does not eliminate it.

**Why it matters:** If specific financial conditions drive the CEO's compensation and career trajectory, those conditions become our engagement's primary ROI anchors. A CEO who is personally incentivized to close the €420M guidance-to-consensus gap and hit the 2028 >10% margin target is a vision sponsor who has skin in the game. [FACT GAP — CEO contract performance conditions not publicly disclosed]

---

### Q15 — What does the post-World Cup organizational structure look like, and when does bandwidth free up?

**Impact:** MEDIUM
**Counterargument addressed:** CA-3, CA-9 (Bandwidth)

"Between TRANS4RM active deployments and FIFA World Cup execution, we recognize that Q2 2026 is likely the most bandwidth-constrained period your commercial, supply chain, and technology teams have experienced in several years. Can you give us a sense of the organizational cadence: when does the World Cup execution team shift from activation to analysis mode? When do the supply chain and commercial teams working on the active TRANS4RM modules have capacity for a new structured engagement? And is there a post-World Cup organizational review — new team structures, budget resets, strategic planning cycles — that we should be aware of as we think about engagement timing?"

**What a good answer sounds like:** Clear post-World Cup transition timeline (August–September 2026 as natural re-engagement window); specific teams who will have bandwidth after the tournament; a budget planning cycle in H2 2026 that our engagement can feed into.

**What a worrying answer sounds like:** "We have major organizational commitments through the end of 2026" — meaning even a post-World Cup start is premature, and we need to plan for an H1 2027 full engagement.

**Why it matters:** Engagement timing is as important as engagement content. Arriving with the right scope at the wrong organizational moment produces a polite deferral, not a contract. Understanding the post-World Cup bandwidth calendar determines whether we structure a rapid diagnostic for April–June (leading into World Cup) and a full engagement kick-off for August–September, or whether we need to plan for a longer pre-engagement diagnostic period. [INFERENCE — standard program management dynamics; specifics not determinable externally]

---

## MASTER SUMMARY — QUESTIONS BY COUNTERARGUMENT

| Question | Counterargument Addressed | Impact Level |
|----------|--------------------------|--------------|
| Q1 — Agent Digital Twin fleet scope | CA-1: AI house more advanced than assumed | CRITICAL |
| Q2 — Enterprise AI strategy ownership | CA-1, CA-5: AI governance gap | CRITICAL |
| Q3 — TRANS4RM go-live status and freeze zones | CA-3: TRANS4RM bandwidth constraint | CRITICAL |
| Q4 — EPAM/Infosys AI scope boundary | CA-2: Delivery partners own the relationship | CRITICAL |
| Q5 — World Cup data and DTC activation strategy | CA-9, CA-7: World Cup window; North America | HIGH |
| Q6 — Tariff scenario modeling process | CA-1; SC-1 (tariff intelligence) validation | HIGH |
| Q7 — Demand planning response to viral moments | SC-2 (demand sensing) validation | HIGH |
| Q8 — o9 deployment and adoption depth | CA-1: Tech house already full | HIGH |
| Q9 — Ship-from-store operational status | SC-3 validation | HIGH |
| Q10 — adiClub data depth and personalization use | Marketing personalization opportunity | HIGH |
| Q11 — North America root cause diagnosis | CA-7: North America underperformance | HIGH |
| Q12 — GenAI brand governance and AI Archive integration | Marketing AI execution risk | MEDIUM |
| Q13 — Second-tier supplier visibility | SC-1: Multi-tier tariff risk | MEDIUM |
| Q14 — Gulden contract performance milestones | Executive alignment and urgency framing | MEDIUM |
| Q15 — Post-World Cup organizational bandwidth | CA-3, CA-9: Engagement timing | MEDIUM |

---

## QUESTION SEQUENCING GUIDE FOR FIRST MEETING

The first meeting must answer Q1 through Q4 above all else. These four questions determine the fundamental shape of the engagement. Recommended opening framing:

> "Before we share our analysis, we want to ask you four questions — because the answers will completely determine what we recommend and whether it is useful to you. We'd rather hear the answers first than present assumptions that may already be resolved."

This approach signals intellectual honesty, respects adidas's AI maturity, and positions us as a partner who does diagnostics rather than a consultant who sells pre-packaged solutions. Given the sophistication of adidas's internal AI capability (production agent fleets, 85% Copilot adoption, MosaicML at scale), any approach that treats adidas as a technology laggard will be immediately discredited.

---

*Sources: All prior step outputs (Steps 1–6); due_diligence.md (Step 7 v2); adidas Annual Reports 2020–2025; FY2025 results press release (March 4, 2026); adidas Compensation Report 2024; Databricks Data + AI Summit 2025/2026 session catalog; earnings call transcripts; current_signals.md; Reuters; UBS analyst note; FDRA tariff survey*
