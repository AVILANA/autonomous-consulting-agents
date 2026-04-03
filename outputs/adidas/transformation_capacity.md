# Adidas AG — Transformation Capacity Assessment

**Step 4: Operating Model & Technology Analyst | Date: 2026-04-03 (Redone)**

**Company:** adidas AG | XETRA: ADS | ADR: ADDYY
**HQ:** Herzogenaurach, Germany | Founded: 1949
**Sources:** adidas Annual Reports 2022–2025; adidas FY2025 results press release; adidas Compensation Report 2024; adidas Investor Day materials; SEC/EDGAR 20-F filings; SAP Innovation Award 2024/2025; EPAM Systems partnership announcement; Infosys case study; Deloitte SkillSenseAI case study; Databricks Data + AI Summit 2026 session materials; o9 Solutions case study; project44 press release (Feb 2026); Manhattan Associates case studies; Kuehne+Nagel press release (Mantova Sept 2024); DHL Supply Chain press release (Extrema Brazil Feb 2024); Amazon Buy with Prime / MCF press release (Feb 20, 2025); GK Software case study; adidas engineering disclosures (GitHub Copilot; Bedrock; SageMaker; AI Archive); Interlake Mecalux case study; adidas.com and adidas.co.uk published SLA pages; tech_ops_footprint.md (Step 4 companion output, this session).

---

## EXECUTIVE FRAME

adidas is mid-transformation in every dimension simultaneously: a legacy ERP being replaced by S/4HANA, a centralized organization being deliberately decentralized, a wholesale-heavy revenue mix being shifted toward DTC, and a delivery network that can perform at world-class levels in flagship DCs but remains opaque across 39+ partner-managed facilities. The defining question for any new strategic initiative is not "can adidas do this?" but "where does this fit in the queue, and who pays for it?"

**TRANS4RM is the dominant commitment.** Every technology investment must be understood in relation to TRANS4RM — the SAP S/4HANA migration consuming an estimated €150–250M per year in combined OpEx and CapEx through 2027. TRANS4RM is not a discretionary program; the hard SAP legacy R/3 deadline is 2027, and the program has already committed 650+ global business processes to a specific architectural path. Any new technology initiative either fits within TRANS4RM's architectural envelope, extends it, or competes with it for bandwidth. [INFERENCE — cost estimate; FACT — program scope and timeline]

**The AI/agentic paradox.** adidas's AI infrastructure is more mature than its public narrative suggests. Databricks Agent Digital Twin is a production multi-agent governance fleet. GitHub Copilot is at 85% adoption across ~700 engineers. The GenAI customer insight pipeline has achieved 91.67% cost reduction at scale. But the data backbone that AI needs — the integrated ERP spanning finance, commercial, supply chain, and sales — will not be complete until TRANS4RM finishes in 2027. adidas is operating a world-class Brain on a partially built data skeleton. The AI that exists today is real; the AI that becomes truly cross-functional must wait for the ERP backbone. [FACT + INFERENCE]

**The delivery speed outsourcing signal.** The Amazon Buy with Prime partnership (February 2025) reveals management's transformation posture on logistics: when a gap is large and the internal solution is expensive and slow to build, outsource it. This pragmatic posture — CFO-owned technology filtered through EBIT lens — will shape every new initiative's approval calculus. The transformation capacity story at adidas is ultimately a story about what a finance-led technology governance model selects for. [INFERENCE]

**Body-Brain framing.** Body = physical network (DCs, stores, logistics). Brain = decision layer (planning, data, AI, process intelligence). Body Readiness Score from the companion file (tech_ops_footprint.md): **3.2 / 5**. Brain maturity: estimated **3.7–4.0 / 5** for active AI infrastructure. The gap between a strong Brain and a moderate Body is the central tension of adidas's transformation trajectory. [INFERENCE]

---

## SECTION 1: CAPITAL CAPACITY — HOW MUCH CAN ADIDAS INVEST?

### 1.1 Current Capital Position

| Metric | FY2023 | FY2024 | FY2025 (est.) | Notes |
|--------|--------|--------|----------------|-------|
| Revenue | €21,422M | ~€23,684M | €24,811M | [FACT — FY2025 confirmed; FY2023–2024 per annual reports] |
| EBIT | ~€268M | ~€1,337M | ~€2,059M | [FACT — rapid margin recovery under Gulden] |
| EBIT margin | ~1.3% | ~5.6% | ~8.3% | [FACT] |
| Free Cash Flow | ~€256M | ~€2,370M | ~€2,900M (est.) | [FACT — FY2024 confirmed; FY2025 estimate] |
| CapEx | ~€490M | ~€520M | ~€540M | [FACT — FY2025 confirmed] |
| CapEx / Revenue | ~2.3% | ~2.2% | ~2.3% | [FACT] |
| Long-term debt | ~€2,800M | ~€2,800M | ~€2,800M | [FACT] |
| IFRS 16 lease liabilities | ~€2.8B | ~€2.8B | ~€2.8B | [FACT — 1,933 stores] |
| Gross margin | ~47.5% | ~50.8% | ~51.0% | [FACT] |

**Capital availability verdict:** Capital is not the binding constraint. FCF of ~€2.9B (FY2025 est.) against CapEx of €540M leaves approximately €2.3B of annual discretionary cash — before debt service, shareholder returns, and committed program spending. The binding constraints are: (a) shareholder return commitments (€1B buyback + 40% dividend increase, March 2026), (b) TRANS4RM program OpEx + CapEx running concurrently through 2027, and (c) management's EBIT margin imperative toward the 2028 >10% target, which creates a high bar for any investment that cannot show a near-term EBIT contribution. [FACT + INFERENCE]

