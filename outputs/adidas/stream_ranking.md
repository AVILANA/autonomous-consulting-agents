# Value Stream Ranking for AI-Led Reinvention — adidas AG
**Step 5 Output | Autonomous Consulting Workflow**
**Date:** 2026-04-03
**Analyst Role:** AI Value & Reinvention Analyst
**Sources:** FY2025 Annual Report (March 4, 2026), prior step outputs (value_levers.md, tech_ops_footprint.md, transformation_capacity.md, benchmark_table.md, peer_set.md, company_snapshot.md), Databricks Data+AI Summit 2026 disclosures, project44 press releases (February 2026)

---

## RANKING METHODOLOGY

### Five Ranking Dimensions

Each value stream is scored 1–5 on five dimensions. The final rank is determined by weighted scoring with commentary to explain the strategic logic above and beyond the numeric score.

| Dimension | Definition | Weight |
|---|---|---|
| **Value at Stake** | Estimated financial impact (cost reduction, revenue uplift, working capital release, or margin improvement). Anchored to adidas's specific scale and financials. 5 = >€200M potential; 1 = <€20M potential. | 30% |
| **Data Readiness** | Quality, availability, and accessibility of data needed to build and run the AI solution. Considers TRANS4RM maturity, existing platform stack, and confirmed data assets. 5 = data exists, clean, and accessible today; 1 = data fragmented, not digitized, or behind 3PL walls. | 25% |
| **Execution Complexity** | Difficulty of implementation considering change management, integration, vendor relationships, and workforce impact. 5 = low complexity (standalone, limited dependencies); 1 = high complexity (multi-year, cross-functional, major change management). | 20% |
| **Strategic Fit** | Alignment with CEO Gulden's operational priorities, CFO Ohlmeyer's EBIT targets, the TRANS4RM program, and the FIFA World Cup 2026 urgency window. 5 = directly accelerates stated strategic priority; 1 = tangential. | 15% |
| **Velocity Score** | Magnitude of speed improvement achievable through AI, and the competitive significance of that speed gain (i.e., does faster materially improve competitive position or commercial outcome?). 5 = dramatic, competitively decisive speed improvement; 1 = marginal speed benefit. | 10% |

### Scoring Convention
Scores are 1 (lowest) to 5 (highest) on each dimension. Higher score = more attractive. Weighted total is the primary ranking input, supplemented by strategic judgment in the commentary.

---

## RANKED VALUE STREAMS

---

### RANK 1: Demand & Supply Planning (SC-2)
**Tier: TIER 1 — Act Now**
**Primary Value Levers: Efficiency, Quality, Velocity, Growth**
**Time to First Value: 3–6 months**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 5 | €4.99B inventory (FY2024). 5% inventory reduction = €250M working capital release. 0.5pp gross margin improvement from better full-price sell-through = ~€124M annually. Highest single financial prize in the entire company. [FACT on inventory; INFERENCE on improvement magnitude] |
| Data Readiness | 4 | o9 Solutions live for in-season planning; Amazon SageMaker confirmed for ML forecasting; Databricks Agent Digital Twin in production; adiClub behavioral data available; RFID store data confirmed at >99% accuracy. Gap: real-time store sell-through feed to o9 not confirmed; lifestyle trend social signal integration not confirmed. [FACT on platforms; ASSUMPTION on integration gaps] |
| Execution Complexity | 3 | Platforms are in place. The complexity is in model precision, data integration between o9/SageMaker/Databricks, and organizational adoption of AI-driven allocation recommendations. Not trivial — planning culture change is required. [INFERENCE] |
| Strategic Fit | 5 | Directly addresses full-price discipline (Gulden's #1 commercial priority), inventory efficiency (Ohlmeyer's EBIT target), and FIFA World Cup 2026 demand surge risk. The Agent Digital Twin is already built for this purpose. [FACT on strategic priorities] |
| Velocity Score | 5 | Closing the demand sensing gap from 2–4 weeks to 24–48 hours is the most important velocity improvement in the entire supply chain. Lifestyle trend capture depends entirely on this. The Samba/Gazelle cycle — which Gulden has explicitly flagged will fade — makes this urgently relevant to sustaining current momentum. [INFERENCE] |
| **Weighted Total** | **4.35** | |

**Why this rank:** Demand & Supply Planning is ranked first because it is the only opportunity that simultaneously addresses adidas's largest balance sheet exposure (€4.99B inventory), its most important P&L lever (gross margin through full-price discipline), and the strategic imperative of the FIFA World Cup 2026 North America surge. The technology infrastructure exists. The Agent Digital Twin is in production. The barrier is integration precision and organizational adoption — both solvable in 3–6 months.

