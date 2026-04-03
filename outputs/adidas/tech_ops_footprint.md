# Adidas AG — Technology & Operating Model Footprint

**Step 4: Operating Model & Technology Analyst | Date: 2026-04-03 (Redone)**

**Company:** adidas AG | XETRA: ADS | ADR: ADDYY
**HQ:** Herzogenaurach, Germany | Founded: 1949
**Employees:** 62,035 (end-2024)
**Revenue FY2025:** €24,811M | **EBIT:** ~€2,059M (8.3% margin) | **Gross Margin:** ~51.0%
**Sources:** adidas Annual Reports 2022–2025; SEC/EDGAR 20-F filings; adidas Investor Day materials; SAP case studies and Innovation Award 2024/2025; EPAM Systems partnership announcement; o9 Solutions case study; project44 press release (Feb 2026); Manhattan Associates case studies; Dematic case study (Manchester); Geek+ press release (Suzhou Sept 2023); Honeywell Intelligrated documentation (Spartanburg); Interlake Mecalux case study (Wilkes-Barre); Kuehne+Nagel press release (Mantova Sept 2024); DHL Supply Chain press release (Extrema Brazil Feb 2024); GK Software case study and Gold Convrt Award 2024; Amazon Buy with Prime / MCF press release (Feb 20, 2025); adidas.com and adidas.co.uk published SLA pages; Deloitte SkillSenseAI case study; ServiceNow Knowledge 2025 (HAM); Infosys managed services documentation; Databricks + MosaicML GenAI review pipeline case study; adidas engineering disclosures (GitHub Copilot; Amazon Bedrock; SageMaker; AI Archive); Databricks Data + AI Summit 2026 session materials.

---

## EXECUTIVE FRAME

adidas is not a manufacturing company. It is a brand and intellectual property business that designs, markets, and distributes sporting goods and lifestyle products through a fully outsourced production model and a mixed owned/partner distribution network. Understanding adidas operationally requires holding three facts simultaneously: (1) the company controls nothing upstream of its 124 manufacturing partners and 283 factories; (2) it controls more of its downstream distribution than it has historically disclosed; and (3) it is mid-way through TRANS4RM, one of the largest SAP S/4HANA retail implementations on earth, which will determine the ceiling for everything else it can build.

**TRANS4RM as defining context.** Every technology and operating model conversation with adidas is, at bottom, a conversation about TRANS4RM. Central Finance went live November 2023. Finance and Purchasing modules are completing through 2024. Supply chain and Sales modules run 2025–2027. The hard SAP legacy R/3 deadline is 2027. Until TRANS4RM completes, adidas operates on a split ERP backbone — some processes on modern S/4HANA, others on legacy R/3 — which limits data integration, real-time visibility, and the AI applications that depend on clean transactional data. [FACT]

**The delivery speed finding.** adidas's owned delivery network is capable but not competitive against pure-play digital peers. US standard delivery is 3–7 days; UK standard is 3–5 working days. Amazon Prime delivers in 1–2 days. Nike's express tier delivers in 2–3 days. The gap is structural: adidas manages 60+ DCs globally with mixed automation maturity, and its last-mile is entirely 3PL. The strategic response — partnering with Amazon Multi-Channel Fulfillment for Buy with Prime in February 2025 — is pragmatic and signals management's posture: outsource the speed problem rather than build owned capability. [FACT + INFERENCE]

**Body vs. Brain framing.** In this analysis, "Body" refers to the physical operating network — warehouses, distribution centers, logistics routes, store infrastructure, and fulfillment mechanics. "Brain" refers to the decision layer — planning systems, data platforms, AI/ML applications, and process intelligence. adidas has invested heavily in the Brain (Databricks Agent Digital Twin in production, GitHub Copilot at 85% engineer adoption, GenAI customer insight pipeline processing 2M+ reviews/year) while the Body remains heterogeneous — world-class in specific DCs (Mantova, Wilkes-Barre, Suzhou) but uneven across its 39+ partner-managed facilities. The Body Readiness Score in Section 6 quantifies this precisely.

---

## SECTION 2: OPERATING MODEL — WHAT ADIDAS ACTUALLY DOES

### 2.1 Business Model Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ADIDAS AG                                    │
│              Brand | Design | IP | Marketing | Distribution         │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
   DESIGN & IP      SUPPLY CHAIN      GO-TO-MARKET
   ─────────────    ────────────      ─────────────
   Herzogenaurach   124 mfg partners  Wholesale (~60%)
   design studios   283 factories     DTC stores (~22%)
   AI Archive       92% Asia sourced  E-commerce (~18%)
   75-yr archive    Vietnam 27%       adiClub loyalty
                    Indonesia 19%     Amazon MCF (US)
                    China 16%
                    100% outsourced
