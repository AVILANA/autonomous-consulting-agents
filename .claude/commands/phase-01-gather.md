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

## Step 3: Technology and Operations Data — DEEP DISCOVERY

This step must be EXHAUSTIVE. Missing a confirmed technology implementation leads to provocations that destroy credibility with the client. The TJX case proved that companies often DO NOT publicize their vendor relationships — you must search indirect sources.

### 3A — Direct Vendor Searches (existing, keep these)
Search: '$ARGUMENTS' + each: Blue Yonder, Manhattan Associates, SAP TM, SAP EWM, SAP IBP, Oracle Transportation Management, Oracle WMS, Kinaxis, o9 Solutions, Coupa, Jaggaer, Ariba, GEP, project44, FourKites, Transporeon, Descartes, E2open, Korber, Honeywell Intelligrated, Locus Robotics, AutoStore, Ocado Solutions
Search: '$ARGUMENTS' + each: SAP S/4HANA, Oracle Cloud, Microsoft Dynamics, Salesforce, Workday, ServiceNow, NetSuite
Search: '$ARGUMENTS' + each: Databricks, Snowflake, AWS SageMaker, Azure ML, Palantir, UiPath, Celonis
Search: '$ARGUMENTS' + each: Accenture, Deloitte, McKinsey, Capgemini, TCS, Infosys, IBM Consulting

### 3B — JOB POSTING SEARCHES (NEW — CRITICAL)
Job postings are the single most revealing source of technology implementations. Companies that never issue press releases about vendor selections DO post jobs requiring expertise in those systems.

Search: '$ARGUMENTS jobs transportation management system TMS'
Search: '$ARGUMENTS jobs warehouse management system WMS'
Search: '$ARGUMENTS jobs Blue Yonder OR JDA'
Search: '$ARGUMENTS jobs Manhattan Associates'
Search: '$ARGUMENTS jobs SAP EWM OR SAP TM OR SAP IBP'
Search: '$ARGUMENTS jobs freight payment audit'
Search: '$ARGUMENTS jobs supply chain analyst systems'
Search: '$ARGUMENTS careers logistics technology'
Search: 'site:linkedin.com $ARGUMENTS transportation management'
Search: 'site:linkedin.com $ARGUMENTS freight payment audit'
Search: 'site:linkedin.com $ARGUMENTS supply chain technology'

For each job posting found, extract: system name mentioned, role level (analyst/manager/director), location (HQ vs DC), and whether the posting describes an existing system or a new implementation.

### 3C — VENDOR REFERENCE AND AWARD SEARCHES (NEW)
Search: '$ARGUMENTS' on each vendor's customer page or case study section
Search: '$ARGUMENTS award supply chain logistics'
Search: '$ARGUMENTS SmartWay EPA transportation'
Search: '$ARGUMENTS innovation supply chain partner'
Search: 'site:fourkites.com $ARGUMENTS'
Search: 'site:descartes.com $ARGUMENTS'
Search: 'site:blueyonder.com $ARGUMENTS'
Search: 'site:manh.com $ARGUMENTS' (Manhattan Associates)
Search: 'site:project44.com $ARGUMENTS'

Also search for the company's executives on advisory boards:
Search: '$ARGUMENTS chief logistics officer advisory board'
Search: '$ARGUMENTS VP supply chain advisory board'
Search: '$ARGUMENTS supply chain executive board member'

### 3D — TECHNOLOGY DATABASE SEARCHES (NEW)
Search: 'site:appsruntheworld.com $ARGUMENTS'
Search: '$ARGUMENTS technographics software stack'
Search: '$ARGUMENTS EDI supply chain integration'
Search: '$ARGUMENTS SPS Commerce OR Coupa OR Ariba supplier portal'

### 3E — EXISTING SYSTEM VERIFICATION (NEW — CRITICAL)
Before concluding that a company LACKS a system, verify the absence by searching:
Search: '$ARGUMENTS' + 'TMS' OR 'transportation management'
Search: '$ARGUMENTS' + 'freight audit' OR 'freight payment'
Search: '$ARGUMENTS' + 'WMS' OR 'warehouse management'
Search: '$ARGUMENTS' + 'yard management'
Search: '$ARGUMENTS' + 'labor management system'

RULE: You may ONLY state "no confirmed [system]" if ALL of the following return zero results:
1. Direct vendor search (3A)
2. Job posting search (3B) — no job mentions the system
3. Vendor reference search (3C) — no vendor lists the company
4. Technology database search (3D)
5. General system search (3E)

If ANY of these five search categories returns a result suggesting the system exists, tag it as LIKELY or CONFIRMED and include it in tech_ops_raw.md.

### 3F — DELIVERY SPEED AND FULFILLMENT (keep existing)
Search: '$ARGUMENTS delivery time SLA fulfillment speed'
Search: '$ARGUMENTS distribution center warehouse locations'
Search: '$ARGUMENTS ship from store microfulfillment dark store'
Search: '$ARGUMENTS supply chain visibility automation robotics'

Save everything as: tech_ops_raw.md
Tag each finding as CONFIRMED (multiple independent sources), LIKELY (single credible source like job posting or vendor database), or UNCONFIRMED (indirect evidence only).

LESSON LEARNED (April 2026 — TJX): TJX runs Blue Yonder TMS, Oracle OTM, Manhattan WMS, Voxware voice picking, Descartes logistics, and FourKites visibility — NONE of which appeared in their 10-K, earnings calls, or press releases. All were found through job postings, vendor databases, LinkedIn profiles, and advisory board memberships. If Phase 1 had only searched vendor press releases and SEC filings, it would have missed the entire technology stack. NEVER assume a company lacks a system just because they don't publicize it.

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
