# AI Value Levers Analysis — adidas AG
**Step 5 Output | Autonomous Consulting Workflow**
**Date:** 2026-04-03
**Analyst Role:** AI Value & Reinvention Analyst
**Sources:** FY2025 Annual Report (March 4, 2026), SEC 20-F filings, earnings call transcripts, Databricks Data+AI Summit 2026 disclosures, Manhattan Associates user conference materials, project44 press releases (February 2026), corporate press releases, prior step outputs (company_snapshot.md, tech_ops_footprint.md, transformation_capacity.md, benchmark_table.md, peer_set.md)

---

## ANALYTICAL FRAME

### What adidas actually is
adidas AG is not a manufacturer. It does not own factories. It does not move goods by default — it coordinates a global network that does. [FACT: 100% outsourced manufacturing across 124 supplier partners and 283 factories.] This distinction matters enormously for AI value mapping. The value of AI at adidas is not primarily in automating physical operations it owns — it is in making the coordination layer smarter, faster, and more precise.

The adidas "brain" sits above a complex, outsourced "body." When demand planning is wrong, adidas carries €4.99B of inventory. [FACT] When allocation is slow, markdown exposure rises. When supply chain visibility is poor, adidas cannot respond to tariff shocks in time. When personalization is weak, adiClub's 3× conversion premium leaks. Every dollar of AI investment at adidas should be evaluated against this coordination logic — not against a factory automation thesis.

### TRANS4RM Context
TRANS4RM (SAP S/4HANA on AWS) is the dominant technology commitment and the backbone of all future AI infrastructure. [FACT: Finance/Purchasing live 2023–2024; Supply Chain + Sales modules rolling 2025–2027; SAP legacy R/3 hard deadline 2027.] Any AI initiative must coexist with, complement, or accelerate TRANS4RM — not compete with it. AI opportunities that can run independently of TRANS4RM (on Databricks, o9, project44, or existing WMS layers) have higher near-term feasibility. AI opportunities that depend on clean S/4HANA master data are 12–24 months from full readiness in many areas.

### FIFA World Cup 2026 Urgency
The FIFA World Cup 2026 (US, Mexico, Canada) is the single largest brand moment adidas has in North America in a decade. [FACT: adidas is exclusive sporting goods partner.] North America is a structural underperformance region — growing +4% CN in FY2025 vs +13% global. [FACT] The window from now (April 2026) to tournament peak (June–July 2026) is approximately 90 days. Any AI initiative with a velocity impact on DTC fulfillment, marketing content activation, or demand responsiveness in North America has strategic urgency beyond its financial case. This urgency should be treated as a multiplier on near-term velocity initiatives.

### CFO as Technology Buyer
There is no CTO or CDO at adidas Executive Board level. [FACT] CFO Harm Ohlmeyer owns Technology AND Supply Chain since August 2024. [FACT] This means every AI pitch must be framed in P&L language — cost reduction, margin expansion, working capital release, revenue per employee improvement. The 2028 target of >10% EBIT margin (vs 8.3% in FY2025) is the governing financial constraint. Every AI initiative must be traceable to that number. Gulden's stated preference — "smarter processes, fewer manual steps, faster decisions" — defines the tone. AI framing must avoid digital transformation language and lean hard into operational precision.

---

# PART A: SUPPLY CHAIN DEEP DIVE

## SC-1: PROCUREMENT & SOURCING

### Current Situation
adidas sources from 124 supplier partners operating 283 factories across 32 countries. [FACT] Manufacturing is 100% outsourced. [FACT] Geographic concentration is high: 92% Asia (Vietnam 27%, Indonesia 19%, China 16%). [FACT] The 2025 US tariff shock forced rapid supplier network adjustments — China-to-US sourcing was eliminated during 2025. [FACT] A residual tariff headwind of ~€200M is embedded in 2026 guidance. [FACT] Procurement uses SAP BTP for purchase order amendments with 3,000+ external factory users. [FACT] Spend management is handled through Coupa (AP automation confirmed in Latin America). [FACT] Supplier code of conduct compliance is monitored, but the cadence and depth of factory-level monitoring is not disclosed publicly. [INFERENCE: Given 283 factories, manual audit cadence likely creates coverage gaps.]

### Likely Pain Points
1. **Tariff scenario planning is reactive, not predictive.** The 2025 tariff disruption required emergency sourcing pivots. There is no evidence of a real-time tariff intelligence and scenario simulation capability that could have pre-positioned supplier contracts. [INFERENCE]
2. **Supplier performance visibility is lagging.** With 283 factories and 100% outsourced production, on-time-in-full (OTIF) signals likely reach adidas after goods have shipped or are in transit — too late for proactive intervention. [INFERENCE]
3. **Supplier onboarding and amendment workflows are partially digitized but not AI-augmented.** The SAP BTP PO amendment tool covers 3,000+ external users — a good foundation — but AI-driven contract anomaly detection, spend analytics, and supplier risk scoring are not confirmed. [ASSUMPTION]
4. **Geographic concentration creates correlated risk.** 92% Asia sourcing means that any single regional disruption (geopolitical, logistics, weather, pandemic) creates simultaneous disruption across the majority of supply. [FACT-based INFERENCE] Risk modeling for correlated supplier failure is unlikely to be real-time. [ASSUMPTION]

### Value Levers Applicable
- **Efficiency:** Reduce sourcing cycle times, automate PO processing, eliminate manual compliance workflows
- **Quality:** Improve supplier quality signal detection; reduce defect-driven rework and returns at origin
- **Velocity:** Compress tariff response time from weeks to days via continuous scenario simulation
- **Productivity:** Free procurement staff from manual spend analysis; automate supplier scorecarding

### AI Opportunity
1. **Tariff Intelligence & Trade Policy Simulation Agent:** A continuously running AI agent (compatible with Databricks multi-agent architecture already in production) that monitors trade policy feeds, tariff schedule changes, US CBP rulings, and geopolitical signals, and automatically models the landed cost impact across all 283 factories. Outputs: ranked sourcing shift recommendations, cost-per-unit delta by scenario, lead time impact, and contract renegotiation priority queue. This is an immediate win given the confirmed €200M tariff headwind in 2026 guidance. Time to deploy: 3–6 months on existing Databricks infrastructure. [ASSUMPTION: requires clean supplier master data in SAP S/4HANA or Coupa as input.]
2. **Supplier Risk Scoring & Early Warning System:** ML model trained on supplier OTIF history, capacity utilization signals (via satellite imagery or third-party data providers), geopolitical risk indices, and port disruption feeds. Generates a weekly supplier health score for each of the 283 factories. Flags at-risk suppliers 4–6 weeks before likely disruption rather than 1–2 days after. Compatible with SAP IBP and o9 Solutions integration.
3. **AI-Assisted Spend Analytics on Coupa:** Deploy Coupa's native AI spend intelligence layer (Coupa Spend Guard) to detect off-contract spend, identify consolidation opportunities across the 124 supplier partners, and automatically flag procurement policy violations. Estimated addressable spend: €8–12B annually across manufacturing, logistics, and indirect. Even 0.5% leakage recovery = €40–60M.
4. **Automated PO Exception Management:** AI triage layer on top of SAP BTP PO amendment workflow. Classifies incoming amendments by risk (price deviation, quantity change, delivery date shift), auto-approves low-risk amendments, escalates high-risk to procurement staff. Reduces manual touchpoints by an estimated 40–60% on routine amendments. [ASSUMPTION on current manual exception rate.]

### Benefit Potential
**HIGH.** A €200M embedded tariff headwind in 2026 guidance provides immediate financial justification. The Databricks multi-agent infrastructure is already in production. Coupa is already deployed. The barrier is clean master data and procurement team adoption — not infrastructure.

### Velocity Assessment

