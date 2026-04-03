# Body vs. Brain Diagnosis — adidas AG
**Step 5 Output | Autonomous Consulting Workflow**
**Date:** 2026-04-03
**Analyst Role:** AI Value & Reinvention Analyst
**Sources:** FY2025 Annual Report (March 4, 2026), prior step outputs (value_levers.md, stream_ranking.md, tech_ops_footprint.md, transformation_capacity.md, company_snapshot.md), Databricks Data+AI Summit 2026 disclosures, Manhattan Associates user conference materials, project44 press releases (February 2026), GK Software disclosures, Kuehne+Nagel Mantova case study

---

## DEFINITIONS

### What is the BODY?
The **BODY** is the physical network that adidas operates within or depends upon. It is defined by geography, capital, and physical assets. The BODY includes: warehouses, distribution centers, stores, transportation lanes, factory locations, port infrastructure, and third-party logistics partner physical assets.

**A change is a BODY change if it requires:**
- Building, leasing, or closing a physical facility
- Moving production to a new country or factory
- Adding new transportation lanes or carrier relationships from scratch
- Installing new physical automation equipment (robotics, conveyors, ASRS)
- Opening or closing stores in new markets

BODY changes are typically slow (12–24+ months), capital-intensive (€10M–€350M per major DC), and operationally disruptive to change. They are the domain of network design strategy, not AI deployment.

### What is the BRAIN?
The **BRAIN** is the operating intelligence layer that runs within the Body. It is defined by data, algorithms, systems, and human decisions. The BRAIN includes: demand planning systems, allocation models, routing engines, WMS configurations, AI/ML models, control tower logic, supplier risk scoring, and decision-support tools.

**A change is a BRAIN change if it requires:**
- Updating software, models, or algorithms
- Building new data pipelines or integrations between existing systems
- Training ML models on available data
- Configuring AI agents or orchestration engines
- Changing how humans make decisions (supported by AI)

**KEY RULE:** If you can change it without physically moving or closing something, it is BRAIN. The distinction matters because BRAIN investments have 3–6 month deployment timelines and do not require capital approval at board level, while BODY investments take 2–5 years and require €100M+ commitments.

---

## ADIDAS BODY

### What Constitutes the adidas Body

| Body Component | Description | Scale / Key Facts |
|---|---|---|
| Manufacturing network | 100% outsourced to supplier partners | 124 supplier partners; 283 factories; 92% Asia (Vietnam 27%, Indonesia 19%, China 16%) [FACT] |
| Distribution centers (owned) | Owned and operated fulfillment hubs | 21 owned DCs globally; includes Wilkes-Barre PA (843K sq ft), Spartanburg SC (258 acres), Manchester UK (350K sq ft) [FACT] |
| Distribution centers (3PL-managed) | Third-party-operated warehousing | 39 3PL-managed DCs; includes Mantova Italy (130K sqm, Kuehne+Nagel), Suzhou China (139K sqm, Geek+ AMR), Brazil Extrema (40K sqm, DHL) [FACT] |
| Own retail stores | Concept stores and factory outlets | 1,933 stores: 838 concept + 1,095 factory outlets [FACT] |
| Physical DC automation | Installed robots, ASRS, conveyors | Mantova: 700+ robots; Suzhou: Geek+ AMR fleet; Manchester: Dematic ASRS + GTP; Wilkes-Barre: Interlake Mecalux racking; Spartanburg: Honeywell Intelligrated [FACT] |
| Transportation network | Carrier relationships and logistics lanes | Ocean (primary), air (expedited), trucking (wholesale/DC transfers); project44 adopted Feb 2026 for visibility [FACT] |
| Store RFID infrastructure | Physical RFID tag readers and tag inventory | >99% RFID accuracy at own stores; 1,300+ stores with GK OmniPOS deployed [FACT] |

### Body Assessment: Partially Right-Sized, Under Active Redesign