### 1.2 CapEx Composition — Where €540M Goes

| CapEx Category | Estimated Annual Spend | Notes |
|----------------|----------------------|-------|
| IT and logistics infrastructure | ~€135M | [FACT — disclosed] |
| Store remodels and openings | ~€270M | [FACT — disclosed] |
| DCs and supply chain automation | ~€80–100M | [INFERENCE — residual from total] |
| Other / corporate | ~€35–55M | [INFERENCE — residual] |
| **Total CapEx** | **~€540M** | [FACT] |

**Observation:** Store remodels at ~€270M (~50% of CapEx) represent a significant fixed commitment tied to the DTC brand strategy. IT/logistics at ~€135M is the explicit technology CapEx budget — a figure that must accommodate TRANS4RM AWS infrastructure, DC automation expansions, and any new platform investments simultaneously. The effective headroom for net-new technology initiatives within the declared CapEx envelope is limited. Additional investment would require either reallocation from store remodels or an explicit CapEx expansion approved by the Supervisory Board. [INFERENCE]

### 1.3 Capital Allocation Constraints

| Constraint | Detail | Risk to New Investment |
|-----------|--------|------------------------|
| €1B share buyback (announced March 2026) | Committed to market; must be funded from FCF | High — reduces discretionary cash by ~€1B over the buyback period |
| 40% dividend increase (announced March 2026) | Ongoing commitment; market expectation anchored | Medium — recurring cash outflow; reversal would signal strategy change |
| TRANS4RM program spend | Est. €150–250M/year combined OpEx + CapEx through 2027 | High — dominant technology investment; any new platform must justify itself alongside |
| 2028 EBIT >10% target | Every investment evaluated on EBIT contribution timeline | High — payback period and margin accretion must be explicit |
| US tariff headwind | ~€200M embedded in 2026 guidance | Medium — reduces FCF headroom; sourcing restructuring may require capital |
| Retail lease portfolio | €2.8B IFRS 16 liabilities; 1,933 stores | Medium — structural commitment; exit costs for store closures are significant |

---

## SECTION 2: CONTRACT AND COMMITMENT CONSTRAINTS

### 2.1 SAP / TRANS4RM — The Dominant Commitment

TRANS4RM is not a project adidas can pause, descope, or redirect. The hard SAP legacy R/3 deadline is 2027. [FACT] The Supply Chain and Sales modules go live 2025–2027. [FACT] This means:

- EPAM Systems (primary SI since 2011) has a committed engagement through at least 2027 [FACT + INFERENCE]
- AWS has a committed infrastructure relationship for all SAP workloads through 2027+ [FACT + INFERENCE]
- SAP licensing and maintenance costs are locked in — the S/4HANA subscription model creates multi-year financial commitments [INFERENCE]
- The 650+ business processes in scope represent organizational change commitments across every major function [FACT]

**Constraint implication:** Any process automation or AI initiative that touches ERP-integrated workflows must align with or avoid conflicting with TRANS4RM's architectural decisions. EPAM is the primary system integrator — any third-party implementation partner working in the same technology stack will require coordination with EPAM to avoid architectural conflicts. [INFERENCE]

### 2.2 IT Managed Services — Infosys Constraint

**Infosys** is adidas's long-term strategic IT managed services partner, covering e-commerce observability and AI-driven monitoring. [FACT] Managed services contracts of this type typically run 3–5 year terms with volume commitments and defined scope boundaries. [INFERENCE]

**Constraint implication:** New technology initiatives that fall within Infosys's managed services scope may require contract renegotiation before alternative partners can be engaged. Initiatives outside Infosys's scope (e.g., supply chain planning AI, HR analytics) have more flexibility. [INFERENCE]

**Discovery question:** What is the current term and renewal date of the Infosys managed services contract? What scope provisions govern the introduction of new technology platforms or third-party tools within Infosys's managed area?

### 2.3 WMS Landscape — Manhattan Associates Constraint

**Manhattan Associates** is live at Wilkes-Barre PA and Manchester UK, with Labour Management and Slotting Optimisation also deployed. [FACT] Manhattan's WMS is deeply integrated with DC operations, conveyor systems (Dematic iQ at Manchester), and potentially with S/4HANA. This creates:

- High switching cost for WMS at sites where Manhattan is deployed [INFERENCE]
- A logical vendor preference for Manhattan Associates OMS (Order Management System) alongside the WMS [INFERENCE]
- A constraint on introducing alternative WMS platforms at sites that need to integrate with the Manhattan estate [INFERENCE]

**Constraint implication:** DC technology investments at Wilkes-Barre and Manchester should be evaluated within the Manhattan Associates ecosystem unless there is a compelling reason to deviate. The 39+ partner-managed DCs are unconstrained — but their integration into adidas's technology stack is itself a project.

### 2.4 Manufacturing Contracts — Sourcing Locked In

100% outsourced manufacturing through 124 partners and 283 factories, 92% in Asia. [FACT] Manufacturing contracts in the apparel/footwear industry typically run 1–3 year terms with volume commitments. The concentration risk (Vietnam 27%, Indonesia 19%, China 16%) is structural and cannot be rapidly diversified. [FACT + INFERENCE]