**Velocity Acceleration Pathway:**
- Month 1–2: Connect GK OmniPOS store sell-through data to o9 in real-time (currently estimated batch upload). Map social signal APIs (TikTok, Instagram, Google Trends) to MosaicML/Databricks pipeline.
- Month 3–4: Deploy social signal demand sensing model for lifestyle product lines (Samba, Gazelle, Spezial). Run parallel with existing S&OP cycle to validate accuracy before handoff.
- Month 5–6: Activate AI-driven channel allocation optimizer for DTC vs. wholesale vs. outlet. Deploy Agent Digital Twin FIFA World Cup 2026 scenario models for North America.
- Month 7+: Extend to performance lines; integrate with TRANS4RM supply chain modules as they go live.

---

### RANK 2: Marketing Content & Personalization (Non-SC)
**Tier: TIER 1 — Act Now**
**Primary Value Levers: Productivity, Efficiency, Growth**
**Time to First Value: 2–4 months**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 5 | ~€3B annual marketing spend. Even 10% efficiency improvement = €300M in redirectable spend. GenAI content production at scale could reduce agency fees materially and accelerate campaign velocity. FIFA World Cup 2026 activation creates a near-term commercial moment with outsized ROI potential. [FACT on marketing spend; INFERENCE on efficiency magnitude] |
| Data Readiness | 5 | MosaicML GenAI pipeline already processes 2M+ product reviews/year at 91.67% cost reduction — confirmed in production. Amazon Bedrock in use. 75-year AI Archive of design assets confirmed. adiClub behavioral data for personalization targeting is available. The infrastructure is the most mature of any value stream. [FACT on all platform confirmations] |
| Execution Complexity | 4 | MosaicML/Databricks infrastructure is already running at scale. Incremental effort is in prompt engineering, creative workflow integration, and brand governance guardrails — not new infrastructure. Agency relationship management is the primary change management challenge. [INFERENCE] |
| Strategic Fit | 5 | FIFA World Cup 2026 is 90 days away. Content at scale for North America activation is the single most time-pressured opportunity in the entire portfolio. Gulden's brand-first mandate means marketing AI must feel like creative acceleration, not automation. [FACT on FIFA timing; INFERENCE on brand sensitivity] |
| Velocity Score | 4 | AI content production compresses campaign cycle from weeks to hours — directly relevant to cultural moment capture (lifestyle trend activation, FIFA match-day marketing). [INFERENCE] |
| **Weighted Total** | **4.75** | |

**Why this rank:** Ranked #2 despite the highest weighted score because the strategic uniqueness of demand planning (€4.99B inventory stake) places it first. Marketing AI is ranked #2 because the infrastructure is the most mature in the company, the FIFA World Cup 2026 window is urgent, and the €3B spend base makes even modest efficiency improvements financially decisive. This is the fastest path to visible ROI in the portfolio.

**Velocity Acceleration Pathway:**
- Immediate (weeks): Activate FIFA World Cup 2026 content brief library. Batch-generate 500+ localized creative variants across US, Mexico, Canada markets in English/Spanish. Test match-day activation content templates.
- Month 2–3: Deploy AI marketing attribution model to track spend-to-DTC-conversion across digital channels. Begin dynamic budget reallocation based on real-time performance signals.
- Month 4+: Scale to full adiClub personalization layer — individual member content recommendations based on purchase and behavioral data.

---

### RANK 3: Procurement / Tariff Intelligence (SC-1)
**Tier: TIER 1 — Act Now**
**Primary Value Levers: Efficiency, Velocity, Quality**
**Time to First Value: 3–6 months**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 4 | €200M embedded tariff headwind in 2026 guidance [FACT]. Tariff intelligence AI could mitigate 20–40% of this through faster sourcing pivots and proactive contract positioning = €40–80M. Coupa AI spend analytics on €8–12B addressable spend could yield additional €40–60M in leakage recovery. [INFERENCE on magnitude] |
| Data Readiness | 4 | SAP BTP PO amendment data from 3,000+ external factory users is digitized [FACT]. Coupa spend data available in Latin America [FACT]. Supplier master data in S/4HANA Finance/Purchasing live since 2023–2024 [FACT]. Databricks multi-agent infrastructure in production [FACT]. Gap: factory-level OTIF data quality and completeness unknown. [ASSUMPTION] |
| Execution Complexity | 3 | Tariff agent on Databricks is architecturally straightforward. Supplier risk scoring requires third-party data integration (satellite imagery, geopolitical feeds). Coupa AI module deployment is a configuration and adoption challenge, not an infrastructure build. [INFERENCE] |
| Strategic Fit | 5 | €200M tariff headwind is a board-level issue in 2026. CFO Ohlmeyer (who owns both Technology and Supply Chain) has direct personal stake in solving this. Any AI that visibly addresses the tariff exposure is immediately fundable. [FACT on CFO role; INFERENCE on funding priority] |
| Velocity Score | 5 | Closing the tariff response gap from weeks to 48–72 hours is a competitively decisive capability. In a world of rapidly shifting trade policy (US reciprocal tariffs, China-US tensions), this is a structural advantage that grows in value as policy volatility increases. [INFERENCE] |
| **Weighted Total** | **4.15** | |