| Velocity Dimension | Adidas Current State | Best-in-Class Benchmark / Gap |
|---|---|---|
| Tariff response time (policy change to sourcing pivot decision) | Estimated weeks — 2025 China pivot took months [INFERENCE] | Best-in-class: 48–72 hours with continuous scenario simulation. Gap: ~4–8 weeks |
| Supplier OTIF signal latency | Estimated: post-shipment confirmation (3–7 days lag) [INFERENCE] | Best-in-class: real-time factory floor signal via IoT/EDI. Gap: 3–7 days |
| PO amendment cycle time | Estimated: 2–5 days for complex amendments via SAP BTP [INFERENCE] | Best-in-class: <4 hours with AI triage. Gap: ~3–4 days |
| Supplier risk assessment cadence | Estimated: quarterly or event-driven [ASSUMPTION] | Best-in-class: continuous scoring updated weekly. Gap: 3 months |
| New supplier onboarding time | Not disclosed publicly [ASSUMPTION: 4–8 weeks] | Best-in-class: <2 weeks with AI-assisted due diligence. Gap: unknown |

### Bottleneck Analysis
The primary procurement velocity constraint is **BRAIN** — specifically, the absence of continuous intelligence on trade policy, supplier risk, and spend patterns. The physical supplier network (124 partners, 283 factories) is the BODY, and it is largely fixed in the near term — moving factories takes 12–24 months minimum and involves significant relationship and quality risk. The velocity unlock is not in changing the Body but in making the Brain respond faster to signals that the Body is generating. The tariff intelligence agent is the highest near-term velocity win: it requires no Body change, runs on existing Databricks infrastructure, and addresses a €200M live headwind. Ship-from-store and microfulfillment are not relevant to this SC area.

### Key Discovery Questions
1. What is the current process and average cycle time from a US tariff policy announcement to a final sourcing shift decision — and who owns that decision? [ASSUMPTION: the process is largely manual and takes weeks]
2. Does adidas have a real-time supplier OTIF feed per factory, or is performance visibility aggregated only at the supplier-partner level? [ASSUMPTION: factory-level real-time OTIF is not available]
3. What percentage of PO amendments currently require manual procurement intervention, and what is the average resolution time? [ASSUMPTION: manual intervention rate is high for non-standard amendments]

---

## SC-2: DEMAND & SUPPLY PLANNING

### Current Situation
adidas operates a layered demand planning stack: o9 Solutions for in-season retail planning, allocation, and DTC demand sensing; Amazon SageMaker for seasonal ML forecasting; and SAP IBP likely alongside for enterprise-level S&OP. [FACT: o9 Solutions and SageMaker confirmed from technology disclosures; SAP IBP inferred from S/4HANA deployment.] Despite this stack, adidas closed FY2024 with €4.99B in inventory [FACT] — a figure that implies meaningful demand-supply imbalance or deliberate buffer stocking. The Yeezy inventory liquidation distorted recent planning signals; the underlying structural accuracy of adidas demand forecasting for standard product lines is not publicly disclosed. [INFERENCE] The business has significant seasonality (football seasons, lifestyle trend cycles) and event-driven demand spikes (FIFA World Cup 2026). [FACT]

### Likely Pain Points
1. **Forecast accuracy degrades at the SKU/store level even when acceptable at the brand/region level.** With 71K+ SKUs at the Wilkes-Barre DC alone [FACT], the combinatorial challenge of per-SKU, per-channel, per-location forecasting almost certainly exceeds what any planning team can manually validate. [INFERENCE]
2. **Lifestyle trend products (Samba, Gazelle) have compressed planning windows.** Cultural demand spikes are driven by social media signals that move faster than traditional planning cycles (typically 4–12 weeks). If adidas cannot sense and respond to these signals within days, it either overstocks after the peak or stockouts during it. [INFERENCE]
3. **Channel allocation between DTC, wholesale, and outlet is a recurring tension.** DTC (€4.3B, 18% of revenue) and wholesale are structurally competing for the same inventory pool. Allocation decisions made at S&OP level may not incorporate real-time sell-through signals at the SKU level across channels. [INFERENCE]
4. **Multi-tier supply latency limits planning responsiveness.** Even if demand sensing improves, manufacturing lead times from Asia (4–12 weeks typical for footwear) mean that mid-season demand signal improvements can only influence allocation and in-transit rerouting — not production. [FACT-based INFERENCE]

### Value Levers Applicable
- **Efficiency:** Reduce inventory levels; decrease markdown rates; lower stock-out frequency
- **Quality:** Improve forecast accuracy at SKU/channel/location level
- **Velocity:** Compress demand signal-to-allocation decision cycle from weeks to days
- **Growth:** Capture lifestyle trend demand that currently leaks due to stockout; improve full-price sell-through

### AI Opportunity
1. **Social Signal Demand Sensing Layer:** A real-time ML pipeline that ingests social media engagement signals (TikTok, Instagram), search trend data (Google Trends API), and adiClub behavioral signals, and feeds them as leading indicators into the o9 demand sensing engine. Specifically tuned to lifestyle product lines where trend cycles compress traditional planning windows. Estimated latency improvement: demand signal from social to allocation adjustment within 24–48 hours vs current estimated 2–4 weeks. [ASSUMPTION on current latency] Compatible with existing MosaicML GenAI pipeline (which already processes 2M+ product reviews/year at 91.67% cost reduction) and Databricks infrastructure.
2. **AI-Driven Allocation Optimizer (DTC vs. Wholesale vs. Outlet):** An ML model that dynamically recommends optimal inventory allocation across channels for each SKU, incorporating real-time sell-through rates, full-price vs. markdown risk, channel margin profiles, and adiClub demand signals. Reduces reliance on static allocation rules set at S&OP. Estimated margin impact: 0.5–1.0pp gross margin improvement from better full-price sell-through. [ASSUMPTION: addressable through allocation, not production changes]
3. **Agent Digital Twin for FIFA World Cup 2026 Demand Planning:** Extend the confirmed Databricks Agent Digital Twin (in production as of Databricks Data+AI Summit 2026) to model FIFA World Cup 2026 demand scenarios across North America — product by product, city by city, channel by channel. Simulate stockout risk under optimistic/base/pessimistic attendance and viewership scenarios. This is immediately actionable given the 90-day window to tournament peak. [FACT: Databricks Agent Digital Twin is in production]
4. **In-Season Replenishment Agent:** An AI agent that monitors sell-through at own stores (via GK OmniPOS and RFID >99% accuracy [FACT]) and wholesale partners, identifies emerging stockout risk 2–3 weeks ahead, and automatically triggers replenishment POs or allocation transfers from surplus locations. Reduces reliance on wholesale partner reorder signals, which typically arrive too late for effective response.

### Benefit Potential
**HIGH — the highest single-value-stream opportunity in the entire company.** Inventory at €4.99B represents ~20% of annual revenue. A 5% inventory reduction through improved planning accuracy = €250M in working capital release. A 0.5pp improvement in gross margin through better full-price sell-through = ~€124M annually at current revenue scale. The technology foundation (o9, SageMaker, Databricks, RFID, adiClub data) exists. The constraint is integration and model precision — not infrastructure.

### Velocity Assessment

| Velocity Dimension | Adidas Current State | Best-in-Class Benchmark / Gap |
|---|---|---|
| Demand sensing latency (social signal to planning update) | Estimated 2–4 weeks [INFERENCE] | Best-in-class (Zara/fast fashion): 1–2 weeks; pure-digital (ASOS): 48–72 hours. Gap: 2–3 weeks |
| S&OP cycle time | Estimated monthly S&OP cycle [INFERENCE from industry norm] | Best-in-class: rolling weekly or continuous. Gap: 3 weeks per cycle |
| Allocation adjustment speed (sell-through signal to reallocation) | Estimated 1–2 weeks [INFERENCE] | Best-in-class: 24–48 hours with AI. Gap: ~10 days |
| Forecast accuracy at SKU/store level | Not publicly disclosed [ASSUMPTION: 60–70% accuracy common in footwear at SKU level] | Best-in-class: 85%+ at SKU level with ML. Gap: estimated 15–25pp |
| Event-driven demand simulation cycle | Not confirmed — ad hoc [ASSUMPTION] | Best-in-class: pre-built scenario models activated in hours. Gap: days to weeks |

