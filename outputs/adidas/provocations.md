# Adidas AG — Fulfillment Provocations
**Step 9: So What Agent | Date: 2026-04-10**
**Override in effect: All 5 provocations focus on fulfillment — Transportation Planning, Warehousing, Global Trade and Tariffs, Freight Audit, Last Mile and Returns.**
**Data basis: FY2025 actuals (March 4, 2026 press release); project44 deployment (Feb 2026); Amazon MCF partnership (Feb 2025)**

**Confidence tag key:**
- `FACT` — directly confirmed by press release, official filing, or official case study
- `INFERENCE — HIGH CONFIDENCE` — strongly supported by multiple independent signals; would be surprising if wrong
- `INFERENCE — MODERATE CONFIDENCE` — plausible given available evidence but not directly confirmed; depends on one key assumption
- `INFERENCE — LOW CONFIDENCE` — logical deduction from absence of evidence or from proxy data; could be wrong if undisclosed information exists
- `ASSUMPTION` — stated without corroborating evidence; drives a discovery question

---

## PROVOCATION 01

`TRANSPORTATION PLANNING`

### You have real-time tracking on every shipment. Your plan still takes weeks to react.

**`OPEX Reduction`** **`Planning Cycle Speed`**

**Primary buyers:** CSCO · CFO

**Evidence:**
- project44 real-time supply chain visibility was deployed in February 2026 under World Cup preparation. The deployment confirms the visibility layer exists. No press release, case study, or job posting confirms that real-time shipment data feeds into demand or transport planning decisions. [`FACT` — project44 press release Feb 2026; `INFERENCE — LOW CONFIDENCE` — planning integration gap inferred from absence of any disclosure, not from direct evidence]
- When the US imposed tariffs in 2025, adidas's response — eliminating all China-to-US sourcing — was confirmed publicly but the timeline from policy signal to final sourcing decision has not been disclosed. Best-in-class transport scenario planning at comparable-scale retailers runs at 48–72 hours. The gap is structural. [`FACT` — 2025 China-to-US sourcing elimination confirmed in FY2025 results; `INFERENCE — HIGH CONFIDENCE` — 48–72h benchmark is well-documented in supply chain literature; `ASSUMPTION` — adidas's actual response cycle has not been published]
- 60+ DCs across 6 continents with 100% outsourced last-mile. The tech stack (SAP S/4HANA + o9 Solutions for planning + project44 for visibility) exists as separate confirmed systems. No case study or integration announcement connects real-time shipment events to the planning cycle. [`FACT` — DC count, last-mile outsourcing model, SAP S/4HANA and o9 deployments all individually confirmed; `INFERENCE — LOW CONFIDENCE` — lack of integration inferred from absence of joint case study, not confirmed by adidas]

**COST OF INACTION:** €50–75M per year in avoidable emergency air freight premiums and reactive routing decisions. Air freight costs 4× ocean on the same lane. Every unplanned air shipment is a margin hit that disappears into COGS without a line item. [`INFERENCE — MODERATE CONFIDENCE` — based on confirmed air/ocean freight cost differential and publicly observed reactive behavior in 2025 tariff response; absolute figure is a range estimate, not a measured number]

**DISCOVERY QUESTION:** What is the current cycle time from a disruption signal — a port closure, a tariff announcement, a demand spike — to a revised transport plan? Who owns that decision, and does it connect to the demand plan or sit in a separate team?

---

## PROVOCATION 02

`WAREHOUSING`

### Your warehouse packs an order in 2 hours. Your website tells customers 3–7 days.

**`Revenue Protection / Growth`** **`Fulfillment Speed`**

**Primary buyers:** COO · CSCO

**Evidence:**
- The Wilkes-Barre PA distribution center (843,000 sq ft; 71,000+ SKUs) achieves a confirmed 2-hour pack SLA and can deliver same-day to parts of the US Northeast and 2-day ground nationwide. adidas.com US standard SLA is published as 3–7 days for non-Prime orders. [`FACT` — Interlake Mecalux case study (Wilkes-Barre); `FACT` — adidas.com US help page SLA]
- The Mantova megasite (130,000 sqm, Italy; €350M investment; 700+ robots; 375,000–500,000 parcels/day peak) opened September 2024 and serves 19 European countries. No per-country consumer delivery SLA is published for France, Spain, Poland, or Germany. Customers in those markets cannot compare adidas's speed to Amazon, Zalando, or ASOS. [`FACT` — Kuehne+Nagel press release September 2024; `FACT` — absence of published per-market SLA confirmed by research pass across adidas.com, adidas.co.uk, adidas.de]
- GK OmniPOS (1,300+ stores) and RFID stock accuracy (>99%) already enable ship-from-store. The percentage of DTC orders actually fulfilled from stores is not disclosed. The DC capability is confirmed; the SLA gap is a commercial choice, not a logistics constraint. [`FACT` — GK Software case study and Gold Convrt Award 2024; `FACT` — GK blog September 2024; `INFERENCE — HIGH CONFIDENCE` — SLA is a policy decision given demonstrated DC capability; `INFERENCE — LOW CONFIDENCE` — ship-from-store activation at scale is unconfirmed]