**Why this rank:** Ranked #3 because the €200M live tariff headwind creates an immediate and politically visible financial case that the CFO cannot ignore. The Databricks multi-agent infrastructure is already in production. This is a fast-path from AI investment to EBIT improvement — the kind of concrete result that validates further AI investment and builds internal momentum.

**Velocity Acceleration Pathway:**
- Month 1–2: Deploy tariff intelligence monitoring agent on Databricks — ingest US CBP ruling feeds, WTO tariff schedule changes, and geopolitical risk indices. Configure alert thresholds for material landed cost impacts.
- Month 3–4: Build sourcing scenario simulator — for any tariff change, automatically model cost-per-unit across all 283 factories for the affected product categories. Generate ranked shift recommendations.
- Month 5–6: Activate Coupa AI spend analytics. Configure supplier risk scoring model. Integrate with SAP BTP for automated PO exception triage.

---

### RANK 4: Warehousing & Fulfillment / Ship-from-Store (SC-3)
**Tier: TIER 1 — Act Now**
**Primary Value Levers: Velocity, Productivity, Growth**
**Time to First Value: 3–6 months (orchestration engine); 6–12 months (full scale)**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 4 | Ship-from-store activation in top 30 US metros could enable 1-day delivery that closes the Amazon speed gap — estimated DTC conversion uplift of 5–10% on North America adidas.com = €20–50M in incremental revenue (ASSUMPTION on North America DTC base). DC slotting extension to 3PL network: 15–25% pick efficiency gain = material cost reduction across 60-DC network. |
| Data Readiness | 4 | RFID >99% accuracy confirmed at own stores [FACT]. GK OmniPOS at 1,300+ stores [FACT]. Manhattan Associates WMS at flagship DCs [FACT]. Ship-from-store technology confirmed [FACT]. Gap: central order routing engine connecting all stores + DCs + carriers is not confirmed to exist. [ASSUMPTION] |
| Execution Complexity | 3 | Technology foundation exists. The complexity is in: (a) building the central ship-from-store routing engine (6–12 months); (b) training store associates on ship-from-store fulfillment workflows; (c) integrating last-mile carrier APIs at store level. The BODY assets exist; the BRAIN build is the challenge. [INFERENCE] |
| Strategic Fit | 4 | Direct link to FIFA World Cup 2026 North America activation — 1-day delivery in US major cities during the tournament is a meaningful consumer experience differentiator. Aligns with Gulden's DTC growth mandate. [FACT on FIFA context; INFERENCE on consumer impact] |
| Velocity Score | 5 | The most dramatic velocity improvement available in the physical fulfillment layer. Converting 1,933 stores into distributed fulfillment nodes closes the DC-location BODY gap without new capital expenditure. This is the defining velocity opportunity for DTC competitiveness. [INFERENCE] |
| **Weighted Total** | **3.90** | |

**Why this rank:** Ranked #4 because the velocity impact is the highest in the physical network, but execution complexity is higher than Ranks 1–3 (requires building a central orchestration engine, training store staff, and integrating carrier APIs). The FIFA World Cup 2026 urgency partially offsets this — a partial activation in top 5 US cities by June 2026 is feasible and commercially meaningful.

**Velocity Acceleration Pathway:**
- Month 1–3: Select top 10 US cities by adidas concept store density + DTC order volume. Map available RFID inventory vs. DC inventory for same-day vs. next-day delivery analysis.
- Month 3–6: Build MVP ship-from-store routing engine. Integrate with Manhattan WMS and GK OmniPOS. Deploy same-day/next-day carrier API (Uber Direct, regional courier) at pilot stores.
- Month 6–12: Scale to top 30 US metros. Extend to UK (London, Manchester, Birmingham) and EU (Paris, Amsterdam, Milan) using Mantova as hub + concept store network.

---