### Bottleneck Analysis
The demand planning velocity constraint is entirely **BRAIN** — the physical supply network cannot be compressed by AI alone, but the intelligence layer that operates within it absolutely can. The latency between a social signal (e.g., Samba trending on TikTok) and an allocation decision is a BRAIN problem: the data exists (MosaicML processes 2M+ reviews/year, RFID tracks store inventory in real time, adiClub tracks consumer behavior), but the closed-loop AI system that connects these signals to allocation decisions has not been confirmed as fully operational. The highest near-term velocity AI win is a social-signal-to-allocation closed loop for lifestyle products — this can be built on existing Databricks infrastructure and does not require TRANS4RM completion. Ship-from-store is relevant here as an allocation escape valve (see SC-3). Microfulfillment and dark stores are not confirmed for adidas and would require Body investment first.

### Key Discovery Questions
1. What is the current forecast accuracy at the SKU/store/week level for both performance and lifestyle product lines, and how does this break down by channel? [ASSUMPTION: SKU-level accuracy is materially below brand/region level accuracy]
2. How are DTC and wholesale allocation decisions made when both channels are simultaneously under-inventoried — who arbitrates, on what data, and how often? [ASSUMPTION: this decision is made manually at senior commercial level rather than algorithmically]
3. Is the o9 Solutions demand sensing engine receiving real-time GK OmniPOS sell-through data from own stores as a live input, or is store data batch-uploaded on a daily or weekly basis? [ASSUMPTION: batch upload is the current norm, creating a latency gap that AI could close]

---

## SC-3: WAREHOUSING, FULFILLMENT & SHIP-FROM-STORE

### Current Situation
adidas operates 60 DCs globally (21 owned, 39 3PL-managed). [FACT] Key facilities include: Wilkes-Barre PA (843K sq ft, 200K units/day peak, 71K SKUs, 2-hour order-to-pack, Manhattan Associates WMS with Slotting Optimisation and Labour Management, Interlake Mecalux racking) [FACT]; Spartanburg SC (258 acres, Honeywell Intelligrated automation) [FACT]; Mantova Italy (130K sqm, €350M investment, 700+ robots, 500K shipments/day peak, 19-country service, Kuehne+Nagel operated) [FACT]; Suzhou China (139K sqm, 1M+ pieces/day, Geek+ AMR) [FACT]; Manchester UK (350K sq ft, Dematic ASRS + GTP, Manhattan WMS) [FACT]; Brazil Extrema (40K sqm, DHL, automated conveyors) [FACT]. Ship-from-store technology is confirmed (GK OmniPOS + RFID >99% accuracy at own stores) [FACT], but scale of active ship-from-store utilization is not publicly quantified. [INFERENCE: the technology exists but the operational program scale is unknown] adidas operates 1,933 own stores (838 concept + 1,095 factory outlets). [FACT]

### Likely Pain Points
1. **Slotting and labor efficiency gains are realized at flagship DCs but likely inconsistent across 39 3PL-managed sites.** Manhattan Associates Slotting Optimisation and Labour Management are confirmed at Wilkes-Barre and Manchester — but 3PL contracts and system integrations at other sites likely vary significantly in technology sophistication. [INFERENCE]
2. **Ship-from-store is technologically enabled but operationally underutilized.** 1,933 stores with RFID and GK OmniPOS represent an enormous distributed fulfillment network — but without a central ship-from-store orchestration engine routing orders to optimal store + DC combinations, this asset is largely dormant for e-commerce fulfillment purposes. [INFERENCE]
3. **The 60-DC global network creates coordination complexity.** With 21 owned and 39 3PL-managed DCs, achieving consistent order routing logic, real-time inventory visibility, and cross-DC transfer efficiency requires a central orchestration capability not confirmed to be fully deployed. [ASSUMPTION]
4. **Peak capacity management at key DCs creates seasonal bottlenecks.** Wilkes-Barre at 200K units/day peak [FACT] and Mantova at 500K shipments/day peak [FACT] suggest high utilization rates during peak — leaving limited headroom for demand surges (e.g., FIFA World Cup 2026 in North America). [INFERENCE]

### Value Levers Applicable
- **Productivity:** Improve pick/pack efficiency via AI-driven slotting; optimize labor deployment against intraday demand forecasts
- **Efficiency:** Reduce cost-per-order at 3PL-managed sites; decrease returns processing cost
- **Velocity:** Activate ship-from-store to deliver 1-day fulfillment in major cities without new DC investment
- **Growth:** Capture DTC revenue currently lost to fulfillment speed competitors (Amazon 1–2 day Prime; Zalando 1–3 day)

### AI Opportunity
1. **Ship-from-Store AI Orchestration Engine:** The most immediately impactful velocity initiative available to adidas without Body investment. Deploy an AI routing engine that, for each DTC order, evaluates: (a) DC inventory and estimated delivery time; (b) nearest stores with available inventory per RFID; (c) store labor capacity and order processing time; (d) carrier options from that store. Routes each order to the optimal fulfillment point in real-time. Leverages existing RFID, GK OmniPOS, and Manhattan WMS infrastructure. Could enable 1-day delivery in top 30–50 US metropolitan areas where adidas has concept store density, without building a single new DC. [FACT foundation: RFID >99% accuracy, ship-from-store technology confirmed; ASSUMPTION: central orchestration engine does not yet exist at scale]
2. **AI-Driven Slotting Optimization Across 3PL Network:** Extend the Manhattan Associates Slotting Optimisation logic (confirmed at Wilkes-Barre) to 3PL-managed sites via an API layer or 3PL data sharing agreement. AI continuously re-slots based on current and forecast demand patterns, reducing travel time per pick. Industry benchmarks: 15–25% pick efficiency improvement from dynamic AI slotting. At 200K units/day peak at Wilkes-Barre alone, a 15% efficiency gain = 30K additional units/day capacity without CapEx. [INFERENCE]
3. **Intraday Labor Demand Forecasting at DC Level:** ML model predicting hourly order volume by DC, feeding Manhattan Labour Management to optimize shift schedules and temporary labor deployment. Reduces both labor waste (overstaffing) and fulfillment slowdowns (understaffing during demand spikes). Estimated 8–12% labor cost reduction at operated DCs. [ASSUMPTION on current labor optimization maturity]
4. **Returns Processing AI:** Computer vision + RFID integration at DC receiving docks to assess returned item condition automatically (resalable, refurbishable, donate/liquidate), route items to appropriate next step without human triage, and update inventory availability in real time. Reduces returns processing time from estimated 2–5 days to same-day, releasing working capital faster. [INFERENCE on current returns processing time]

### Benefit Potential
**HIGH for ship-from-store velocity; MEDIUM for DC efficiency gains.** The ship-from-store opportunity is the single largest velocity unlock available to adidas without Body investment — 1,933 stores are a dormant fulfillment network that could close the 1–2 day delivery gap with Amazon and Zalando in key markets. DC efficiency gains at 3PL-managed sites are meaningful but depend on 3PL contractual flexibility.

### Velocity Assessment

| Velocity Dimension | Adidas Current State | Best-in-Class Benchmark / Gap |
|---|---|---|
| Order-to-pack time (DC) | 2 hours at Wilkes-Barre [FACT] | Best-in-class: <1 hour (Amazon fulfillment centers). Gap: ~1 hour |
| Standard US DTC delivery | 3–7 days standard; 2-day nationwide [FACT] | Amazon Prime: 1–2 days; same-day 90%+ US addresses. Gap: 1–5 days depending on location |
| Standard EU DTC delivery | 3–7 days estimated [INFERENCE] | Zalando: 1–3 days with own logistics network. Gap: 0–4 days |
| Ship-from-store fulfillment speed | Technology confirmed; operational scale unknown [ASSUMPTION: limited deployment] | Best-in-class (Nike, Zara): >50% of DTC orders fulfilled from store in major cities. Gap: unknown but likely significant |
| Returns processing time | Not disclosed [ASSUMPTION: 3–7 days] | Best-in-class: same-day to 48 hours. Gap: estimated 2–5 days |

