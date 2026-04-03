# Adidas AG — Visuals Data
**Step 8: Final Memo | Date: 2026-04-03**
**Purpose:** Structured data inputs for four pursuit presentation charts

---

## VISUAL 1: SPIDER CHART — Company vs. Peer Average vs. Best-in-Class

**Chart type:** Radar / Spider chart (hexagon with 6 axes)
**Purpose:** Show adidas's relative competitive position across six performance dimensions vs. peer average and best-in-class.

### Metric Definitions and Normalization

All scores normalized to 0–100 scale. 100 = best-in-class across the full peer set. 0 = worst-in-class.

| Metric | Description | Best-in-Class (100) | Worst-in-Class (0) | Method |
|--------|-------------|--------------------|--------------------|--------|
| Gross Margin | Gross profit ÷ revenue | Anta Sports 63.4% | Nike 40.6% | Min-max linear scaling |
| Operating Margin | Operating profit ÷ revenue | Anta Sports 26.3% | Under Armour 3.8% (adj.) | Min-max linear scaling |
| Revenue Growth | 3-year revenue compound annual growth rate | On Running ~50% | Under Armour ~–5% | Min-max linear scaling |
| SG&A Efficiency | Lower SG&A% = better (inverted scale) | Deckers 34.2% | Under Armour 50.2% | Inverted min-max: (50.2 – value) / 16 × 100 |
| DTC Penetration | DTC revenue as % of total | Lululemon ~95% | Anta Sports ~25% | Min-max linear scaling |
| Revenue per Employee | Revenue ÷ headcount (productivity) | On Running ~$830K | Lululemon ~$272K | Min-max linear scaling |

### Normalized Scores by Company

| Company | Gross Margin | Operating Margin | Revenue Growth | SG&A Efficiency | DTC Penetration | Rev/Employee | **Average** |
|---------|-------------|-----------------|---------------|-----------------|-----------------|--------------|-------------|
| **adidas** | **46** | **20** | **15** | **47** | **23** | **23** | **29** |
| Nike | 0 | 9 | 9 | 97 | 22 | 58 | 33 |
| PUMA | 30 | 15 | 15 | 62 | 4 | 32 | 26 |
| On Running | 97 | 39 | 100 | 19 | 24 | 100 | 63 |
| Lululemon | 82 | 88 | 36 | 81 | 100 | 0 | 65 |
| Deckers / HOKA | 76 | 88 | 42 | 100 | 7 | 77 | 65 |
| Anta Sports | 100 | 100 | 36 | 83 | 0 | 23 | 57 |
| ASICS | 67 | 48 | 42 | 57 | 14 | 39 | 44 |
| Under Armour | 32 | 0 | 0 | 0 | 0 | 7 | 7 |

### Three Reference Lines for Spider Chart

| Reference | Gross Margin | Operating Margin | Revenue Growth | SG&A Efficiency | DTC Penetration | Rev/Employee |
|-----------|-------------|-----------------|---------------|-----------------|-----------------|--------------|
| **adidas (subject)** | **46** | **20** | **15** | **47** | **23** | **23** |
| **Peer Average** (excl. adidas) | 61 | 48 | 35 | 62 | 21 | 42 |
| **Best-in-Class** | 100 | 100 | 100 | 100 | 100 | 100 |

### Normalization Calculations (Reference)

**Gross Margin** — range: 40.6% (Nike) to 63.4% (Anta), span 22.8pp
- adidas 51.0%: (51.0 – 40.6) / 22.8 × 100 = **46**
- Nike 40.6%: 0 | PUMA 47.4%: 30 | On 62.8%: 97
- Lululemon 59.2%: 82 | Deckers 57.9%: 76 | Anta 63.4%: 100
- ASICS 55.8%: 67 | Under Armour 47.9%: 32

**Operating Margin** — range: 3.8% (UA adj.) to 26.3% (Anta), span 22.5pp
- adidas 8.3%: (8.3 – 3.8) / 22.5 × 100 = **20**
- Nike 5.8%: 9 | PUMA 7.1%: 15 | On 12.5%: 39
- Lululemon 23.7%: 88 | Deckers 23.7%: 88 | Anta 26.3%: 100
- ASICS 14.7%: 48 | Under Armour 3.8%: 0