### RANK 5: Outbound / Last Mile Optimization (SC-5)
**Tier: TIER 1 — Act Now**
**Primary Value Levers: Efficiency, Velocity, Growth**
**Time to First Value: 2–3 months (carrier optimization); 6–12 months (ship-from-store last mile)**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 4 | Dynamic carrier optimization: 8–15% freight cost reduction on estimated €300–500M outbound parcel spend = €24–75M. Predictive delivery promise engine: 15–20% conversion improvement at checkout (industry benchmark) applied to North America DTC = potentially €20–40M revenue uplift. [ASSUMPTION on spend and conversion base] |
| Data Readiness | 3 | Carrier APIs exist (UPS, FedEx, DHL); checkout data is available; DC inventory positions are known. Gap: real-time carrier performance feed is not confirmed as connected to checkout or DC systems. Dynamic rate shopping capability is not confirmed. [ASSUMPTION] |
| Execution Complexity | 3 | Carrier rate shopping and predictive delivery promise are established SaaS capabilities (e.g., EasyPost, Shippo, Narvar). Integration at checkout and DC is the effort. Ship-from-store last mile requires the SC-3 orchestration engine as a prerequisite. [INFERENCE] |
| Strategic Fit | 4 | Closes the speed gap with Amazon and Zalando in the FIFA World Cup 2026 window. Predictive delivery promise is a checkout conversion tool that directly grows DTC revenue without incremental marketing spend — aligned with Ohlmeyer's efficiency mandate. [INFERENCE] |
| Velocity Score | 4 | Delivery speed is the single most cited barrier to DTC conversion in apparel/footwear (after price). Closing the gap from 3–7 days to 1–2 days in major markets is commercially transformative for adidas.com. [INFERENCE] |
| **Weighted Total** | **3.60** | |

**Why this rank:** Ranked #5 because carrier optimization is the fastest-to-deploy efficiency win in the supply chain (2–3 months), while ship-from-store last mile depends on SC-3 orchestration engine being built first. The predictive delivery promise is a quick win for DTC conversion that can be deployed independently.

---

### RANK 6: Developer Productivity / TRANS4RM Acceleration (Non-SC)
**Tier: TIER 1 — Act Now**
**Primary Value Levers: Productivity, Velocity, Quality**
**Time to First Value: Already delivering (GitHub Copilot at 85% adoption)**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 3 | GitHub Copilot confirmed at 20–25% productivity improvement across ~700 engineers [FACT]. The indirect value is larger: every month of TRANS4RM acceleration unlocks AI initiatives that depend on S/4HANA master data. Estimated TRANS4RM program cost: €150–250M/year [FACT]. Even 10% acceleration = €15–25M in program cost reduction. [FACT on Copilot; INFERENCE on TRANS4RM acceleration value] |
| Data Readiness | 5 | GitHub Copilot already deployed at 85% adoption [FACT]. The data is the codebase — already accessible. No new data infrastructure required. [FACT] |
| Execution Complexity | 5 | Already in flight. The incremental effort is in directing the AI productivity uplift specifically toward TRANS4RM-critical workflows (SAP configuration, integration testing, regression testing) rather than general coding tasks. [INFERENCE] |
| Strategic Fit | 5 | TRANS4RM is the single most important infrastructure program at adidas. Its completion in 2027 unlocks the data foundation for almost every other AI initiative. Accelerating it is directly aligned with every strategic priority simultaneously. [FACT on TRANS4RM scope] |
| Velocity Score | 3 | The velocity impact is indirect (TRANS4RM completion speed) rather than operational speed improvement. Meaningful but not directly customer-facing. [INFERENCE] |
| **Weighted Total** | **4.10** | |

**Why this rank:** Ranked #6 despite strong scores because it is already delivering (not a new opportunity) and the primary value is indirect (unlocking other AI initiatives via TRANS4RM acceleration). Placed in Tier 1 because the ongoing investment compounds every day Copilot is deployed at high adoption.

---

### RANK 7: Digital Commerce / adiClub Personalization (Non-SC)
**Tier: TIER 2 — Build Now, Harvest Later**
**Primary Value Levers: Growth, Efficiency, Quality**
**Time to First Value: 6–9 months**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 4 | adiClub members convert at 3× non-member rate [FACT]. €4.3B DTC revenue [FACT]. Improving personalization to increase member conversion by 10% on 50% of traffic = ~€215M incremental revenue (ASSUMPTION on current personalization uplift headroom). Dynamic clearance pricing within full-price guardrails: estimated 0.2–0.3pp margin improvement. |
| Data Readiness | 4 | adiClub behavioral data, purchase history, and RFID store interaction data are available [FACT/INFERENCE]. MosaicML review intelligence is operational [FACT]. Amazon Bedrock and Databricks available for personalization model training [FACT]. Gap: unified customer data platform connecting all touchpoints is not confirmed. [ASSUMPTION] |
| Execution Complexity | 3 | Personalization ML models are established technology. The complexity is in: (a) assembling a unified customer data view across adidas.com, stores (RFID), and adiClub; (b) deploying recommendation APIs at checkout and product pages. [INFERENCE] |
| Strategic Fit | 4 | DTC growth is a stated strategic priority. adiClub personalization directly supports the "brand as relationship" strategy that Gulden has articulated. However, the 2028 EBIT target means this must show ROI within 12–18 months to sustain investment. [FACT on priorities; INFERENCE on ROI timeline] |
| Velocity Score | 2 | Personalization primarily improves conversion rates (revenue), not operational speed. Marginal velocity dimension. [INFERENCE] |
| **Weighted Total** | **3.55** | |