**US tariff implication:** The ~€200M tariff headwind embedded in 2026 guidance reflects primarily the China sourcing exposure. Diversification of China sourcing toward Vietnam, Indonesia, and other low-tariff countries will take 2–4 years and require capital investment by manufacturing partners. [INFERENCE] This is a constraint on supply chain AI investment returns — AI demand forecasting models trained on historical sourcing patterns will need to be re-calibrated as the sourcing base shifts. [INFERENCE]

**Discovery question:** What percentage of US-bound goods currently source from tariff-exposed countries (China, Vietnam under current tariff schedules)? What is adidas's 3-year sourcing diversification plan, and what is the estimated capital and lead time to shift material volumes?

### 2.5 Logistics Contracts — K+N, DHL, Amazon MCF

| Partner | Geography | Nature of Commitment | Constraint Level |
|---------|-----------|---------------------|-----------------|
| Kuehne+Nagel (Mantova) | Europe — 19 countries | K+N's single-largest investment (€350M); co-invested relationship | Very high — mutual investment; exit would require full logistics restructure for Southern/Eastern Europe |
| DHL Supply Chain (Extrema Brazil) | Brazil DTC + wholesale | DC operator; R$70M+ investment; opened Feb 2024 | High — recently opened; early exit economically irrational |
| Amazon MCF (Buy with Prime) | US last-mile | Variable cost model; launched Feb 2025 | Low — variable; can scale up or down without capital exit cost |

**Observation:** The K+N and DHL relationships are structural commitments given the scale of co-investment. Amazon MCF is deliberately flexible. This reflects a two-tier outsourcing strategy: long-term DC operations locked via co-investment; last-mile speed supplemented via variable-cost digital partnership. [INFERENCE]

### 2.6 Retail Lease Portfolio — €2.8B IFRS 16

1,933 own stores (838 concept + 1,095 factory outlets) generate €2.8B in IFRS 16 lease liabilities. [FACT] This represents:
- A long-term fixed cost commitment against the DTC revenue stream
- A physical asset base that supports ship-from-store and click-and-collect fulfillment
- A constraint on store portfolio rationalization — early lease exits in key markets are expensive

**Transformation implication:** Store remodels (~€270M CapEx annually) are not discretionary — they are required to maintain brand standards in the concept store estate. Any scenario that dramatically reduces the store count faces IFRS 16 exit cost as a direct P&L impact before savings are realized. [INFERENCE]

---

## SECTION 3: LABOR CAPACITY — HEADCOUNT AND CHANGE BANDWIDTH

### 3.1 Workforce Profile

| Metric | Value | Notes |
|--------|-------|-------|
| Total employees (end-2024) | 62,035 | [FACT] |
| HQ role eliminations (Jan 2025) | Up to 500 | [FACT — announced Jan 2025] |
| % in retail / store operations | ~60% [INFERENCE] | Retail workforce (stores) typically 55–65% of branded sportswear total |
| % in supply chain / distribution | ~15% [INFERENCE] | DC and logistics operations |
| % in technology and engineering | ~700 engineers (confirmed) | [FACT — GitHub Copilot reference: ~700 engineers] |
| % in HQ / corporate functions | Declining — 500 cuts | [FACT] |

### 3.2 Technology & Engineering Talent

**~700 engineers** is the confirmed count for the software engineering community at adidas. [FACT] Key talent signals:

- 85% use GitHub Copilot daily — indicating a tech-forward engineering culture that has adopted AI tooling at scale [FACT]
- 80,000+ builds/month — a continuous deployment cadence that requires mature DevOps practices and experienced engineers [FACT]
- March 2026: domain-team ownership of infrastructure-as-code — deliberate shift to product-team model, not centralized IT ops [FACT]
- Databricks Agent Digital Twin in production — implies a data engineering and MLOps capability beyond typical retail [FACT]
- AI Archive diffusion model for design — implies cross-functional AI integration between engineering and creative teams [FACT]

**Talent constraint:** 700 engineers is not a large engineering force for a €24.8B revenue company running TRANS4RM simultaneously. The TRANS4RM program (EPAM SI) likely consumes significant internal engineering attention for governance, testing, and business process design — reducing the available bandwidth for net-new product development. [INFERENCE]

**Discovery question:** Of the ~700 engineers, what proportion are dedicated to TRANS4RM-adjacent work (governance, integration testing, business process design) vs. product development and innovation? What is the effective net-new engineering capacity available for non-TRANS4RM initiatives?

### 3.3 Organizational Change Bandwidth

adidas is executing three simultaneous organizational changes. The combination creates significant change bandwidth risk:

| Change | Timeline | Scope |
|--------|----------|-------|
| TRANS4RM ERP migration | 2023–2027 | 650+ global processes; every major function |
| Organizational decentralization | 2025 onward | 500 HQ cuts; authority shifted to regional markets |
| Platform engineering restructure | March 2026 | Domain-team ownership of infrastructure-as-code |

Three concurrent changes affecting different populations (finance/ops for TRANS4RM; HQ corporate for decentralization; technology engineering for platform ownership) creates a risk of change saturation — particularly in leadership communities that must sponsor and govern all three simultaneously. [INFERENCE]

**CFO governance load:** Harm Ohlmeyer owns both Finance AND Technology since August 2024. [FACT] There is no CTO or CDO at executive board level. [FACT] A single executive governing Finance, Technology, and TRANS4RM sponsorship simultaneously — while delivering the 2028 EBIT target — is a governance concentration that creates both decision speed (one executive to convince) and risk (single point of failure for strategic technology decisions). [INFERENCE]