**Stable (not changing in near term):**
- Factory partner network (geographical shift takes 12–24 months minimum per category)
- Major owned DC locations (Wilkes-Barre, Spartanburg, Manchester — long-term leases or owned assets)
- Mantova Italy mega-DC (€350M investment, recently completed — no near-term change expected)

**Actively changing (in motion now):**
- Sourcing geography: China-to-US sourcing eliminated in 2025 [FACT]; further shifts in response to tariff headwind [INFERENCE]
- Transportation visibility layer: project44 adopted February 2026 [FACT] — not a physical change but a Body/Brain boundary investment
- TRANS4RM supply chain modules: rolling out across the network 2025–2027 [FACT]
- Store network optimization: concept store vs. outlet mix being managed, but no confirmed major store closure program [INFERENCE]

**Suboptimal (Body limitation constraining performance):**
- Western US: no major owned DC equivalent to Wilkes-Barre for the Eastern US — creates 5–7 day delivery times to California and Pacific Northwest [INFERENCE]
- 39 3PL-managed sites: varying automation levels; not uniformly equipped with AI-ready WMS or real-time inventory visibility [INFERENCE]
- No confirmed urban micro-fulfillment centers or dark stores in any market [FACT by absence of public disclosure]
- Ship-from-store physical capability exists (RFID + GK OmniPOS at 1,933 stores) but is not confirmed to be activated at scale as a fulfillment mode [ASSUMPTION]

---

## ADIDAS BRAIN

### What Constitutes the adidas Brain

| Brain Component | Current State | Maturity (1–5) | Rationale |
|---|---|---|---|
| Demand planning (o9 Solutions) | In-season retail planning, allocation, DTC demand sensing confirmed in production | 4 | Confirmed deployment; cutting-edge platform; integration gaps with real-time store sell-through suspected [FACT on platform; ASSUMPTION on gaps] |
| Seasonal ML forecasting (SageMaker) | Confirmed in production for seasonal forecasting | 3 | Good platform; unclear how deeply integrated with store-level signals or lifestyle trend data [FACT on platform; ASSUMPTION on integration depth] |
| Databricks AI platform | Agent Digital Twin in production (confirmed Databricks Data+AI Summit 2026); MosaicML GenAI processing 2M+ reviews/year at 91.67% cost reduction | 5 | Most mature AI platform in the company; multi-agent governance fleet confirmed operational [FACT] |
| ERP / master data (SAP S/4HANA) | Finance + Purchasing live 2023–2024; Supply Chain + Sales modules 2025–2027 | 3 | Progressing but not complete; supply chain master data quality varies by module completion [FACT on timeline; INFERENCE on data quality] |
| Transportation visibility (project44) | Adopted February 2026; track-and-trace layer being established | 2 | Infrastructure deployed; AI scenario planning not confirmed activated; integration with DC scheduling not confirmed [FACT on adoption; ASSUMPTION on activation] |
| WMS / DC intelligence (Manhattan Associates) | Slotting Optimisation + Labour Management confirmed at Wilkes-Barre and Manchester | 4 | Best-in-class WMS with AI capabilities; deployed at flagship DCs; coverage across 39 3PL sites unknown [FACT on deployment; INFERENCE on 3PL coverage] |
| Store intelligence (GK OmniPOS + RFID) | 1,300+ stores with GK OmniPOS; RFID >99% accuracy | 4 | Excellent store data foundation; integration to central order management for ship-from-store routing not confirmed [FACT on deployment; ASSUMPTION on routing integration] |
| Procurement intelligence (Coupa + SAP BTP) | Coupa deployed for AP automation (Latin America confirmed); SAP BTP PO amendments (3,000+ external users) | 3 | Solid foundation; AI spend analytics and supplier risk scoring not confirmed [FACT on platforms; ASSUMPTION on AI augmentation] |
| Developer AI (GitHub Copilot) | 85% adoption across ~700 engineers; 20–25% productivity improvement confirmed | 5 | Highest adoption and confirmed impact of any AI tool at adidas [FACT] |
| HR AI (SkillSenseAI + SuccessFactors) | Deloitte SkillSenseAI deployed for job architecture | 3 | Deployed for skills mapping; connection to mobility and attrition prediction not confirmed [FACT on deployment; ASSUMPTION on scope] |
| Customer data / adiClub | Millions of members; 3× conversion rate vs. non-members confirmed | 3 | Strong loyalty data asset; whether unified customer data platform exists across adidas.com + stores + app is not confirmed [FACT on conversion; ASSUMPTION on CDP maturity] |
| Marketing AI (Amazon Bedrock + MosaicML) | GenAI content pipeline operational; Amazon Bedrock in use; 75-year AI Archive available | 4 | Infrastructure mature for content; closed-loop attribution and dynamic budget allocation not confirmed [FACT on platforms; ASSUMPTION on attribution capability] |
| Finance AI (S/4HANA Central Finance + Coupa) | Central Finance live November 2023; Coupa spend management active | 3 | Financial data foundation is strong; FP&A scenario modeling and AI-driven variance analysis not confirmed [FACT on platforms; ASSUMPTION on AI augmentation] |