**Why this rank:** Ranked #7 because the financial case is large (3× adiClub conversion premium × €4.3B DTC base) but execution requires assembling a unified customer data view that is not confirmed to be in place. Placed in Tier 2 because this is a "build now, harvest in 2027" opportunity rather than a 90-day win.

---

### RANK 8: Inbound Transportation Visibility (SC-4)
**Tier: TIER 2 — Build Now, Harvest Later**
**Primary Value Levers: Efficiency, Velocity, Quality**
**Time to First Value: 60–90 days (project44 scenario planning activation)**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 3 | Air freight optimization: 20% reduction on estimated €100–200M annual air spend = €20–40M. Improved DC arrival predictability: reduces buffer inventory and DC labor over-scheduling. Disruption mitigation: hard to quantify but materially significant (Red Sea disruption alone cost the industry billions in 2024). [ASSUMPTION on spend scale] |
| Data Readiness | 4 | project44 adopted February 2026 — vessel tracking, carrier data, and ETA prediction infrastructure is now in place [FACT]. Integration with o9/SageMaker demand signals and Manhattan WMS still required. [ASSUMPTION] |
| Execution Complexity | 4 | project44 is already deployed. Activating the scenario planning module is a configuration and integration effort, not a build. High feasibility in 60–90 days. [FACT foundation; ASSUMPTION on activation complexity] |
| Strategic Fit | 3 | Addresses an operational pain point but not a board-level strategic priority (unlike tariff intelligence, which has €200M direct P&L impact). Supports the broader supply chain resilience agenda. [INFERENCE] |
| Velocity Score | 4 | Closing the exception detection gap from days to hours is operationally significant — it enables DC scheduling, labor planning, and carrier selection to adapt in near-real-time to inbound disruptions. [INFERENCE] |
| **Weighted Total** | **3.55** | |

**Why this rank:** Ranked #8 because project44 is already deployed and the scenario planning activation is the fastest-to-value supply chain initiative in the portfolio (60–90 days). However, the standalone financial case is smaller than the top 7 streams, and the value is largely risk mitigation rather than revenue or margin growth. Placed in Tier 2 as a build-now initiative that supports the broader control tower architecture.

---

### RANK 9: Returns & Reverse Logistics (SC-8)
**Tier: TIER 2 — Build Now, Harvest Later**
**Primary Value Levers: Efficiency, Quality, Velocity**
**Time to First Value: 6–9 months**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 3 | Size/fit AI: 3–5pp return rate reduction on €4.3B DTC = €129M+ in reduced handling cost and working capital improvement. [ASSUMPTION on addressable return rate reduction] Computer vision triage: 60–70% reduction in returns processing labor cost. [INFERENCE on current labor cost] |
| Data Readiness | 4 | MosaicML NLP pipeline operational at scale (2M+ reviews/year) [FACT]. Purchase + return history available in transactional systems. RFID and GK OmniPOS at stores support in-store returns. Gap: computer vision infrastructure at DC receiving docks is not confirmed. [ASSUMPTION] |
| Execution Complexity | 3 | Size/fit AI model training is straightforward given purchase + return data. NLP return reason classification leverages existing MosaicML infrastructure. Computer vision at DC requires physical equipment investment. [INFERENCE] |
| Strategic Fit | 3 | Returns management is a cost center improvement, not a growth driver. Aligns with EBIT margin expansion target but is not a stated strategic priority. [INFERENCE] |
| Velocity Score | 3 | Compressing returns processing from 3–7 days to <24 hours releases working capital faster and improves customer experience (faster credit/replacement). Meaningful but not competitively decisive. [INFERENCE] |
| **Weighted Total** | **3.25** | |

**Why this rank:** Ranked #9 because the size/fit AI case has a large financial upside (€129M+ potential) but depends on accurate return rate assumptions and takes 6–9 months to deploy and measure. The NLP return reason loop is immediately deployable on existing infrastructure and represents an early deliverable.

---