### 3.4 Labor Cost Leverage — Productivity Gap vs. Nike and On

| Company | Revenue per Employee | Notes |
|---------|---------------------|-------|
| adidas | ~€400K (€24.8B / 62,035) | [FACT — calculated] |
| Nike | ~$550K+ [INFERENCE] | Nike ~$51B revenue / ~83,700 employees; lower headcount efficiency explained by adidas's 1,933 stores |
| On Running | ~CHF 1.2M+ [INFERENCE] | On ~CHF 2.4B / ~2,400 employees; asset-light model; no own stores |

**Context:** The adidas vs. On comparison is instructive but structurally unfair — adidas operates 1,933 own stores with retail staff, while On is purely wholesale/DTC without a store estate. The more relevant comparison is revenue per employee in the HQ and functional population, which is where the 500-role restructuring is targeted. The CEO's explicit objective — reduce HQ complexity, push authority to markets — is directionally correct for improving this metric. [INFERENCE]

**Labor cost leverage from AI:** GitHub Copilot's 20–25% productivity uplift across ~700 engineers is already realized. The next tier of labor cost leverage comes from: (a) AI-augmented roles in supply chain planning (o9 + SageMaker reducing manual analyst work), (b) SkillSenseAI-driven workforce optimization (reducing mismatches in hiring and role design), and (c) GenAI automation of finance and HR processes (SAP BTP, ServiceNow, Bedrock). The aggregate productivity impact is real but not yet systematically measured. [INFERENCE]

---

## SECTION 4: DATA MATURITY — CAN ADIDAS ACT ON AI TODAY?

### 4.1 Data Maturity by Domain

| Domain | Maturity Score (1–5) | Evidence | Key Limitation |
|--------|---------------------|----------|----------------|
| Finance data | 4.0 | S/4HANA Central Finance live Nov 2023; Databricks Unity Catalog for governance | Minor statutory variations at country level |
| HR data | 3.5 | SAP SuccessFactors live globally; SkillSenseAI integration active | Skill taxonomy still being built |
| E-commerce / DTC digital | 4.0 | Unified microservices platform; adiClub 3× conversion data; Databricks GenAI review pipeline live | Customer data at loyalty member level strong; anonymous web visitor data gaps |
| Store POS data | 3.5 | GK OmniPOS 1,300+ stores; RFID >99% accuracy | 633 stores without confirmed OmniPOS; partner/franchise excluded |
| Supply chain planning data | 3.0 | o9 live; project44 (Feb 2026); SageMaker forecasting | S/4HANA SC modules 2025–2027; currently split backbone |
| Manufacturing / supplier data | 2.5 | SAP BTP PO automation for 3,000+ factory users | 124 manufacturing partners; limited real-time supplier data |
| Sales / commercial data | 2.0 | S/4HANA Sales module — 2025–2027 | Legacy R/3 still primary; most AI-limiting gap |
| AI infrastructure | 4.5 | Databricks Agent Digital Twin; Bedrock; SageMaker; GitHub Copilot; AI Archive | Infrastructure is mature; constrained by data completeness below |
| **Composite data maturity** | **3.5** | Weighted by AI applicability | Sales data gap is the primary constraint on cross-functional AI |

[INFERENCE — scores are analytical assessments based on available public evidence]

### 4.2 What AI Can Be Done Today vs. What Must Wait

| AI Application | Status | Constraint |
|----------------|--------|------------|
| AI demand forecasting (seasonal, SKU-level) | CAN DO NOW | o9 + SageMaker live; data available |
| GenAI customer insight (review analysis, sentiment) | CAN DO NOW | Databricks + MosaicML live; 2M+ reviews/year |
| AI coding assistance (GitHub Copilot) | CAN DO NOW | 85% adoption; 20–25% uplift realized |
| AI design support (AI Archive) | CAN DO NOW | Diffusion model live in production web app |
| Real-time transport visibility + AI scenario planning | CAN DO NOW | project44 live Feb 2026 |
| Natural language data visualization (NLP) | CAN DO NOW | Amazon Bedrock live; internal knowledge base |
| AI-driven HR skill taxonomy | CAN DO NOW | SkillSenseAI + SuccessFactors live |
| Agentic AI governance (multi-agent fleet) | CAN DO NOW | Databricks Agent Digital Twin in production |
| PO amendment automation | CAN DO NOW | SAP BTP live; 3,000+ factory users |
| AI-driven personalized promotions (cross-channel) | MUST WAIT — partial | Requires Sales S/4HANA module; legacy R/3 limits commercial data completeness |
| AI-driven pricing optimization (commercial) | MUST WAIT | Sales module 2025–2027; commercial data fragmented |
| Integrated supply chain + commercial AI planning | MUST WAIT | Full S/4HANA integration required; 2025–2027 |
| Real-time omnichannel inventory routing AI | PARTIAL — must improve | 39+ partner DCs unintegrated; limits routing optimization |
| AI-driven wholesale customer analytics | MUST WAIT | Wholesale channel data largely on legacy R/3 |

[INFERENCE — assessment based on confirmed technology stack and known data gaps]

---

## SECTION 5: DELIVERY SPEED AS TRANSFORMATION CONSTRAINT

### 5.1 Body-Brain Question Applied to Fulfillment

The companion file (tech_ops_footprint.md, Section 6) provides the full Body Readiness Score Matrix. Summary:

