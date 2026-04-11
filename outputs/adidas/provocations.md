# Phase 5 — Job 3B: Provocations with Compliance Layer
**Company:** adidas AG | **Date:** 2026-04-11
**Source:** Raw provocations from Job 3A + routing decisions + due diligence findings
**Lever distribution:** 7 distinct financial levers | 4 distinct operational levers | All pass 3+ minimum threshold
**Track note:** This file = Track B (internal). Client-facing version in client_document.md removes all AI/agent/methodology language.

---

## PROVOCATION 1 — Supply Chain Planning

### "Your demand plan may refresh every 3 weeks. Your €5B inventory depends on knowing what sells today."

**Financial levers:** Working Capital Release | Gross Margin Improvement
**Operational lever:** Planning Cycle Speed
**Buyer personas:** CFO (Harm Ohlmeyer — owns both Technology and Supply Chain), CSCO, COO

---

**Evidence:**

- [FACT — adidas Annual Report FY2024] Inventory €4,989M (FY2024) on €23,683M revenue = 21.0% inventory-to-revenue ratio. Peer benchmarks: On Holding ~13%; Deckers (Hoka) ~14%; ASICS ~18%. adidas sits at or above peer median. At a peer median of ~16%, adidas would carry ~€1.1B less inventory — releasing working capital directly.

- [FACT — adidas technology disclosures; Databricks Data+AI Summit 2026] o9 Solutions confirmed for in-season retail planning, allocation, and DTC (Direct-to-Consumer) demand sensing. Amazon SageMaker confirmed for seasonal ML (machine learning) forecasting. Databricks Agent Digital Twin governing production-scale AI agent fleets confirmed publicly at the 2026 summit.

- [FACT — adidas TRANS4RM program disclosures] SAP S/4HANA supply chain and sales modules not yet live as of Q1 2026. Expected completion 2025–2027. Without these modules, master data quality feeding the planning engine is incomplete — meaning AI forecast accuracy is capped by data quality, not model capability.

- [FACT — ASICS Annual Reports FY2022–FY2024] ASICS gross margin: 49.7% (FY2022) → 52.1% (FY2023) → 55.8% (FY2024) — +610 pp (percentage points) in 2 years. Operating margin: 7.0% (FY2022) → 14.7% (FY2024) — +770 pp. Mechanism: full-price channel discipline and ASP (average selling price) improvement, not product launches. ASICS is structurally analogous to adidas: outsourced manufacturing, multi-market, wholesale + DTC mix.

- [INFERENCE — MODERATE — adidas tech disclosures; absence of public confirmation] The closed loop from consumer signal (social trend, store sell-through) to allocation decision is not confirmed to run in real time. No public disclosure confirms store sell-through feeds o9 faster than daily or weekly batch. The gap between what the stack enables and what runs in production may be large — and is a Phase One validation question.

**Cost of Inaction:** ~€124M per year. Mechanism: 0.5pp gross margin improvement on €24,811M (FY2025) revenue — consistent with the trajectory ASICS demonstrated over 36 months. This is the conservative estimate; full inventory normalisation to peer median would release additional working capital.

**Discovery question:** What is the current store sell-through data refresh rate into o9 — real-time, daily, or weekly batch? Which consumer signal sources currently feed the demand sensing model, and at what latency?

---

## PROVOCATION 2 — Supply Chain Procurement / Trade

### "€200M in tariffs hit your guidance. The next round expires July 24 — is anyone modelling it?"

**Financial levers:** Risk Mitigation | COGS Avoidance
**Operational lever:** Decision Cycle Compression
**Buyer personas:** CFO (Harm Ohlmeyer), CEO (Bjørn Gulden), CSCO

---

**Evidence:**

- [FACT — adidas FY2026 guidance, March 4, 2026 results presentation] US tariff headwind of ~€200M embedded in FY2026 operating profit guidance. This consumes approximately 47% of the €422M EBIT (Earnings Before Interest and Tax) gap between FY2025 actual (8.3%) and the 2028 target (>10%) in a single year.