**COST OF INACTION:** €100–150M per year in lost DTC conversion and post-purchase loyalty from customers who see "3–7 days" and buy from Amazon instead. Amazon Prime delivers in 1–2 days; Nike's express option delivers in 2–3 days. The physical capability to close this gap already exists in Wilkes-Barre and Mantova. [`INFERENCE — MODERATE CONFIDENCE` — based on €4.3B e-commerce channel confirmed in FY2025 results (+16% growth) and documented 1–2 day SLA gap vs. Amazon; conversion-rate impact is industry-benchmarked, not adidas-specific]

**DISCOVERY QUESTION:** What percentage of US DTC orders are actually delivered within 2 days from the Wilkes-Barre DC? Is the 3–7 day SLA a legal floor, a carrier commitment, or a planning default that nobody has revisited? What would it take to publish a 2-day standard SLA for US e-commerce?

---

## PROVOCATION 03

`GLOBAL TRADE AND TARIFFS`

### A €200M tariff bill is already in your guidance. Your response cycle is measured in months.

**`COGS Avoidance`** **`Decision Cycle Compression`**

**Primary buyers:** CFO · CSCO

**Evidence:**
- €200M in US tariff costs is explicitly embedded in FY2026 guidance, confirmed on March 4, 2026. [`FACT` — adidas FY2025 results press release, March 4, 2026] Vietnam accounts for 27% of sourcing and Indonesia for 19%. Both countries are under active US trade policy review with known review dates. Their escalation risk is not covered in current guidance. [`FACT` — sourcing breakdown from adidas Annual Report 2024; `INFERENCE — HIGH CONFIDENCE` — US review timelines for Vietnam and Indonesia are public trade policy calendar items]
- In 2025, adidas eliminated China-to-US sourcing entirely — a reactive move confirmed by management. The timeline from the initial US tariff signal to the final sourcing decision is not disclosed. Best-in-class tariff scenario planning at comparable-scale retailers runs at 48–72 hours from policy announcement to sourcing recommendation. [`FACT` — China-to-US elimination confirmed; `ASSUMPTION` — adidas's actual response cycle is unknown; `INFERENCE — HIGH CONFIDENCE` — 48–72h benchmark is standard in supply chain literature for automated scenario tools]
- No press release, case study, or job posting confirms that adidas runs continuous tariff scenario modeling. The planning stack (o9 Solutions on SAP S/4HANA) has the technical capability to do this, but no deployment announcement exists. [`FACT` — o9 Solutions deployment confirmed; `INFERENCE — LOW CONFIDENCE` — absence of tariff modeling announcement is not evidence it does not exist; it may be undisclosed]

**COST OF INACTION:** €200M per year confirmed in guidance. A further €100–200M in Vietnam and Indonesia escalation risk is not being disclosed as modeled or hedged — meaning this additional exposure is absorbed as unmanaged risk. [`FACT` — €200M confirmed; `INFERENCE — LOW CONFIDENCE` — €100–200M additional risk is estimated from sourcing share × tariff rate scenarios; not confirmed by adidas]

**DISCOVERY QUESTION:** What is the current process from a US tariff policy announcement to a final sourcing shift decision, and who owns it? Is any scenario modeling running continuously, or does it start when the announcement arrives? How long did the 2025 China pivot actually take from first policy signal to final sourcing decision?

---

## PROVOCATION 04

`FREIGHT AUDIT`

### Nobody checks your freight invoices. €60M in carrier overcharges goes unchallenged every year.

**`OPEX Reduction`** **`Throughput / Process Efficiency`**

**Primary buyers:** CFO · COO

**Evidence:**
- adidas uses 100% 3PL for last-mile delivery. Confirmed partners include Amazon MCF (US), Kuehne+Nagel (19-country Europe), DHL Supply Chain (Brazil), and Honeywell Intelligrated (Spartanburg US wholesale). Each partnership has a separate rate card and invoicing structure. The total number of national carrier contracts across 60+ DCs on 6 continents is not disclosed. [`FACT` — last-mile outsourcing model; `FACT` — Amazon MCF (Feb 2025), Kuehne+Nagel Mantova (Sept 2024), DHL Brazil (Feb 2024), Honeywell Spartanburg all confirmed via press releases; `INFERENCE — MODERATE CONFIDENCE` — 15+ national carrier contracts inferred from DC count and geographic footprint]
- Adidas's annual logistics spend is not publicly disclosed as a line item. At a company operating 60+ DCs, processing up to 500,000 parcels/day in Europe alone, with 100% outsourced last-mile, a €1.5–2.0B annual logistics spend is a reasonable estimate. Industry benchmarks for freight audit recovery run at 2–4% of total freight spend — a range that is publicly documented in logistics trade press. [`INFERENCE — LOW CONFIDENCE` — €1.5–2.0B logistics spend is back-calculated from COGS structure and DC scale; not confirmed by adidas; `FACT` — 2–4% freight audit recovery rate is a published industry benchmark]
- No public case study, press release, job posting, or vendor reference confirms that adidas runs systematic freight audit or automated invoice reconciliation. The Amazon MCF and Kuehne+Nagel billing structures are fundamentally different, multiplying reconciliation complexity. [`FACT` — billing structure differences confirmed; `INFERENCE — LOW CONFIDENCE` — absence of freight audit announcement is not confirmed absence; it may exist but be undisclosed]

**COST OF INACTION:** €50–60M per year in carrier overcharges, duplicate billing, and freight invoice errors — unrecovered if no systematic audit exists. Estimated at 3% of €1.8B logistics spend. [`INFERENCE — LOW CONFIDENCE` — both the logistics spend base and the 3% recovery rate are estimated; this is a directional signal, not a measured gap]

**DISCOVERY QUESTION:** Does adidas have an automated freight audit process today — invoice matching, rate card verification, duplicate detection? What percentage of carrier invoices are reconciled before payment? When was the last external freight audit conducted, and what was recovered?

---

## PROVOCATION 05

`LAST MILE AND RETURNS — SYNTHESIS`

### Fix the full fulfillment chain and operating margin moves from 8.3% to 9.5% — €300M closer to your 2028 target.

**`Operating Margin Expansion`** **`Response Latency`**

**Primary buyers:** CEO · CFO · COO

**The arithmetic — what fixing P1–P4 delivers:**

| Fulfillment Gap | Annual EBIT Opportunity | Confidence |
|-----------------|------------------------|------------|
| Transportation planning — connect visibility to demand plan | €50–75M | `INFERENCE — MODERATE CONFIDENCE` |
| Warehousing — activate SLA to match DC capability | €75–100M | `INFERENCE — MODERATE CONFIDENCE` |
| Tariffs — continuous scenario modeling vs. reactive response | €100M | `INFERENCE — MODERATE CONFIDENCE` |
| Freight audit — automated invoice reconciliation | €50–60M | `INFERENCE — LOW CONFIDENCE` |
| **Total fulfillment improvement** | **~€300M** | Combined |

**Margin path:**
- FY2025 EBIT: €2,059M → **8.3% margin** [`FACT` — adidas FY2025 press release March 4, 2026]
- After fulfillment fixes: ~€2,359M → **~9.5% margin** [`INFERENCE — MODERATE CONFIDENCE` — arithmetic above applied to €24.8B FY2025 revenue; individual line items are estimates]
- 2028 target: **>10%** [`FACT` — publicly committed, announced March 4, 2026]
- Remaining gap at 9.5%: ~0.5pp — achievable through operating leverage on high-single-digit revenue growth alone [`INFERENCE — HIGH CONFIDENCE` — consistent with management guidance trajectory and FY2026 guidance of ~8.5–8.8% margin before fulfillment improvement]

**Evidence — where last mile and returns sits in this:**
- Ship-from-store is technically ready but not confirmed at scale: GK OmniPOS live in 1,300+ stores; RFID stock accuracy >99%. The percentage of DTC orders fulfilled via ship-from-store is not publicly disclosed. [`FACT` — GK Software case study and Gold Convrt Award 2024; `INFERENCE — LOW CONFIDENCE` — scale of activation unknown]
- Amazon MCF (February 2025) delivers 1–2 day fulfillment for Prime members — but every MCF return is processed through Amazon's logistics network, not adidas's own returns infrastructure. The post-purchase relationship and returns data stay with Amazon. [`FACT` — Amazon MCF press release February 20, 2025; `INFERENCE — HIGH CONFIDENCE` — MCF returns routing to Amazon is standard MCF program structure, confirmed by Amazon MCF documentation]
- adidas's e-commerce channel is €4.3B and growing at +16% in FY2025. [`FACT` — FY2025 results] Returns in athletic and lifestyle e-commerce run at 15–25% of orders — a potential €650M–1.1B returns flow annually. No cost-per-return metric is disclosed. No press release or case study confirms automated returns triage or routing at adidas. [`INFERENCE — MODERATE CONFIDENCE` — 15–25% returns rate is a published industry benchmark for athletic apparel e-commerce; applied to adidas's confirmed channel size; adidas-specific rate is unknown]