**Revenue Growth (3yr CAGR)** — range: –5% (UA) to 50% (On), span 55pp
- adidas 3.3%: (3.3 + 5) / 55 × 100 = **15**
- Nike –0.3%: 9 | PUMA 3%: 15 | On 50%: 100
- Lululemon 15%: 36 | Deckers 18%: 42 | Anta 15%: 36
- ASICS 18%: 42 | Under Armour –5%: 0

**SG&A Efficiency (inverted)** — range: 34.2% (Deckers, best) to 50.2% (UA, worst), span 16pp
- adidas 42.7%: (50.2 – 42.7) / 16 × 100 = **47**
- Nike 34.7%: 97 | PUMA 40.3%: 62 | On 47.1%: 19
- Lululemon 37.2%: 81 | Deckers 34.2%: 100 | Anta 37%: 83
- ASICS 41.1%: 57 | Under Armour 50.2%: 0

**DTC Penetration** — range: 25% (Anta/UA) to 95% (Lululemon), span 70pp
- adidas 41%: (41 – 25) / 70 × 100 = **23**
- Nike 40.5%: 22 | PUMA 27.5%: 4 | On 41.8%: 24
- Lululemon 95%: 100 | Deckers 30%: 7 | Anta 25%: 0
- ASICS 35%: 14 | Under Armour 25%: 0

**Revenue per Employee** — range: $272K (Lululemon) to $830K (On), span $558K
- adidas €400K (~$430K): (430 – 272) / 558 × 100 = **23** (rounded, EUR/USD near parity)
- Nike $595K: 58 | PUMA €449K (~$483K): 38 | On $830K: 100
- Lululemon $272K: 0 | Deckers ~$700K est.: 77 | Anta ~$430K est.: 28
- ASICS €450K (~$484K): 38 | Under Armour $311K: 7

### Chart Annotation Notes
- adidas is below peer average on 5 of 6 dimensions
- adidas's single relative strength is DTC Penetration — roughly at peer average
- The largest gaps vs. peer average: Operating Margin (–28 pts), Revenue Growth (–20 pts), Gross Margin (–15 pts)
- Best-in-class benchmarks are drawn from different companies on each axis — no single peer dominates all six

---

## VISUAL 2: VALUE LEVER HEATMAP — Supply Chain Area × AI Value Lever

**Chart type:** Heatmap table
**Purpose:** Show which AI value levers (rows) apply most strongly to which supply chain areas (columns), scored H/M/L.
**Scoring:** H = primary lever / high direct impact, M = secondary lever / moderate impact, L = indirect lever / low direct impact, — = not applicable

### Five AI Value Levers Defined

| Lever | Definition |
|-------|-----------|
| **Productivity** | More output per unit of labor or asset — doing more with the same resources |
| **Efficiency** | Lower cost per unit of activity — reducing the expense of each operation |
| **Quality** | Better decisions, fewer errors, higher accuracy — improving outcomes per action |
| **Velocity** | Faster response and execution — reducing cycle time from signal to action |
| **Growth** | More revenue generated — higher conversion, better pricing, or larger addressable market |

### Heatmap Scores

| Value Lever | Procurement / Sourcing | Demand & Supply Planning | Warehousing & Fulfillment | Inbound Transportation | Outbound / Last Mile | Transport Planning | Freight Bill Audit | Returns & Reverse Logistics |
|------------|----------------------|------------------------|--------------------------|----------------------|---------------------|-------------------|-------------------|---------------------------|
| **Productivity** | L | M | **H** | L | M | **H** | **H** | M |
| **Efficiency** | **H** | **H** | **H** | **H** | **H** | **H** | **H** | **H** |
| **Quality** | **H** | **H** | M | M | **H** | M | M | **H** |
| **Velocity** | **H** | **H** | M | **H** | M | M | L | L |
| **Growth** | M | **H** | L | L | M | L | L | M |