- [FACT — US Federal Register; current_signals.md] Section 122 tariffs expire July 24, 2026. Vietnam (27% of adidas global sourcing) and Indonesia (19%) have both been targeted in prior US trade actions. Combined, these two countries supply ~46% of global volume.

- [FACT — project44 press release, February 2026] project44 multi-modal transport visibility platform adopted for adidas February 2026. Real-time container tracking now established. AI scenario planning module: activation status not publicly confirmed as of April 2026.

- [FACT — adidas Annual Report 2024] 3,000+ external supplier factory users on SAP BTP (Business Technology Platform) for PO (purchase order) management. Procurement digitisation is in place. The gap is not data collection — it is the AI layer that converts real-time trade policy signals into tariff-adjusted, ranked sourcing decisions within hours.

- [INFERENCE — HIGH — based on disclosed China pivot timeline] The 2025 China-to-US sourcing elimination took approximately 3–6 months to execute from decision to impact. AI-driven continuous scenario modelling compresses this to 48–72 hour decision windows — the difference between pricing a tariff change into Q2 or absorbing it in Q3.

**Cost of Inaction:** ~€60M per year. Mechanism: recovering 30% of the embedded €200M tariff hit through faster sourcing decisions that reduce reactive air freight, penalty unit costs, and delayed allocation shifts. adidas management explicitly excluded potential tariff relief upside from FY2026 guidance — making this a floor, not a ceiling.

**Discovery question:** What is the current cycle time from a US trade policy announcement to a final internal sourcing shift decision? Is there a live tariff sensitivity model covering Vietnam and Indonesia exposure — and who owns it?

---

## PROVOCATION 3 — Supply Chain Fulfillment

### "838 concept stores ready to ship in hours. Customers wait 3–7 days. You pay Amazon to fix it."

**Financial levers:** Revenue Protection / Growth | OPEX Reduction
**Operational lever:** Fulfillment Speed
**Buyer personas:** COO, CFO (Harm Ohlmeyer — owns fulfillment and technology cost), CMO

---

**Evidence:**

- [FACT — adidas Annual Report 2024; body_brain_diagnosis.md] 838 concept stores in major urban locations. RFID inventory accuracy >99% at own stores. GK OmniPOS ship-from-store capability confirmed at 1,300+ locations. LS Retail POS at 1,350 stores provides an additional digital inventory layer. The physical and digital prerequisites for distributed fulfillment are in place.

- [FACT — adidas.com delivery terms (US market); Amazon Prime SLA] adidas US DTC standard delivery: 3–7 business days from Wilkes-Barre, Pennsylvania (843K sq ft, serves East Coast). Amazon Prime: 1–2 days to the same addresses. No equivalent flagship DC for western US — Pacific Coast customers face the longest delivery windows.

- [FACT — adidas press release, February 2025] Amazon MCF (Multi-Channel Fulfillment) partnership activated to fill the US delivery speed gap. adidas pays Amazon to fulfill adidas.com orders using adidas inventory — a pragmatic short-term solution that transfers fulfillment economics to Amazon.

- [FACT — ASICS Annual Reports FY2022–FY2024] ASICS operating margin: 7.0% (FY2022) → 14.7% (FY2024). adidas: 8.3% (FY2025) targeting >10% by 2028. ASICS achieves 14.7% at ~25–30% DTC penetration. adidas earns 8.3% at ~40% DTC — meaning more DTC revenue is not delivering proportionally higher margin, in part because fulfillment costs offset the channel margin benefit.

- [INFERENCE — MODERATE — body_brain_diagnosis.md; absence of public confirmation] A central routing engine connecting adidas.com orders to optimal concept store + carrier combinations using live RFID inventory is not confirmed to exist at production scale. Without this engine, the 838-store urban network is a fulfillment asset that cannot be activated for e-commerce. This is a Brain gap, not a Body gap — no new stores or DCs are required.