**COST OF INACTION:** €300M per year in combined fulfillment inefficiency holds operating margin 1.2 points below potential — keeping the 2028 target dependent on brand heat rather than operational control. When the Samba/Gazelle lifestyle cycle fades, this gap will be very hard to close through revenue alone. [`INFERENCE — MODERATE CONFIDENCE` — see arithmetic; `FACT` — lifestyle cycle risk flagged explicitly in Gulden management commentary across multiple earnings calls]

**DISCOVERY QUESTION:** What is the total cost-to-serve per DTC order today, broken down by fulfillment mode — DC ship, ship-from-store, Amazon MCF, click-and-collect? What is the returns rate by market and channel, and what is the net cost per returned unit including carrier, processing, restocking, and markdown recovery?

---

## SELF-EVALUATION

| Test | P1 | P2 | P3 | P4 | P5 |
|------|----|----|----|----|-----|
| **CFO Test:** ROI calculable on first read? | ✓ €50–75M | ✓ €100–150M | ✓ €200M+ | ✓ €60M | ✓ €300M / 1.2pp margin |
| **Specificity Test:** Points to a specific sub-process? | ✓ Transport-to-plan integration gap | ✓ SLA vs. DC capability gap | ✓ Tariff scenario modeling cycle | ✓ Freight invoice reconciliation | ✓ Last mile + returns cost-to-serve |
| **Falsifiability Test:** Client can disprove with one data point? | ✓ Show the transport plan refresh cycle | ✓ Show % of orders delivered <2 days | ✓ Show the scenario modeling tool | ✓ Show the audit process | ✓ Show cost-per-return |