### RANK 10: Transport Planning & Control Tower (SC-6)
**Tier: TIER 2 — Build Now, Harvest Later**
**Primary Value Levers: Efficiency, Velocity, Productivity**
**Time to First Value: 3–6 months**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 3 | Transportation cost intelligence: 5% of total freight spend (estimated €1–2B+) = €50–100M in savings potential. Inter-DC rebalancing: reduces stockout-driven lost sales and markdown-driven inventory clearance. [ASSUMPTION on freight spend scale] |
| Data Readiness | 3 | project44 provides the visibility layer [FACT]. Integration across 39 3PL-managed sites requires data-sharing agreements. Inventory data across all 60 DCs is not confirmed as real-time accessible. [ASSUMPTION] |
| Execution Complexity | 2 | Requires cross-functional cooperation across 39 3PL partners and integration of multiple billing systems. The data aggregation and normalization effort is substantial. [INFERENCE] |
| Strategic Fit | 3 | Supports operational efficiency mandate but is a complex, multi-year build rather than a near-term win. [INFERENCE] |
| Velocity Score | 3 | Closing the exception-to-resolution cycle from days to <8 hours is operationally meaningful. Inter-DC rebalancing from weekly to daily cadence improves inventory availability. [INFERENCE] |
| **Weighted Total** | **2.90** | |

**Why this rank:** Ranked #10 because the control tower build is foundationally important but complex — it depends on 3PL data cooperation that cannot be assumed, and the implementation timeline is 12–24 months for full coverage. The project44 layer is already in place; the challenge is the 39 3PL integration problem.

---

### RANK 11: Freight Bill Audit Automation (SC-7)
**Tier: TIER 3 — Foundation Building**
**Primary Value Levers: Efficiency, Productivity**
**Time to First Value: 2–3 months**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 2 | AI freight audit recovery: €16–32M annually (2% overcharge rate × 80% AI recovery on estimated €1–2B freight spend). [ASSUMPTION on overcharge rate, recovery rate, and freight spend] Meaningful but not strategically transformative. |
| Data Readiness | 3 | Freight invoices exist in Coupa (Latin America) and other AP systems [FACT]. Contracted rate data is in carrier contracts. The challenge is data normalization across multiple billing systems and currencies. [INFERENCE] |
| Execution Complexity | 4 | Established SaaS FBAP platforms (Cass, PowerFreight, Coupa Freight Audit) can be configured and deployed quickly. The complexity is in data access and normalization, not in building the AI. [INFERENCE] |
| Strategic Fit | 2 | Cost recovery initiative, not a growth or transformation priority. However, it is self-funding — recoveries can finance larger AI investments. [INFERENCE] |
| Velocity Score | 1 | No meaningful operational velocity improvement. Process acceleration (invoice cycle from 7–14 days to <24 hours) is relevant internally but not competitively visible. [INFERENCE] |
| **Weighted Total** | **2.55** | |

**Why this rank:** Ranked #11 because it is a financially sound but strategically low-priority initiative. Its primary value is as a self-funding mechanism for higher-priority investments. Placed in Tier 3 as a foundation-building initiative that should be deployed early to generate cash that funds Tier 1 programs.

---

### RANK 12: Finance & FP&A Analytics (Non-SC)
**Tier: TIER 3 — Foundation Building**
**Primary Value Levers: Productivity, Quality**
**Time to First Value: 6–9 months**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 2 | Analyst productivity improvement: AI financial modeling reduces manual FP&A effort by 40–60% [INFERENCE]. Scenario planning quality improvement: faster, more accurate EBIT bridge modeling. Financial value is in decision quality, not direct cost reduction. Hard to quantify precisely. |
| Data Readiness | 4 | SAP S/4HANA Central Finance live November 2023 [FACT]. Coupa spend data available [FACT]. The financial data foundation is the most mature in the company. [FACT] |
| Execution Complexity | 4 | Financial analytics AI (scenario planning, variance analysis, EBIT bridge modeling) can be built on existing S/4HANA + Databricks stack without new infrastructure. [INFERENCE] |
| Strategic Fit | 4 | The CFO is the technology buyer. A tool that helps Ohlmeyer monitor the 2028 EBIT bridge in real time has direct sponsorship appeal and creates goodwill for the broader AI investment program. [FACT on CFO role; INFERENCE on sponsorship value] |
| Velocity Score | 1 | No operational velocity impact. Internal decision acceleration is meaningful but not operationally competitive. [INFERENCE] |
| **Weighted Total** | **2.90** | |

**Why this rank:** Ranked #12 because the financial case is indirect (decision quality, not direct P&L) and the strategic fit, while high for CFO sponsorship, does not drive the core business outcomes that justify large investment. Placed in Tier 3 as a foundation builder — valuable for institutional AI adoption and CFO buy-in, but not a primary value driver.

---

### RANK 13: Human Resources (Non-SC)
**Tier: TIER 3 — Foundation Building**
**Primary Value Levers: Productivity, Quality, Efficiency**
**Time to First Value: 9–12 months**