```

[FACT — revenue channel split; FACT — manufacturing model]

### 2.2 Ownership Model — What Adidas Owns vs. Outsources

| Domain | Owned/Controlled | Outsourced/3PL | Notes |
|--------|-----------------|----------------|-------|
| Product design | YES | No | Core competency; AI Archive active |
| Manufacturing | No | YES — 100% | 124 partners, 283 factories |
| DC operations (key sites) | YES — 21 company DCs | PARTIAL — 39+ partner DCs | Mantova (K+N), Brazil (DHL) |
| DC automation | YES at tier-1 sites | Unknown at partner sites | Black box risk |
| Last-mile delivery | No | YES — 100% 3PL | Amazon MCF, K+N, DHL, others |
| Retail stores | YES — 1,933 stores | Franchise model separate | 838 concept + 1,095 factory outlets |
| E-commerce platform | YES | Infosys managed services | Microservices on AWS |
| ERP / data systems | YES (TRANS4RM) | SAP + EPAM + AWS | In rollout |
| HR systems | YES (SuccessFactors) | Deloitte implementation | Live |
| IT managed services | PARTIAL | Infosys | Long-term strategic contract |

[FACT — ownership model per public disclosures and vendor case studies]

### 2.3 Geographic Footprint

| Region | Revenue Contribution | Manufacturing Role | Key DCs |
|--------|---------------------|-------------------|---------|
| Europe | ~38% of revenue [INFERENCE] | None — sourcing only | Mantova (IT), Manchester (UK) |
| North America | ~23% of revenue [INFERENCE] | None | Wilkes-Barre PA, Spartanburg SC |
| Greater China | ~15% of revenue [INFERENCE] | 16% of sourcing | Suzhou DC |
| Asia-Pacific | ~13% of revenue [INFERENCE] | 46% of sourcing (VN+ID) | Various partner DCs |
| Latin America | ~7% of revenue [INFERENCE] | None | Extrema MG + São Paulo (Brazil) |
| EMEA other | ~4% of revenue [INFERENCE] | None | Partner DCs |

Note: Revenue breakdowns are inferred from adidas regional reporting structure; precise splits require 2025 Annual Report. [INFERENCE]

---

## SECTION 3: DELIVERY SPEED & SLA ASSESSMENT (MANDATORY)

This section explicitly addresses all 10 required delivery and fulfillment dimensions. Where information cannot be confirmed from public sources, a specific discovery question is provided.

### Item 1: Average Delivery Time from DC to End Consumer — by Market

| Market | Standard SLA | Express SLA | Same-Day | Source / Confidence |
|--------|-------------|-------------|----------|---------------------|
| US (adidas.com) | 3–7 days (3–5 metro) | Available at checkout; no flat published SLA | Not available via adidas directly | [FACT — adidas.com SLA page] |
| US (Amazon Buy with Prime) | 1–2 days for Prime members; free | Not applicable | Available in select metros via Amazon | [FACT — Amazon MCF press release Feb 20, 2025] |
| US (Wilkes-Barre PA DC capability) | 1-day ground NE; 2-day ground nationwide | Orders packed within 2 hours | Same-day to select NE locations | [FACT — Interlake Mecalux case study] |
| UK (adidas.co.uk) | 3–5 working days; free >£40 or adiClub; £3.99 otherwise | 1–2 days (£5.95; order before 7pm Mon–Sat, 3:30pm Sun) | Not available | [FACT — adidas.co.uk SLA page] |
| EU (via Mantova DC) | 1–3 days achievable (19 countries served) | Not publicly published per-market | Not available | [INFERENCE — Mantova 375K parcels/day capacity and 19-country scope; no published per-market SLA] |
| China | Not publicly published | Not publicly published | Not publicly published | [FACT — absence of public SLA] |
| Brazil | Not publicly published | Not publicly published | LIKELY via DHL same-day | [INFERENCE — DHL Brazil same-day capability] |

**Discovery question (Item 1):** What are the actual DC-to-consumer transit times by market, broken down by channel (DTC direct, wholesale, Amazon MCF)? How does adidas track on-time delivery performance internally, and what is the current NPS impact of delivery speed vs. competitor benchmarks?

### Item 2: Published Delivery SLAs — by Market

| Market | Standard | Express | Same-Day | Notes |
|--------|----------|---------|----------|-------|
| US | 3–7 days; free via adiClub or $5 | Available at checkout; SLA not flat-published | Not offered direct | Buy with Prime provides 1–2 days via Amazon |
| UK | 3–5 working days | 1–2 days at £5.95 | Not available | Next-day available via John Lewis (third-party) |
| EU | Not uniformly published per-market | Not uniformly published | Not available | Mantova serves 19 countries; per-country SLA not disclosed |
| China | Not publicly disclosed | Not publicly disclosed | Not disclosed | — |
| Global | No single global SLA framework published | — | — | [FACT — absence] |

[FACT — US and UK SLAs per published adidas.com and adidas.co.uk terms; all others reflect absence of published data]

**Discovery question (Item 2):** Does adidas maintain an internal SLA framework across all markets, and what percentage of orders meet standard SLA commitments by region? What is the escalation and compensation process when SLAs are breached?

### Item 3: Competitive Delivery Benchmark — Full Table

| Retailer | US Standard | US Express | US Same-Day | UK Standard | EU Standard | Strategic Last-Mile Model |
|----------|-------------|------------|-------------|-------------|-------------|--------------------------|
| **adidas** | 3–7 days | Available; SLA unpublished | Not offered direct | 3–5 working days | Not published per-market | 100% 3PL + Amazon MCF supplement |
| **Nike** | 3–5 days | 2–3 days ($15) | Not broadly offered | 3–5 days | 2–5 days | 3PL; Nike owned DCs |
| **Amazon** | 2 days (Prime) | Next-day (Prime) | Same-day select metros | 1–2 days (Prime) | 2–3 days (Prime) | Owned fulfillment network; owned last-mile |
| **Zalando** | 3–7 days | 1–3 days | 2-hour pilot Paris (2019) | 3–5 days | 1–3 days | Zalando Fulfillment Solutions; owned logistics centers |
| **ASOS** | 3–7 days | 1–3 days | Not offered | 1–3 days | 2–5 days | 3PL; ASOS fulfillment centers |

**Key finding:** adidas US standard (3–7 days) lags Amazon Prime (1–2 days) by 2–5 days and Nike express (2–3 days) by at least 1 day at comparable price points. The Amazon MCF partnership narrows this gap for eligible orders but does not eliminate it for the full catalog. The Wilkes-Barre DC's operational capability (2-hour pack, same-day NE, 2-day nationwide) significantly exceeds the published 3–7 day SLA — suggesting the gap is partly a communications and last-mile activation issue, not purely a logistics capacity issue. [FACT + INFERENCE]

### Item 4: Ship-from-Store Capabilities

**Status: TECHNOLOGY CONFIRMED; OPERATIONAL SCALE UNQUANTIFIED**

The technological foundation for ship-from-store is confirmed and advanced:
- GK Software OmniPOS is live in 1,300+ stores with ship-from-store capability enabled [FACT]
- RFID stock accuracy exceeds 99% across the store estate — the foundational requirement for reliable ship-from-store execution [FACT]
- GK's own documentation (September 2024) explicitly states "unified inventory visibility underpinning services such as click and collect and ship-from-store" [FACT]
- adidas received the Gold Convrt Award 2024 for Customer Experience Initiative, referencing omnichannel fulfillment capabilities [FACT]

What is not confirmed: the percentage of DTC orders fulfilled via ship-from-store, which markets have activated the capability operationally, and whether store operations teams are trained and incentivized for fulfillment volume at scale. [INFERENCE]

**Discovery question (Item 4):** What percentage of DTC orders are currently fulfilled via ship-from-store vs. DC? In which markets is ship-from-store operationally active vs. merely technically enabled? What is the carrier cost and margin per ship-from-store order vs. DC fulfillment, and what is the breakeven order density for ship-from-store routing?

### Item 5: Microfulfillment Centers

**Status: NOT IN USE — No evidence found**

adidas does not operate microfulfillment centers (small, automated fulfillment nodes, typically sub-10,000 sq ft, designed for 1–2 hour urban delivery). No evidence of this model exists in any public source reviewed. [FACT — absence of evidence]

This is consistent with adidas's network strategy of large-format, highly automated regional DCs (Mantova at 130,000 sqm; Wilkes-Barre at 843,000 sq ft). The scale of these capital investments makes a parallel micro-DC network financially unlikely in the near term. [INFERENCE]

**Discovery question (Item 5):** Has adidas evaluated microfulfillment as a complement to its regional DC model for high-density urban markets (New York, London, Shanghai)? If not, is this a deliberate strategic choice or an unexplored option? What is the volume threshold at which microfulfillment would become economically viable in adidas's DTC context?

### Item 6: Dark Store Operations

**Status: NOT IN USE — Deliberate strategic absence**

Dark stores (retail locations converted entirely to fulfillment operations, closed to walk-in customers) are not part of the adidas operating model. [FACT — absence] This is consistent with adidas's DTC brand strategy, which requires physical retail presence for brand experience — the economic justification for 1,933 own stores and €2.8B in IFRS 16 lease liabilities. Converting stores to dark fulfillment nodes would contradict the brand-experience rationale for the store portfolio. [INFERENCE]

No discovery question warranted — this reflects a deliberate strategic choice consistent with the DTC model, unless adidas signals a strategic shift in retail portfolio strategy.

### Item 7: Click-and-Collect / BOPIS (Buy Online, Pick Up In Store)

**Status: CONFIRMED AND OPERATIONAL**

Click-and-collect — also known as BOPIS (Buy Online, Pick Up In Store) — is live across the adidas store estate:
- GK Software OmniPOS enables click-and-collect across 1,300+ stores [FACT]
- UK SLA: 0–5 days; free [FACT]
- US: Available but SLA not uniformly published [FACT]
- RFID >99% accuracy enables reliable order reservation and pickup confirmation [FACT]
- adiClub free shipping incentive drives channel preference toward DTC pickup [FACT]

**Discovery question (Item 7):** What percentage of DTC orders are fulfilled via click-and-collect vs. home delivery, by market? How does BOPIS conversion rate and basket size compare to home delivery orders? Are there markets where BOPIS penetration is meaningfully above the global average, and what drives that outperformance?

### Item 8: Number and Location of Distribution Centers

**Full DC inventory — all confirmed locations:**

| # | Location | Size | Channel | Operator | Status |
|---|----------|------|---------|----------|--------|
| 1 | Wilkes-Barre/Hanover Township, PA (US) | 843,000 sq ft | US DTC e-commerce primary | adidas owned | Operational |
| 2 | Spartanburg, SC (US) | 258-acre campus (two DCs) | US wholesale + retail replenishment | adidas owned | Operational; 300+ hiring 2025 |
| 3 | Mantova/Mantua, Italy (EU) | 130,000 sqm | 19-country Southern/Eastern Europe | Kuehne+Nagel operated | Operational (Sept 2024) |
| 4 | Manchester/Trafford, UK | 350,000 sq ft | UK + Ireland + Benelux | adidas owned | Operational |
| 5 | Suzhou, China | 139,000 sqm | China DTC + wholesale | adidas / Geek+ | Operational (Sept 2023) |
| 6 | Extrema, Minas Gerais, Brazil | ~40,000 sqm | Brazil DTC + wholesale | DHL Supply Chain | Operational (Feb 2024) |
| 7 | São Paulo, Brazil | Not published | Latin America fulfillment | adidas / partner | Operational (legacy) |
| 8–47 | 39+ partner-managed DCs globally | Not disclosed | Various | Various 3PL partners | Operational; automation details unknown [INFERENCE] |

**Total:** 60+ DCs globally; 21 company-owned/operated; 39+ partner-managed [FACT]

### Item 9: Automated DC Capabilities — Specific Technology per Site

| DC | Automation Technology | Automation Tier |
|----|----------------------|----------------|
| Wilkes-Barre PA | Manhattan Associates Active WMS + Labour Management + Slotting Optimisation; Interlake Mecalux racking; 2-hour pack SLA; 200,000 units/day; 71,000+ SKUs | Tier 2 — advanced WMS; physical automation solid but below tier-1 robotics density |
| Spartanburg SC | Honeywell Intelligrated conveyor + sortation system | Tier 2 — conveyor-driven; WMS platform not confirmed |
| Mantova, Italy | 700+ robots; 675 automatic shuttles; 12 miles conveyor; Kuehne+Nagel operated; 375,000 parcels/day standard; 500,000 peak | Tier 1 — world-class; purpose-built for European DTC scale |
| Manchester UK | Dematic ASRS (Automated Storage and Retrieval System) + goods-to-person; Dematic iQ software; Manhattan Associates WMS; 40,000+ split cases/day; 1,500 units/hour peak; £20M investment | Tier 1 — ASRS + goods-to-person is best-practice automation |
| Suzhou China | Geek+ AMR (Autonomous Mobile Robots); 1M+ pieces/day; 10M pieces storage | Tier 1 — AMR-driven at scale |
| Extrema Brazil | Cloud WMS; automatic conveyors; automated sorting; robotics in e-commerce area | Tier 2 — recently opened Feb 2024; robotics scope not fully detailed |
| São Paulo Brazil | 2.1km conveyor network | Tier 2 — conveyor-driven legacy |
| 39+ partner DCs | Unknown — black box | Tier 3 / Unknown — no public data |

[FACT — per vendor case studies and press releases for each named DC]

### Item 10: Last-Mile Delivery Partners and Model

**Own fleet: NONE — 100% 3PL for last-mile** [FACT]

| Partner | Geography | Arrangement | Confirmation Status |
|---------|-----------|-------------|---------------------|
| Amazon Multi-Channel Fulfillment (MCF) | US | Buy with Prime — 1–2 day Prime delivery for eligible orders; free for Prime members | CONFIRMED — launched Feb 20, 2025 |
| Kuehne+Nagel | Europe (Mantova; 19 countries) | DC operator + last-mile coordination | CONFIRMED |
| DHL Supply Chain | Brazil (Extrema DC) | DC operator + last-mile | CONFIRMED |
| UPS / FedEx / USPS | US (general) | Standard parcel delivery from Wilkes-Barre and Spartanburg | LIKELY [INFERENCE — industry standard for US DC operations; specific carrier not confirmed] |
| DPD / national carriers | EU, UK | Standard last-mile | INFERENCE — specific carriers not publicly named |
| Various national carriers | Asia, LatAm | Standard last-mile | INFERENCE — not publicly named |
| Zalando Logistics (France) | France (Paris) | 2-hour pilot (2019); current status post-pilot unclear | CONFIRMED for pilot; ASSUMPTION for current status |

**Discovery question (Item 10):** Who are adidas's primary last-mile carriers by market (UPS, FedEx, DHL Express, DPD, etc.)? What are the contracted rate structures, and how do they compare to Nike's and Zalando's carrier economics? Is there a carrier diversification strategy in place, or is adidas exposed to single-carrier concentration risk in key markets?

---

### DELIVERY SPEED FINDINGS SUMMARY

adidas's physical delivery capability is materially stronger than its published SLAs suggest, but weaker than its digital-first competitors where it matters most for consumer conversion. The Wilkes-Barre PA DC can pack orders within 2 hours and achieve same-day delivery to parts of the US Northeast — yet adidas.com still publishes 3–7 day standard SLAs, which shapes consumer expectation before an order is even placed. The Mantova megasite processes 375,000–500,000 parcels per day and serves 19 European countries, yet per-market SLAs are not publicly published, meaning adidas competes on brand rather than delivery promise in Europe. The Amazon MCF partnership (February 2025) is the most revealing strategic signal: rather than invest in owned last-mile speed, management chose to route eligible DTC orders through Amazon's fulfillment infrastructure, achieving 1–2 day delivery for Prime members without capital commitment — but ceding last-mile data and the post-purchase customer experience for those orders. The net assessment is that adidas's Body is capable in flagship markets and pragmatically outsourced for speed supplementation, but the 39+ partner-managed DCs represent a black box where automation maturity and SLA performance are entirely unknown. The World Cup 2026 (June–July, US host) is the next hard test of this network's event-surge capability, and the adequacy of the Wilkes-Barre + Amazon MCF combination for a concentrated demand spike has not been publicly validated.

---

## SECTION 4: FULFILLMENT MODELS

### 4.1 Fulfillment Architecture

```
ORDER CAPTURE LAYER
──────────────────────────────────────────────────────────────
  adidas.com / app ──┐
  Wholesale portals  ├──► Order Management (SAP S/4HANA — in rollout)
  GK OmniPOS stores  ┘
                         │
                         ▼