### Brain Assessment: Intermediate and Unevenly Deployed

**Brain Strengths:**
- Databricks multi-agent infrastructure is world-class and already in production at scale [FACT]
- GitHub Copilot deployment is best-in-class by any industry standard (85% adoption, confirmed productivity gain) [FACT]
- Store data layer (RFID + GK OmniPOS) is exceptionally rich for a retailer of this size and complexity [FACT]
- o9 Solutions is a cutting-edge demand sensing platform [FACT]
- MosaicML GenAI at 91.67% cost reduction demonstrates genuine AI capability, not just vendor talk [FACT]

**Brain Weaknesses:**
- TRANS4RM is only partially complete — Supply Chain and Sales modules not live until 2025–2027, limiting master data quality for many AI use cases [FACT]
- No confirmed central ship-from-store routing engine connecting stores + DCs + carriers [ASSUMPTION]
- project44 just adopted (February 2026); AI scenario planning layer not yet confirmed active [FACT/ASSUMPTION]
- No CTO or CDO at Executive Board — technology decisions filtered through a P&L lens by a CFO, which creates approval barriers for investments whose returns are distributed over 18–24 months [FACT]
- 39 3PL-managed DCs represent a Brain shadow: adidas may have limited visibility into and control over the intelligence layer at these sites [INFERENCE]
- No confirmed unified customer data platform connecting adidas.com, stores (RFID), and adiClub into a single view [ASSUMPTION]

---

## VELOCITY BOTTLENECK CLASSIFICATION