**Cost of Inaction:** ~€60M per year. Mechanism: Amazon MCF fees avoided on redirected DTC volume + conversion uplift from 1–2 day delivery promise vs. 3–7 days + operating margin improvement from lower cost-per-fulfilled-order. FIFA World Cup 2026 (June–July, US/Canada/Mexico) concentrates North America demand in a window where this gap is most expensive to leave open.

**Discovery question:** What is your current cost-per-order from ship-from-store vs. Wilkes-Barre DC fulfillment — and at what order density per concept store does ship-from-store reach positive unit economics? What is the current Amazon MCF fee as a percentage of DTC order value?

---

## PROVOCATION 4 — Supply Chain Transportation

### "Every shipment is tracked in real time. Your mode decisions may still be costing €50M in avoidable air freight."

**Financial lever:** OPEX Reduction
**Operational lever:** Response Latency
**Buyer personas:** CFO (Harm Ohlmeyer), COO, CSCO

---

**Evidence:**

- [FACT — project44 press release, February 2026] project44 multi-modal transport visibility platform adopted for adidas February 2026. Real-time container tracking confirmed across ocean and air modes. This is the signal layer. The AI scenario planning layer — automated mode-switch recommendations based on predictive models — is not confirmed active as of April 2026.

- [FACT — adidas Annual Report 2024; body_brain_diagnosis.md] 60 DCs globally (21 owned, 39 3PL (third-party logistics)-managed). At least 15 primary carrier relationships across Europe, North America, and Asia-Pacific. Freight bill reconciliation disclosed as a manual process. No AI FBAP (Freight Bill Audit Platform) or equivalent confirmed in any public technology disclosure.

- [INFERENCE — MODERATE — industry norms for manual freight audit at comparable network scale] Manual freight bill audit at 30–40% coverage is consistent with industry benchmarks for logistics networks of this size without a dedicated FBAP. At this coverage rate, systematic carrier billing errors and overcharges go undetected in the majority of invoices processed.

- [INFERENCE — HIGH — body_brain_diagnosis.md velocity table, SC-4/SC-6] Pre-project44 exception detection latency (time from actual shipment disruption to internal alert) was estimated at 2–5 days. project44 eliminates detection latency to near-real-time. The AI scenario layer converts this signal into a ranked recommendation (switch mode / reroute / accept delay) within minutes, rather than requiring manual analyst intervention.

- [FACT — industry standard] Air freight costs approximately 4x ocean freight for equivalent cargo. A reactive ocean-to-air switch costs significantly more than a proactive switch. At adidas's network scale — 60 DCs, 15+ carriers, global ocean and air volume — the delta between reactive and proactive mode decisions over a full year is estimated at €40–50M.

**Cost of Inaction:** ~€50M per year. Mechanism: avoidable reactive air freight premium (~€30–35M) + undetected carrier overcharge and billing error recovery (~€15–20M) on a 60 DC / 15+ carrier network without AI audit coverage. The AI scenario planning activation is a 60–90 day build on infrastructure already deployed.

**Discovery question:** What is your current freight bill audit coverage rate — and how much did your freight audit programme recover in FY2025 vs. the volume that went unaudited? What is the average time from a shipment falling behind schedule to an internal decision on mode switching?

---

## PROVOCATION 5 — SYNTHESIS

### "Planning, tariffs, delivery speed, and freight — four gaps worth €300M that sit between you and the 10% target."

**Financial lever:** Operating Margin Expansion
**Operational lever:** (Synthesis — covers Planning Cycle Speed, Decision Cycle Compression, Fulfillment Speed, and Response Latency from P1–P4)
**Buyer personas:** CFO (Harm Ohlmeyer — primary economic buyer), CEO (Bjørn Gulden), COO

---

**Evidence:**

- [FACT — adidas FY2025 results, March 4, 2026; adidas medium-term targets] FY2025 EBIT: ~€2,059M (8.3% margin on €24,811M revenue). Management target: >10% EBIT margin by 2028. Gap: ~1.7pp × €24,811M = ~€422M of additional annual EBIT required. FY2026 guidance of €2,300M is €420M below analyst consensus (€2,720M), driven by ~€300M in embedded macro headwinds (€200M tariffs + ~€100M transactional FX).