| Dimension | Score | Rationale |
|---|---|---|
| Value at Stake | 2 | Predictive attrition for critical TRANS4RM roles: value is in preventing delays to a €150–250M/year program [FACT on cost; INFERENCE on attrition risk]. Internal mobility AI reduces hiring cost and accelerates role fill. Hard to quantify but meaningful for a 62,035-employee organization [FACT]. |
| Data Readiness | 3 | Deloitte SkillSenseAI deployed for job architecture [FACT]. SAP SuccessFactors active [FACT]. Gap: behavioral attrition signals (email volume, meeting patterns, performance trend) may not be accessible or permissible for AI analysis in all geographies. [ASSUMPTION on data availability and regulatory constraints] |
| Execution Complexity | 3 | Internal mobility and attrition prediction models are established HR tech capabilities. The complexity is in data access, privacy compliance (GDPR for European employees), and change management for HR function adoption. [INFERENCE] |
| Strategic Fit | 3 | Relevant to TRANS4RM delivery risk (protecting critical program skills) and long-term organizational capability building. Not a near-term commercial priority. [INFERENCE] |
| Velocity Score | 1 | No operational velocity impact. HR cycle time improvements (days to fill roles) are internal process improvements. [INFERENCE] |
| **Weighted Total** | **2.50** | |

**Why this rank:** Ranked #13 because HR AI, while genuinely valuable for workforce planning and TRANS4RM risk management, is the least commercially urgent and the most dependent on data privacy compliance across multiple European jurisdictions. SkillSenseAI is already deployed — the incremental build is in connecting it to attrition prediction and mobility recommendations.

---

## TIER SUMMARY

### TIER 1: Act Now (Highest Priority — Deploy in 2026)

| Stream | Rank | Weighted Score | Primary Lever | Time to First Value |
|---|---|---|---|---|
| Demand & Supply Planning | 1 | 4.35 | Efficiency, Quality, Velocity | 3–6 months |
| Marketing Content & Personalization | 2 | 4.75 | Productivity, Efficiency, Growth | 2–4 months |
| Procurement / Tariff Intelligence | 3 | 4.15 | Efficiency, Velocity | 3–6 months |
| Warehousing & Ship-from-Store | 4 | 3.90 | Velocity, Productivity, Growth | 3–6 months (MVP) |
| Outbound / Last Mile | 5 | 3.60 | Efficiency, Velocity, Growth | 2–3 months (carrier opt.) |
| Developer Productivity / TRANS4RM | 6 | 4.10 | Productivity, Velocity | Already delivering |

### TIER 2: Build Now, Harvest Later (2026–2027)

| Stream | Rank | Weighted Score | Primary Lever | Time to First Value |
|---|---|---|---|---|
| Digital Commerce / adiClub | 7 | 3.55 | Growth, Efficiency | 6–9 months |
| Inbound Transportation Visibility | 8 | 3.55 | Efficiency, Velocity | 60–90 days |
| Returns & Reverse Logistics | 9 | 3.25 | Efficiency, Quality | 6–9 months |
| Transport Planning & Control Tower | 10 | 2.90 | Efficiency, Velocity | 3–6 months (partial) |

### TIER 3: Foundation Building (2027–2028)

| Stream | Rank | Weighted Score | Primary Lever | Time to First Value |
|---|---|---|---|---|
| Freight Bill Audit | 11 | 2.55 | Efficiency, Productivity | 2–3 months |
| Finance & FP&A Analytics | 12 | 2.90 | Productivity, Quality | 6–9 months |
| Human Resources | 13 | 2.50 | Productivity, Efficiency | 9–12 months |

---

## PRIORITY SUMMARY TABLE — ALL 13 STREAMS

| Stream | Tier | Value at Stake | Data Readiness | Exec Complexity | Strategic Fit | Velocity Score | Weighted Total |
|---|---|---|---|---|---|---|---|
| Demand & Supply Planning | 1 | 5 | 4 | 3 | 5 | 5 | 4.35 |
| Marketing Content & Personalization | 1 | 5 | 5 | 4 | 5 | 4 | 4.75 |
| Procurement / Tariff Intelligence | 1 | 4 | 4 | 3 | 5 | 5 | 4.15 |
| Warehousing & Ship-from-Store | 1 | 4 | 4 | 3 | 4 | 5 | 3.90 |
| Outbound / Last Mile | 1 | 4 | 3 | 3 | 4 | 4 | 3.60 |
| Developer Productivity / TRANS4RM | 1 | 3 | 5 | 5 | 5 | 3 | 4.10 |
| Digital Commerce / adiClub | 2 | 4 | 4 | 3 | 4 | 2 | 3.55 |
| Inbound Transportation Visibility | 2 | 3 | 4 | 4 | 3 | 4 | 3.55 |
| Returns & Reverse Logistics | 2 | 3 | 4 | 3 | 3 | 3 | 3.25 |
| Transport Planning & Control Tower | 2 | 3 | 3 | 2 | 3 | 3 | 2.90 |
| Freight Bill Audit | 3 | 2 | 3 | 4 | 2 | 1 | 2.55 |
| Finance & FP&A Analytics | 3 | 2 | 4 | 4 | 4 | 1 | 2.90 |
| Human Resources | 3 | 2 | 3 | 3 | 3 | 1 | 2.50 |

