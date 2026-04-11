# Phase 5 — Job 2: Due Diligence — Challenging the Thesis
**Company:** adidas AG | **Date:** 2026-04-11
**Purpose:** Stress-test the five proposed provocations before finalizing. Five counterarguments with evidence, validation tests, and confidence assessments.

---

## THE THESIS BEING CHALLENGED

We are arguing that four supply chain intelligence gaps — demand planning latency, tariff response speed, dormant ship-from-store, and an underpowered transportation control tower — represent ~€300M of addressable EBIT improvement that adidas can capture before its 2028 10% margin target. This section attempts to disprove that thesis.

---

## COUNTERARGUMENT 1: "The demand planning gap may already be closed internally"

### The challenge
adidas has deployed o9 Solutions — one of the most advanced demand planning platforms in consumer goods — plus Amazon SageMaker for ML forecasting, and the Databricks Agent Digital Twin in production governance. The 2-4 week demand sensing lag we are asserting may have been closed. We are working from public disclosures; the company may be ahead of what it publishes.

### Evidence for the counterargument
- o9 Solutions is described as live for "in-season retail planning, allocation, and DTC demand sensing" — not a pilot [FACT]
- Databricks Agent Digital Twin session at the 2026 summit demonstrates production-scale multi-agent governance [FACT]
- MosaicML processes 2M+ product reviews/year at 91.67% cost reduction — consumer signal ingestion is active [FACT]
- FY2025 gross margin of ~51.0% is adidas's highest in over a decade — planning is clearly improving [FACT]

### Evidence against the counterargument
- No public disclosure confirms store sell-through data feeds o9 in real-time rather than daily/weekly batch [FACT — absence of disclosure]
- No confirmation that social signal data (trend spikes) connects to the demand sensing engine [FACT — absence]
- €4,989M inventory at FY2024 on €23,683M revenue = 21% inventory/revenue — above peer median [FACT]
- Implied inventory turns ~4.7x — below Deckers (~7x) and On (~6x) [INFERENCE — HIGH]
- Supply chain and Sales modules of S/4HANA not yet live — master data quality in planning is still incomplete [FACT]

### Validation test
Ask adidas: "What is your current store sell-through data refresh rate into the o9 planning engine — real-time, daily, or weekly? Which social signal APIs currently feed the demand sensing model?" One question closes this definitively.

### Confidence assessment
**MEDIUM.** The TRANS4RM incompleteness is confirmed fact and creates a structural ceiling on planning precision. The closed-loop integration gaps are structurally observable. But we cannot rule out undisclosed integrations. Phase One validates this directly.

---

## COUNTERARGUMENT 2: "The ship-from-store opportunity overstates what we can actually deliver"

### The challenge
The 1,933 stores include 1,095 factory outlets — typically in outlet malls on city peripheries, not where same-day delivery economics work. Store associates are trained for retail, not warehouse fulfillment. Unit economics of ship-from-store (carrier cost per order from a single store) may be worse than DC bulk fulfillment for many orders. Management already made a judgment call by adopting Amazon MCF instead of activating their own stores.

### Evidence for the counterargument
- 1,095 of 1,933 stores are factory outlets — typically 30-60 minutes outside urban centers [FACT on count; INFERENCE — HIGH on location type]
- Ship-from-store labor productivity at retail stores is typically 40-60% lower than DC pick-pack [INFERENCE — MODERATE — industry benchmarks]
- Amazon MCF was adopted February 2025 specifically because adidas's own network cannot deliver Prime-equivalent speed — management has already priced this in [FACT]

### Evidence against the counterargument
- 838 concept stores are in premium urban locations — the right stores for same-day urban coverage [FACT]
- RFID accuracy >99% means inventory data at concept stores is reliable for order routing [FACT]
- GK OmniPOS ship-from-store capability confirmed at 1,300+ stores [FACT]
- The AI routing engine only routes to stores where economics are positive — it is not a blanket policy [INFERENCE — HIGH]
- Nike, Zara, and John Lewis operate urban ship-from-store with positive unit economics at sufficient order density [INFERENCE — MODERATE]

### Validation test
Ask: "What is your current cost-per-order from ship-from-store vs. DC fulfillment? At what order density per store does ship-from-store reach positive unit economics?" If concept stores already prove out, the routing engine is the only missing piece.

### Confidence assessment
**MEDIUM-HIGH.** Adjustment applied: the provocation focuses on the 838 concept stores in urban locations, not the full 1,933. The routing engine decides optimally — it does not route blindly to every store.

---

## COUNTERARGUMENT 3: "adidas's internal AI team may not need us for this"

### The challenge
The Databricks Data+AI Summit 2026 presentation shows adidas governing production-scale multi-agent AI fleets — ahead of most consumer goods companies. 85% of engineers use GitHub Copilot daily with 20-25% confirmed productivity gains. The internal team is clearly sophisticated. Our value proposition must be something they cannot do alone.

### Evidence for the counterargument
- Multi-agent AI governance architecture in production — not a proof of concept [FACT]
- 85% GitHub Copilot daily adoption — best-in-class by any industry standard [FACT]
- MosaicML 91.67% cost reduction on GenAI — genuine AI engineering capability [FACT]
- Active AI/ML hiring (NLP, Computer Vision, Deep Learning) in Q1 2026 [FACT]

### Evidence against the counterargument
- No CTO or CDO at Executive Board level — technology filtered through CFO's P&L lens, creating approval barriers for cross-functional AI architecture [FACT]
- AI sits in fragmented point solutions: Databricks, AWS Bedrock, SageMaker, o9, project44 — no confirmed unified enterprise AI strategy [INFERENCE — HIGH]
- 39 3PL-managed DCs represent a "Brain shadow" — adidas AI has limited visibility at these sites [INFERENCE — HIGH]
- TRANS4RM is incomplete — master data in supply chain and sales is still limited [FACT]
- Building individual AI models is different from integrating them across 62,000 employees, 39 3PL partners, and an incomplete ERP [INFERENCE — HIGH]