### Bottleneck Analysis
The warehousing velocity constraint is a combination of **BODY** (DC network designed for bulk wholesale dispatch, not e-commerce speed) and **BRAIN** (no confirmed AI orchestration layer connecting DC inventory, store inventory, and carrier routing in real time). The highest near-term velocity AI win is the ship-from-store orchestration engine — this is a pure BRAIN investment that activates an existing BODY asset (1,933 stores with RFID) without new Body expenditure. The FIFA World Cup 2026 window creates urgency for the North America application specifically — activating ship-from-store in major US metro areas before June 2026 would directly support the commercial moment. Dark stores are not confirmed and are unlikely to be cost-effective given store density. Microfulfillment centers are not confirmed and are a longer-term Body consideration.

### Key Discovery Questions
1. What percentage of DTC orders are currently fulfilled via ship-from-store vs. central DCs, and what is the operational bottleneck preventing scale — is it routing software, store labor training, carrier integration, or commercial prioritization? [ASSUMPTION: operational ship-from-store scale is currently minimal]
2. Do 3PL-managed DC contracts include data-sharing provisions that would allow adidas to deploy its own WMS or optimization logic, or do the 3PL operators control the system stack at each site? [ASSUMPTION: 3PL contracts vary and some may restrict adidas system access]
3. What is the actual RFID read accuracy and inventory reconciliation cadence at own stores — is RFID data available in real time for order routing, or is it batch-synchronized? [ASSUMPTION: RFID accuracy is high but synchronization to a central order management system may be batch-based]

---

## SC-4: INBOUND TRANSPORTATION & SUPPLIER-TO-DC VISIBILITY

### Current Situation
adidas adopted project44 in February 2026 for real-time visibility and AI scenario planning across its global transportation network. [FACT] Prior to this adoption, inbound transportation visibility was almost certainly fragmented across 3PL systems, freight forwarder portals, and manual tracking. [INFERENCE] The manufacturing base is 92% Asia, meaning the vast majority of inbound freight travels via ocean or air from Vietnam, Indonesia, China, and other Asian countries to distribution hubs in Europe, North America, and other regions. [FACT] Ocean transit times from Asia to North America (West Coast) are approximately 14–21 days; to Europe 20–30 days via Suez or 25–35 days via Cape of Good Hope. [FACT-based industry knowledge] Air freight is used for urgent or high-value shipments but at a cost premium of 4–6× ocean. [FACT-based industry knowledge]

### Likely Pain Points
1. **Before project44, inbound visibility was almost certainly event-based (departure, port arrival) rather than continuous.** This means exceptions (delays, port congestion, customs holds) were identified reactively — often after the delay had already propagated into DC scheduling and order fulfillment. [INFERENCE]
2. **Carrier and routing diversity across a 124-partner, 283-factory network creates data fragmentation.** Different factories use different freight forwarders. Each forwarder has different EDI/API standards. Aggregating a coherent single-view of all in-transit inventory before project44 was likely manual or incomplete. [INFERENCE]
3. **Port disruption events (Red Sea, US West Coast labor, Panama Canal capacity) require manual rerouting decisions.** Without AI scenario planning, each disruption triggers a manual response cycle involving procurement, logistics, and commercial teams — compressing response time and increasing cost. [INFERENCE]
4. **Air freight cost discipline is likely reactive.** When a shipment is at risk of missing a critical DC arrival window, the decision to upgrade to air is likely made ad hoc rather than optimized against carrying cost vs. air premium vs. stockout risk. [ASSUMPTION]

### Value Levers Applicable
- **Efficiency:** Reduce air freight premiums through predictive exception management; optimize mode selection before departure
- **Quality:** Improve DC arrival predictability; reduce planning signal noise caused by inbound uncertainty
- **Velocity:** Compress exception-to-response cycle from days to hours via continuous AI monitoring
- **Productivity:** Reduce logistics team manual tracking effort; automate exception escalation

### AI Opportunity
1. **project44 AI Scenario Planning Activation:** project44 is confirmed adopted (February 2026) and includes AI scenario planning capabilities. The immediate priority is activating the scenario planning module — not just track-and-trace — to generate predictive ETA updates and automated alerts when an in-transit shipment is at risk of missing its DC arrival window. This is an activation challenge, not an infrastructure challenge. Time to value: 60–90 days. [FACT foundation: project44 adopted; ASSUMPTION: scenario planning module not yet fully activated]
2. **Dynamic Air-vs-Ocean Mode Switch Model:** ML model that, at point of production completion at factory, calculates optimal shipping mode based on: current DC inventory level for that SKU, demand forecast for the next 4 weeks, ocean ETA probability distribution, air freight premium, and carrying cost of delay. Automatically flags shipments where air premium is justified. Could reduce discretionary air spend by 15–25% while maintaining fill rates. [ASSUMPTION on current air freight decision process]
3. **Port Disruption Early Warning Integration:** Feed project44 vessel tracking data into a disruption model that predicts port congestion 7–14 days ahead (using vessel queue data, weather, and historical patterns). Triggers automatic rerouting simulations and recommends alternative ports or carriers before the disruption fully materializes. [INFERENCE: project44 has this data; the AI layer needs to be built on top]
4. **Customs Clearance Prediction & Pre-positioning:** ML model that predicts customs clearance duration by port, carrier, commodity code, and declared value, and automatically prepares documentation packages for high-risk shipments. Reduces customs dwell time and improves DC arrival predictability.

### Benefit Potential
**MEDIUM-HIGH.** project44 adoption is confirmed and recent — the infrastructure investment is already made. The value extraction is in activating AI scenario planning and building exception management workflows. Financial case: if AI-driven mode optimization reduces air freight by 20% on estimated annual air freight spend of €100–200M [ASSUMPTION on air freight scale], savings are €20–40M annually. Additionally, improved DC arrival predictability reduces buffer inventory and DC labor planning costs.

### Velocity Assessment

| Velocity Dimension | Adidas Current State | Best-in-Class Benchmark / Gap |
|---|---|---|
| Exception detection time (disruption to alert) | Pre-project44: days [INFERENCE]; post-adoption: improving but not fully activated [ASSUMPTION] | Best-in-class: <4 hours with AI continuous monitoring. Gap: estimated days to hours |
| Rerouting decision cycle time | Estimated days (manual, cross-functional) [INFERENCE] | Best-in-class: <24 hours with AI scenario simulation. Gap: ~3–5 days |
| ETA accuracy (within ±1 day) | Not disclosed [ASSUMPTION: 60–70% accuracy at port arrival level] | Best-in-class: 90%+ with ML-enhanced vessel tracking. Gap: ~20–30pp |
| Air-vs-ocean decision lead time | Estimated: 2–3 days before departure [ASSUMPTION] | Best-in-class: at point of production completion (7–14 days before departure). Gap: 5–10 days |
| Proactive disruption identification (days ahead) | Near-zero before project44 [INFERENCE] | Best-in-class: 7–14 days ahead with predictive models. Gap: ~7–14 days |

### Bottleneck Analysis
Inbound transportation velocity is a **BRAIN** constraint at this stage — the Body (ocean + air lanes, port infrastructure, carrier relationships) is largely fixed in the near term. The project44 adoption creates the data substrate for a BRAIN upgrade. The bottleneck is activation and integration: project44's AI capabilities must be connected to the demand planning signal (o9/SageMaker) and the DC scheduling system (Manhattan WMS) to create a closed loop. The highest near-term velocity AI win is activating project44's scenario planning module and integrating its ETA predictions into DC arrival scheduling — a 60–90 day initiative that requires no new infrastructure spend.

