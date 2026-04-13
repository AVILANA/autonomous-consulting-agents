# TJX Companies — Routing Decisions
## Phase 5 Job 1: April 2026 (Revised — incorporates updated tech_ops_raw.md)
## Source: company_snapshot.md, benchmark_table.md, body_brain_diagnosis.md, tech_ops_raw.md

---

## TECHNOLOGY GAP VERIFICATION — MANDATORY CORRECTIONS TO PRIOR PHASE ASSUMPTIONS

Before routing decisions can be finalized, Phase 4 assumptions must be corrected against the updated tech_ops_raw.md.

**Correction 1 — WMS:**
body_brain_diagnosis.md states "No confirmed WMS — CONFIRMED (absence)."
tech_ops_raw.md (updated) confirms: **Manhattan WMS CONFIRMED** (selected 2016, displacing legacy). **Manhattan WMS upgrade evaluation CONFIRMED** (November 2025 — active procurement signal for likely Manhattan Active WMS cloud migration).

Impact: DC provocations CANNOT claim TJX has no WMS. The framing must shift from "absent WMS" to "WMS in upgrade evaluation — is the new architecture designed to include automation hardware in the four new DCs under construction?"

**Correction 2 — TMS:**
value_levers.md (Area 6) states "No confirmed TMS — CONFIRMED absence."
tech_ops_raw.md confirms: TMS CONFIRMED to exist. Freight Payment Coordinator role: "Authorizes payment of over $700 million in domestic and international logistics costs annually" through the TMS. Transportation Planning Analyst role confirms TMS configuration and load building. Oracle OTM is LIKELY (OTM User Conference 2023 attendance). EDI Specialist TMS role confirmed in Canada.

Impact: Transport provocations CANNOT claim TJX has no TMS. The framing must focus on whether the TMS (processing $700M+ in freight) has automated invoice audit logic or relies on manual processes.

**Correction 3 — Freight Audit:**
value_levers.md (Area 7) implies absence. tech_ops_raw.md confirms: freight audit function EXISTS internally — dedicated Freight Payment Specialist role + carrier invoice audit + routing guide chargeback management. No confirmed third-party freight audit provider (Cass, Trax, nVision). Appears internally managed via TMS-embedded logic.

Impact: Freight provocation must be about SCALE AND AUTOMATION of the existing audit process — not about absence of a function.

**Correction 4 — Supply Chain Visibility:**
FourKites real-time tracking LIKELY — TJX's Chief Logistics Officer (CLO) Raina Avalon is listed on FourKites' Executive Customer Advisory Board. Advisory board seats are reserved for paying customers.

Impact: Cannot claim absence of tracking visibility. Can claim the gap between having tracking data and using it to drive forward planning decisions.

---

## CONDITION FLAG: HIGH GROWTH

**Source:** company_snapshot.md — explicitly flagged.

TJX: $60.4B revenue (FY2026, +7% YoY), record 11.9% operating margin, $4.92B FCF (FY2026), 146 net new stores planned FY2027, CapEx guidance $2.2B–$2.3B (FY2027). Long-term target: 7,000 stores (current 5,214 — gap of 1,786 stores).

**Routing instruction:** All 5 provocations must connect to "can TJX sustain 11.9%+ operating margins at 7,000 stores, or will infrastructure bottlenecks erode unit economics as volume grows?" The frame is challenge-from-success, not challenge-from-weakness.

No FINANCIAL DISTRESS flag. No cost-cutting language. Every efficiency argument is about protecting and extending a record that is already working.

---

## STANDOUT PEER FLAG: ROSS STORES — OPERATIONAL BENCHMARK

**Source:** peer_set.md, benchmark_table.md

Ross Stores: **12.2% operating margin (FY2025)** on **$21.1B revenue** — higher than TJX at **11.9% (FY2026)** on **$60.4B**. At 2.7x less scale, Ross outperforms TJX on consolidated margin. Standard scale economics says the larger operator should win.

Three explanations (from benchmark_table.md):
1. TJX International at 7.3% drags consolidated — Marmaxx alone runs 14.4%, far above Ross
2. Multi-banner overhead (8 banners, 9 countries) not present in Ross
3. Ross investing $1.1B FY2026 CapEx including DC automation; TJX at 2.4% CapEx intensity vs. Ross 5.2%

**Routing instruction:** Ross must be central to at least two provocations. The anomaly (larger operation, lower consolidated margin) is the most commercially uncomfortable fact in the peer set.

**Burlington — DC automation benchmark:**
Burlington's new highly automated DC in Savannah, GA opens in 2026. Burlington CapEx intensity: 8.9% of revenue vs. TJX 2.4% — 3.7x more intensive, explicitly in automation. Burlington is the primary peer evidence for DC automation provocation.

---

## BODY VS. BRAIN ROUTING (CORRECTED)

**Source:** body_brain_diagnosis.md + tech_ops_raw.md corrections above