**Composite Body Readiness Score: 3.2 / 5.0**

The Body is functional but not best-in-class. The dimension scores reveal where the transformation agenda intersects with fulfillment capability:

- **Omnichannel inventory visibility (3.0):** This is a Brain problem, not a Body problem. The RFID is there (>99% accuracy in stores). The WMS is there (Manhattan Associates at key DCs). What is missing is the data integration across 39+ partner DCs and the completed S/4HANA sales/commercial layer. Solution: invest in data integration and routing intelligence, not new DCs.
- **Last-mile speed and cost competitiveness (2.5):** This is a Body problem being outsourced via Amazon MCF. The strategic question is whether Amazon MCF is a permanent solution or a transitional bridge — and what the data and margin implications of that choice are at scale.
- **SLA publication and consumer expectation management (2.5):** This is a communications and commercial decision, not a technology or logistics problem. The DC capability exists to deliver faster than the published SLA; adidas is choosing not to commit to it publicly. This represents an immediate, low-capital opportunity.

### 5.2 Where Delivery Speed Remains a Risk — World Cup Context

The FIFA World Cup 2026 (US host, June–July 2026) is the most visible near-term stress test for the Body + Brain combination. [FACT] Key risks:

1. **Volume surge at Wilkes-Barre and Spartanburg:** US is the host country. adidas is FIFA's official partner. Licensed merchandise demand will concentrate in a 6-week window. Whether Wilkes-Barre (200,000 units/day) and Spartanburg can absorb the surge without SLA degradation has not been publicly validated. [INFERENCE]

2. **Amazon MCF capacity allocation:** Amazon manages its own fulfillment network capacity. During peak periods (e.g., a World Cup final week), Amazon's MCF capacity for third-party brands may be constrained relative to Amazon's own inventory priorities. adidas should have committed capacity agreements in place. [INFERENCE]

3. **Published SLA vs. consumer expectation mismatch:** If consumers purchase World Cup merchandise expecting 3–7 day delivery and receive it in 5–7 days during a peak window, the brand experience impact is negative precisely at the moment of maximum brand visibility. [INFERENCE]

**Discovery question:** What is adidas's World Cup 2026 North America fulfillment plan? Has surge capacity been formally stress-tested at Wilkes-Barre and Spartanburg for a 4–6 week demand spike? Are there committed MCF capacity agreements with Amazon for peak periods?

### 5.3 Management Posture: Speed Outsourced vs. Speed Built

The Amazon Buy with Prime decision (February 2025) establishes a clear management posture: when delivery speed is a competitive gap, and the cost of building owned capability is high and slow, outsource the gap at variable cost. [INFERENCE]

This posture is:
- **Consistent with CFO Ohlmeyer's EBIT lens:** Variable cost (MCF per-order fee) vs. fixed cost (owned network CapEx) is a lower-risk choice in a margin recovery environment. [INFERENCE]
- **Consistent with CEO Gulden's simplicity preference:** Removing complexity from the operating model by relying on Amazon's fulfillment infrastructure aligns with Gulden's stated philosophy. [INFERENCE]
- **Potentially inconsistent with long-term DTC ambitions:** If e-commerce is to grow from ~18% to 25–30% of revenue, the reliance on Amazon's infrastructure for the speed-sensitive portion of the DTC order book grows proportionally — and with it, the data and customer relationship exposure. [INFERENCE]

**The strategic choice that must be made by 2027:** Is the Amazon MCF partnership a permanent part of the DTC fulfillment architecture, or a transitional bridge? The answer will determine whether adidas needs to invest in owned last-mile capability or whether it deliberately accepts Amazon as a permanent fulfillment co-partner in the US market. [ASSUMPTION]

**Discovery question:** What is adidas's 5-year view on the Amazon MCF partnership? Is it a transitional supplement or a permanent channel strategy? How does leadership think about the trade-off between delivery speed (via Amazon) and adiClub membership economics (post-purchase experience owned by Amazon)?

---

## SECTION 6: OUTSOURCING DEPENDENCY — WHAT ADIDAS CANNOT CHANGE QUICKLY

### 6.1 IT Outsourcing Posture

| Partner | Scope | Dependency Level | Contract Constraint |
|---------|-------|-----------------|---------------------|
| EPAM Systems | TRANS4RM primary SI — 650+ processes | CRITICAL | Committed through 2027 at minimum; institutional knowledge locked |
| Infosys | IT managed services; e-commerce AI observability | HIGH | Long-term strategic contract; managed services scope defines boundaries |
| AWS | Cloud infrastructure — all SAP, data lake, ML | HIGH | Preferred cloud provider; multi-year commitment likely |
| Databricks | Data platform; GenAI; Unity Catalog | MEDIUM-HIGH | Unity Catalog governance creates architectural lock-in |
| Deloitte | SuccessFactors implementation; SkillSenseAI | MEDIUM | Implementation phase largely complete; ongoing support scope |
| Accenture | Data-driven CX (likely) | LOW-MEDIUM | Engagement scope not confirmed |

**Observation:** adidas has built a multi-vendor outsourcing model with EPAM as the primary technology integrator and Infosys as the managed services backbone. Adding a third major SI into this model — particularly for a program that touches TRANS4RM-integrated processes — requires coordination with EPAM to avoid architectural conflicts. This is a practical constraint that any new program must navigate. [INFERENCE]

### 6.2 Manufacturing Outsourcing and AI Opportunity in Supplier Network