| SC Area | Speed Constraint Description | Bottleneck Type | AI-Addressable? | Timeline |
|---|---|---|---|---|
| SC-1: Procurement & Tariff | Tariff response weeks; OTIF signals lag shipment; PO amendment cycle 2–5 days | BRAIN — no continuous intelligence layer on trade policy or supplier risk | Yes — tariff intelligence agent on Databricks; supplier risk scoring | 3–6 months |
| SC-2: Demand & Supply Planning | Demand sensing 2–4 week lag; monthly S&OP cycles; SKU-level forecast accuracy low | BRAIN — data exists but closed-loop AI from signal to allocation not operational | Yes — social signal sensing + AI allocation optimizer + Databricks Agent Digital Twin | 3–6 months |
| SC-3: Warehousing & Ship-from-Store | 2hr order-to-pack at flagship DCs (good); ship-from-store dormant at scale; 3PL DC efficiency variable | BODY + BRAIN — DC locations fixed; ship-from-store orchestration engine missing | Partially — BRAIN build can activate BODY assets (stores); 3PL efficiency requires data cooperation | 3–12 months |
| SC-4: Inbound Transportation | Exception detection days (pre-project44); ETA accuracy ~60–70%; air/ocean decision reactive | BRAIN — project44 data layer now exists; scenario planning AI not activated | Yes — project44 AI scenario planning activation + air/ocean mode switch model | 60–90 days |
| SC-5: Outbound / Last Mile | 3–7 day standard US; no dynamic carrier routing; delivery promise is a static range | BODY + BRAIN — DC locations constrain western US speed; carrier routing and predictive promise are BRAIN | Partially — carrier optimization and predictive promise are pure BRAIN; western US gap requires ship-from-store (BRAIN activating BODY) | 2–12 months |
| SC-6: Transport Planning & Control Tower | Exception management reactive; inter-DC rebalancing weekly; transportation cost visibility fragmented | BRAIN — project44 infrastructure now in place; AI control tower layer not built | Yes — AI control tower on project44; inter-DC rebalancing model | 3–6 months |
| SC-7: Freight Bill Audit | Manual audit with low coverage; overcharge detection ~30–40%; recovery slow | BRAIN — process intelligence gap; no AI-native FBAP platform confirmed | Yes — deploy FBAP AI platform (Cass, PowerFreight, or Coupa Freight Audit module) | 2–3 months |
| SC-8: Returns & Reverse Logistics | Returns processing 3–7 days; condition assessment manual; size/fit returns preventable but not AI-addressed | BRAIN — CV triage, NLP return reason analysis, size/fit AI all deployable on existing infrastructure | Yes — CV returns triage + size/fit AI + MosaicML return reason NLP | 6–9 months |

---

## BODY vs. BRAIN DECISION MAP

The following table classifies ~20 specific initiatives as BODY or BRAIN with rationale.

| Initiative | Classification | Rationale |
|---|---|---|
| Build a new western US DC for faster Pacific Coast delivery | BODY | Requires facility lease/build, capital commitment, equipment installation, staff hiring. 3–5 year timeline. Not consulting scope. |
| Activate ship-from-store AI routing engine | BRAIN | Uses existing stores (BODY); the routing engine, carrier API integrations, and workflow changes are pure BRAIN. 6–12 months. |
| Install Geek+ AMR robots at additional DCs | BODY | Physical automation equipment installation. Capital-intensive. 12–24 months per site. |
| Deploy AI slotting optimization at 3PL DCs via API | BRAIN | Software configuration on top of existing WMS. No physical change required. 3–6 months (subject to 3PL cooperation). |
| Open urban micro-fulfillment centers / dark stores | BODY | Requires lease, equipment, staff. Capital-intensive. Not confirmed and not recommended without BRAIN layer first. |
| Build predictive delivery promise engine at checkout | BRAIN | ML model on top of existing carrier + DC + order data. No physical change. 2–3 months. |
| Activate project44 AI scenario planning module | BRAIN | Software configuration and integration. project44 infrastructure already deployed. 60–90 days. |
| Move sourcing from Vietnam to alternative countries | BODY | Physical factory relationships, quality certification, lead time restructuring. 12–24 months minimum. |
| Deploy tariff intelligence agent on Databricks | BRAIN | ML model + data feeds on existing Databricks infrastructure. No physical change. 3–6 months. |
| Extend Manhattan WMS Slotting Optimisation to 3PL sites | BRAIN | API integration or configuration export. Subject to 3PL data access agreements. 3–6 months. |
| Build social signal demand sensing pipeline | BRAIN | Data pipeline + ML model on existing Databricks/MosaicML/o9 stack. No physical change. 3–4 months. |
| Add conveyor automation to Extrema Brazil DC | BODY | Physical equipment. Capital-intensive. Multi-year. |
| Deploy AI allocation optimizer (DTC vs. wholesale) | BRAIN | ML model operating on existing o9/Databricks stack. No physical change. 4–6 months. |
| Implement size/fit AI at adidas.com checkout | BRAIN | ML model trained on purchase + return data. API integration to product pages. No physical change. 4–6 months. |
| Deploy computer vision returns triage at DCs | BRAIN + minor BODY | CV cameras at DC receiving docks (minor physical equipment) + ML model. Primarily BRAIN. 6–9 months. |
| Deploy freight bill audit AI (FBAP platform) | BRAIN | SaaS platform configuration. Invoice data integration. No physical change. 2–3 months. |
| Build AI control tower on project44 | BRAIN | Software layer on existing project44 platform. 3–6 months. |
| Expand Mantova DC physical capacity | BODY | Physical expansion of a 130K sqm facility. Capital-intensive. Not near-term. |
| Connect RFID store data to central order management in real-time | BRAIN | Data pipeline and API integration. No physical change to RFID infrastructure. 2–4 months. |
| Deploy predictive attrition model for TRANS4RM staff | BRAIN | ML model on SuccessFactors + SkillSenseAI data. No physical change. 6–9 months. |