### Reading Notes
- **Efficiency** is the dominant lever across all 8 supply chain areas — consistent with adidas's primary strategic challenge (SG&A reduction to hit 10% EBIT margin)
- **Quality** and **Velocity** are co-primary in the two highest-priority areas: Procurement/Sourcing (tariff response speed + supplier risk accuracy) and Demand & Supply Planning (forecast accuracy + cultural signal detection)
- **Growth** appears only in Demand Planning and Transportation — the former because better forecasting drives full-price sell-through (margin improvement with revenue impact), the latter because last-mile cost reduction enables profitable DTC growth investment
- **Productivity** is strongest in Warehousing and Freight Audit — where AI replaces manual labor-intensive processes

---

## VISUAL 3: BODY vs. BRAIN DIAGNOSIS — Per Supply Chain Area

**Chart type:** Categorized table or two-column split diagram
**Purpose:** Clearly show which supply chain constraints require physical investment (body) vs. intelligence and process improvement (brain), and what the immediate bottleneck is in each area.

### Diagnosis Table

| Supply Chain Area | Body Component (Physical Constraint) | Brain Component (Decision/Process Gap) | Primary Bottleneck | Consulting Opportunity |
|------------------|--------------------------------------|----------------------------------------|-------------------|----------------------|
| **Procurement / Sourcing** | Factory location, trade lane infrastructure (body already changing: China exit underway) | Tariff scenario modeling, supplier performance AI, multi-tier risk mapping | **BRAIN** — decisions are manual; the physical re-routing is already happening | Immediately actionable — deploy tariff scenario intelligence on current data |
| **Demand & Supply Planning** | N/A — adidas does not own manufacturing; body constraint is factory lead times (external) | Demand sensing accuracy, social signal integration, wholesale sell-through intelligence | **BRAIN** — forecasting tools exist (o9, SageMaker) but read backward-looking data | High priority — upgrade data inputs to o9/SageMaker; social signal integration feasible now |
| **Warehousing & Fulfillment** | Physical automation gap: top 5 DCs world-class; remaining 55 under-automated | Slotting optimization, labor planning, omnichannel order routing logic | **MIXED** — body investment needed in lagging DCs (multi-year capital program); brain improvements actionable now in all DCs | Brain-first for immediate value; body investment in parallel for lagging facilities |
| **Inbound Transportation** | Port infrastructure at Vietnam/Indonesia (external; cannot be changed by adidas) | Visibility and mode optimization decisions (project44 early-stage) | **BRAIN** — project44 just deployed; integration to demand planning not yet complete | Immediate — connect project44 to o9 demand planning; build mode optimization model |
| **Outbound / Last Mile** | Last-mile carrier network (managed externally) | Carrier selection logic, returns propensity prediction, delivery promise accuracy | **BRAIN** — carrier selection rules are static; returns management is reactive | Medium priority — actionable on current data; returns propensity feasible with adiClub data |
| **Transport Planning** | Multi-modal network exists; physical infrastructure is adequate | Planning is siloed by mode and region; no unified optimization | **BRAIN** — planning fragmentation is a process problem, not a physical problem | Build unified control tower on project44 data layer |
| **Freight Bill Audit** | N/A — purely financial and data process | Manual invoice review; no automated contract compliance checking | **BRAIN** — pure process automation opportunity; S/4HANA Central Finance is the data layer | Near-term feasibility high; connect S/4HANA Finance to freight data for automated audit |
| **Returns & Reverse Logistics** | Physical return processing facilities exist (1,933 stores + DC network) | Returns triage, disposition decision, propensity prediction | **BRAIN** — disposition decisions are manual; customer interface is reactive | Medium priority — computer vision triage and GenAI customer interface feasible on current infrastructure |

### Summary Counts

| Category | Count | Supply Chain Areas |
|----------|-------|-------------------|
| Pure Brain bottleneck | 6 | Procurement, Demand Planning, Inbound Transport, Transport Planning, Freight Audit, Returns |
| Mixed (Body + Brain) | 1 | Warehousing & Fulfillment |
| Pure Body bottleneck | 0 | — |

**Net diagnosis:** Adidas's supply chain intelligence constraints are overwhelmingly brain problems — not physical infrastructure problems. This means the consulting opportunity is available now, without waiting for capital programs or physical construction. The one mixed area (warehousing) has brain improvements that can be deployed immediately in parallel with the longer-horizon body investment.

---

## VISUAL 4: OPPORTUNITY SUMMARY TABLE — Supply Chain AI Portfolio