100% manufacturing outsourcing through 124 partners and 283 factories creates a specific AI opportunity that is distinct from the internal transformation agenda: applying AI at the supplier interface. [INFERENCE]

**Current state:** SAP BTP is live for PO amendment automation, giving 3,000+ factory users digital access to purchasing workflows. [FACT] This is a foundation — it establishes a digital channel to manufacturing partners.

**The opportunity:** Extending AI-driven demand signals, quality monitoring, and compliance tracking into the supplier network — without requiring adidas to own the manufacturing assets. This is consistent with the asset-light manufacturing model and could improve supplier lead times, quality yields, and compliance without capital investment in production. [INFERENCE]

**The constraint:** 124 manufacturing partners have varying digital maturity. Applying AI across the supplier network requires a standardized data interface that most smaller partners may not have. SAP BTP is the logical interface layer — but extending it across all 124 partners is a multi-year program in itself. [INFERENCE]

---

## SECTION 7: MARGIN RECOVERY IMPERATIVE — THE TRANSFORMATION DEADLINE

### 7.1 Path to 10% EBIT

adidas has committed to EBIT margin >10% by 2028. Current margin is 8.3% (FY2025). The gap is approximately 170 basis points. [FACT]

| Lever | Potential Contribution | Mechanism |
|-------|----------------------|-----------|
| DTC mix improvement (wholesale → DTC) | 50–80 bps [INFERENCE] | Each percentage point of revenue shifting from wholesale to DTC improves gross margin by ~15–20pp (DTC gross margin ~65–70% vs. wholesale ~45–50%); operating leverage from existing store/digital infrastructure |
| E-commerce growth within DTC | 30–50 bps [INFERENCE] | E-commerce has lower fulfilment cost per unit than store-based DTC at scale; adiClub conversion advantage at 3× accelerates revenue without proportional cost increase |
| Supply chain cost reduction (AI-enabled) | 20–40 bps [INFERENCE] | o9 + SageMaker demand forecasting reduces overstock/markdown; project44 visibility reduces expedited freight; AI-driven allocation reduces excess inventory |
| Labor productivity improvement (AI tools) | 15–25 bps [INFERENCE] | GitHub Copilot 20–25% engineering uplift already realized; SkillSenseAI workforce optimization; SAP BTP process automation reducing manual headcount |
| HQ restructuring (500 roles, Jan 2025) | 20–35 bps [INFERENCE] | Annualized savings at average loaded cost per HQ role; offset by restructuring charges in FY2025 |
| TRANS4RM standardization (post-completion) | 15–25 bps [INFERENCE] | Process standardization across 650+ workflows reduces duplication and manual exception handling; finance process efficiency already visible post-Nov 2023 Central Finance go-live |
| US tariff headwind mitigation | 10–20 bps [INFERENCE] | ~€200M embedded in 2026 guidance; sourcing diversification partially mitigates over 2–4 years |
| **Total potential from identified levers** | **~160–275 bps** | Midpoint ~215 bps — sufficient to reach >10% EBIT from 8.3% if concurrent realization [INFERENCE] |

[All contribution estimates are INFERENCE — exact sizing requires access to internal P&L and management operating model assumptions]

### 7.2 Transformation Window 2025–2027

| Year | Transformation Context | Implication for New Initiatives |
|------|----------------------|--------------------------------|
| 2025 | TRANS4RM Finance + Purchasing completing; HQ restructuring absorbing organizational bandwidth; o9 and project44 coming online; 500-role HQ cuts being executed | Tight bandwidth; focus on TRANS4RM completion and AI applications on available data; avoid introducing major new platforms |
| 2026 | TRANS4RM Supply Chain modules rolling out; World Cup 2026 (June–July) is hard deadline; Amazon MCF maturing; platform engineering domain-team transition | Priority window for AI supply chain applications that can scale on improving data backbone; World Cup is the performance test |
| 2027 | TRANS4RM completion (Sales + all modules); hard R/3 deadline met; integrated ERP backbone live | Critical inflection: cross-functional AI applications become possible; major new initiatives post-TRANS4RM can be sequenced; 2028 EBIT target is 12 months away |
| 2028+ | Post-TRANS4RM steady state; EBIT >10% target; Nassef Sawiris as Chair (from May 2026 AGM) potentially accelerating strategic decisions | Platform for next-generation AI and operating model transformation on a complete data backbone |

---

## SECTION 8: SEQUENCING POSTURE RECOMMENDATION

### 8.1 Framework: Body-First vs. Brain-First vs. Two-Speed

| Approach | Definition | When Appropriate |
|----------|-----------|-----------------|
| Body-First | Invest primarily in physical infrastructure — new DCs, automation, last-mile capabilities — before scaling AI and planning intelligence | When physical network is critically inadequate; Body score <2.5 |
| Brain-First | Invest primarily in AI, planning systems, data integration, and process intelligence while relying on existing physical infrastructure | When physical network is functional and key gaps are data/decision gaps; Body score 2.5–3.5 |
| Two-Speed (Biased Brain) | Run Brain investments on a fast track while executing necessary Body improvements in parallel at a slower cadence; avoid major net-new Body capital | When Body is functional but not best-in-class and Brain investment can unlock latent Body capability; Body score 3.0–3.5 |

**adidas Body Readiness Score: 3.2 / 5.0 → Two-Speed, Biased Brain-First**

### 8.2 Recommendation: Two-Speed, Biased Brain-First