---

## THE CRITICAL FINDING: The Ship-from-Store Body-Brain Gap

### The Evidence
- adidas operates **1,933 own stores** with **838 concept locations** and **1,095 factory outlets**. [FACT]
- **RFID inventory accuracy is >99%** across own stores. [FACT]
- **GK OmniPOS is deployed at 1,300+ stores** with ship-from-store capability confirmed. [FACT]
- **LS Retail POS at 1,350 stores** provides an additional digital inventory layer. [FACT]
- **Ship-from-store technology is confirmed** — the capability exists at the store level. [FACT]
- **Scale of active ship-from-store fulfillment is not publicly quantified.** [INFERENCE: likely minimal at this stage]
- **No central AI routing engine** connecting DTC orders to optimal DC + store + carrier combinations is confirmed to exist. [ASSUMPTION]

### The Implication
adidas has invested in the physical prerequisites of a distributed fulfillment network (stores, RFID, POS systems capable of ship-from-store) but has not built the BRAIN layer that activates this network for e-commerce fulfillment at scale. This is not a BODY gap — the BODY is in place. It is a BRAIN gap: the intelligence layer that should connect an incoming adidas.com order with the optimal fulfillment point (nearest store with inventory, carrier option, store labor capacity) does not appear to exist in production at meaningful scale.

The competitive consequence: adidas delivers in 3–7 days standard to US customers while Amazon delivers in 1–2 days. [FACT] Nike, Zara, and other omnichannel leaders use ship-from-store to match Amazon's speed in major cities without matching Amazon's DC density. [INFERENCE] adidas has the physical network to do the same — but not the BRAIN to activate it.

### Brain Investment Required
1. Central order routing engine that evaluates DC + store inventory in real time against order destination and carrier options
2. Real-time RFID-to-OMS data feed (from batch to near-real-time or continuous)
3. Store labor capacity signaling (how many ship-from-store orders can each store process per hour given current store traffic)
4. Last-mile carrier API integration at store level (same-day courier or next-day parcel from store address)
5. Store associate workflow management (pick list generation, packing station configuration, carrier label printing at store)

None of these require new BODY investment. All are pure BRAIN builds on existing infrastructure.

---

## DIAGNOSIS: adidas is a Brain-First Opportunity with a Specific Velocity Unlock

### Why Brain-First is Right for adidas

1. **The BODY is largely fixed.** 283 factories are not moving. 60 DCs are not being restructured. 1,933 stores are not being relocated. Consulting scope should not be redesigning the Body — it should be making the Brain smarter within the existing Body constraints. [FACT on Body scale; INFERENCE on consulting scope]

2. **The data infrastructure is partially mature.** Databricks Agent Digital Twin is in production. MosaicML processes 2M+ reviews. RFID is at >99% accuracy. o9 is live for demand sensing. GitHub Copilot is at 85% adoption. The raw material for Brain AI is largely in place — what is missing is integration and closed-loop activation. [FACT on all platforms]

3. **TRANS4RM will complete the foundation.** The S/4HANA supply chain and sales modules going live in 2025–2027 will provide the master data quality that many AI initiatives need. Brain-first initiatives should prioritize those that can run independently of TRANS4RM now, and position to leverage TRANS4RM completion in 2027. [FACT on TRANS4RM timeline]