**Chart type:** Structured table (suitable for executive slide, sortable by benefit potential)
**Purpose:** Provide a single-page overview of all supply chain AI opportunities with estimated benefit, primary lever, and key validation question.

| # | Supply Chain Area | AI Opportunity | Value Lever | Benefit Potential | TRANS4RM Dependency | Time to Value | Key Validation Question |
|---|------------------|---------------|-------------|------------------|---------------------|--------------|------------------------|
| 1 | Demand & Supply Planning | Social signal demand sensing — connect TikTok/Instagram/search trends to o9 forecasting | Quality + Efficiency | **HIGH** — 1pp gross margin recovered = €248M EBIT | None | 6–12 months | What is the current demand forecast error rate by category? What is the annual markdown cost? |
| 2 | Demand & Supply Planning | Wholesale sell-through intelligence — predict stockout/overstock at retail partner level | Quality + Velocity | **HIGH** — reduces markdown and overstock across 60% of revenue | Partial (Sales module) | 12–18 months | What sell-through data sharing exists with Foot Locker, Dick's, JD Sports today? |
| 3 | Procurement / Sourcing | Tariff scenario intelligence — always-on landed cost simulation across all sourcing options | Efficiency + Velocity | **HIGH** — €200M current headwind; €200–300M additional Vietnam/Indonesia risk | None | 6–12 months | Has adidas modeled a Vietnam/Indonesia-specific tariff escalation scenario? |
| 4 | Procurement / Sourcing | Supplier performance prediction — predict late delivery, defects, capacity constraints in advance | Quality + Efficiency | **HIGH** — across 124 partners and €24.8B revenue base | None | 6–12 months | Is supplier performance tracked in a single system, or aggregated manually across markets? |
| 5 | Warehousing & Fulfillment | AI-powered product placement (slotting) optimization — continuous re-optimization by demand velocity | Efficiency + Productivity | **MEDIUM-HIGH** — 15–25% travel time reduction per pick at scale | None | 6–12 months | What WMS (Warehouse Management System) platforms are deployed across the 60 distribution centers? |
| 6 | Warehousing & Fulfillment | Omnichannel order routing AI — ship from DC or nearest store based on inventory and proximity | Efficiency + Quality | **MEDIUM-HIGH** — reduces last-mile distance and cost as DTC grows | Partial (Sales module) | 12–18 months | What is the current cost per DTC order vs. wholesale pallet delivery? |
| 7 | Inbound Transportation | project44 → o9 integration — close the loop between in-transit status and demand planning signals | Velocity + Efficiency | **MEDIUM** — reduces safety stock buffer required to cover transit uncertainty | None | 6–9 months | What percentage of inbound shipments currently have real-time track-and-trace visibility? |
| 8 | Inbound Transportation | Dynamic ocean vs. air mode selection — AI evaluates real-time stockout risk vs. air freight premium | Efficiency | **MEDIUM** — 2–5% freight cost reduction; eliminates manual escalation | None | 6–12 months | What is the current annual cost premium for air freight above ocean equivalent? |
| 9 | Outbound / Last Mile | Returns propensity prediction — flag high-return-risk orders; surface size/fit guidance at purchase | Quality + Growth | **MEDIUM** — 1pp return rate reduction on €4.3B DTC base = €10M+ | None | 9–15 months | What is the current e-commerce return rate by category? |
| 10 | Outbound / Last Mile | Carrier selection optimization — dynamic carrier routing by cost, performance, and carbon footprint | Efficiency + Quality | **MEDIUM** — reduces per-delivery cost and carrier compliance risk | None | 6–9 months | Is carrier selection currently rules-based (static) or dynamically optimized? |
| 11 | Transport Planning | AI transport control tower — continuous re-routing across carriers, modes, and lanes | Efficiency + Quality | **MEDIUM** — 3–5% total freight spend reduction | None | 12–18 months | Is there a single unified visibility and planning platform across all transport modes? |
| 12 | Transport Planning | CO2 routing optimization — transport route selection minimizing emissions within service constraints | Quality | **MEDIUM** — supports ESG executive compensation metric; CSRD compliance | None | 12–18 months | How is Scope 3 transport emissions currently measured for CSRD reporting? |
| 13 | Freight Bill Audit | Automated invoice audit — ML flags invoice deviations from contracted rates | Efficiency + Productivity | **MEDIUM** — recovers 1–3% of freight spend in billing errors (industry benchmark) | None | 3–6 months | What percentage of freight invoices are currently manually reviewed? |
| 14 | Freight Bill Audit | Landed cost automation — AI calculates true product cost per SKU from invoice + customs data | Efficiency + Quality | **MEDIUM** — improves gross margin reporting accuracy; supports tariff response | None | 6–9 months | How is landed cost currently calculated per product? How quickly does it reflect actual invoiced costs? |
| 15 | Returns & Reverse Logistics | AI returns triage and disposition — computer vision classifies returned items; auto-routes disposition | Efficiency + Quality | **MEDIUM** — improves recovery margin on returned inventory vs. blanket liquidation | None | 9–15 months | What is the average cycle time from return initiation to inventory re-availability? |
| 16 | Returns & Reverse Logistics | GenAI customer returns interface — automated returns initiation and tracking via AI | Productivity | **MEDIUM** — reduces customer service FTE for returns handling | None | 3–6 months | Is returns handling currently managed through live agents, automated systems, or a mix? |