### Key Discovery Questions
1. Is project44's AI scenario planning module currently activated and generating automated alerts, or is the current deployment limited to track-and-trace visibility? [ASSUMPTION: initial deployment is likely limited to visibility, with AI planning capabilities not yet activated]
2. How are inbound ETA changes currently propagated to DC scheduling teams — is there an automated workflow, or does a logistics coordinator manually update the DC schedule when ETAs shift? [ASSUMPTION: the propagation is largely manual, creating latency in DC labor planning]
3. What is the current annual air freight spend and what percentage is classified as "emergency upgrade" vs. planned premium — and is there an explicit cost-per-unit threshold that triggers an air upgrade decision? [ASSUMPTION: air freight decisions are made ad hoc without a formal ML-optimized threshold]

---

## SC-5: OUTBOUND TRANSPORTATION & LAST MILE

### Current Situation
adidas delivers to DTC customers via a mix of parcel carriers (UPS, FedEx, DHL, and national carriers) and wholesale customers via LTL/FTL trucking. [INFERENCE from US market context; specific carrier contracts not publicly disclosed] DTC e-commerce was €4.3B in FY2025 (+16% CN). [FACT] US standard delivery is 3–7 days; 2-day nationwide from Wilkes-Barre; same-day in select NE US locations; Amazon Buy with Prime (MCF) live Spring 2025 enabling 1–2 day delivery for Prime members on adidas.com. [FACT] UK: 3–5 working days standard; 1–2 day express at £5.95. [FACT] There is no confirmed carrier rate optimization or dynamic routing engine for outbound parcel. [ASSUMPTION] The Amazon Buy with Prime MCF integration is a significant step toward closing the speed gap with Amazon — but it is available only for Prime members and effectively outsources last-mile to Amazon's network. [FACT]

### Likely Pain Points
1. **3–7 day standard US delivery is a competitive disadvantage vs. Amazon (1–2 day) and Zalando EU (1–3 day).** For consumers conditioned by Prime, standard 3–7 day delivery creates a friction point that depresses DTC conversion rates. [INFERENCE]
2. **Carrier rate optimization is likely static.** Annual carrier contracts are common in the industry. Without dynamic rate shopping at shipment creation time, adidas likely overpays on certain lanes or cannot react quickly to carrier capacity shifts. [ASSUMPTION]
3. **Last-mile performance visibility post-shipment is likely limited.** Without real-time carrier performance tracking feeding back to customer service and to DC operations, adidas cannot proactively manage delivery exceptions or optimize future carrier allocation. [INFERENCE]
4. **Amazon Buy with Prime is a partial solution with structural limits.** It closes the speed gap for Prime members but creates dependency on Amazon's infrastructure, potentially cannibalizing adidas's own data capture on those transactions. [INFERENCE]

### Value Levers Applicable
- **Efficiency:** Reduce outbound freight cost per order via dynamic carrier rate optimization
- **Velocity:** Compress delivery speed in key markets through AI routing and ship-from-store activation
- **Growth:** Improve DTC conversion rates by offering faster delivery options; reduce cart abandonment from delivery speed concerns
- **Quality:** Reduce delivery exception rates; improve customer communication accuracy

### AI Opportunity
1. **Dynamic Carrier Rate Shopping & Allocation Engine:** At point of shipment creation, an AI engine evaluates all available carrier options for that origin DC, destination ZIP code, weight/dimension, and service level — and routes to the lowest-cost carrier meeting the service level requirement. Updates carrier allocation rules daily based on performance data. Industry benchmarks: 8–15% outbound freight cost reduction. At estimated DTC parcel volume of 40–60M shipments/year (ASSUMPTION from ~€4.3B DTC at ~€70–100 average order value), even 5% cost reduction = €15–20M annually.
2. **Predictive Delivery Promise Engine:** ML model that, at checkout, predicts the actual delivery date for that specific customer location, DC inventory position, and carrier performance — rather than showing a static "3–7 days" range. Improves conversion (consumers prefer specific promised dates over ranges) and reduces customer service contacts for delivery inquiries. Industry data: specific date promises improve conversion 15–20% vs. date ranges. [INFERENCE]
3. **Ship-from-Store Last Mile Activation (linked to SC-3):** For metropolitan areas where adidas stores have inventory, an AI engine routes DTC orders to the nearest store, triggers ship-from-store pick/pack, and selects same-day or next-day last-mile carrier (e.g., Uber Direct, Shipt, local courier). Enables 1-day delivery in top 30 US cities without new DC investment. [FACT foundation: RFID, GK OmniPOS, ship-from-store technology confirmed]
4. **Wholesale Delivery Optimization for Key Accounts:** ML model optimizing LTL/FTL consolidation for wholesale deliveries, reducing cost per unit delivered to key retail accounts. Also predicts retailer DC capacity windows to schedule deliveries that avoid retailer congestion penalties. [ASSUMPTION on current wholesale routing sophistication]

### Benefit Potential
**HIGH for velocity (ship-from-store); MEDIUM for cost (carrier optimization).** The ship-from-store last-mile case directly addresses the delivery speed gap with Amazon and Zalando in major markets. The FIFA World Cup 2026 North America moment creates urgency for the US application before June 2026. The dynamic carrier optimization case is financially straightforward and can be implemented in 60–90 days.

### Velocity Assessment

| Velocity Dimension | Adidas Current State | Best-in-Class Benchmark / Gap |
|---|---|---|
| Standard US DTC delivery | 3–7 days; 2-day from Wilkes-Barre [FACT] | Amazon Prime: 1–2 days; same-day 90%+ US addresses. Gap: 1–5 days |
| Standard EU DTC delivery | Estimated 3–7 days [INFERENCE] | Zalando: 1–3 days with own logistics network. Gap: 0–4 days |
| Express option availability | Amazon Buy with Prime: 1–2 days for Prime members on adidas.com [FACT] | Best-in-class: 1-day standard for loyalty members. Gap: available but restricted to Prime members |
| Delivery promise accuracy at checkout | Static range (e.g., "3–7 days") [INFERENCE] | Best-in-class: specific date prediction with >95% accuracy. Gap: significant |
| Metropolitan same-day delivery | Select NE US locations only [FACT] | Amazon: same-day 90%+ US addresses; Zalando: same-day key EU cities. Gap: dramatic |

### Bottleneck Analysis
Outbound velocity constraint is **BODY and BRAIN combined**. The Body constraint is DC location relative to major metropolitan population centers — Wilkes-Barre is well-positioned for the Eastern US but the Western US is underserved for speed. The BRAIN constraint is the absence of: (a) dynamic carrier routing, (b) predictive delivery promise at checkout, and (c) ship-from-store orchestration. The ship-from-store orchestration is the highest near-term velocity win because it converts existing Body assets (1,933 stores) into fulfillment nodes, addressing the BODY location limitation without new DC capital expenditure. The carrier rate optimization is the highest near-term efficiency win and can be implemented fastest.

### Key Discovery Questions
1. What is the current DTC cart abandonment rate at checkout, and has adidas conducted A/B testing to understand how much of that abandonment is attributable to delivery speed or cost compared to alternatives? [ASSUMPTION: delivery speed is a material contributor to DTC conversion loss vs. Amazon]
2. Does adidas have a real-time carrier performance API feed that tracks delivery exceptions at the package level, and is this feed connected to customer service case management? [ASSUMPTION: carrier performance visibility is batch or dashboard-based rather than real-time and exception-triggered]
3. What is the current cost per DTC shipment by carrier and lane, and does adidas have a dynamic rate shopping capability or is carrier allocation governed by annual fixed-allocation contracts? [ASSUMPTION: annual fixed-allocation contracts are the current norm, limiting real-time optimization]

---

## SC-6: TRANSPORT PLANNING & CONTROL TOWER

