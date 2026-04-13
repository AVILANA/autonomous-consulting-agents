# TJX Companies — Routing Decisions
## Phase 5 Job 1: Conditional Routing
## April 2026 | No web search used.

---

## ROUTING ANALYSIS

### CONDITION CHECK: company_snapshot.md

**PRIMARY CONDITION: HIGH GROWTH**

company_snapshot.md flags explicitly: "CONDITION: HIGH GROWTH — weight all subsequent analysis toward scalability, distribution infrastructure, and efficiency bottlenecks at scale."

Supporting evidence:
- Net sales $60.4B (FY2026), +7% year-on-year [FACT]
- Operating margin at record 11.9% (FY2026) [FACT]
- Free cash flow $4.92B (FY2026) [FACT]
- 146 net new stores planned FY2027; long-term target 7,000 stores [FACT]
- CapEx guidance $2.2B–$2.3B for FY2027 — largest in company history [FACT]
- New market entries in FY2027: Spain, Mexico JV expansion, Middle East stake (Brands for Less) [FACT]

**Routing instruction applied:** All 5 provocations must connect to the question "can TJX sustain 11.9%+ operating margins at 7,000 stores, or will infrastructure bottlenecks erode unit economics as volume grows 7% per year?"

**No FINANCIAL DISTRESS flag.** TJX carries $6.2B cash (FY2026), 0.34x debt/equity, and $4.92B FCF (FY2026). Cost-reduction weighting alone is not the pitch. The frame is: efficiency at scale — protecting and extending the margin record as the store network and vendor universe expand.

---

### STANDOUT PEER CHECK: benchmark_table.md

**STANDOUT PEER CONFIRMED: Gap Inc. (+600bp in 2 years)**

Gap Inc. improved operating margin from approximately 1% (FY2022) to approximately 7% (FY2024) — approximately +600 basis points (bp = hundredths of a percentage point) in 2 years. This clears the >5pp in 2 years threshold established in memory.md for STANDOUT PEER routing.

Routing instruction: Gap Inc. must appear as a named evidence reference in at least 2 of the 5 provocations. Specifically: Gap's +600bp improvement demonstrates that operational discipline at a comparable revenue scale can produce margin step-changes within a 24-month window. This is the "it is achievable and fast" argument for TJX's COO.

**Primary operational benchmark: Ross Stores**

Ross Stores operates at 12.2% operating margin (FY2025) on $21.1B revenue — 30bp higher than TJX at 2.9x less revenue and scale. Economics of scale predicts the larger business should have higher margins. TJX does not demonstrate this vs. Ross on a consolidated basis. More directly: Ross generates approximately $240K revenue per employee (FY2025 estimate) vs. TJX's approximately $163K (FY2026 estimate) — a 47% productivity gap on a comparable off-price operating model. Ross is the near-term operational benchmark and must appear in at least 2 provocations.

Note on the previous run's routing: The prior execution of Phase 5 for this company selected Gap as the single standout peer and included store labor scheduling as a supply chain provocation. Labor scheduling is explicitly excluded from the valid supply chain definition (see memory.md section 21B). The prior routing also used International margin gap as a standalone provocation without tracing it to a specific supply chain operational cause. This run corrects both issues.

**Burlington Stores: DC automation benchmark**

Burlington's new highly automated Distribution Center (DC) in Savannah, Georgia is the most specific DC benchmark in the peer set. Burlington CapEx intensity: 8.9% of revenue (FY2025) vs. TJX 2.4% (FY2026 implied) — 3.7x more CapEx per dollar of revenue, explicitly targeting automated DC infrastructure. Burlington is the primary evidence reference for the DC automation provocation.

---

### BODY VS. BRAIN CHECK: body_brain_diagnosis.md

**MASTER DIAGNOSIS: BODY-ADEQUATE, BRAIN-CONSTRAINED — one body upgrade required**