FULFILLMENT ROUTING (routing logic: AI-driven; post-TRANS4RM)
──────────────────────────────────────────────────────────────
        ┌──────────┬──────────┬─────────────┬─────────────┐
        │          │          │             │             │
        ▼          ▼          ▼             ▼             ▼
   Ship-from   Click &    Amazon MCF   Ship-from    Wholesale
      DC       Collect    (US only)     Store        DC feed
        │          │          │        (enabled;
        │          │          │         scale TBD)
        ▼          ▼          ▼
DELIVERY LAYER
──────────────────────────────────────────────────────────────
  3PL last-mile (K+N, DHL, Amazon, national carriers)
  Own fleet: NONE
```

### 4.2 Fulfillment Model Assessment Table

| Fulfillment Model | Status | Evidence | Scale | Maturity |
|-------------------|--------|----------|-------|----------|
| Ship-from-DC | CONFIRMED — dominant | All major DCs serve DTC e-commerce | High — primary model | High |
| Click-and-collect (BOPIS) | CONFIRMED | GK OmniPOS 1,300+ stores; UK 0–5 days free | Medium — available globally | High |
| Ship-from-store | CONFIRMED (technology); UNQUANTIFIED (operational scale) | GK OmniPOS + RFID >99%; GK Sept 2024 statement; Gold Convrt Award 2024 | Unknown — not disclosed | Medium |
| Amazon MCF / Buy with Prime | CONFIRMED | Feb 20, 2025 press release; 1–2 day Prime delivery | Medium — US only; eligible orders | Medium (newly launched) |
| Microfulfillment centers | NOT IN USE | No evidence found | Zero | Not applicable |
| Dark stores | NOT IN USE | No evidence found | Zero | Not applicable |
| Zalando express (France) | PILOT ONLY (2019) | Zalando logistics Moissy-Cramayel; 2-hour delivery | Unknown post-pilot | Unknown |
| DHL same-day (Brazil) | INFERENCE | DHL Brazil DC Feb 2024; DHL operates same-day in Brazil | Likely limited | Low |
| Own last-mile fleet | NOT IN USE | Explicit absence | None | Not applicable |

### 4.3 Click & Collect and Ship-from-Store Technology Layer

The technology stack for omnichannel fulfillment is mature and integrated. **GK Software OmniPOS** is live in 1,300+ stores globally, natively supporting ship-from-store, click-and-collect, and RFID-driven inventory management. [FACT] The Gold Convrt Award 2024 for Customer Experience Initiative recognizes adidas's deployment as industry-leading. [FACT]

**RFID at >99% stock accuracy** is the foundational enabler. At this accuracy level, store inventory can be committed to online orders with confidence — a critical requirement for ship-from-store economics. Picking from inaccurate inventory creates cancellations and customer experience failures. adidas has already cleared this threshold at best-in-class levels (industry RFID average where deployed is typically 93–97%). [FACT + INFERENCE]

**The activation gap is not technical — it is operational.** Scaling ship-from-store requires: (a) store operations teams trained and incentivized for fulfillment; (b) carrier integration at the store level; (c) a routing algorithm that optimizes the DC vs. store fulfillment decision per order based on proximity, inventory, and SLA; and (d) management acceptance of the margin impact of higher per-unit fulfillment cost from store vs. DC. None of these are technology problems. [INFERENCE]

### 4.4 Last-Mile Model and Amazon MCF Implications

The Amazon MCF partnership (launched February 20, 2025) is the most strategically consequential fulfillment decision adidas has made in recent years. [INFERENCE]

**What it achieves:** Orders placed on adidas.com and the adidas app by Amazon Prime members can be routed through Amazon's Multi-Channel Fulfillment network, delivering in 1–2 days with free shipping for Prime members. This directly addresses the most visible competitive gap for US consumers — without requiring adidas to build or acquire last-mile infrastructure. [FACT]

**What it costs strategically:** Amazon captures last-mile data and delivery experience ownership for those orders. The consumer's post-purchase experience (tracking, returns, delivery notifications) is mediated by Amazon rather than adidas. The long-term implication for adiClub membership economics and DTC loyalty is material and unquantified. [INFERENCE]

**Management posture signal:** The choice to outsource speed rather than build it is consistent with CFO Harm Ohlmeyer's approach of filtering technology investments through EBIT impact. Building a US owned-last-mile network at scale would cost hundreds of millions and take years; Amazon MCF achieves the speed outcome in months at marginal variable cost. Given the 2028 EBIT target of >10%, this trade-off is coherent. [INFERENCE]

---

## SECTION 5: DISTRIBUTION NETWORK — DETAILED FOOTPRINT

### 5.1 Key Distribution Centers — Full Table

| DC | Operator | Scale | Throughput | Key Technology | Channel Focus | Notes |
|----|----------|-------|-----------|----------------|---------------|-------|
| Wilkes-Barre/Hanover Township PA | adidas owned | 843,000 sq ft | 200,000 units/day; 71,000+ SKUs; 16M case capacity | Manhattan Associates Active WMS + Labour Mgmt + Slotting; Interlake Mecalux racking | US DTC e-commerce primary | Orders packed within 2 hours; same-day select NE; 1-day ground NE; 2-day ground US |
| Spartanburg SC | adidas owned | 258-acre campus; two DCs | Not publicly published | Honeywell Intelligrated conveyor + sortation | US wholesale + retail replenishment | 300+ hiring 2025 |
| Mantova, Italy | Kuehne+Nagel | 130,000 sqm | 375,000 parcels/day standard; 500,000 peak | 700+ robots; 675 automatic shuttles; 12 miles conveyor | 19-country Southern/Eastern Europe | LEED Gold; €350M K+N's single-largest investment; opened Sept 2024 |
| Manchester/Trafford UK | adidas owned | 350,000 sq ft | 40,000+ split cases/day; 1,500 units/hour peak | Dematic ASRS + goods-to-person; Dematic iQ; Manhattan Associates WMS | UK + Ireland + Benelux | £20M automation; opened pre-2024 |
| Suzhou, China | adidas / Geek+ | 139,000 sqm | 1M+ pieces/day; 10M pieces storage | Geek+ AMR (Autonomous Mobile Robots) | China DTC + wholesale | Opened Sept 2023 |
| Extrema, Minas Gerais, Brazil | DHL Supply Chain | ~40,000 sqm | Not publicly published | Cloud WMS; automatic conveyors; automated sorting; robotics (e-commerce area) | Brazil DTC + wholesale | R$70M+ investment; opened Feb 2024 |
| São Paulo, Brazil | adidas / partner | Not published | Not published | 2.1km conveyor network | Latin America fulfillment | Legacy DC |

### 5.2 DC Automation Tier Assessment

**Tier 1 — World-Class Automation (full robotics + ASRS + very high throughput):**
- Mantova, Italy (700+ robots; 675 shuttles; 375K–500K parcels/day)
- Suzhou, China (Geek+ AMR; 1M+ pieces/day)
- Manchester UK (Dematic ASRS + goods-to-person; 1,500 units/hour peak)

**Tier 2 — Advanced Automation (conveyor + WMS + partial robotics or ASRS):**
- Wilkes-Barre PA (Manhattan WMS + Mecalux racking; 200K units/day; 2-hr pack SLA)
- Extrema Brazil (cloud WMS + conveyors + sorting + some robotics)
- São Paulo Brazil (2.1km conveyor — legacy but significant scale)
- Spartanburg SC (Honeywell Intelligrated conveyor/sortation — solid but no confirmed robotics)

**Tier 3 — Standard / Unknown (partner-managed; automation details unavailable):**
- 39+ partner-managed DCs globally [INFERENCE — insufficient public data to assess; treated as Tier 3 or unknown]

### 5.3 The 39 Partner-Managed DC Black Box Risk

adidas operates 60+ DCs globally, of which 21 are company-owned or company-operated and 39+ are managed by third-party logistics partners. [FACT] The automation technology, WMS platforms, SLA performance, and labor practices at these 39+ facilities are not publicly disclosed and could not be confirmed from any source reviewed. [FACT — absence]

This matters for three specific reasons:

1. **Inventory visibility:** If the 39 partner DCs are not integrated into adidas's Manhattan Associates WMS or S/4HANA data backbone, adidas has no real-time inventory visibility across roughly 65% of its physical DC footprint by count. This creates systematic planning blind spots. [INFERENCE]

2. **AI applicability ceiling:** AI demand forecasting (o9, SageMaker) and supply chain visibility (project44) can only optimize what they can see. Opaque partner-DC inventory creates structural limits on how much value AI planning tools can deliver. [INFERENCE]

3. **Customer experience consistency:** If SLA performance at partner DCs is materially worse than at tier-1 facilities, there is a hidden customer satisfaction risk that is not visible in aggregate NPS or delivery metrics reported publicly. [INFERENCE]

**Discovery question:** How many of the 39+ partner-managed DCs are integrated into adidas's WMS and S/4HANA data layer? What is the measured SLA performance gap between company-managed and partner-managed DCs? Is there an integration roadmap for the partner DC network, and if so, what is the timeline?

---

## SECTION 6: BODY READINESS SCORE

### 6.1 Body Readiness Score Matrix

This is the primary deliverable of this step. "Body" = the physical operating network. Score 1–5: 1 = inadequate, 2 = below standard, 3 = functional, 4 = competitive, 5 = best-in-class.

| # | Delivery/Fulfillment Dimension | Weight | Score (1–5) | Key Finding |
|---|-------------------------------|--------|-------------|-------------|
| 1 | Delivery speed — US market | 15% | 3.0 | 3–7 day standard; Amazon MCF provides 1–2 day supplement for eligible orders; DC capability (2-hr pack, same-day NE) exceeds published SLA [FACT] |
| 2 | Delivery speed — UK/EU market | 15% | 3.0 | UK 3–5 days standard (1–2 day express available); EU per-market SLA not published; Mantova capable but promises opaque [FACT + INFERENCE] |
| 3 | DC automation maturity — tier-1 sites | 10% | 4.5 | Mantova, Suzhou, Manchester are world-class; best-in-class robotics, ASRS, and goods-to-person [FACT] |
| 4 | DC automation maturity — network-wide | 10% | 2.5 | 39+ partner DCs unknown; Spartanburg mid-tier; network-wide average significantly below tier-1 [INFERENCE] |
| 5 | Ship-from-store capability | 10% | 3.5 | Technology confirmed (GK OmniPOS + RFID >99%); operational scale not disclosed; capability built but not fully activated [FACT + INFERENCE] |
| 6 | Click-and-collect / BOPIS | 8% | 4.0 | Confirmed and operational globally; GK OmniPOS + RFID; UK 0–5 days free; well-deployed [FACT] |
| 7 | Omnichannel inventory visibility | 10% | 3.0 | RFID >99% in stores; 39+ partner DCs opaque; S/4HANA partially live — full cross-channel visibility post-TRANS4RM 2027 [FACT + INFERENCE] |
| 8 | Last-mile speed and cost competitiveness | 12% | 2.5 | 100% 3PL; no owned fleet; Amazon MCF narrows US gap but only for eligible orders; 3–7 day US standard remains the benchmark SLA consumers see [FACT] |
| 9 | Fulfillment model diversification | 5% | 3.5 | Ship-from-DC dominant; click-and-collect live; Amazon MCF live; ship-from-store technically ready; no dark stores or micro-DC [FACT] |
| 10 | SLA publication and consumer expectation management | 5% | 2.5 | Published SLAs (3–7 US; 3–5 UK) do not reflect DC operational capability; no SLA published for EU or China; expectation gap vs. actual performance [FACT + INFERENCE] |

### 6.2 Composite Body Readiness Score

**Weighted calculation:**

| Dimension | Weight | Score | Weighted Contribution |
|-----------|--------|-------|-----------------------|
| Delivery speed — US | 15% | 3.0 | 0.450 |
| Delivery speed — UK/EU | 15% | 3.0 | 0.450 |
| DC automation (tier-1) | 10% | 4.5 | 0.450 |
| DC automation (network-wide) | 10% | 2.5 | 0.250 |
| Ship-from-store | 10% | 3.5 | 0.350 |
| Click-and-collect / BOPIS | 8% | 4.0 | 0.320 |
| Omnichannel inventory visibility | 10% | 3.0 | 0.300 |
| Last-mile speed / cost | 12% | 2.5 | 0.300 |
| Fulfillment model diversification | 5% | 3.5 | 0.175 |
| SLA publication / expectation management | 5% | 2.5 | 0.125 |
| **TOTAL** | **100%** | — | **3.170** |

---

## COMPOSITE BODY READINESS SCORE: **3.2 / 5.0**

---

### 6.3 What This Score Means

**Paragraph 1 — Lifestyle / Retro Products (Samba, Gazelle):**
A Body Readiness Score of 3.2 is functional but not competitive for lifestyle products where delivery speed has become a hygiene factor rather than a differentiator. The Samba and Gazelle are adidas's current volume engines — high-demand, fashion-sensitive, often purchased on impulse after social media exposure. At 3–7 days US standard, adidas risks losing the impulse purchase window to Amazon (1–2 days) or Nike (2–3 days express). The consumer who encounters a Samba on social media at 10pm and wants it by the weekend will face a structural friction point at adidas.com. The adiClub free shipping incentive partially addresses cost friction, but it does not address speed. Critically, the technical capability to do better already exists — Wilkes-Barre can pack within 2 hours and deliver same-day to the Northeast — but that capability is not translated into consumer-facing SLA promises that would change purchase behavior. The Body readiness gap for lifestyle products is therefore partly an operational credibility issue, not purely a logistics capacity constraint. [INFERENCE]

**Paragraph 2 — Event-Driven / Impulse Demand (World Cup 2026):**
The FIFA World Cup 2026 (US host, June–July 2026) is a hard deadline for North America DTC brand activation. adidas is FIFA's official partner and will carry concentrated licensed merchandise demand for a compressed 6-week window. Event-driven demand has distinct characteristics: unpredictable volume spikes, time-sensitive purchase intent (the tournament bracket creates micro-demand events), and a high gifting proportion where faster delivery is expected. The Body Readiness Score of 3.2 flags meaningful risk for this scenario. The 39+ partner-managed DCs are unknown quantities under surge conditions. The published 3–7 day US SLA will create consumer friction during a moment of peak brand relevance. The Amazon MCF supplement helps but applies only to Prime-eligible SKUs from the adidas catalog. Whether the Wilkes-Barre + Spartanburg network can absorb World Cup surge without SLA degradation has not been publicly validated. An event-specific SLA improvement — even temporary — could represent a significant revenue protection and brand-experience opportunity. [INFERENCE]

**Paragraph 3 — Brain-First Sequencing Implication:**
A Body score of 3.2 does not disqualify adidas from a Brain-first AI investment agenda — it actively supports one. The physical network is functional, not broken. The tier-1 DCs are genuinely world-class. The gaps are not in automation hardware; they are in inventory visibility across the 39+ partner DCs, in SLA communication precision, and in the operational activation of already-built capabilities (ship-from-store at scale, consistent EU SLA publication, routing intelligence). These are Brain problems — data integration, decision logic, planning system completeness — not capital-intensive Body investments requiring new DC construction. This means AI investment in supply chain planning (o9), demand forecasting (SageMaker), real-time transport visibility (project44), and omnichannel inventory routing unlocks already-built physical capability without major new capital expenditure. The strategic implication is direct: Brain investment has high ROI on a 3.2 Body score precisely because it activates latent capability in an already substantial physical network. [INFERENCE]

### 6.4 Critical Finding

**Score 3.2 is BELOW the 3.5 threshold. Assessment: ACCEPTABLE RISK — NOT CRITICAL.**

The score falls short of 3.5 but does not constitute a critical operating risk because:
- Tier-1 DCs (serving the majority of DTC volume in the US, Europe, and China) operate at 4.0–4.5 maturity
- Amazon MCF actively supplements the US speed gap for eligible orders
- TRANS4RM completion (2027) will materially improve omnichannel inventory visibility, directly lifting dimensions 4, 7, and 10
- The Body gaps are addressable through Brain investment rather than new physical capital expenditure

The score would rise to CRITICAL if: (a) Mantova or Wilkes-Barre were below tier-2 automation, (b) RFID accuracy were below 95% (preventing reliable ship-from-store), or (c) no Amazon MCF supplement existed for the US market. None of these conditions apply. [INFERENCE]

### 6.5 Body Readiness vs. Peers

| Retailer | Body Readiness Estimate | Last-Mile Model | DC Automation Level | SLA Transparency |
|----------|------------------------|-----------------|--------------------|--------------------|
| **adidas** | **3.2 / 5** | 100% 3PL + Amazon MCF | Excellent tier-1; opaque partner DC network | Low — published SLAs conservative |
| Nike | ~3.4 / 5 [INFERENCE] | 100% 3PL | Strong owned DC network | Medium |
| Zalando | ~4.0 / 5 [INFERENCE] | Zalando Fulfillment Solutions + 3PL | Strong; purpose-built logistics centers | High — 1–3 day standard published |
| Amazon | 5.0 / 5 [INFERENCE] | Owned fulfillment + owned last-mile | Best-in-class globally | Highest — 2-day Prime guarantee |

[INFERENCE — peer scores are analytical estimates based on public information; not audited]

---

## SECTION 7: TECHNOLOGY STACK — LAYER BY LAYER

### 7.1 ERP — TRANS4RM / SAP S/4HANA

adidas is executing one of the largest S/4HANA retail implementations globally, running on AWS. [FACT] The program, branded TRANS4RM, is the defining technology context for the business through 2027.

**Key facts:**
- 75+ TB transactional data in scope [FACT]
- 9.4 billion financial transactions at initial cutover [FACT]
- 650+ global business processes in scope [FACT]
- Primary SI: EPAM Systems (strategic partner since 2011) [FACT]
- Central Finance go-live: November 2023 [FACT]
- Finance + Purchasing modules: planned completion 2024 [FACT]
- Supply chain + Sales modules: 2025–2027 [FACT]
- Hard SAP legacy R/3 deadline: 2027 [FACT]
- SAP BTP (Business Technology Platform): live — PO amendment automation for 3,000+ factory users; SAP Innovation Award 2024/2025 [FACT]

**Strategic implication:** Until Supply Chain and Sales modules go live (2025–2027), adidas operates on a split backbone. Commercial data (sales, customer) remains partially on legacy R/3, limiting the completeness of any cross-functional AI application requiring integrated financial, commercial, and supply chain data. [INFERENCE]

### 7.2 Supply Chain Planning — o9 Solutions + Amazon SageMaker + project44

Three distinct layers address the supply chain planning stack:

**o9 Solutions:** AI-driven demand prediction, allocation, replenishment, and in-season forecasting; integrated with S/4HANA. [FACT] o9 is the intended planning backbone for the post-TRANS4RM state, replacing fragmented legacy planning tools.

**Amazon SageMaker:** Seasonal demand forecasting using ML models. [FACT] SageMaker likely operates at the SKU/product level, generating statistical forecasts that feed into o9 for allocation and replenishment decisions. [INFERENCE]

**project44:** Real-time transport visibility with AI scenario planning. Adopted February 2026. [FACT] project44 provides shipment-level visibility from factory to DC, addressing the upstream blind spot created when 124 manufacturing partners ship across 92% Asia sourcing lanes.

**Likely additions (not yet confirmed):** SAP IBP (Integrated Business Planning) and SAP TM (Transportation Management) are standard S/4HANA companion modules. Neither has been confirmed as a standalone announcement. [INFERENCE]

### 7.3 WMS — Manhattan Associates + Dematic iQ

**Manhattan Associates Active WMS** is confirmed at multiple sites (Wilkes-Barre PA, Manchester UK). [FACT] Manhattan also provides Labour Management and Slotting Optimisation modules, indicating a mature, multi-module deployment rather than a base installation.

**Dematic iQ** provides automation control software at Manchester UK, integrated with Manhattan Associates WMS. [FACT] Dematic iQ manages the ASRS and goods-to-person automation systems.

**SAP EWM** (Extended Warehouse Management) is a standard S/4HANA companion module and likely runs alongside Manhattan Associates at sites directly integrated with S/4HANA supply chain modules. [INFERENCE — not confirmed as standalone announcement]

**Network gap:** Of the 60+ DCs globally, Manhattan Associates is confirmed at 2 named sites and likely at others. WMS platforms at the 39+ partner-managed DCs are entirely unknown. [FACT — absence]

### 7.4 POS & Retail Operations — GK Software OmniPOS + RFID

**GK Software OmniPOS** is live in 1,300+ stores globally, supporting ship-from-store, click-and-collect, and RFID-integrated inventory management. [FACT] Gold Convrt Award 2024 for Customer Experience Initiative. [FACT]

**RFID:** Stock accuracy exceeds 99% across the store estate. [FACT] Best-in-class by retail industry standards — industry average where RFID is deployed typically runs 93–97%. [INFERENCE — industry benchmark]

### 7.5 Digital Commerce — Microservices Architecture

adidas operates a mature e-commerce platform built on microservices principles:
- 4,000+ pods; 200+ nodes; Docker/Kubernetes orchestration [FACT]
- 80,000+ builds/month — continuous deployment at scale [FACT]
- Akamai CDN and security [FACT]
- E-commerce ~18% of revenue (~€4.5B) [FACT]
- adiClub members convert at 3× web non-member average [FACT]

The 80,000+ monthly build cadence reflects a mature DevOps practice. GitHub Copilot at 85% of ~700 engineers further accelerates this velocity. [FACT + INFERENCE]

### 7.6 HR Systems — SAP SuccessFactors + Deloitte SkillSenseAI

**SAP SuccessFactors:** Live globally for HR. Workday is not in use — SuccessFactors is the confirmed platform. [FACT]

**Deloitte SkillSenseAI:** Integrated with SuccessFactors for job architecture and skill taxonomy. [FACT] This is a meaningful operational signal: adidas is using AI to map its workforce skills at scale — foundational for workforce planning in the context of 500 HQ role eliminations and TRANS4RM-driven process changes. [INFERENCE]

### 7.7 Enterprise Service Management — ServiceNow

ServiceNow has been live since 2015, making adidas an early enterprise adopter. [FACT] Current scope: ASPEN Service Shop (self-service portal for IT, HR, and Finance services) and Hardware Asset Management (HAM), presented at Knowledge 2025. [FACT] Any process automation agenda must work with or justify replacing ServiceNow — its 11-year tenure represents significant switching cost. [INFERENCE]

### 7.8 Procurement — Coupa + SAP Ariba (Likely)

**Coupa:** Confirmed live in Latin America. Global scope unclear. [FACT]

**SAP Ariba within S/4HANA purchasing:** Highly likely as part of the purchasing module rollout (targeted 2024 completion). [INFERENCE]

**SAP BTP PO automation:** Live — PO amendment automation for 3,000+ factory users; SAP Innovation Award 2024/2025. [FACT] This is a concrete, production AI/automation application in procurement already delivering value.

### 7.9 Loyalty Ecosystem — adiClub + Confirmed Apps

**adiClub:** adidas's primary loyalty platform. Members convert at 3× the non-member web average. [FACT] Free shipping for adiClub members (US and UK confirmed). [FACT] adiClub is the primary mechanism for DTC revenue growth, lower customer acquisition cost, and personalization data collection. [INFERENCE]

**Drop app:** Confirmed application for limited-release product drops. [FACT]
**adidas training app:** Confirmed. [FACT]

### 7.10 AI / GenAI Stack

adidas's AI/GenAI stack is more mature than most enterprise retail peers — and significantly more mature than the public brand narrative implies. [INFERENCE]

**Databricks Agent Digital Twin:** A production multi-agent AI governance fleet. Presenting at Databricks Data + AI Summit 2026. [FACT] This signals adidas has moved beyond proof-of-concept GenAI to agentic AI in production, with a governance architecture to manage a fleet of AI agents. This is unusual for a company of this profile.

**GitHub Copilot:** 85% of ~700 engineers use it daily. 20–25% productivity uplift. Expanded from a 500-person pilot. 91% found it useful. [FACT] At this adoption rate, GitHub Copilot functions as infrastructure — not an experiment.

**AI Archive (Generative Design):** A diffusion model trained on 75 years of adidas footwear archive, deployed as a production web application for designers. [FACT] Few brands have this depth of archival training data and have operationalized it as a design tool.

**GenAI Customer Insight Pipeline:** Processes 2M+ product reviews/year using Databricks + MosaicML. Outcomes: 60% latency reduction, 91.67% cost reduction, 98.5% token reduction, 20% productivity improvement. [FACT] These metrics indicate a mature, optimized production pipeline — not a pilot.

**Amazon Bedrock:** Internal GenAI knowledge base + natural language data visualization. [FACT]

**Amazon SageMaker:** Seasonal demand forecasting ML. [FACT]

### 7.11 Data Platform & Cloud Architecture

**Cloud:** AWS is the preferred provider. All SAP S/4HANA workloads, data lake, and ML workloads run on AWS. [FACT]

**Databricks:** GenAI pipelines; Agent Digital Twin governance; Unity Catalog for data governance; multi-agent production fleet. [FACT] Unity Catalog implies a mature data governance posture — cross-cloud, unified access control, lineage tracking.

**Data maturity composite (estimated):** Finance data: 4/5; AI infrastructure: 4.5/5; supply chain and commercial: 3/5; sales data: 2/5 (pending Sales module on S/4HANA). Overall: ~3.5/5. [INFERENCE]

---

## SECTION 8: TECHNOLOGY IMPLEMENTATION LANDSCAPE

### ERP & Business Platform

| System | Vendor | Scope | SI Partner | Timeline | Confidence | Evidence |
|--------|--------|-------|------------|----------|------------|---------|
| SAP S/4HANA (TRANS4RM) | SAP | Global ERP — Finance, Purchasing, Supply Chain, Sales | EPAM Systems | 2023–2027 | CONFIRMED | adidas annual report; SAP case study; EPAM announcement |
| SAP BTP | SAP | PO amendment automation; 3,000+ factory users | Not named | Live | CONFIRMED | SAP Innovation Award 2024/2025 |
| SAP legacy R/3 | SAP | Legacy — being retired | — | Retire by 2027 | CONFIRMED | adidas public roadmap |
| SAP IBP | SAP | Integrated business planning (S/4HANA companion) | Likely EPAM | Likely in scope | LIKELY | Logical S/4HANA companion; no standalone announcement |
| SAP TM | SAP | Transportation management | Likely EPAM | Likely in scope | LIKELY | Standard S/4HANA module |
| SAP EWM | SAP | Extended warehouse management | Likely EPAM | Likely in scope | LIKELY | Standard S/4HANA; Manhattan Associates also live |
| SAP Ariba | SAP | Procurement (within S/4HANA purchasing) | Likely EPAM | Likely 2024 | LIKELY | Purchasing module in scope |

### Supply Chain Planning

| System | Vendor | Scope | SI Partner | Timeline | Confidence | Evidence |
|--------|--------|-------|------------|----------|------------|---------|
| o9 Solutions | o9 | Allocation, replenishment, in-season forecasting, AI demand prediction; S/4HANA integration | Not named | Live | CONFIRMED | o9 Solutions case study |
| Amazon SageMaker | AWS | Seasonal demand forecasting ML | Internal | Live | CONFIRMED | adidas engineering blog |
| project44 | project44 | Real-time transport visibility; AI scenario planning | Not named | Feb 2026 | CONFIRMED | project44 press release Feb 2026 |

### WMS + Logistics

| System | Vendor | Scope | SI Partner | Timeline | Confidence | Evidence |
|--------|--------|-------|------------|----------|------------|---------|
| Manhattan Associates Active WMS | Manhattan Associates | Multi-site WMS — Wilkes-Barre PA, Manchester UK, likely others | Not named | Live | CONFIRMED | Manhattan Associates case studies |
| Manhattan Associates Labour Management | Manhattan Associates | DC workforce management | Not named | Live | CONFIRMED | Case study |
| Manhattan Associates Slotting Optimisation | Manhattan Associates | DC slotting | Not named | Live | CONFIRMED | Case study |
| Dematic iQ | Dematic | Manchester DC automation control (ASRS + goods-to-person) | Not named | Live | CONFIRMED | Dematic case study |
| Geek+ AMR | Geek+ | Suzhou China DC — autonomous mobile robots | Not named | Live (Sept 2023) | CONFIRMED | Geek+ press release |
| Honeywell Intelligrated | Honeywell | Spartanburg SC — conveyor + sortation | Not named | Live | CONFIRMED | Honeywell documentation |
| Interlake Mecalux | Mecalux | Wilkes-Barre PA — racking systems | Not named | Live | CONFIRMED | Mecalux case study |
| Manhattan Associates OMS | Manhattan Associates | Order management (alongside WMS) | Not named | LIKELY | LIKELY | Standard Manhattan suite |

### Procurement

| System | Vendor | Scope | SI Partner | Timeline | Confidence | Evidence |
|--------|--------|-------|------------|----------|------------|---------|
| Coupa | Coupa | Latin America confirmed; global scope unclear | Not named | Live (LatAm) | CONFIRMED (LatAm) | Coupa documentation |
| SAP BTP automation | SAP | PO amendment — 3,000+ factory users | Not named | Live | CONFIRMED | SAP Innovation Award |

### Enterprise Service Management

| System | Vendor | Scope | SI Partner | Timeline | Confidence | Evidence |
|--------|--------|-------|------------|----------|------------|---------|
| ServiceNow | ServiceNow | ITSM; HR services; Finance services; HAM; ASPEN Service Shop | Not named | Live since 2015 | CONFIRMED | ServiceNow Knowledge 2025 |

### POS & Retail

| System | Vendor | Scope | SI Partner | Timeline | Confidence | Evidence |
|--------|--------|-------|------------|----------|------------|---------|
| GK Software OmniPOS | GK Software | 1,300+ stores; ship-from-store; click-and-collect; RFID | Not named | Live | CONFIRMED | GK case study; Gold Convrt Award 2024 |

### HR Systems

| System | Vendor | Scope | SI Partner | Timeline | Confidence | Evidence |
|--------|--------|-------|------------|----------|------------|---------|
| SAP SuccessFactors | SAP | Global HR | Deloitte | Live | CONFIRMED | adidas / Deloitte announcement |
| Deloitte SkillSenseAI | Deloitte | Job architecture; skill taxonomy; integrated with SuccessFactors | Deloitte | Live | CONFIRMED | Deloitte case study |

### Data, AI & Analytics

| System | Vendor | Scope | SI Partner | Timeline | Confidence | Evidence |
|--------|--------|-------|------------|----------|------------|---------|
| Databricks | Databricks | GenAI pipelines; Agent Digital Twin governance; Unity Catalog; multi-agent production fleet | Not named | Live | CONFIRMED | Databricks Summit 2026 session |
| Amazon Bedrock | AWS | Internal GenAI knowledge base; NLP data visualization | Internal | Live | CONFIRMED | adidas engineering disclosure |
| Amazon SageMaker | AWS | ML demand forecasting | Internal | Live | CONFIRMED | adidas engineering disclosure |
| GitHub Copilot | Microsoft / GitHub | AI coding assist; 85% of ~700 engineers; 20–25% productivity uplift | Not named | Live | CONFIRMED | adidas developer disclosure |
| AI Archive (diffusion model) | Internal (adidas) | Design tool; trained on 75-year footwear archive | Internal | Live | CONFIRMED | adidas design team disclosure |
| GenAI review pipeline | Databricks + MosaicML | 2M+ product reviews/year; 91.67% cost reduction; 98.5% token reduction | Internal | Live | CONFIRMED | Databricks case study |

### Implementation Partners

| Partner | Relationship | Scope | Confidence | Evidence |
|---------|-------------|-------|------------|---------|
| EPAM Systems | Primary SI — TRANS4RM | SAP S/4HANA implementation since 2011 | CONFIRMED | EPAM announcement |
| Infosys | IT managed services; e-commerce observability | Long-term strategic; AI observability for e-commerce | CONFIRMED | Infosys case study |
| Deloitte | SuccessFactors + SkillSenseAI | HR systems implementation | CONFIRMED | Deloitte case study |
| Accenture | Data-driven CX engagement | SAP Platinum Partner; CX engagement (published case study) | LIKELY | Published CX case study; former adidas CEO Hainer on Accenture board |
| Kuehne+Nagel | DC operator — Europe | Mantova Italy; K+N's single-largest investment (€350M) | CONFIRMED | K+N press release |
| DHL Supply Chain | DC operator — Brazil | Extrema Brazil | CONFIRMED | DHL press release |
| IBM Consulting | Unknown | Not confirmed | UNCONFIRMED | No evidence found |
| Capgemini | Unknown | Not confirmed | UNCONFIRMED | No evidence found |
| TCS | Unknown | Not confirmed | UNCONFIRMED | No evidence found |

---

## SECTION 9: PROCESS STANDARDIZATION

### 9.1 ERP-Driven Standardization Progress by Domain

| Domain | Standardization Level | ERP Module Status | Key Gaps |
|--------|----------------------|-------------------|----------|
| Finance | HIGH | S/4HANA Central Finance — live Nov 2023 | Minor: local statutory variations |
| Purchasing | MEDIUM-HIGH | S/4HANA Purchasing — targeted 2024 completion | Coupa LatAm vs. SAP global — integration gap |
| Supply chain planning | MEDIUM | o9 live; S/4HANA SC modules 2025–2027 | Integration partial; improving post-TRANS4RM |
| Sales / commercial | LOW-MEDIUM | S/4HANA Sales — 2025–2027 | Legacy R/3 still primary; major AI data gap |
| POS / retail | HIGH | GK OmniPOS 1,300+ stores; RFID | Partner/franchise stores not confirmed |
| E-commerce | HIGH | Unified microservices platform | — |
| WMS | MEDIUM-HIGH | Manhattan Associates multi-site | 39+ partner DCs — unknown WMS landscape |
| HR | MEDIUM | SuccessFactors live globally | SkillSenseAI integration scope |
| ITSM | HIGH | ServiceNow since 2015; 11 years live | — |
| Procurement | MEDIUM | SAP BTP live for PO; Coupa LatAm | Global Coupa vs. SAP Ariba not fully resolved |

### 9.2 Organizational Model — Centralized vs. Decentralized Tension

adidas is executing a deliberate organizational paradox: centralizing data and systems (TRANS4RM creating a single global ERP backbone) while simultaneously decentralizing decision-making authority to regional markets. [FACT + INFERENCE]

**The centralizing forces:** TRANS4RM creates a single source of truth for finance, purchasing, supply chain, and ultimately sales. Databricks Unity Catalog provides centralized data governance. Global WMS standardization on Manhattan Associates. One global e-commerce microservices platform.

**The decentralizing forces:** January 2025 — 500 HQ roles eliminated; CEO Gulden explicitly cited "reduce complexity, decentralize decision-making to local markets." [FACT] March 2026 — platform engineering shifting to domain-team ownership of infrastructure-as-code. [FACT]

**The risk:** Decentralized decision-making on a centralizing data backbone can create conflicting incentives — regional markets optimizing for local P&L metrics while the ERP enforces global process standards. Managing this tension requires strong operating model governance, which is not currently visible as a named program. [INFERENCE]

---

## SECTION 10: INTEGRATION MATURITY ASSESSMENT

| Dimension | Current Maturity (1–5) | Key Gap |
|-----------|----------------------|---------|
| ERP integration — finance + purchasing | 4.0 | S/4HANA live; purchasing near-complete |
| ERP integration — supply chain | 2.5 | SC modules 2025–2027; split backbone |
| ERP integration — sales + commercial | 2.0 | Sales module 2025–2027; legacy R/3 primary |
| WMS integration — named DCs | 3.5 | Manhattan Associates live at key sites |
| WMS integration — partner DCs | 1.5 | 39+ partner DCs — black box |
| Supply chain planning integration (o9 + ERP) | 3.0 | o9 live; ERP integration partial |
| Real-time transport visibility | 3.5 | project44 live Feb 2026; covers main lanes |
| POS + inventory integration | 4.0 | GK OmniPOS + RFID >99% |
| Data governance and lineage | 3.5 | Databricks Unity Catalog live |
| AI/ML integration into operational systems | 3.0 | Strong at specific use cases; not yet cross-functional |
| **Overall integration maturity** | **3.0** | Split ERP backbone is the primary constraint |

**What changes at TRANS4RM completion (2027):** Supply chain and sales integration rise from 2.0–2.5 to 4.0+, pulling the overall integration maturity score to approximately 3.8–4.0. AI applications built and tested in 2025–2026 on available data will be positioned to scale on the complete platform. This is the primary argument for investing in AI Brain capability now rather than waiting for 2027. [INFERENCE]

---

## SECTION 11: KEY TECHNOLOGY PARTNERSHIPS — DEPENDENCY MAP

| Partner | Relationship Type | Strategic Dependency | Switching Cost |
|---------|------------------|---------------------|---------------|
| SAP | ERP backbone (TRANS4RM) | CRITICAL — entire ERP, BTP, SuccessFactors, likely IBP/EWM/TM | Extremely high — 650+ processes; 2011–2027+ commitment |
| EPAM Systems | Primary SI (TRANS4RM) | HIGH — primary implementation knowledge | Very high — 15-year relationship; institutional knowledge risk |
| AWS | Cloud (all SAP + data + ML) | HIGH — preferred cloud; all critical workloads | High — multi-year commitment; SageMaker + Bedrock deeply integrated |
| Databricks | Data platform + GenAI | MEDIUM-HIGH — Agent Digital Twin + Unity Catalog in production | Medium-high — Unity Catalog lineage creates friction |
| Manhattan Associates | WMS (multi-site) | MEDIUM-HIGH — WMS at flagship DCs | High — multi-site; Labour Management + Slotting integrated |
| GK Software | POS (1,300+ stores) | MEDIUM-HIGH — global POS estate | High — 1,300+ store deployment; RFID integration |
| Infosys | IT managed services; e-commerce | MEDIUM — long-term strategic contract | Medium — managed services contracts typically 3–5 year terms |
| o9 Solutions | Supply chain planning | MEDIUM — allocation + replenishment backbone | Medium — S/4HANA data integration creates switching cost |
| Kuehne+Nagel | Mantova DC (€350M investment) | MEDIUM — K+N co-invested; mutual dependency | Medium-high — K+N co-invested; renegotiation complex |
| Amazon MCF | US last-mile speed supplement | LOW-MEDIUM — commercially important; not operationally critical | Low — can exit without infrastructure impact |
| project44 | Transport visibility | LOW-MEDIUM — Feb 2026 adoption; not yet deeply embedded | Low — relatively new; not mission-critical yet |

---

## SECTION 12: DIGITAL CHANNEL PERFORMANCE

| Metric | Current State | Best-in-Class Peer | Gap | Implied Opportunity |
|--------|--------------|-------------------|-----|---------------------|
| E-commerce as % of revenue | ~18% (~€4.5B) [FACT] | ~30–35% (digital-first peers) | ~12–17pp | Each +1pp e-commerce mix ~€250M revenue at current scale [INFERENCE] |
| adiClub conversion vs. non-member | 3× [FACT] | 2–4× industry range | At or near best-in-class | Opportunity: grow member base; deepen personalization |
| US standard delivery speed | 3–7 days [FACT] | 1–2 days (Amazon Prime) | 2–5 days | Conversion uplift from speed improvement is measurable; Amazon MCF is partial fix |
| Digital platform build cadence | 80,000+ builds/month [FACT] | Industry-leading | At best-in-class | GitHub Copilot accelerating further |
| GenAI pipeline efficiency | 91.67% cost reduction; 98.5% token reduction [FACT] | Not publicly benchmarked | Likely best-in-class | Replicable model for other GenAI pipelines |
| AI coding productivity | 20–25% uplift; 85% adoption [FACT] | 15–30% industry range | At or above industry midpoint | Scale to adjacent non-engineering teams |
| DTC mix (stores + e-commerce) | ~40% [FACT] | 40–50% (Nike, On) | 0–10pp | EBIT uplift from DTC mix: higher gross margin vs. wholesale |

---

## SECTION 13: DISCOVERY QUESTIONS — TECHNOLOGY & OPERATING MODEL

**1. Partner-managed DC integration and SLA performance**
How many of the 39+ partner-managed DCs are integrated into adidas's Manhattan Associates WMS and S/4HANA data backbone? What is the measured SLA performance gap between company-managed and partner-managed DCs, and what is the customer satisfaction impact of orders fulfilled from partner facilities? Is there a DC network integration roadmap, and what is the timeline?

**2. Ship-from-store operational activation and economics**
The technology for ship-from-store is confirmed (GK OmniPOS + RFID >99% accuracy). What percentage of DTC orders are currently fulfilled via ship-from-store, and in which markets is the capability operationally active? What is the per-order margin impact of ship-from-store vs. DC fulfillment, and what is the decision framework for when ship-from-store routing is triggered?

**3. World Cup 2026 North America surge planning**
FIFA World Cup 2026 (US host, June–July) will concentrate North America DTC demand in a 6-week window. What is adidas's surge capacity plan for the Wilkes-Barre and Spartanburg DCs? Has the Amazon MCF supplement been stress-tested for World Cup SKU volumes, and are there committed SLA arrangements with Amazon for peak periods?

**4. TRANS4RM commercial data go-live timeline**
The Sales module of S/4HANA goes live 2025–2027. What is the specific go-live date? Until then, what data integration constraints exist for AI applications requiring integrated commercial + financial + supply chain data — such as AI-driven pricing, personalized promotions, and inventory-to-demand matching?

**5. Amazon MCF strategic boundaries and data sharing**
What percentage of adidas.com US orders are currently eligible for MCF routing? What customer and order data does adidas retain vs. share with Amazon for MCF-fulfilled orders? Is there a long-term strategy for this partnership, or is it a transitional measure? How does it interact with adiClub membership economics?

**6. Databricks Agent Digital Twin — scope, authority, and governance**
adidas is presenting a production multi-agent AI governance fleet at Databricks Data + AI Summit 2026. What business processes are governed by this agent fleet? What decision authority do the agents hold (advisory vs. autonomous action)? Who owns the risk governance for agentic AI decisions, and how does this relate to the absence of a CTO/CDO at executive board level?

**7. Process automation landscape — SAP BTP vs. ServiceNow vs. other platforms**
SAP BTP is confirmed for PO automation (3,000+ factory users). ServiceNow is confirmed for ITSM and service delivery. Is there a formal enterprise process automation strategy that defines which use cases go to SAP BTP, which to ServiceNow, and which might use other platforms? Has adidas evaluated process mining tools (e.g., Celonis) for identifying automation opportunities, and what is the current state of process intelligence tooling?

**8. Technology investment governance — who decides and how**
CFO Harm Ohlmeyer owns Technology since August 2024; no CTO or CDO sits at executive board level. Who owns the technology architecture roadmap decisions — platform selection, buy vs. build, AI strategy? How are new technology investments prioritized relative to TRANS4RM commitments and shareholder return obligations (€1B buyback, 40% dividend increase announced March 2026)? What does the approval threshold and business case process look like for a new technology initiative of €20M+ scope?

---

*Sources: adidas Annual Reports 2022–2025; SEC/EDGAR 20-F filings; adidas Investor Day presentations; SAP TRANS4RM case study and SAP Innovation Award 2024/2025 documentation; EPAM Systems partnership announcement; Databricks Data + AI Summit 2026 session materials; o9 Solutions case study; project44 press release (February 2026); Manhattan Associates case studies (Wilkes-Barre PA, Manchester UK); Dematic case study (Manchester UK); Geek+ press release (Suzhou, September 2023); Honeywell Intelligrated documentation (Spartanburg SC); Interlake Mecalux case study (Wilkes-Barre PA); Kuehne+Nagel press release (Mantova, September 2024); DHL Supply Chain press release (Extrema Brazil, February 2024); GK Software case study and Gold Convrt Award 2024; Amazon Buy with Prime / MCF press release (February 20, 2025); adidas.com published SLA pages (US); adidas.co.uk published SLA pages (UK); Deloitte SkillSenseAI case study; ServiceNow Knowledge 2025 presentation (HAM); Infosys managed services documentation; Databricks + MosaicML GenAI review pipeline case study; adidas engineering blog disclosures (GitHub Copilot; Amazon Bedrock; SageMaker; AI Archive diffusion model; microservices platform metrics).*