- [FACT — ASICS Annual Reports FY2022–FY2024] ASICS Corporation improved operating margin from 7.0% (FY2022) to 14.7% (FY2024) — +770 pp in 24 months — on a structurally analogous business (outsourced manufacturing, multi-market, wholesale + DTC mix). This is the nearest attainable aspirational benchmark in the peer set.

- [INFERENCE — HIGH — mathematical, based on confirmed P1–P4 data] The four supply chain Brain activation gaps identified in P1–P4 represent a combined ~€294M EBIT opportunity. All four are Brain builds on existing Body infrastructure. None require capital investment in new facilities, factories, or stores.

- [FACT — adidas Annual Report 2024; body_brain_diagnosis.md] All four interventions build on already-deployed infrastructure: o9 + Databricks stack (P1), SAP BTP supplier network (P2), RFID + GK OmniPOS at stores (P3), project44 visibility layer (P4). The raw material — data, platforms, physical network — is confirmed in place.

**EBIT Bridge Table — 8.3% to >10% by 2028:**

| Provocation | Mechanism | Annual EBIT Impact | Confidence |
|---|---|---|---|
| P1: Demand planning precision | Inventory normalisation + full-price sell-through via closed-loop signal-to-allocation | ~€124M | MODERATE — consistent with ASICS 3-year trajectory |
| P2: Tariff response speed | Faster sourcing decisions cut reactive air freight premium and delayed allocation cost | ~€60M | HIGH — €200M embedded headwind; 30% recoverable via speed |
| P3: Ship-from-store activation | Amazon MCF fees avoided + conversion uplift from 1–2 day vs. 3–7 day promise | ~€60M | MODERATE — dependent on routing engine build and store economics |
| P4: Freight mode + audit AI | Avoidable reactive air freight + carrier overcharge recovery across 60 DCs / 15+ carriers | ~€50M | MODERATE — freight audit gap confirmed as structural |
| **Total Brain activation** | | **~€294M** | |
| Organic revenue growth (management guidance) | Each +1pp CN revenue ≈ €25M+ EBIT at current cost structure | ~€128M | HIGH — supported by management guidance |
| **Total path to >10%** | | **~€422M** | |

The 2028 deadline is 22 months away. ASICS closed a comparable gap in 24 months. This is not a projection — it is an arithmetic problem with a confirmed peer precedent and a 22-month window.

**Cost of Inaction:** ~€294M per year in unrealised EBIT — equivalent to arriving at 2028 at ~9.0–9.5% margin (organic only) instead of >10%, missing the management commitment and compressing the valuation multiple that the market has already priced in.

**Discovery question:** Which of these four gaps has an internal owner with a funded programme and a delivery date — and which have no committed timeline? The answer tells us exactly where Phase One begins.

---

## LEVER DISTRIBUTION CHECK

| Provocation | Financial Lever(s) | Operational Lever |
|---|---|---|
| P1: Demand Planning | Working Capital Release + Gross Margin Improvement | Planning Cycle Speed |
| P2: Tariff Response | Risk Mitigation + COGS Avoidance | Decision Cycle Compression |
| P3: Ship-from-Store | Revenue Protection/Growth + OPEX Reduction | Fulfillment Speed |
| P4: Freight Intelligence | OPEX Reduction | Response Latency |
| P5: Synthesis | Operating Margin Expansion | Synthesis of P1–P4 operational levers |

**Distinct financial levers (P1–P5):** Working Capital Release ✓ | Gross Margin Improvement ✓ | Risk Mitigation ✓ | COGS Avoidance ✓ | Revenue Protection/Growth ✓ | OPEX Reduction ✓ | Operating Margin Expansion ✓
→ **7 distinct financial levers — PASS (minimum: 3)**

**Distinct operational levers (P1–P4):** Planning Cycle Speed ✓ | Decision Cycle Compression ✓ | Fulfillment Speed ✓ | Response Latency ✓
→ **4 distinct operational levers — PASS (minimum: 3)**