| Stream | Body State | Brain State (CORRECTED) | Routing |
|---|---|---|---|
| DC Operations | Expanding: 4 new DCs (El Paso 1.6M+ sq ft, Sunbridge FL 1.93M sq ft, Ohio $170M, NJ 1.3M sq ft) | WMS CONFIRMED (Manhattan, 2016) + UPGRADE EVALUATION (Nov 2025). Automation hardware uncommitted. | Provocation: automation design in new DCs — this is the open window, not WMS absence |
| Buyer Intelligence | Healthy: 1,400 buyers, global vendor relationships | No AI deal-scoring confirmed. Oracle EBS deal history available. India GCC Data & Automation growing. | Provocation: AI augmentation during peak deal flow — pure brain, start immediately |
| Freight / Transport | TMS CONFIRMED ($700M+ annual freight). Internal audit function confirmed. | No freight audit AUTOMATION confirmed. Manual human review at $700M+ scale. | Provocation: automated invoice audit on existing process — scale the brain, not install it |
| Store Allocation | Oracle Retail Allocation CONFIRMED. | No AI new-store demand bootstrapping. 146 new stores in FY2027. | Provocation: allocation accuracy for new stores — improve the brain layer on existing allocation system |

**Phase Two body priority:**
DC automation hardware design in new facilities (NJ, El Paso, Sunbridge FL, Ohio) must be decided during the current construction planning phase — estimated 12-month window before concrete locks automation prerequisites. This is the one time-sensitive body decision. All other improvements are pure brain, no body prerequisite.

---

## SUPPLY CHAIN MODEL IDENTIFICATION — MANDATORY

**(1) What makes this company's supply chain unique?**
TJX buys excess, cancelled, and overstock inventory opportunistically from ~21,000 vendors across 100+ countries. No forward factory orders. No stable SKU (Stock Keeping Unit) catalog. No replenishment cycle. Every lot is different. The supply chain is driven by vendor surplus availability, not consumer demand forecasts. The full flow is: vendor excess exists → buyer accepts or rejects deal → DC receives non-standard lot → Oracle Retail Allocation sends product to stores → store sells with no reorder possible. Every decision is one-shot.

**(2) What is the core operational differentiator?**
The speed and quality of the buying decision. TJX's 1,400 buyers evaluate deals from 21,000 vendors daily. The difference between a 45% discount and a 40% discount on ~$41.7B estimated FY2026 COGS = ~$2B in gross profit. Buying quality — markon achieved, markdown avoided — is where gross margin is made or lost.

**(3) Three most critical daily supply chain decisions:**
1. Accept, reject, or price a vendor deal — multiplied across 1,400 buyers, this is where gross margin is set
2. Which stores receive which portion of which lot (allocation) — determines markdown rate and cash conversion speed
3. How fast to process non-standard incoming lots through DCs — determines time from purchase commitment to store shelf and cash

**(4) Supply chain processes that handle the most money:**
- Buying / vendor negotiation: ~$41.7B estimated COGS (FY2026)
- DC receiving and processing: estimated $1B–$2B in DC labor embedded in COGS [INFERENCE — MODERATE]
- Inbound + outbound freight: estimated $1B–$3B total [INFERENCE — MODERATE — not separately disclosed]; $700M+ confirmed processed through TMS domestically and internationally

**Connection test:** Every provocation must connect to item 2, 3, or 4 above.
- P1 (DC automation) → Decision 3 + Process 2 ✓
- P2 (Buyer intelligence) → Decision 1 + Process 1 ✓
- P3 (Freight audit) → Process 3 ✓
- P4 (Allocation) → Decision 2 + Process 1 ✓
- P5 (Synthesis) → all ✓

---

## ROUTING SUMMARY TABLE

| # | Provocation Topic | Routing Basis | Key Peers | Core Urgency |
|---|---|---|---|---|
| P1 | DC automation design in new facilities | HIGH GROWTH + 12-month construction window | Burlington (highly automated, 8.9% CapEx) + Ross ($1.1B CapEx) | Automation designed in = baseline cost. Retrofit after opening = 3–5x cost. |
| P2 | Buyer deal-ranking during peak deal flow | HIGH GROWTH + brain gap + tariff windfall | Ross (12.2% margin at 2.7x less scale — productivity gap) | CEO calls this the best buying environment in company history. Buyer bandwidth is the real constraint. |
| P3 | Freight invoice audit automation | HIGH GROWTH + $700M+ confirmed freight at manual audit scale | DHL-managed TJX Europe (internal contrast — Europe's logistics is systematically managed; US is manual) | $700M+ in confirmed freight payments with human-intensive audit across multi-carrier, 9-country network |
| P4 | New store allocation accuracy | HIGH GROWTH + 146 new stores/year with zero demand history | Inditex (8–9x inventory turns; allocation precision) + lower markdowns as confirmed TJX margin driver | 146 new stores this year, each with one first allocation and no reorder if it's wrong |
| P5 | Synthesis: four gaps → margin sustainability | All of P1–P4 + 7,000-store commitment | Ross (margin benchmark — same model, higher margin at lower scale) | $365M+ total annual value; 60bp margin improvement; connects to sustaining 11.9% through 7,000-store expansion |

**Financial lever distribution:** COGS Avoidance (P1) + Gross Margin Improvement (P2) + OPEX Reduction (P3) + Gross Margin Improvement/Working Capital (P4) + Operating Margin Expansion (P5) = 4 distinct financial levers ✓
**Operational lever distribution:** Throughput/Process Efficiency (P1) + Decision Cycle Compression (P2) + Planning Cycle Speed (P3) + Production-to-Shelf Velocity (P4) + Response Latency (P5) = 5 distinct operational levers ✓
**Supply chain coverage:** Transport/freight (P3) ✓ + Sourcing/procurement (P2) ✓ + DC operations/inventory flow (P1, P4) ✓

---

*Sources: company_snapshot.md, benchmark_table.md, body_brain_diagnosis.md, tech_ops_raw.md, value_levers.md, stream_ranking.md, peer_set.md. No web search used.*