4. **The CFO is the buyer, and the CFO owns both Technology and Supply Chain.** Brain investments have faster ROI cycles (3–12 months) than Body investments (3–5 years). This directly aligns with Ohlmeyer's P&L accountability and 2028 EBIT target. [FACT on CFO role]

5. **The velocity unlock (ship-from-store) is a pure Brain investment.** The most important near-term competitive move — enabling 1-day delivery in major markets to close the Amazon speed gap — requires no new stores, no new DCs, no new robots. It requires building the routing engine, real-time data feeds, and carrier APIs that activate an existing BODY asset. [INFERENCE on solution architecture]

---

## SEQUENCING RECOMMENDATION

### Speed 1 — Brain Initiatives Available Today (No TRANS4RM Dependency)

These initiatives can begin immediately on existing infrastructure.

| Initiative | Brain Area | Feasibility | Time to Value | Velocity Impact |
|---|---|---|---|---|
| FIFA World Cup 2026 content AI (MosaicML/Databricks) | Marketing AI | HIGH — infrastructure live | 2–4 months | Indirect — brand activation speed |
| Tariff intelligence agent (Databricks) | Procurement AI | HIGH — infrastructure live | 3–6 months | HIGH — tariff response from weeks to days |
| project44 AI scenario planning activation | Transportation AI | HIGH — infrastructure live | 60–90 days | HIGH — exception detection from days to hours |
| Social signal demand sensing (Databricks + o9) | Planning AI | MEDIUM-HIGH — requires integration | 3–6 months | HIGH — demand sensing from weeks to 24–48 hours |
| Dynamic carrier rate optimization | Logistics AI | HIGH — SaaS platforms available | 2–3 months | MEDIUM — delivery speed and cost |
| Freight bill audit AI deployment | Finance AI | HIGH — SaaS platforms available | 2–3 months | LOW (operational) |
| Return reason NLP (MosaicML) | Returns AI | HIGH — infrastructure live | 3–4 months | MEDIUM — product quality feedback |
| GitHub Copilot TRANS4RM focus | Engineering AI | HIGH — already deployed | Already delivering | MEDIUM — indirect via TRANS4RM acceleration |

### Speed 2 — Brain Initiatives Requiring TRANS4RM Progress (2026–2027)

These initiatives need Supply Chain or Sales module data from TRANS4RM to reach full effectiveness.

| Initiative | Brain Area | TRANS4RM Dependency | Time to Value | Velocity Impact |
|---|---|---|---|---|
| Ship-from-store AI orchestration engine | Fulfillment AI | Partial — needs S/4HANA inventory integration | 6–12 months | VERY HIGH — 1-day delivery in top 30 US metros |
| AI allocation optimizer (DTC vs. wholesale) | Planning AI | Moderate — needs S/4HANA sales order data | 6–9 months | HIGH — full-price sell-through improvement |
| adiClub personalization ML | Commerce AI | Low — adiClub data is outside S/4HANA | 6–9 months | MEDIUM — DTC conversion lift |
| AI control tower on project44 | Logistics AI | Moderate — needs inventory + order data from S/4HANA | 6–12 months | MEDIUM-HIGH — end-to-end visibility |
| Supplier risk scoring model | Procurement AI | Low — can run on Databricks + external data | 4–6 months | HIGH — OTIF signal improvement |
| Predictive delivery promise engine | Commerce AI | Low — uses carrier data + DC inventory | 3–6 months | HIGH — checkout conversion improvement |

### Body Actions That Must Run in Parallel (Not Consulting Scope)

