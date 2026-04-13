# TJX Companies — Visuals Data
## Phase 6 Output | April 2026
## Structured data for Phase 7 HTML rendering (Plotly + Tailwind)

---

## CHART 1 — SPIDER / RADAR CHART
### Competitive Benchmarking: 8 Peers Across 5 Dimensions (Normalized 0–100)

**Chart type:** Radar / Spider
**Library:** Plotly radar trace (one trace per company)
**Dimensions:** Operating Margin, Revenue Growth, E-commerce Penetration, Gross Margin, Revenue per Employee
**Scale:** 0 = worst in peer set, 100 = best in peer set (linear normalization within each dimension)
**Highlight:** TJX trace in brand teal (#007680); all others in grey (#9CA3AF); hover tooltip shows raw value + score

**Normalization method:**
Each score = (company_value − min_value) / (max_value − min_value) × 100
For Operating Margin: min = 2.5% (JWN est.), max = 19.7% (Inditex)
For Revenue Growth: min = −2.3% (H&M), max = +11.6% (Next)
For E-commerce: min = 0% (Ross/Burlington), max = 50%+ (Next)
For Gross Margin: min = 27.8% (Ross), max = 57.8% (Inditex) — Burlington excluded (accounting non-comparable)
For Revenue/Employee: min = $147K (JWN), max = $240K (Ross)

```json
{
  "chart_type": "radar",
  "title": "Competitive Positioning — 8-Peer Benchmark (Normalized 0–100)",
  "subtitle": "0 = worst in peer set; 100 = best in peer set. Burlington excluded from Gross Margin (accounting difference). E-commerce figures are estimated for TJX.",
  "dimensions": ["Operating Margin", "Revenue Growth (1yr)", "E-commerce %", "Gross Margin", "Revenue / Employee"],
  "companies": [
    {
      "name": "TJX Companies",
      "highlight": true,
      "color": "#007680",
      "scores": [55, 69, 4, 11, 17],
      "raw_values": ["11.9%", "+7.1%", "~2% [EST.]", "31.0%", "$155K"],
      "fiscal_year": "FY2026"
    },
    {
      "name": "Ross Stores",
      "highlight": false,
      "color": "#9CA3AF",
      "scores": [56, 44, 0, 0, 100],
      "raw_values": ["12.2%", "+3.5%", "0%", "27.8%", "~$240K [EST.]"],
      "fiscal_year": "FY2025"
    },
    {
      "name": "Burlington Stores",
      "highlight": false,
      "color": "#9CA3AF",
      "scores": [23, 85, 0, null, 17],
      "raw_values": ["~6.5% [EST.]", "+9.3%", "~0%", "n/a (non-comparable)", "~$163K [EST.]"],
      "fiscal_year": "FY2025"
    },
    {
      "name": "Inditex / Zara",
      "highlight": false,
      "color": "#9CA3AF",
      "scores": [100, 72, 60, 100, 99],
      "raw_values": ["~19.7%", "+7.5% [EST.]", "~30%", "57.8%", "~$239K [EST.]"],
      "fiscal_year": "FY2024"
    },
    {
      "name": "H&M Group",
      "highlight": false,
      "color": "#9CA3AF",
      "scores": [33, 3, 56, 85, 34],
      "raw_values": ["8.1%", "−2.3% [EST.]", "~28%", "53.4%", "~$179K [EST.]"],
      "fiscal_year": "FY2025"
    },
    {
      "name": "Next plc",
      "highlight": false,
      "color": "#9CA3AF",
      "scores": [86, 100, 100, 24, 14],
      "raw_values": ["~17% net [proxy]", "+11.6% [EST.]", "~50%+", "~35% [EST.]", "~$160K [EST.]"],
      "fiscal_year": "FY2025"
    },
    {
      "name": "Gap Inc.",
      "highlight": false,
      "color": "#9CA3AF",
      "scores": [26, 28, 70, 42, 15],
      "raw_values": ["~7.0%", "+1.3%", "~35%", "~40.5%", "~$161K [EST.]"],
      "fiscal_year": "FY2024"
    },
    {
      "name": "Nordstrom (JWN)",
      "highlight": false,
      "color": "#9CA3AF",
      "scores": [0, 5, 40, 24, 0],
      "raw_values": ["~2.5% [EST.]", "~−2.0% [EST.]", "~20% [EST.]", "~35% [EST.]", "~$147K [EST.]"],
      "fiscal_year": "FY2024"
    }
  ],
  "key_insight": "TJX scores well on revenue growth momentum (69/100) but ranks near-bottom on e-commerce penetration (4/100) and labor productivity (17/100) — the two dimensions most directly addressable through operational investment.",
  "annotations": [
    "TJX e-commerce score based on estimated ~2% penetration — company does not disclose.",
    "Burlington gross margin excluded from scoring (non-comparable occupancy cost accounting).",
    "Next plc operating margin score uses net profit margin as proxy."
  ]
}
```

---

## CHART 2 — OPERATING MARGIN COMPARISON (BAR CHART + LINE TRAJECTORY)
### Three-Year Operating Margin Trend: TJX vs. Key Peers

**Chart type:** Grouped bar chart with trend lines overlay
**Library:** Plotly bar + scatter combo
**X-axis:** Year (3 years + most recent)
**Y-axis:** Operating Margin %
**Highlight:** TJX bar in teal; peers in muted colors; "Marmaxx internal" as a dashed line

```json
{
  "chart_type": "grouped_bar_with_trend",
  "title": "Operating Margin — Three-Year Trajectory",
  "subtitle": "TJX consolidated vs. selected peers. Marmaxx segment shown separately as internal benchmark. [EST.] = estimated.",
  "x_axis_label": "Fiscal Year",
  "y_axis_label": "Operating Margin (%)",
  "series": [
    {
      "name": "TJX Companies (consolidated)",
      "color": "#007680",
      "type": "bar",
      "data": [
        {"year": "FY2024", "value": 10.7, "confidence": "FACT"},
        {"year": "FY2025", "value": 11.2, "confidence": "FACT"},
        {"year": "FY2026", "value": 11.9, "confidence": "FACT"}
      ]
    },
    {
      "name": "Marmaxx segment (internal)",
      "color": "#007680",
      "type": "dashed_line",
      "note": "Internal segment benchmark — shows what consolidated TJX can reach",
      "data": [
        {"year": "FY2026", "value": 14.4, "confidence": "FACT"}
      ]
    },
    {
      "name": "TJX International segment (internal)",
      "color": "#EF4444",
      "type": "dashed_line",
      "note": "Drag on consolidated margin — the 710bp gap",
      "data": [
        {"year": "FY2026", "value": 7.3, "confidence": "FACT"}
      ]
    },
    {
      "name": "Ross Stores",
      "color": "#6B7280",
      "type": "bar",
      "data": [
        {"year": "FY2023", "value": 11.3, "confidence": "FACT"},
        {"year": "FY2024", "value": 12.2, "confidence": "FACT"},
        {"year": "FY2025", "value": 12.2, "confidence": "FACT"}
      ]
    },
    {
      "name": "Burlington Stores",
      "color": "#D1D5DB",
      "type": "bar",
      "data": [
        {"year": "FY2023", "value": 5.0, "confidence": "EST."},
        {"year": "FY2024", "value": 6.5, "confidence": "EST."},
        {"year": "FY2025", "value": 6.5, "confidence": "EST."}
      ]
    },
    {
      "name": "Gap Inc.",
      "color": "#9CA3AF",
      "type": "bar",
      "note": "Standout peer — +600bp in 2 years",
      "data": [
        {"year": "FY2022", "value": 1.0, "confidence": "FACT"},
        {"year": "FY2023", "value": 5.0, "confidence": "FACT"},
        {"year": "FY2024", "value": 7.0, "confidence": "FACT"}
      ]
    },
    {
      "name": "Inditex",
      "color": "#4B5563",
      "type": "bar",
      "note": "Structural ceiling benchmark",
      "data": [
        {"year": "FY2022", "value": 17.6, "confidence": "FACT"},
        {"year": "FY2023", "value": 18.8, "confidence": "FACT"},
        {"year": "FY2024", "value": 19.7, "confidence": "FACT"}
      ]
    }
  ],
  "annotations": [
    {
      "x": "FY2026",
      "y": 14.4,
      "text": "Marmaxx: 14.4% — TJX's own internal proof",
      "color": "#007680"
    },
    {
      "x": "FY2026",
      "y": 7.3,
      "text": "International: 7.3% — 710bp gap",
      "color": "#EF4444"
    },
    {
      "x": "FY2024",
      "y": 7.0,
      "text": "Gap Inc. +600bp in 2 years",
      "color": "#9CA3AF"
    }
  ],
  "key_insight": "TJX is expanding consistently (+120bp/year) but Marmaxx alone at 14.4% already shows 13%+ is achievable consolidated — the constraint is International at 7.3%, not US operations."
}
```

---

## CHART 3 — SUPPLY CHAIN OPPORTUNITY HEATMAP
### Five Levers × Eight Supply Chain Areas (Benefit Potential × AI Feasibility Score)

**Chart type:** Heatmap (annotated grid)
**Library:** Plotly heatmap
**Rows:** 8 supply chain areas + 2 non-supply-chain areas
**Columns:** 5 value levers (Productivity, Efficiency, Quality, Velocity, Growth)
**Values:** 0–5 (5 = very high combined benefit potential and AI feasibility; 0 = not applicable)
**Color scale:** 0 = white, 5 = deep teal (#007680)

```json
{
  "chart_type": "heatmap",
  "title": "Supply Chain Opportunity Map — Benefit Potential × Feasibility",
  "subtitle": "Score 1–5: higher = stronger combination of value potential and operational feasibility. Zero = not applicable. Based on Phase 4 value lever analysis.",
  "rows": [
    "Procurement / Sourcing",
    "Supply / Demand Planning",
    "Warehousing / Fulfillment",
    "Inbound Transport",
    "Outbound / Last Mile (DC to Store)",
    "Transport Planning & Execution",
    "Freight Audit",
    "Returns / Reverse Logistics",
    "Store Labor Scheduling",
    "Loss Prevention / Shrink"
  ],
  "columns": ["Productivity", "Efficiency", "Quality", "Velocity", "Growth"],
  "values": [
    [4, 3, 5, 3, 2],
    [2, 3, 5, 4, 1],
    [5, 5, 3, 4, 0],
    [2, 4, 3, 3, 0],
    [2, 4, 3, 4, 0],
    [2, 4, 3, 3, 0],
    [1, 4, 4, 1, 0],
    [1, 2, 2, 1, 0],
    [4, 4, 3, 2, 0],
    [1, 3, 5, 1, 0]
  ],
  "highlighted_cells": [
    {"row": "Warehousing / Fulfillment", "col": "Productivity", "note": "P1 — DC Automation"},
    {"row": "Warehousing / Fulfillment", "col": "Efficiency", "note": "P1 — DC Automation"},
    {"row": "Procurement / Sourcing", "col": "Quality", "note": "P2 — Buyer Intelligence"},
    {"row": "Store Labor Scheduling", "col": "Productivity", "note": "P3 — Labour Scheduling"},
    {"row": "Store Labor Scheduling", "col": "Efficiency", "note": "P3 — Labour Scheduling"}
  ],
  "color_scale": {
    "0": "#FFFFFF",
    "1": "#E0F2F1",
    "2": "#80CBC4",
    "3": "#26A69A",
    "4": "#00897B",
    "5": "#007680"
  },
  "key_insight": "Highest scores: Warehousing/Fulfillment (Productivity=5, Efficiency=5) and Procurement/Quality (5) — these are the three cells that anchor Provocations 1 and 2.",
  "data_confidence": "INFERENCE — MODERATE. Scores derived from Phase 4 value lever analysis using confirmed technology gap data and industry benchmark benefit ranges. Phase One validation required for specific sizing."
}
```

---

## CHART 4 — BODY VS. BRAIN DIVERGING BAR CHART
### Supply Chain Operational Readiness: Physical Network vs. Intelligence Layer

**Chart type:** Diverging horizontal bar chart
**Library:** Plotly bar (horizontal, dual-direction)
**Interpretation:** Body (left / negative) = physical infrastructure readiness (positive = adequate, negative = constraint). Brain (right / positive) = operational intelligence readiness (positive = deployed, negative = absent/gap). Center = neutral reference point.
**Scale:** −5 to +5 (−5 = severe constraint/gap; +5 = fully deployed and optimized)

```json
{
  "chart_type": "diverging_bar",
  "title": "Body vs. Brain — Physical vs. Intelligence Readiness",
  "subtitle": "Left (negative) = physical infrastructure constraint. Right (positive) = intelligence / analytics readiness. Master diagnosis: BODY-ADEQUATE, BRAIN-CONSTRAINED.",
  "x_axis_label": "← Physical Constraint | Intelligence Gap →",
  "rows": [
    {
      "area": "DC Operations",
      "body_score": -2,
      "brain_score": -5,
      "body_label": "Expanding but unautomated. 3 new DCs under construction — design decision pending.",
      "brain_label": "No WMS, no AI task assignment, no throughput analytics. Most significant tech gap.",
      "urgency": "12-MONTH DECISION WINDOW"
    },
    {
      "area": "Buying Intelligence",
      "body_score": 0,
      "brain_score": -4,
      "body_label": "1,400 buyers, global relationships, functioning well — no body constraint.",
      "brain_label": "No deal-scoring model, no AI synthesis on Oracle EBS history. Data exists; intelligence layer absent.",
      "urgency": "START IMMEDIATELY"
    },
    {
      "area": "Allocation / Replenishment",
      "body_score": 0,
      "brain_score": -2,
      "body_label": "Oracle Retail Allocation deployed — partial brain already in place.",
      "brain_label": "Allocation tool in use; AI enhancement for non-SKU patterns not confirmed.",
      "urgency": "PHASE TWO CANDIDATE"
    },
    {
      "area": "Store Labor Scheduling",
      "body_score": 0,
      "brain_score": -3,
      "body_label": "5,214 stores, KODE Labs EMIS deployed — body assets healthy and growing.",
      "brain_label": "UKG deployed for absence only. Demand-based scheduling not confirmed. EMIS not integrated.",
      "urgency": "START IMMEDIATELY"
    },
    {
      "area": "Loss Prevention",
      "body_score": 0,
      "brain_score": -2,
      "body_label": "In-store human coverage across all banners — functioning.",
      "brain_label": "AI loss prevention implied but not confirmed at network scale. FY2024 shrink improvement suggests partial deployment.",
      "urgency": "FORMALIZE NOW"
    },
    {
      "area": "Inbound Transport",
      "body_score": -1,
      "brain_score": -3,
      "body_label": "21,000+ vendors, 100+ countries — complex but functioning.",
      "brain_label": "No confirmed TMS (Transportation Management System). Freight cost embedded in COGS, not visible.",
      "urgency": "PHASE TWO CANDIDATE"
    },
    {
      "area": "International Operations",
      "body_score": -1,
      "brain_score": -4,
      "body_label": "9 countries, multiple DCs — smaller scale than US, less mature.",
      "brain_label": "No confirmed shared buying analytics or DC efficiency standards connecting Marmaxx and TK Maxx.",
      "urgency": "P4 — HIGH VALUE"
    }
  ],
  "legend": {
    "body_color": "#60A5FA",
    "brain_color": "#007680",
    "label_body": "Physical Network (Body)",
    "label_brain": "Intelligence Layer (Brain)"
  },
  "master_diagnosis": "BODY-ADEQUATE, BRAIN-CONSTRAINED — with one body upgrade required in DC design during 12-month window. Everything else is a brain investment that can start immediately on existing infrastructure.",
  "key_insight": "The DC Operations row is the only stream where both body AND brain are in deficit. All other streams are body-healthy but brain-constrained — the investment path is primarily software and analytics, not physical infrastructure."
}
```

---

## CHART 5 — OPPORTUNITY SUMMARY TABLE
### EBIT Bridge: Four Operational Gaps to 13%+ Operating Margin

**Chart type:** Horizontal stacked bar (conservative vs. high range) + summary table
**Library:** Plotly horizontal bar (error bars or range markers for conservative vs. high)

```json
{
  "chart_type": "opportunity_bridge",
  "title": "EBIT Bridge — Four Operational Gaps to 13%+ Operating Margin",
  "subtitle": "All figures INFERENCE — MODERATE. Phase One validation converts directional estimates to confirmed baselines. Conservative = most defensible; High = full potential range.",
  "current_margin": 11.9,
  "target_margin": 13.0,
  "target_label": "13%+ (Marmaxx already at 14.4%)",
  "revenue_base": 60400,
  "revenue_unit": "USD millions",
  "components": [
    {
      "id": "P1",
      "label": "P1 — Distribution Center Operations",
      "mechanism": "15% throughput improvement reducing embedded DC labor in COGS",
      "financial_lever": "COGS Avoidance",
      "operational_lever": "Throughput / Process Efficiency",
      "ebit_conservative_m": 150,
      "ebit_high_m": 300,
      "margin_impact_conservative_bp": 25,
      "margin_impact_high_bp": 50,
      "confidence": "INFERENCE — MODERATE",
      "peer_anchor": "Burlington: 20–30% throughput target; 3.7x CapEx intensity gap",
      "color": "#0D9488"
    },
    {
      "id": "P2",
      "label": "P2 — Buying Decision Quality",
      "mechanism": "25–50bp markon improvement across ~$41.7B annual COGS",
      "financial_lever": "Gross Margin Improvement",
      "operational_lever": "Decision Cycle Compression",
      "ebit_conservative_m": 104,
      "ebit_high_m": 209,
      "margin_impact_conservative_bp": 17,
      "margin_impact_high_bp": 35,
      "confidence": "INFERENCE — MODERATE",
      "peer_anchor": "Ross: $240K revenue/employee vs. TJX $163K — 47% productivity gap",
      "color": "#0891B2"
    },
    {
      "id": "P3",
      "label": "P3 — Store Labor Scheduling",
      "mechanism": "5% scheduling efficiency on estimated $5B–$7B store labor",
      "financial_lever": "OPEX Reduction",
      "operational_lever": "Planning Cycle Speed",
      "ebit_conservative_m": 250,
      "ebit_high_m": 350,
      "margin_impact_conservative_bp": 41,
      "margin_impact_high_bp": 58,
      "confidence": "INFERENCE — MODERATE",
      "peer_anchor": "Gap Inc.: +600bp operating margin improvement in 2 years via store operational discipline",
      "color": "#7C3AED"
    },
    {
      "id": "P4",
      "label": "P4 — International Margin",
      "mechanism": "200–300bp addressable improvement on $8.0B International revenue",
      "financial_lever": "OPEX Reduction + Working Capital Release",
      "operational_lever": "Response Latency",
      "ebit_conservative_m": 160,
      "ebit_high_m": 240,
      "margin_impact_conservative_bp": 26,
      "margin_impact_high_bp": 40,
      "confidence": "INFERENCE — MODERATE (addressable component; full 710bp gap is FACT)",
      "peer_anchor": "Inditex: 19.7% EBIT in same EU markets. Gap Inc.: +600bp in 2 years.",
      "color": "#DC2626"
    }
  ],
  "totals": {
    "ebit_conservative_m": 664,
    "ebit_high_m": 1099,
    "margin_impact_conservative_bp": 110,
    "margin_impact_high_bp": 182,
    "resulting_margin_conservative": 13.0,
    "resulting_margin_high": 13.7,
    "eps_impact_conservative": 0.45,
    "eps_impact_high": 0.50,
    "eps_note": "INFERENCE — MODERATE at TJX effective tax rate and current share count"
  },
  "internal_proof": {
    "label": "Marmaxx segment (internal proof)",
    "margin": 14.4,
    "note": "TJX's own US operations already demonstrate that 13%+ consolidated is achievable — it is not a benchmark comparison, it is an internal gap."
  },
  "key_insight": "The $664M conservative case = +110bp, taking consolidated TJX from 11.9% to ~13.0%. The Marmaxx segment at 14.4% proves the model can get there — the consolidated gap is driven by International and DC unit economics, not by any structural limitation of the off-price model."
}
```

---

## CHART 6 — KPI SCORECARD DATA
### Structured data for client presentation scorecard rendering in Phase 7

```json
{
  "chart_type": "kpi_scorecard",
  "title": "The Scorecard",
  "subtitle": "Key operational KPIs benchmarked against 7 global peers. Public filings only.",
  "peer_set": ["Ross Stores", "Burlington Stores", "Inditex/Zara", "H&M Group", "Next plc", "Gap Inc.", "Nordstrom"],
  "tiers": [
    {
      "tier_id": 1,
      "tier_label": "TIER 1 — OPERATIONS CONTROLS DIRECTLY",
      "kpis": [
        {
          "id": "inventory_rev",
          "name": "Inventory / Revenue",
          "description": "Cash tied up in unsold product relative to annual sales",
          "tjx_value": "12.4%",
          "tjx_year": "FY2025",
          "tjx_confidence": "FACT",
          "peer_median": "12.0%",
          "peer_n": 7,
          "peer_confidence": "EST.",
          "best_in_class_company": "Inditex",
          "best_in_class_value": "~6%",
          "status": "AMBER",
          "provocation_link": null,
          "note": "Lower is better. TJX slightly above peer median — 3% worse than median, within 15% RED threshold."
        },
        {
          "id": "inventory_turns",
          "name": "Inventory Turns",
          "description": "How fast stock converts to sales (COGS ÷ average inventory)",
          "tjx_value": "5.6×",
          "tjx_year": "FY2025",
          "tjx_confidence": "INFERENCE — HIGH",
          "peer_median": "5.5×",
          "peer_n": 7,
          "peer_confidence": "EST.",
          "best_in_class_company": "Inditex",
          "best_in_class_value": "~8–9× [EST.]",
          "status": "GREEN",
          "provocation_link": null,
          "note": "Higher is better. TJX at or above peer median."
        },
        {
          "id": "gross_to_op_spread",
          "name": "Gross-to-Operating Margin Spread",
          "description": "Profit consumed between gross margin and operating income",
          "tjx_value": "19.1pp",
          "tjx_year": "FY2026",
          "tjx_confidence": "FACT",
          "peer_median": "33.0pp",
          "peer_n": 6,
          "peer_confidence": "EST.",
          "best_in_class_company": "Ross Stores",
          "best_in_class_value": "15.6pp",
          "status": "GREEN",
          "provocation_link": null,
          "note": "Lower is better. TJX significantly below (better than) peer median. Note: TJX COGS includes DC/logistics costs that peers include in SG&A — read together with SG&A/Revenue. Burlington excluded (accounting difference)."
        }
      ]
    },
    {
      "tier_id": 2,
      "tier_label": "TIER 2 — OPERATIONS SIGNIFICANTLY INFLUENCES",
      "kpis": [
        {
          "id": "gross_margin",
          "name": "Gross Margin (%)",
          "description": "Revenue retained after cost of purchased goods",
          "tjx_value": "31.0%",
          "tjx_year": "FY2026",
          "tjx_confidence": "FACT",
          "peer_median": "37.8%",
          "peer_n": 6,
          "peer_confidence": "EST.",
          "best_in_class_company": "Inditex",
          "best_in_class_value": "57.8%",
          "status": "AMBER",
          "provocation_link": "P2",
          "note": "Structural model difference: off-price vs. full-price fashion. Within off-price, TJX (31.0%) outperforms Ross (27.8%). P2 addresses the markon improvement opportunity within the off-price model. Burlington excluded."
        },
        {
          "id": "sga_rev",
          "name": "SG&A / Revenue",
          "description": "Overhead and operating cost efficiency",
          "tjx_value": "19.4%",
          "tjx_year": "FY2025",
          "tjx_confidence": "FACT",
          "peer_median": "33.5%",
          "peer_n": 5,
          "peer_confidence": "EST.",
          "best_in_class_company": "Ross Stores",
          "best_in_class_value": "~15.6% [EST.]",
          "status": "GREEN",
          "provocation_link": null,
          "note": "Lower is better. TJX significantly below (better than) peer median. Caution: TJX COGS includes DC and logistics costs that peers include in SG&A — compresses TJX SG&A ratio. Next plc and Burlington excluded."
        },
        {
          "id": "rev_per_employee",
          "name": "Revenue per Employee",
          "description": "Revenue generated per employee — labor productivity signal",
          "tjx_value": "$155K",
          "tjx_year": "FY2025",
          "tjx_confidence": "FACT",
          "peer_median": "$163K",
          "peer_n": 7,
          "peer_confidence": "EST.",
          "best_in_class_company": "Ross Stores",
          "best_in_class_value": "~$240K [EST.]",
          "status": "AMBER",
          "provocation_link": null,
          "note": "Higher is better. TJX 5% below peer median — within 15% RED threshold. TJX vs. best-in-class Ross: 35% gap. Some gap is structural (TJX's higher receiving complexity per store); some addressable through scheduling and DC automation."
        },
        {
          "id": "international_vs_marmaxx",
          "name": "TJX International vs. Marmaxx Operating Margin",
          "description": "Internal gap: Europe/Australia vs. US operations",
          "tjx_value": "7.3% (International)",
          "tjx_year": "FY2026",
          "tjx_confidence": "FACT",
          "peer_median": "14.4% (Marmaxx — internal benchmark)",
          "peer_n": null,
          "peer_confidence": "FACT",
          "best_in_class_company": "Marmaxx (internal)",
          "best_in_class_value": "14.4%",
          "status": "RED",
          "provocation_link": "P4",
          "note": "710bp internal gap confirmed as FACT. At $8.0B International revenue, 200bp addressable improvement = $160M annual operating income. New markets (Spain, Mexico, Middle East) add International revenue at current 7.3% margin before improvements take hold."
        }
      ]
    }
  ],
  "excluded_kpis": [
    {
      "name": "DTC Delivery Speed",
      "reason": "No published SLA for any TJX banner. INFERENCE — MODERATE only.",
      "phase_one_request": "Obtain published or internal delivery SLA for US (tjmaxx.com) and UK/EU (tkmaxx.com) — compare to Amazon Prime (1–2 days US, next-day UK) and Zara (2–3 days US)."
    },
    {
      "name": "Logistics Cost / Revenue",
      "reason": "DC and logistics costs embedded in COGS, not separately disclosed. Confidence below MODERATE for external estimation.",
      "phase_one_request": "DC labor cost + outbound transport cost + inbound freight cost, each as % of COGS or revenue."
    },
    {
      "name": "Sourcing Concentration (top 2 countries)",
      "reason": "Only <10% direct China confirmed (FACT). Total exposure estimate (~40%) is an analyst estimate, not company-confirmed.",
      "phase_one_request": "Direct sourcing breakdown by country of origin, top 5 countries as % of COGS."
    },
    {
      "name": "E-commerce Growth Rate (YoY %)",
      "reason": "'Double-digits annually' confirmed by management — FACT — but no specific percentage for peer comparison.",
      "phase_one_request": "E-commerce revenue by banner (TJX US, TK Maxx UK, TK Maxx EU) and YoY growth rate."
    }
  ]
}
```

---

## CHART 7 — INTERNATIONAL MARGIN DECOMPOSITION (WATERFALL)
### From Marmaxx 14.4% to TJX International 7.3% — What Explains the 710bp Gap

**Chart type:** Waterfall chart (step-down from 14.4% to 7.3%)
**Library:** Plotly waterfall

```json
{
  "chart_type": "waterfall",
  "title": "International Margin Gap Decomposition — 710bp from Marmaxx to TJX International",
  "subtitle": "Structural vs. addressable split is INFERENCE — MODERATE. Phase One will confirm actual cost category breakdown.",
  "start_value": 14.4,
  "start_label": "Marmaxx Operating Margin (FY2026)",
  "end_value": 7.3,
  "end_label": "TJX International Operating Margin (FY2026)",
  "steps": [
    {
      "label": "Structural: Higher EU/AU labor & occupancy costs",
      "value": -3.5,
      "type": "structural",
      "confidence": "INFERENCE — MODERATE",
      "color": "#9CA3AF",
      "note": "Estimated 300–400bp structural cost difference; not addressable through operations. European retail labor regulations, higher occupancy per sq ft in smaller EU markets."
    },
    {
      "label": "Addressable: Buying analytics maturity gap",
      "value": -1.5,
      "type": "addressable",
      "confidence": "INFERENCE — MODERATE",
      "color": "#EF4444",
      "note": "EU buyers lack equivalent sell-through intelligence and deal-scoring support vs. Marmaxx. Estimated 100–200bp."
    },
    {
      "label": "Addressable: DC operations efficiency gap",
      "value": -1.0,
      "type": "addressable",
      "confidence": "INFERENCE — MODERATE",
      "color": "#EF4444",
      "note": "International DCs at lower automation and WMS maturity vs. US. Estimated 50–100bp."
    },
    {
      "label": "Addressable: Allocation accuracy (EU patterns)",
      "value": -0.6,
      "type": "addressable",
      "confidence": "INFERENCE — MODERATE",
      "color": "#F97316",
      "note": "International allocation uses same logic as US without EU-specific demand pattern calibration. Estimated 50bp."
    },
    {
      "label": "Addressable: Multi-country overhead fragmentation",
      "value": -0.5,
      "type": "addressable",
      "confidence": "INFERENCE — MODERATE",
      "color": "#F97316",
      "note": "9 countries with separate operational processes. Standardization opportunity. Estimated 50bp."
    }
  ],
  "summary": {
    "structural_bp": 350,
    "addressable_bp": 310,
    "addressable_value_m_conservative": 160,
    "addressable_value_m_high": 240,
    "addressable_note": "200–300bp addressable at $8.0B International revenue = $160M–$240M annual operating income"
  },
  "peer_reference": "Inditex operates in same EU markets at 19.7% EBIT — structural EU costs alone do not explain TJX International's 7.3% level.",
  "key_insight": "Approximately half the 710bp gap is structural (labor and occupancy costs in EU and Australia); approximately half is operational and addressable through a shared intelligence platform replicating Marmaxx practices in TK Maxx operations."
}
```

---

## DATA QUALITY NOTES FOR PHASE 7

All [EST.] figures are estimated and should display with a footnote or visual indicator in the HTML. All [FACT] figures are confirmed from disclosed public sources and can display without qualification.

Color scheme for Phase 7 HTML:
- TJX brand teal: #007680 (primary)
- RED status: #EF4444
- AMBER status: #F59E0B
- GREEN status: #10B981
- GREY status (Tier 3 commitments): #6B7280
- Light background: #F9FAFB
- Card background: #FFFFFF
- Text primary: #111827
- Text secondary: #6B7280
- Border: #E5E7EB

Typography scale for Phase 7:
- Section heading: text-2xl font-bold
- KPI name: text-sm font-semibold
- KPI value: text-lg font-mono tabular-nums
- Footnote: text-xs text-gray-500

Status display: flat colored text (RED / AMBER / GREEN), not pill badges or rounded badges, per memory.md rule.

---

*Sources: All prior phase outputs. Scores derived from benchmark_table.md (Phase 3), value_levers.md (Phase 4B), body_brain_diagnosis.md (Phase 4B), provocations.md (Phase 5). No web search used in Phase 6.*