### Current Situation
project44 was adopted in February 2026 [FACT], creating a real-time visibility layer across the transportation network. Prior to this, transportation planning and control tower capability was almost certainly fragmented. [INFERENCE] The 60-DC global network (21 owned, 39 3PL-managed) [FACT] requires coordination across inbound ocean/air, inter-DC transfers, outbound parcel, and wholesale trucking — a multi-modal complexity that demands a sophisticated control tower capability. The Mantova Italy DC serves 19 countries [FACT], implying significant multi-country outbound planning complexity. Whether adidas has a unified control tower capability connecting all modes and regions is not publicly confirmed. [ASSUMPTION: control tower is emergent, not fully operational]

### Likely Pain Points
1. **Multi-modal, multi-region visibility prior to project44 was almost certainly fragmented.** Without a single control tower, exceptions in one part of the network (e.g., a delayed ocean shipment to Mantova) could not be automatically translated into DC scheduling adjustments or customer communication updates. [INFERENCE]
2. **Inter-DC transfer optimization across the 60-DC network is likely manual or rule-based.** When one DC is over-inventoried and another is under-inventoried in the same SKU, the identification of this imbalance and the decision to transfer inventory is likely event-driven rather than continuously optimized. [ASSUMPTION]
3. **Transportation cost visibility across modes is likely opaque.** With 39 3PL-managed sites, each with its own carrier contracts and billing systems, achieving a consolidated view of total transportation cost by lane, mode, and origin-destination pair is likely a finance exercise rather than a real-time operational signal. [INFERENCE]
4. **Exception management is reactive.** Without predictive ETAs and automated exception scoring, logistics coordinators manage exceptions as they materialize rather than pre-empting them. [INFERENCE]

### Value Levers Applicable
- **Efficiency:** Reduce total transportation cost through consolidated control tower optimization
- **Velocity:** Compress exception-to-resolution cycle; accelerate inter-DC rebalancing decisions
- **Quality:** Improve shipment visibility and on-time performance across all modes
- **Productivity:** Reduce logistics coordinator manual workload through AI-automated exception triage

### AI Opportunity
1. **AI-Powered Global Control Tower on project44:** Build an AI control tower layer on the project44 platform that aggregates inbound, inter-DC, and outbound visibility in a single pane, applies ML-based exception scoring (which exceptions truly threaten service levels vs. which are self-resolving), and automatically generates recommended responses. Replaces manual exception log management with an AI-prioritized action queue. Time to value: 3–6 months leveraging project44's existing API ecosystem. [FACT foundation: project44 adopted February 2026]
2. **AI-Driven Inter-DC Inventory Rebalancing:** Continuously running model that monitors SKU-level inventory across all 60 DCs, compares against demand forecasts by market, and generates daily recommended inter-DC transfer orders when the cost of transfer is lower than the cost of stockout or markdown. Requires real-time inventory visibility across all sites — achievable for owned DCs; dependent on 3PL data-sharing agreements for the 39 3PL sites. [ASSUMPTION on 3PL data availability]
3. **Transportation Cost Intelligence Layer:** Unified data pipeline that aggregates freight invoices from all 3PL partners, normalizes to a consistent cost-per-unit-per-lane format, and generates a continuous benchmark against market rate indices (e.g., Freightos Baltic Index, DAT spot rates). Flags lanes where adidas is paying above market and generates renegotiation priority queues for the logistics procurement team. Financial case: even 5% of total freight spend = €100–200M in savings potential. [ASSUMPTION on total freight spend scale]
4. **Predictive DC Capacity Planning:** ML model that predicts DC throughput demand 4–6 weeks ahead by site, incorporating seasonal patterns, inbound shipment ETAs, and order volume forecasts. Feeds workforce planning, temporary labor decisions, and capital planning for temporary storage.

### Benefit Potential
**MEDIUM-HIGH.** project44 creates the infrastructure foundation. The AI layer is the value extraction mechanism. Transportation cost intelligence is immediately actionable and financially significant. Inter-DC rebalancing is high-value but requires 3PL data cooperation.

### Velocity Assessment

| Velocity Dimension | Adidas Current State | Best-in-Class Benchmark / Gap |
|---|---|---|
| Exception detection (disruption to alert) | Improving post-project44 but not confirmed as automated [ASSUMPTION] | Best-in-class: automated detection within minutes. Gap: hours to days |
| Inter-DC rebalancing decision cycle | Estimated weekly or event-driven [ASSUMPTION] | Best-in-class: continuous with daily auto-recommendations. Gap: 5–7 days |
| Control tower coverage (% of freight under real-time visibility) | Improving post-project44 [ASSUMPTION: partial coverage initially] | Best-in-class: 95%+ of freight under real-time visibility. Gap: unknown |
| Exception-to-resolution cycle time | Estimated 24–72 hours [ASSUMPTION] | Best-in-class: <8 hours with AI-prioritized action queue. Gap: ~2 days |
| Transportation cost benchmark cadence | Estimated quarterly review [ASSUMPTION] | Best-in-class: continuous real-time rate benchmarking. Gap: quarterly vs. continuous |

### Bottleneck Analysis
Transport planning velocity is primarily a **BRAIN** constraint. The BODY (DC network locations, carrier relationships, lane structure) is largely fixed. The intelligence layer that should sit above it — a global AI control tower — is embryonic (project44 was only just adopted in February 2026). The highest near-term velocity AI win is building the AI exception management and prioritization layer on top of project44 immediately, before the FIFA World Cup 2026 demand surge. This is a 60–90 day initiative with no infrastructure dependency.

### Key Discovery Questions
1. What is the current scope of project44 deployment — how many of the 60 DCs, freight forwarders, and carrier relationships are currently feeding data into the platform? [ASSUMPTION: initial deployment covers major lanes but not the full 60-DC network]
2. Is there currently a dedicated global control tower team, or is transportation exception management handled by regional logistics teams independently? [ASSUMPTION: regional fragmentation is the current norm, with no global AI-driven control tower]
3. What is the total annual transportation spend (inbound + outbound + inter-DC) across all modes, and what percentage is managed through 3PL contracts where adidas has limited rate visibility? [ASSUMPTION: significant portion of freight spend is embedded in 3PL management fees rather than itemized by lane]

---

## SC-7: FREIGHT BILL AUDIT & PAYMENT

### Current Situation
Freight bill audit and payment (FBAP) is the process of validating carrier invoices against contracted rates, identifying discrepancies, and recovering overbillings before payment. With 60 DCs (21 owned, 39 3PL-managed) [FACT], operations across 100+ countries, and a complex multi-modal carrier mix, the freight invoice volume at adidas is likely in the millions of invoices per year. [INFERENCE] Coupa is confirmed for spend management and AP automation in Latin America [FACT]; whether Coupa or a dedicated FBAP platform covers freight invoicing globally is not publicly disclosed. [ASSUMPTION: no dedicated AI-native FBAP platform is confirmed] Industry benchmarks suggest 2–5% of freight invoices contain errors, and recovery without automated auditing recovers only 30–40% of overcharges. [FACT-based industry knowledge]

### Likely Pain Points
1. **Invoice volume overwhelms manual audit capacity.** At an estimated millions of freight invoices per year across all modes and regions, manual audit is statistically sampling at best. [INFERENCE]
2. **3PL consolidated billing obscures carrier-level rate compliance.** When 3PLs bill adidas on a management fee + cost-pass-through model, validating that the underlying carrier rates match contracted rates requires access to the 3PL's carrier invoices — which may or may not be shared transparently. [ASSUMPTION]
3. **Recovery cycles are slow.** Even when overcharges are identified, the dispute and recovery cycle with carriers can take weeks to months, delaying working capital return. [INFERENCE]
4. **Cross-currency complexity adds error surface.** Operations in 100+ markets across dozens of currencies creates additional invoice error exposure beyond simple rate discrepancies. [INFERENCE]

### Value Levers Applicable
- **Efficiency:** Recover overbillings; reduce AP processing cost per invoice
- **Productivity:** Eliminate manual audit steps; automate dispute initiation
- **Quality:** Improve carrier contract compliance monitoring