### Validation test
Ask: "Who owns the enterprise AI architecture connecting Databricks, project44, o9, and S/4HANA? Is there a funded integration roadmap?" No single owner = our scope is clear.

### Confidence assessment
**HIGH.** The CTO/CDO absence is confirmed fact. The integration gap is structurally observable. Our right to win is enterprise integration, security, change management, and operating model redesign — not individual algorithms.

---

## COUNTERARGUMENT 4: "The organic strategy gets adidas to 10% without supply chain AI"

### The challenge
adidas improved EBIT from 1.3% to 8.3% in 2 years through brand strategy alone — no confirmed AI supply chain program drove this. If Gulden's strategy keeps working — lifestyle momentum, wholesale re-engagement, DTC +16% CN in FY2025 — does adidas reach 10% organically? If yes, our case weakens.

### Evidence for the counterargument
- EBIT +669% in 2 years driven primarily by brand and channel strategy [FACT]
- Gulden's wholesale rebalancing and full-price discipline are working without AI [FACT]
- ASICS achieved its margin improvement similarly — through pricing discipline and DTC mix, not supply chain AI [FACT/INFERENCE — HIGH]
- Each +1% CN revenue growth adds ~€25M+ EBIT at current operating leverage [INFERENCE — HIGH]

### Evidence against the counterargument
- FY2026 guidance: €2.3B vs. analyst consensus €2.72B — a €420M gap [FACT]
- Gap to 10% target: 1.7pp × €24.8B revenue = ~€422M EBIT needed [INFERENCE — HIGH — mathematical from confirmed data]
- €200M tariff headwind consumes 47% of the gap in 2026 alone [FACT]
- Gulden himself flagged the Samba/Gazelle lifestyle cycle will fade — when it does, operational efficiency must hold margin [FACT — earnings call]
- North America at +4% CN vs. +13% global — unfulfilled demand in the World Cup host market [FACT]

### Validation test
Model: if revenue grows +8% per year (management guidance) with current cost structure and no supply chain improvement, implied 2028 EBIT margin is approximately 9.0-9.5% — below target. The last 0.5-1.0pp requires operational efficiency gains.

### Confidence assessment
**MEDIUM.** adidas likely reaches 9-9.5% organically. The last 0.5-1.0pp to 10%+ — against a tariff headwind — requires supply chain efficiency. Our thesis holds for the final leg of the improvement, not the entire journey.

---

## COUNTERARGUMENT 5: "The tariff provocation is backward-looking — the crisis has already passed"

### The challenge
CEO Gulden confirmed in 2025 that China-to-US sourcing has been eliminated. The €200M headwind is already embedded in guidance — management has priced it in. Pre-tariff front-loading was executed ahead of April 2026 effective dates. Is the tariff problem already solved?

### Evidence for the counterargument
- China-to-US sourcing elimination complete [FACT — Gulden statement]
- €200M headwind embedded in FY2026 guidance — priced in [FACT]
- Pre-tariff front-loading executed ahead of April 4-9, 2026 effective dates [FACT]
- 3,000+ supplier factory users on SAP BTP — procurement is digitized [FACT]

### Evidence against the counterargument
- Section 122 tariff expires July 24, 2026 — a second inflection point requires entirely new scenario analysis [FACT — current_signals.md]
- Residual tariff risk sits in Vietnam (27% of sourcing) and Indonesia (19%) — both previously targeted by US trade actions [FACT]
- project44 adopted February 2026 — only 8 weeks old; AI scenario planning not confirmed active [FACT]
- Trade policy under current US administration changes week-to-week — quarterly manual analysis is too slow [FACT — current_signals.md context]
- No confirmed AI-powered continuous tariff scenario simulation in production [FACT — absence]
- The 2025 China pivot took months — not the 48-72 hour response speed that AI enables [INFERENCE — HIGH from timeline]

### Validation test
Ask: "What is the current cycle time from a tariff policy change to a final sourcing shift decision?" If it is weeks, the gap is confirmed.

### Confidence assessment
**HIGH.** The provocation is explicitly forward-looking — the July 24 Section 122 expiry is the anchor, not the 2025 crisis. Vietnam and Indonesia exposure creates ongoing risk. This holds.

---

## OVERALL THESIS ASSESSMENT

| Counterargument | Threat Level | Resolution |
|---|---|---|
| Demand planning gap may be closed | MEDIUM | Phase One validates; TRANS4RM incompleteness is confirmed structural barrier |
| Ship-from-store overstated | MEDIUM | Narrow framing to 838 concept stores; routing engine selects optimally |
| Internal AI team is too capable | LOW-MEDIUM | Integration architecture is our scope — not individual AI components |
| Organic strategy closes 10% gap alone | MEDIUM | Last 0.5-1pp requires supply chain efficiency; tariff headwind absorbs organic gains |
| Tariff problem already solved | LOW | Provocation is forward-looking: July 24 deadline; Vietnam/Indonesia risk confirmed |

**Overall thesis confidence: HIGH.**
All five counterarguments are resolvable with appropriate framing. No provocation is invalidated. Two refinements applied to Job 3A:
1. Ship-from-store provocation specifies concept stores in urban locations, not the full 1,933.
2. Tariff provocation is explicitly forward-looking — anchored to the July 24, 2026 Section 122 expiry, not the 2025 China pivot.