| Stream | Primary Bottleneck | First Action |
|---|---|---|
| DC Operations Intelligence | BOTH — body (automation design in new DCs) AND brain (Warehouse Management System layer) — sequential dependency | Commit to WMS + automation design in NJ, El Paso, Ohio DCs within 12-month window |
| Buyer Intelligence Augmentation | BRAIN only — no body dependency | Start Oracle Enterprise Resource Planning (ERP) data engineering immediately |
| Store Labor + Loss Prevention | BRAIN primarily — activate existing infrastructure (UKG, KODE Labs Energy Management Information System) | UKG AI scheduling extension (upgrade, not new procurement) |

**Body is the primary constraint in 1 area** (DC Operations). The routing threshold for "body is primary constraint in 2+ areas" (which would trigger network optimization as a Phase Two priority) is not fully met.

**However:** The DC body decision has a hard 12-month window. New DCs in New Jersey, El Paso TX, and Ohio are being designed and built during FY2027. Automation designed in at construction = baseline cost. Automation retrofitted after opening = estimated 3–5x cost. This is a one-time, time-sensitive body decision that must be surfaced with explicit urgency. The 12-month window IS the provocation — not the abstract concept of automation.

**Routing instruction applied:** DC automation provocation must be framed as a decision being made right now during construction design, not as a future aspiration. The body network optimization is not flagged as a standalone Phase Two workstream — the DC design commitment is framed as the immediate scoping item within Phase One.

---

### SUPPLY CHAIN MODEL IDENTIFICATION — MANDATORY BEFORE PROVOCATIONS

This section, required by memory.md section 21B, establishes the supply chain lens before any provocation titles are written.

**(1) What makes this company's supply chain unique?**

TJX does not buy predictable, repeating products. It buys excess, cancelled, and overstock inventory from approximately 21,000 vendors across 100+ countries. Every lot is different. No stable SKU (Stock Keeping Unit) catalog. No replenishment cycle. The supply chain is not driven by consumer demand forecasts — it is driven by vendor surplus availability. The entire flow runs: vendor excess inventory → buying decision (accept or pass) → DC receives non-standard lot → allocation to stores → store sells with no ability to reorder. The model rests on the speed and quality of three non-repeatable decisions: which lot to buy, how to allocate it, and how fast the DC can process and dispatch it.

**(2) What is the core operational differentiator?**

The speed and quality of the buying decision. TJX's 1,400 buyers evaluate thousands of deals per year from 21,000 vendors. The difference between accepting a deal at 45% below cost vs. 40% below cost on $41.7B in estimated COGS (FY2026) is approximately $2B in gross margin. Buying quality — markon (markup above cost) achieved plus markdown (further discounting) rate avoided — determines whether gross margin is 31% or 33%. Everything else in the supply chain executes the buying decision: DCs process the deals, allocation distributes them, stores sell the treasure.

**(3) What are the 3 most critical supply chain decisions TJX makes every day?**

1. **Accept/reject/price a vendor deal.** A buyer evaluates a vendor offering branded merchandise at X% below cost. Accept or pass? At what markon? This decision, multiplied across 1,400 buyers and thousands of deals per year, is where gross margin is made or lost.

2. **Which stores receive which portion of which lot.** Oracle Retail Allocation routes each incoming lot to specific stores. Getting this right — right product to stores where it sells fast — directly impacts markdown rate and gross margin. Getting it wrong = either markdown (too much sent to low-demand stores) or lost sales (too little sent to high-demand stores).

3. **How to process incoming lots through DCs efficiently.** 21,000 vendors ship non-standard lots. Each truck arrival requires sorting, tagging, and dispatching to store allocations. DC throughput speed determines how quickly TJX can put product on store shelves and convert it to cash before demand cools.

**(4) What supply chain processes handle the most money?**

