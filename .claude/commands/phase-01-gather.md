# Phase 1: GATHER — Comprehensive Data Collection
This is the ONLY phase that uses web search. Every other phase works exclusively with the files you produce here. If you miss something, no other phase can find it. Be thorough.

Read CLAUDE.md and memory.md first. Apply all quality standards.

## Your Identity
Act as a senior strategy, operations, and AI transformation analyst. Use only public, verifiable sources. Be skeptical of corporate narrative.

## Target Company: $ARGUMENTS

## Step 1: Determine Company Profile
- Is this a US or non-US company?
- What stock exchange? What regulatory body?
- What sector and industry?

## Step 2: Financial Data Collection (minimum 3 years, ideal 5)
Search for and extract ACTUAL NUMBERS from:

FOR US COMPANIES:
- Search: '$ARGUMENTS SEC EDGAR 10-K'
- Search: '$ARGUMENTS SEC EDGAR 10-Q latest'
- Search: '$ARGUMENTS SEC EDGAR DEF 14A proxy'

FOR NON-US COMPANIES:
- Search: '$ARGUMENTS investor relations annual report'
- Search: '$ARGUMENTS annual report [latest year] PDF'
- Search: '$ARGUMENTS quarterly report Q4 [latest year]'
- Search: '$ARGUMENTS corporate governance report'
- Visit the company IR page directly

Extract into a structured table: Revenue, COGS (with logistics/fulfillment components if disclosed), Gross Profit, Gross Margin %, Total Operating Expenses (not just SG&A), SG&A separately, Operating Income, Operating Margin %, EBITDA, Net Income, CapEx, Debt, Working Capital (inventory, receivables, payables).

DATA RECENCY RULE: Always use the MOST RECENT data. FY2025 annual over FY2024. Latest quarterly over annual if more recent. NEVER base analysis solely on data more than 18 months old.

Save as: sources/financial_data.md

## Step 3: Technology and Operations Data
- Search: '$ARGUMENTS' + each: Blue Yonder, Manhattan Associates, SAP TM, SAP EWM, SAP IBP, Oracle TMS, Kinaxis, o9 Solutions, Coupa, project44, FourKites, Transporeon, Descartes, E2open, AutoStore, Ocado
- Search: '$ARGUMENTS' + each: SAP S/4HANA, Oracle Cloud, Salesforce, Workday, ServiceNow
- Search: '$ARGUMENTS' + each: Databricks, Snowflake, AWS SageMaker, Azure ML, Palantir, UiPath, Celonis
- Search: '$ARGUMENTS' + each: Accenture, Deloitte, McKinsey, Capgemini, TCS, Infosys, IBM Consulting
- Search: '$ARGUMENTS delivery time SLA fulfillment speed'
- Search: '$ARGUMENTS distribution center warehouse locations'
- Search: '$ARGUMENTS ship from store microfulfillment dark store'
- Search: '$ARGUMENTS supply chain visibility automation robotics'

Save as: tech_ops_raw.md (tag each finding as CONFIRMED, LIKELY, or UNCONFIRMED)

## Step 4: Peer Data Collection
- Search: 'top publicly listed competitors of $ARGUMENTS'
- For each peer found (target 7-9 peers across Americas, Europe, Asia-Pacific):
  - Search: '[peer name] revenue operating margin gross margin FY2025'
  - Search: '[peer name] FY2024 FY2023 revenue margin'
  - Extract: Revenue (3 years), Gross Margin, Operating Margin, SG&A %, Revenue per Employee, DTC %, E-commerce %

GEOGRAPHIC DIVERSITY RULE: Must include peers from at least 2 of 3 regions (Americas, Europe, Asia-Pacific). Verify with web search that no major public competitor is missing.

Save as: peer_raw_data.md

## Step 5: Current Signals (last 90 days)
- Search: '$ARGUMENTS latest news'
- Search: '$ARGUMENTS leadership changes 2025 2026'
- Search: '$ARGUMENTS hiring AI data engineer supply chain'
- Search: '$ARGUMENTS acquisition partnership announcement'
- Search: '$ARGUMENTS analyst rating upgrade downgrade'
- Search: '$ARGUMENTS tariff trade regulation impact'
- Search: '$ARGUMENTS competitor moves threat'

Save as: current_signals.md

## Step 6: Source Gate Report
Produce source_gate_report.md:
- List every source found with URL and year
- List every source NOT found
- Gate status: PASS (all mandatory met) / PARTIAL (mandatory met, important gaps) / FAIL (mandatory missing)
- If FAIL: stop and tell user what to download manually

Save as: source_gate_report.md and sources/source_index.md