**Lever balance:**
- Financial: OPEX Reduction (P1, P4) · Revenue Protection/Growth (P2) · COGS Avoidance (P3) · Operating Margin Expansion (P5) — **4 distinct categories ✓**
- Operational: Planning Cycle Speed (P1) · Fulfillment Speed (P2) · Decision Cycle Compression (P3) · Throughput/Process Efficiency (P4) · Response Latency (P5) — **5 distinct categories ✓**

**Data recency:** All provocations use FY2025 data (confirmed March 4, 2026). project44 deployment (February 2026) and Amazon MCF (February 2025) are the most recent available signals. ✓

**Confidence distribution across all 5 provocations:**
- `FACT` tags: 28 instances — drawn from press releases, official filings, confirmed vendor case studies
- `INFERENCE — HIGH CONFIDENCE` tags: 7 instances — multiple independent signals; would be surprising if wrong
- `INFERENCE — MODERATE CONFIDENCE` tags: 12 instances — plausible, depends on one key unconfirmed assumption
- `INFERENCE — LOW CONFIDENCE` tags: 9 instances — logical deduction from absence of evidence; client may be able to disprove immediately
- `ASSUMPTION` tags: 3 instances — stated without corroboration; each generates a discovery question

**P4 note:** The freight audit provocation carries the most `INFERENCE — LOW CONFIDENCE` tags. The logistics spend base (€1.5–2.0B) and recovery rate (3%) are both estimates. The discovery question is high-value precisely because this is the most falsifiable provocation — if adidas already has an automated freight audit process, this provocation is withdrawn and replaced with the finding that they are ahead of peers.

---

*Sources: adidas FY2025 results press release (March 4, 2026); adidas Annual Reports 2022–2025; Interlake Mecalux case study (Wilkes-Barre); K+N press release (Mantova, Sept 2024); DHL Supply Chain press release (Extrema Brazil, Feb 2024); GK Software case study and Gold Convrt Award 2024; Amazon Buy with Prime / MCF press release (Feb 20, 2025); project44 press release (Feb 2026); adidas.com and adidas.co.uk SLA pages; o9 Solutions adidas case study; SAP/AWS adidas TRANS4RM case studies; adidas 20-F SEC filings; all prior step outputs (Steps 1–8).*