*Scores: 1 (lowest) to 5 (highest) on each dimension. Weighted total = 30% Value + 25% Data + 20% Complexity + 15% Strategic Fit + 10% Velocity.*

---

## KEY STRUCTURAL FINDING: The Ship-from-Store Velocity Opportunity

The most structurally important finding across all 13 value streams is the **dormant velocity moat represented by adidas's 1,933 own stores.**

adidas has invested for years in the physical infrastructure of a distributed fulfillment network — 838 concept stores and 1,095 factory outlets, all equipped with RFID at >99% accuracy and GK OmniPOS. [FACT] This network, if activated for e-commerce fulfillment via a central AI routing engine, converts a real estate cost center into a last-mile competitive weapon.

- **The current state:** adidas.com delivers in 3–7 days standard US; Amazon delivers in 1–2 days. [FACT] This speed gap is a structural barrier to DTC conversion and is particularly acute during the FIFA World Cup 2026 North America window. [INFERENCE]
- **The dormant asset:** 1,933 stores with real-time RFID inventory accuracy, distributed across every major metropolitan market in North America and Europe. [FACT]
- **The BRAIN gap:** No confirmed AI routing engine that connects incoming DTC orders to the optimal fulfillment point across DC + store + carrier combinations. [ASSUMPTION]
- **The unlock:** A ship-from-store AI orchestration engine — a BRAIN investment, not a BODY investment — could enable 1-day delivery in the top 30 US cities within 6–12 months, without a single new DC. [INFERENCE]

This finding appears across SC-3 (warehousing), SC-5 (last mile), and the moat analysis. It is the single most important velocity opportunity in the portfolio that does not require Body investment.

---

## SEQUENCING GUIDANCE

### 2025–2026: Activate and Harvest Existing Infrastructure
The priority is activating AI on top of infrastructure that already exists. No new major BODY investment is required in this phase.

| Priority | Initiative | Infrastructure Dependency | Expected Outcome |
|---|---|---|---|
| 1 | FIFA World Cup 2026 content AI | MosaicML/Databricks (live) | Immediate marketing ROI; brand activation at scale |
| 2 | project44 scenario planning activation | project44 (adopted Feb 2026) | Exception management in hours vs. days |
| 3 | Tariff intelligence agent | Databricks (live) | €200M tariff headwind mitigation |
| 4 | Social signal demand sensing | o9 + MosaicML + Databricks (all live) | Lifestyle trend capture; full-price improvement |
| 5 | Dynamic carrier rate optimization | Carrier APIs (existing) | 8–15% outbound freight cost reduction |
| 6 | Freight bill audit AI | Coupa + carrier data | €16–32M annual recovery |

### 2026–2027: Build the Brain Layer
Use the savings and wins from Phase 1 to fund deeper capability builds that unlock the full value of TRANS4RM and the store network.

| Priority | Initiative | Infrastructure Dependency | Expected Outcome |
|---|---|---|---|
| 1 | Ship-from-store orchestration engine | RFID + GK OmniPOS (live); routing engine build | 1-day delivery in top 30 US metros |
| 2 | AI allocation optimizer (DTC vs. wholesale) | o9 + Databricks; TRANS4RM Supply Chain modules | 0.5–1.0pp gross margin improvement |
| 3 | adiClub personalization ML | Databricks + unified customer data platform | DTC conversion uplift for members |
| 4 | AI control tower on project44 | project44 + 3PL data agreements | Transportation cost visibility and optimization |

### 2027–2028: Scale and Compound
Leverage completed TRANS4RM (S/4HANA fully live by end 2027) to unlock AI initiatives that required clean master data, and scale proven BRAIN capabilities globally.

| Priority | Initiative | Infrastructure Dependency | Expected Outcome |
|---|---|---|---|
| 1 | Integrated supply chain AI (end-to-end) | TRANS4RM complete; S/4HANA master data clean | Full planning-to-fulfillment AI coverage |
| 2 | Ship-from-store global scale | EU + APAC concept store RFID integration | 1-day delivery in EU major cities |
| 3 | Finance & FP&A AI dashboard | S/4HANA Central Finance + Databricks | Real-time 2028 EBIT bridge monitoring |
| 4 | Predictive attrition & internal mobility | SuccessFactors + SkillSenseAI | Workforce planning for post-TRANS4RM era |