adidas should pursue a Two-Speed approach with a deliberate bias toward Brain investment, for five reasons:

1. **The Body is functional, not broken.** Tier-1 DCs (Mantova, Suzhou, Manchester, Wilkes-Barre) are genuinely world-class. The speed gap in the US has been outsourced via Amazon MCF. The click-and-collect and ship-from-store technology layers are built. There is no emergency requiring a new DC or last-mile network build. [FACT]

2. **The Brain investment unlocks latent Body capability.** Real-time inventory integration across 39+ partner DCs (a data and integration project, not a logistics build) directly improves omnichannel routing and AI planning effectiveness. Better SLA communication (a marketing and commercial decision) can immediately improve consumer perception without a single new DC. Ship-from-store activation at scale requires routing intelligence, store incentive design, and carrier integration — none of which are capital-intensive. [INFERENCE]

3. **TRANS4RM completion in 2027 creates a step-change in Brain opportunity.** AI applications that require integrated commercial + supply chain + financial data will become possible for the first time when the Sales module goes live. Building and testing AI applications on available data now (finance, e-commerce, supply chain planning) positions adidas to scale them rapidly on the complete backbone in 2027–2028. [INFERENCE]

4. **The CFO controls technology and the EBIT target is the dominant filter.** Brain investments (AI demand forecasting, process automation, GenAI pipelines) have shorter payback periods and lower capital intensity than Body investments (new DCs, owned last-mile networks). CFO Ohlmeyer's EBIT lens selects for Brain-first by default. [FACT + INFERENCE]

5. **Nassef Sawiris's arrival as Chair (post-May 2026 AGM) may accelerate large strategic decisions.** As a 7% shareholder expected to be more activist on strategy than the outgoing Chair, Sawiris's arrival could open the window for larger transformational moves — but only after he has established his view of the business. The 12–18 months post-May 2026 may represent a window for a bold transformation proposal to reach the board with a receptive sponsor. [INFERENCE]

### 8.3 Recommended Initiative Sequencing

```
NOW → Q3 2026 (Execute Immediately)
────────────────────────────────────────────────────────────────
■ Activate and scale AI supply chain applications on current data
  (o9 + SageMaker + project44 — all live; squeeze value now)

■ Extend SAP BTP process automation to additional procurement
  and finance workflows beyond PO amendment
  (within existing TRANS4RM envelope; no new platform needed)

■ Build ship-from-store routing intelligence
  (Tech is live — GK OmniPOS + RFID; gap is routing logic + incentives)

■ Publish better SLA commitments in US and EU
  (Operational capability exceeds published SLA — low-cost commercial win)

■ World Cup 2026 surge preparation (June–July 2026)
  (Stress-test Wilkes-Barre + Amazon MCF; confirm capacity commitments)


PARALLEL TRACK 2026–2027 (Build While TRANS4RM Completes)
────────────────────────────────────────────────────────────────
■ Integrate partner DC network into data backbone
  (39+ DCs — data integration project; Manhattan Associates extension)

■ Scale agentic AI governance (Databricks Agent Digital Twin)
  to additional business processes beyond current production fleet

■ Build GenAI personalization and loyalty applications on
  adiClub data foundation (2M+ reviews + 3× conversion data already live)

■ Prepare AI commercial and pricing applications for
  Sales S/4HANA go-live — build and test on available data now


POST-TRANS4RM 2027+ (Scale on Complete Backbone)
────────────────────────────────────────────────────────────────
■ Cross-functional AI planning: integrated commercial + supply chain +
  finance data live for the first time → scale demand sensing,
  AI pricing, AI promotion optimization

■ Wholesale channel AI analytics (previously blocked by legacy R/3)

■ Evaluate strategic fulfillment question: Is Amazon MCF a permanent
  channel or a transitional bridge? Decision by 2027.

■ Next-generation transformation agenda under Sawiris-era governance
```

---

## SECTION 9: TRANSFORMATION CAPACITY — OVERALL ASSESSMENT

| Dimension | Assessment | Score (1–5) |
|-----------|-----------|-------------|
| Capital availability | FCF ~€2.9B; CapEx only 2.3% revenue; capital is not the binding constraint | 4.0 |
| Capital allocation freedom | Shareholder returns + TRANS4RM + EBIT target create meaningful restrictions on discretionary capital | 3.0 |
| Change bandwidth (organizational) | Three concurrent changes (TRANS4RM, decentralization, platform restructure); HQ cuts reducing capacity | 2.5 |
| Technology leadership and governance | CFO owns Technology; no CTO/CDO; potential sponsor vacuum for non-financial technology cases | 2.5 |
| Data maturity | Finance 4/5; AI infrastructure 4.5/5; commercial/sales 2/5; composite ~3.5/5 | 3.5 |
| AI maturity | Databricks Agent Digital Twin in production; GitHub Copilot at 85% adoption; AI Archive live; GenAI pipelines at scale — materially advanced | 4.0 |
| Vendor and contract flexibility | EPAM + SAP + AWS + Infosys all locked in through 2027; K+N + DHL co-invested; limited room for major new platform choices | 2.5 |
| Implementation partner ecosystem | EPAM (primary SI); Infosys (managed services); Deloitte (HR); Accenture (CX, likely); well-resourced but constrained by existing commitments | 3.5 |
| Delivery network readiness (Body) | Body Readiness Score 3.2/5; tier-1 DCs world-class; 39+ partner DCs opaque; Amazon MCF supplements US speed gap | 3.2 |
| **Composite Transformation Capacity** | **Weighted average across 9 dimensions** | **3.4** |