| Initiative | Owner | Timeline | Consulting Role |
|---|---|---|---|
| TRANS4RM Supply Chain module rollout | Internal IT + SAP | 2025–2027 [FACT] | Ensure AI initiatives are designed to integrate with TRANS4RM on completion |
| Sourcing diversification (tariff response) | Procurement + sourcing team | 12–24 months [INFERENCE] | Provide tariff intelligence agent to guide decisions |
| 3PL contract renegotiation for data access | Supply chain + procurement | Ongoing | Identify data-sharing clauses needed to enable AI at 3PL sites |
| Western US DC capacity assessment | Supply chain + real estate | 12–24 months [ASSUMPTION] | Context: ship-from-store may reduce urgency of new DC in the near term |

---

## BODY vs. BRAIN SCORE FOR ADIDAS

| Category | Score (1–5) | Assessment |
|---|---|---|
| Body: Manufacturing Network | 3 | Right-sized for current scale; geographically concentrated risk; tariff-driven shifts in motion [FACT/INFERENCE] |
| Body: Distribution Network | 3 | Flagship DCs are best-in-class; 39 3PL sites are variable; no western US flagship creates delivery speed gap [FACT/INFERENCE] |
| Body: Store Network | 4 | 1,933 stores with RFID and modern POS — excellent physical fulfillment infrastructure, dormant for e-commerce [FACT] |
| Body: Physical Automation | 4 | Mantova (700+ robots), Suzhou (Geek+ AMR), Manchester (Dematic ASRS) — highly automated flagship DCs [FACT] |
| Brain: Demand Planning | 4 | o9 + SageMaker + Databricks Agent Digital Twin — strong stack; integration gaps suspected [FACT/ASSUMPTION] |
| Brain: Transportation AI | 2 | project44 just adopted; AI scenario planning not yet activated; control tower embryonic [FACT/ASSUMPTION] |
| Brain: Store Intelligence | 4 | RFID + GK OmniPOS are best-in-class; ship-from-store routing engine missing [FACT/ASSUMPTION] |
| Brain: Developer AI | 5 | GitHub Copilot at 85% adoption — best-in-class [FACT] |
| Brain: Marketing AI | 4 | MosaicML + Databricks + Amazon Bedrock — mature infrastructure; closed-loop attribution not confirmed [FACT/ASSUMPTION] |
| Brain: ERP / Master Data | 3 | S/4HANA Finance live; Supply Chain + Sales mid-flight; data quality variable [FACT] |
| Brain: Procurement AI | 2 | Coupa + SAP BTP deployed; AI augmentation (tariff intelligence, supplier risk) not confirmed [FACT/ASSUMPTION] |
| **Overall Brain Maturity** | **3.3 / 5** | Intermediate: strongest in developer AI, marketing AI, and demand planning; weakest in transportation AI, procurement AI, and ERP master data |
| **Overall Body Adequacy** | **3.5 / 5** | Partially right-sized: flagship DCs and store network are excellent; 3PL coverage and western US DC gap are limitations |

---

## NET DIAGNOSIS

**adidas is a Brain-First, Brain-Partial opportunity.** The Body is largely fixed, functional, and in some dimensions (Mantova mega-DC, Suzhou AMR fleet, 1,933-store RFID network) genuinely world-class. The Brain is partially deployed and unevenly mature — strongest in developer tooling and marketing AI, weakest in transportation and procurement AI, and constrained by an incomplete TRANS4RM program that limits master data quality in supply chain and sales domains.

The critical finding is that adidas's most important velocity opportunity — enabling 1-day delivery in major markets via ship-from-store — requires zero Body investment. It requires building the Brain routing engine that connects an existing store network (BODY: 1,933 stores, RFID at >99% accuracy, GK OmniPOS) to incoming DTC orders. This is a 6–12 month BRAIN build that, if executed before or during the FIFA World Cup 2026 North America commercial window, would materially shift adidas's competitive position in e-commerce fulfillment speed without a single new distribution center or store.

The consulting opportunity is clear: help adidas close the BRAIN gaps that are leaving existing BODY assets underutilized, and do so in the sequence that delivers the fastest P&L impact within Ohlmeyer's 2028 EBIT margin target framework.