### Portfolio Summary

| Benefit Potential | Count | Supply Chain Areas |
|------------------|-------|--------------------|
| HIGH | 4 | Demand Planning (social sensing, wholesale), Procurement (tariff intelligence, supplier performance) |
| MEDIUM-HIGH | 2 | Warehousing (slotting, omnichannel routing) |
| MEDIUM | 10 | Inbound transport, outbound/last mile, transport planning, freight audit, returns |

| TRANS4RM Dependency | Count |
|---------------------|-------|
| None — actionable on current infrastructure | 13 |
| Partial (Sales module completion helps) | 3 |
| Full TRANS4RM required | 0 |

**Key insight:** 13 of 16 supply chain AI initiatives are actionable on current infrastructure — no SAP S/4HANA Sales module required. The engagement can deliver value immediately while TRANS4RM completes in the background. This is the central sequencing argument for starting now rather than waiting.

---

## SUPPLEMENTARY DATA: FINANCIAL CASE SUMMARY

For use in financial case slide.

| Initiative Cluster | Estimated Annual EBIT Benefit | Confidence | Infrastructure Confirmation |
|-------------------|------------------------------|------------|-----------------------------|
| GenAI marketing content production | €60–120M | HIGH — confirmed Databricks pipeline | Databricks/MosaicML live [FACT] |
| Demand planning accuracy improvement (gross margin) | €75–250M | MEDIUM — requires forecast error baseline | o9 + SageMaker confirmed [FACT]; MAPE not disclosed [ASSUMPTION] |
| Tariff scenario intelligence + procurement AI | €40–100M | MEDIUM — requires tariff modeling gap confirmation | project44 + o9 confirmed [FACT]; modeling gap inferred [ASSUMPTION] |
| Freight audit + landed cost automation | €15–50M | HIGH — S/4HANA Finance is the data layer | S/4HANA Central Finance live [FACT] |
| Developer productivity (GitHub Copilot expansion) | €10–15M direct | HIGH — confirmed productivity gain | GitHub Copilot deployment confirmed [FACT] |
| Returns reduction + last-mile optimization | €20–60M | MEDIUM — requires return rate and cost baseline | adiClub data available; baseline unknown [ASSUMPTION] |
| **Total addressable range** | **€220–595M** | **MEDIUM confidence** | **Anchored to confirmed infrastructure** |

> Present as €300–700M range to the CFO to allow for conservative and optimistic scenarios, and to account for confirmed vs. inferred assumptions. The floor (€300M) is defensible from confirmed infrastructure. The ceiling (€700M) is achievable but requires validation of forecast error rate, return rate, and marketing production cost decomposition. [INFERENCE — financial model based on Steps 3–7 analysis]

---

*Sources: All prior step outputs (Steps 1–7); company_snapshot.md; benchmark_table.md; value_levers.md; stream_ranking.md; body_brain_diagnosis.md; due_diligence.md; current_signals.md; adidas Annual Reports 2023–2025.*