### AI Opportunity
1. **AI-Native Freight Bill Audit Platform:** Deploy a specialized FBAP AI platform (e.g., Cass Information Systems, PowerFreight, or Coupa's freight audit module) that ingests carrier invoices via EDI/API, validates each line item against contracted rates and accessorial charge schedules, auto-approves clean invoices, flags discrepancies for recovery, and initiates dispute workflows automatically. At estimated freight spend of €1–2B+ annually [ASSUMPTION], a 2% average overcharge rate with 80% recovery via AI = €16–32M in annual recoveries vs. estimated €5–10M with manual audit. [ASSUMPTION on overcharge rate and recovery uplift]
2. **Carrier Performance-to-Payment Linkage:** AI system that links carrier on-time performance data (from project44) to invoice payment terms — automatically flagging invoices from carriers with recent service failures for secondary review and potential contractual penalty deduction.
3. **Automated Accessorial Charge Analysis:** ML model specifically trained to identify unjustified accessorial charges (fuel surcharges billed at incorrect rates, residential delivery charges on commercial addresses, oversize charges on standard dimensions). Industry experience: accessorial charges are the largest single source of FBAP recoveries and the hardest to catch manually. [FACT-based industry knowledge]

### Benefit Potential
**MEDIUM.** Financially compelling but not strategically differentiating. Strong financial case (~€20–40M annual recovery potential) with relatively low implementation complexity. Can be deployed without TRANS4RM dependency. Best positioned as a "quick win" to fund larger AI investments.

### Velocity Assessment

| Velocity Dimension | Adidas Current State | Best-in-Class Benchmark / Gap |
|---|---|---|
| Invoice processing cycle time | Estimated 7–14 days for manual audit and approval [ASSUMPTION] | Best-in-class AI: <24 hours for clean invoices. Gap: ~7–13 days |
| Overcharge detection rate | Estimated 30–40% of overcharges detected manually [INFERENCE] | Best-in-class AI: 90%+ detection rate. Gap: ~50pp |
| Dispute resolution cycle time | Estimated weeks [INFERENCE] | Best-in-class: <7 days with automated dispute workflows. Gap: weeks |
| Audit coverage (% of invoices) | Estimated <20% with manual sampling [INFERENCE] | Best-in-class: 100% with AI. Gap: ~80pp |
| Recovery as % of freight spend | Estimated 0.2–0.5% recovered [ASSUMPTION] | Best-in-class: 1.5–3% recovered. Gap: ~1–2pp of freight spend |

### Bottleneck Analysis
Freight bill audit velocity is a pure **BRAIN** constraint. The BODY (the freight lanes, carriers, volumes) is fixed. The audit bottleneck is entirely in the intelligence and workflow layer. This is the most straightforward AI application in the supply chain — high auditability, high confidence in financial return, low complexity. Not a strategic differentiator but an excellent source of self-funding capital for larger AI initiatives. Ship-from-store and dynamic routing are not relevant to this SC area.

### Key Discovery Questions
1. What is the current freight bill audit process — is it 100% reviewed, statistically sampled, or exception-based? And is any portion currently handled by an outsourced audit provider? [ASSUMPTION: manual sampling with low coverage is the current norm]
2. What percentage of freight invoices currently flow through Coupa vs. other AP systems, and is there a consolidated view of freight spend across all 3PLs and carriers? [ASSUMPTION: freight invoices are fragmented across multiple AP systems by region]
3. What is the current annual freight overcharge recovery amount, and what is the dispute-to-resolution cycle time with adidas's major carriers? [ASSUMPTION: recovery is well below industry best practice and dispute cycles are slow]

---

## SC-8: RETURNS & REVERSE LOGISTICS

### Current Situation
Returns in apparel and footwear are a structural cost center. Industry return rates for e-commerce apparel/footwear typically run 20–30%. [FACT-based industry knowledge] adidas's DTC e-commerce was €4.3B in FY2025. [FACT] At a 20% return rate, returns volume could be 8–10M+ units per year on DTC alone. [INFERENCE] The processing of returns involves: receipt at DC, condition assessment, quality triage (resalable, refurbishable, outlet/liquidate, donate/destroy), restock, and credit issuance. GK OmniPOS and RFID are confirmed at stores for inventory accuracy [FACT], which also supports in-store returns processing. However, a specific returns processing AI capability is not confirmed. [ASSUMPTION] Mantova Italy DC (700+ robots, Kuehne+Nagel operated) [FACT] likely handles EU returns at scale, but the returns processing workflow automation level is not disclosed.

### Likely Pain Points
1. **Returns condition assessment is manual and slow.** Without computer vision or AI-assisted triage, each returned item requires a human assessor to examine condition, determine next disposition, and route the item appropriately. [INFERENCE]
2. **Return inventory is not available for resale until processed.** Estimated 3–7 day returns processing cycle means returned inventory is not available for new orders during that window — reducing effective inventory availability and increasing stockout risk. [INFERENCE]
3. **Return fraud detection is likely rule-based.** Identifying suspicious return patterns (wardrobing, price arbitrage, counterfeit returns) with rule-based systems generates both false positives and false negatives. [INFERENCE]
4. **Return reason analytics are underdeveloped.** If return reason data is captured but not systematically analyzed against product design feedback loops, adidas is losing a high-value signal for quality improvement and demand planning refinement. [ASSUMPTION]

### Value Levers Applicable
- **Efficiency:** Reduce returns processing cost; accelerate inventory restock
- **Quality:** Improve return reason analytics as product quality feedback loop; reduce return rates through size/fit AI
- **Velocity:** Compress returns-to-resalable inventory cycle from days to hours
- **Productivity:** Reduce DC labor for manual returns triage

### AI Opportunity
1. **AI-Powered Returns Triage (Computer Vision + RFID):** Computer vision cameras at DC returns receiving docks assess item condition automatically — identifying defects, contamination, and completeness — and route items to the correct disposition path without human triage. Combined with RFID, inventory is updated to resalable status within hours of receipt rather than days. Industry benchmarks: 60–70% reduction in returns processing labor cost; 2–3 day reduction in restock cycle time. [INFERENCE on current processing time]
2. **Return Fraud Detection ML Model:** Train a model on historical return patterns at the customer, SKU, and transaction level to score each return request for fraud probability. High-risk returns are held for secondary review; low-risk returns are auto-approved and trigger immediate replacement or credit.
3. **Return Reason Intelligence Feedback Loop:** NLP pipeline (leveraging existing MosaicML infrastructure) that classifies free-text return reason comments at scale, aggregates patterns by SKU/colorway/size, and feeds insights directly into the product design and demand planning teams. Connected to existing 2M+ product review processing pipeline. [FACT foundation: MosaicML pipeline at 91.67% cost reduction already operational]
4. **Size & Fit AI at Point of Purchase:** ML model trained on purchase + return patterns to generate personalized size recommendations at product page level ("customers with your purchase history typically order a half-size up in this style"). Estimated return rate reduction: 3–5pp from size/fit AI in footwear. At €4.3B DTC and a 20% return rate, a 3pp reduction = €129M less in returns-related handling cost and working capital lock-up. [ASSUMPTION on addressable return rate reduction]

### Benefit Potential
**MEDIUM-HIGH.** The size/fit AI case alone is potentially €100M+ in returns cost reduction and working capital improvement at scale. The infrastructure is mostly available (MosaicML NLP, Databricks, RFID). The return reason intelligence loop also feeds product quality improvement — making it a Quality lever with cross-functional value.

### Velocity Assessment

| Velocity Dimension | Adidas Current State | Best-in-Class Benchmark / Gap |
|---|---|---|
| Returns processing cycle (receipt to resalable inventory) | Estimated 3–7 days [ASSUMPTION] | Best-in-class with AI/CV: <24 hours. Gap: 2–6 days |
| Return credit/replacement issuance | Estimated 3–5 business days [INFERENCE] | Best-in-class: <24 hours automated. Gap: 2–4 days |
| Return reason analytics cycle | Estimated quarterly reporting [ASSUMPTION] | Best-in-class: real-time NLP dashboard updated daily. Gap: weeks |
| Fraud detection latency | Estimated post-return review (days) [ASSUMPTION] | Best-in-class: real-time scoring at return request submission. Gap: days |
| Size recommendation accuracy | Not disclosed [ASSUMPTION: generic size charts] | Best-in-class (Zalando, ASOS): ML-personalized size recommendations per customer. Gap: potentially significant |

### Bottleneck Analysis
Returns velocity is a **BRAIN** constraint. The BODY (DC returns docks, conveyor systems, storage) is adequate; the intelligence layer that should automate triage, accelerate restock, and close the feedback loop to product design is not confirmed as deployed. The highest near-term velocity AI win is the computer vision returns triage combined with the size/fit AI at purchase — the latter prevents returns before they occur, compressing the entire returns cycle at the source. The return reason NLP pipeline is immediately deployable on the existing MosaicML infrastructure.

### Key Discovery Questions
1. What is the current e-commerce return rate by product category (footwear, apparel, accessories) and by channel (adidas.com, wholesale partner returns), and what is the most frequently cited return reason? [ASSUMPTION: size/fit is the leading return reason for footwear, which is the highest AI-addressable category]
2. What is the current end-to-end returns processing time from carrier receipt at DC to inventory restock availability, and is the bottleneck physical handling or system update latency? [ASSUMPTION: the bottleneck is manual condition assessment before system update]
3. Is return reason data currently feeding into any structured feedback loop to the product design or demand planning teams, or is it collected but not systematically analyzed? [ASSUMPTION: return reason data is captured but not systematically connected to product or planning decisions]

---

# PART B: NON-SUPPLY-CHAIN OPPORTUNITIES

## Marketing & Content
adidas spends ~€3B/year on marketing (~12–13% of revenue) [FACT] and already processes 2M+ product reviews/year through its MosaicML GenAI pipeline at 91.67% cost reduction achieved. [FACT] The next frontier is scaling GenAI to content production itself — personalized campaign assets, localized copy variants, and social media content at the speed of cultural trends. The immediate priority is FIFA World Cup 2026 content: with 90 days to peak, an AI content factory that generates localized, channel-specific, athlete-linked creative variants in hours rather than weeks could be decisive for North America market activation. AI-driven attribution modeling across the €3B marketing spend is also high-value — identifying which spend generates DTC conversion vs. wholesale pull vs. brand equity, and dynamically reallocating budget in-season. Value levers: **Productivity** (content at scale), **Efficiency** (marketing ROI optimization), **Growth** (faster cultural moment capture).

## Digital Commerce & adiClub Personalization
adidas.com generates ~€4.3B in DTC revenue with adiClub members converting at 3× the rate of non-members. [FACT] The AI value is in deepening personalization: AI-driven product recommendations (leveraging purchase history, RFID store behavior, adiClub behavioral signals, and MosaicML review intelligence), dynamic pricing for outlet and clearance inventory within guardrails set by Gulden's full-price discipline mandate, and next-best-action recommendation engines that guide adiClub members toward higher-value engagement. The Amazon Buy with Prime MCF integration [FACT] creates a speed advantage for Prime members but risks commoditizing the adidas.com experience — AI personalization is the counter-strategy to retain DTC distinctiveness. Value levers: **Growth** (conversion lift), **Efficiency** (promotional spend precision), **Quality** (member experience depth).

## Finance & FP&A Analytics
SAP S/4HANA Central Finance went live in November 2023 [FACT] and Coupa is deployed for spend management. [FACT] The AI opportunity is in FP&A analytics: scenario planning models for the CFO's 2028 >10% EBIT margin target, automated variance analysis against the financial plan, real-time P&L by channel/region/product line, and tariff impact modeling. The CFO owns both Technology and Supply Chain [FACT], meaning a unified AI dashboard connecting supply chain cost drivers to P&L outcomes would directly serve the economic buyer of all AI investment. A tool that helps Ohlmeyer see the 2028 EBIT bridge in real time has direct budget justification appeal and fast-path sponsorship potential. Value levers: **Productivity** (analyst time reduction), **Quality** (decision speed and accuracy).

## Engineering & Developer Productivity
GitHub Copilot is deployed at 85% adoption across ~700 engineers with a confirmed 20–25% productivity improvement. [FACT] The AI value here is acceleration: the TRANS4RM S/4HANA deployment (2025–2027) is the most complex technology program adidas has run in a decade, and engineering productivity gains directly translate to faster TRANS4RM completion — which unlocks every AI initiative that depends on clean S/4HANA master data. AI-assisted testing, automated SAP configuration validation, and AI-driven regression testing would reduce TRANS4RM deployment risk. This is not a new AI initiative — it is amplifying an existing one with specific focus on TRANS4RM acceleration. Value levers: **Productivity** (engineer output), **Velocity** (TRANS4RM timeline compression), **Quality** (deployment error reduction).

## Human Resources
Deloitte SkillSenseAI is deployed for job architecture and skills mapping. [FACT] The next step is connecting skills intelligence to talent decisions: AI-driven internal mobility recommendations, AI-assisted workforce planning that models the skills gap created by TRANS4RM's shift from SAP R/3 to S/4HANA, and predictive attrition modeling to identify flight-risk employees in critical roles (TRANS4RM program managers, AI engineers, supply chain planners). The workforce planning case is particularly relevant: TRANS4RM requires entirely new skill sets that the current workforce may partially lack. AI can model this gap and recommend build/buy/borrow decisions 12–18 months ahead. Value levers: **Productivity** (talent utilization), **Quality** (retention of critical skills), **Efficiency** (hiring cost reduction).

---

# VELOCITY SUMMARY TABLE

| SC Area | Current Speed Position | AI Speed Improvement Potential | Bottleneck Type | Top AI Lever |
|---|---|---|---|---|
| SC-2: Demand & Supply Planning | LAGGING — demand sensing 2–4 week lag; monthly S&OP cycles | HIGH — demand sensing to <48 hours; allocation adjustment to <24 hours | BRAIN | Social signal demand sensing + AI allocation optimizer |
| SC-3: Warehousing & Ship-from-Store | MODERATE at flagship DCs (2hr order-to-pack); WEAK on ship-from-store | HIGH — 1-day delivery in top 30 US metros via ship-from-store orchestration | BODY + BRAIN (store network exists; orchestration missing) | Ship-from-store AI orchestration engine |
| SC-5: Outbound / Last Mile | LAGGING — 3–7 day standard US; losing to Amazon 1–2 day | HIGH — close delivery gap via ship-from-store + predictive promise | BODY + BRAIN | Ship-from-store last mile + predictive delivery promise |
| SC-1: Procurement & Tariff Intelligence | LAGGING — tariff response weeks; OTIF signal lagging | HIGH — tariff response to 48–72 hours; OTIF to near-real-time | BRAIN | Tariff intelligence AI agent on Databricks |
| SC-4: Inbound Transportation Visibility | IMPROVING — project44 adopted Feb 2026; not yet fully activated | MEDIUM-HIGH — exception detection to <4 hours; ETA accuracy to 90%+ | BRAIN | project44 AI scenario planning activation |
| SC-8: Returns & Reverse Logistics | LAGGING — 3–7 day returns processing; limited size/fit intelligence | MEDIUM-HIGH — returns to <24 hours; reduce return rate 3–5pp | BRAIN | Size/fit AI at purchase + CV returns triage |
| SC-6: Transport Planning & Control Tower | WEAK — project44 just adopted; control tower embryonic | MEDIUM — exception cycle to <8 hours; inter-DC rebalancing to daily | BRAIN | AI control tower on project44 |
| SC-7: Freight Bill Audit | WEAK — manual audit, low coverage | MEDIUM — 100% invoice coverage; 90%+ overcharge detection | BRAIN | AI-native FBAP platform deployment |