- **Buying / vendor negotiation:** ~$41.7B estimated COGS (FY2026). Even 1% improvement in markon across this cost base = ~$417M.
- **DC receiving and processing:** DC labor embedded in COGS. Estimated $1B–$2B in DC labor (INFERENCE — MODERATE — not separately disclosed). Non-standard lot receiving is the most labor-intensive process per unit in TJX's model.
- **Inbound and outbound freight:** Total freight spend (inbound from 100+ source countries + outbound DC to store) estimated $1B–$3B annually (INFERENCE — MODERATE — not separately disclosed). Lower freight costs were explicitly cited as a gross margin driver in FY2024–FY2025 [FACT].

**Mandatory connection check:** Every provocation must connect to items 2, 3, or 4 above.
- P1 (DC automation): connects to Decision 3 + Process 2 (DC processing, labor cost in COGS) ✓
- P2 (Buyer intelligence): connects to Decision 1 + Process 1 (buying determines $41.7B COGS) ✓
- P3 (Freight audit): connects to Process 3 (freight spend is the largest unchecked cost after merchandise) ✓
- P4 (Allocation intelligence): connects to Decision 2 + Process 1 (allocation accuracy determines markdown rate on COGS basis) ✓
- P5 (Synthesis): connects to all ✓

All 5 provocations pass the mandatory connection test. ✓

---

### PROVOCATION ROUTING SUMMARY

| # | Topic | Routing Basis | Key Peers | Core Urgency |
|---|---|---|---|---|
| P1 | DC Automation Design | HIGH GROWTH + one-time body decision window in new DC construction | Burlington (8.9% CapEx intensity) + Ross ($1.1B CapEx, FY2026) | 12-month design window — automation now or 3–5x retrofit cost after opening |
| P2 | Buyer Intelligence | HIGH GROWTH + brain gap during record deal flow + Ross productivity gap | Ross (47% more revenue/person) | Best buying environment in company history; buyer bandwidth is the constraint right now |
| P3 | Freight Audit | HIGH GROWTH + confirmed absence of freight audit + network complexity | Ross (simpler US-only carrier network; structural contrast) + Gap (freight simplification as turnaround driver) | Complex carrier network across 30+ DCs, 21,000 vendors, 9 countries with no confirmed audit system |
| P4 | Allocation Intelligence | HIGH GROWTH + 146 new stores per year with no demand history + markdown risk | Gap (+600bp improvement partly via markdown discipline) + Inditex (8–9x inventory turns vs. TJX 5.6x) | FY2027 new store expansion creates systematic allocation gaps — 146 stores with zero historical data |
| P5 | Synthesis | All of P1–P4 | Ross + Gap | $500M+ opportunity connecting the 4 gaps to the 11.9% → 13%+ operating margin path |

**Lever distribution check (required: 3+ distinct financial AND 3+ distinct operational):**
- Financial levers: COGS Avoidance (P1), Gross Margin Improvement (P2), OPEX Reduction (P3), Working Capital Release (P4), Operating Margin Expansion (P5) = 5 distinct ✓
- Operational levers: Throughput/Process Efficiency (P1), Decision Cycle Compression (P2), Planning Cycle Speed (P3), Production-to-Shelf Velocity (P4), Response Latency (P5) = 5 distinct ✓

**Supply chain coverage check (required: transport/freight, sourcing/procurement, DC operations — all three must be covered):**
- Transport/freight: P3 (freight audit, carrier management) ✓
- Sourcing/procurement: P2 (buying decisions, vendor selection, deal quality) ✓
- DC operations/inventory flow: P1 (DC automation, WMS design) + P4 (DC-to-store allocation) ✓

**Supply chain validity check:** None of the 5 provocations cover store labor scheduling, store layout, marketing, e-commerce UX, HR, or real estate — all excluded per memory.md section 21B. P4 covers DC-to-store allocation (valid), not store-level replenishment planning (excluded). ✓

---

*Source: company_snapshot.md, benchmark_table.md, body_brain_diagnosis.md, value_levers.md, stream_ranking.md, tech_ops_footprint.md, management_roadmap.md (prior phase outputs). No web search used.*