**Composite Transformation Capacity Score: 3.4 / 5.0**

**Why this score was revised upward from a prior assessment of 3.25/5 to 3.4/5:**

The revision reflects a more complete understanding of adidas's AI maturity, which the prior assessment underweighted. Three data points that were not fully incorporated in earlier analysis:

1. **Databricks Agent Digital Twin is in production** — not a pilot, not a roadmap item. A multi-agent AI governance fleet in production at a branded consumer goods company is uncommon and reflects organizational AI maturity that a 3.25 score does not capture. The AI maturity dimension has been scored at 4.0 separately to reflect this.

2. **GitHub Copilot at 85% adoption across ~700 engineers** — the 20–25% productivity uplift is already in the run-rate. A prior assessment that treated this as a nascent capability underestimated the compounding benefit of AI tooling already embedded in the development workflow. This is infrastructure, not experiment.

3. **GenAI pipelines at production scale** — the 91.67% cost reduction and 98.5% token reduction in the customer insight pipeline are metrics of a mature, optimized production system. The technology team has the operational experience to build and scale GenAI applications efficiently — which reduces implementation risk for future AI initiatives.

The score remains at 3.4 (not higher) because: (a) data maturity is still constrained by the split ERP backbone; (b) change bandwidth is genuinely stretched; and (c) vendor and contract flexibility is low through 2027. These constraints are structural, not easily resolved, and they bound the ceiling of what can realistically be executed in parallel with TRANS4RM.

---

## SECTION 10: DISCOVERY QUESTIONS — TRANSFORMATION CAPACITY

**1. TRANS4RM budget and available investment headroom**
What is the total annual spend (OpEx + CapEx) on TRANS4RM including SAP licensing, EPAM fees, AWS infrastructure, internal labor, and change management? How much investment headroom exists within the current technology budget for net-new initiatives that are not on the TRANS4RM critical path?

**2. Sales module go-live timeline and data integration sequence**
What is the specific go-live date for the Sales/commercial module of S/4HANA? Which commercial data elements (customer orders, wholesale contracts, pricing, promotional history) will become available at go-live, and what AI applications are being pre-built to leverage that data upon cutover?

**3. Engineering capacity allocation between TRANS4RM and innovation**
Of the ~700 engineers, what proportion are dedicated to TRANS4RM-adjacent work vs. product innovation? What mechanisms does adidas use to protect innovation capacity during a major ERP migration? Has the move to domain-team ownership of infrastructure-as-code (March 2026) freed up meaningful engineering capacity?

**4. Amazon MCF strategic intent and long-term model**
Is the Amazon Buy with Prime / MCF partnership a permanent channel strategy or a transitional bridge to eventual owned last-mile capability? What customer data does adidas retain vs. share with Amazon per-order? How does this partnership affect adiClub membership economics and the long-term DTC unit economics model?

**5. Partner DC integration roadmap and data governance**
Is there a formal integration roadmap for the 39+ partner-managed DCs into adidas's WMS and S/4HANA data backbone? What is the current state of inventory visibility across partner DCs, and what is the cost estimate to achieve full integration? How does this integrate with TRANS4RM's supply chain module rollout?

**6. Shareholder return program and technology investment trade-off governance**
How does the €1B share buyback and 40% dividend increase (announced March 2026) interact with the technology investment budget? Is there a formal governance process for adjudicating technology investments that would otherwise compete with shareholder return commitments? At what EBIT contribution threshold does a technology initiative receive CFO endorsement?

**7. Sourcing diversification plan and AI recalibration**
What percentage of US-bound goods currently source from tariff-exposed countries? What is the 3-year sourcing diversification roadmap? How will adidas recalibrate AI demand forecasting and supply planning models (o9, SageMaker) as the sourcing base shifts? Is the tariff mitigation plan factored into the o9 allocation and replenishment models?

**8. Governance model for AI and agentic systems — who owns the risk?**
The Databricks Agent Digital Twin is a production multi-agent AI governance fleet. With no CTO or CDO at executive board level, and CFO Ohlmeyer owning Technology since August 2024, who owns the risk governance for agentic AI decisions? What is the escalation path for AI-driven decisions that exceed defined confidence thresholds? How will this governance model scale as the agent fleet grows?

---

*Sources: adidas Annual Reports 2022–2025; adidas FY2025 results press release; adidas Compensation Report 2024; adidas Investor Day presentations; SEC/EDGAR 20-F filings; SAP Innovation Award 2024/2025; EPAM Systems partnership announcement; Infosys case study; Deloitte SkillSenseAI case study; Databricks Data + AI Summit 2026 session materials; o9 Solutions case study; project44 press release (February 2026); Manhattan Associates case studies (Wilkes-Barre PA; Manchester UK); Kuehne+Nagel press release (Mantova, September 2024); DHL Supply Chain press release (Extrema Brazil, February 2024); Amazon Buy with Prime / MCF press release (February 20, 2025); GK Software case study and Gold Convrt Award 2024; Interlake Mecalux case study (Wilkes-Barre PA); adidas engineering disclosures (GitHub Copilot; Amazon Bedrock; Amazon SageMaker; AI Archive diffusion model); adidas.com and adidas.co.uk published SLA pages; tech_ops_footprint.md (Step 4 companion output, 2026-04-03).*
