FIRST: Read memory.md in the project root. This contains accumulated quality standards and learnings from previous executions. Apply all quality standards listed there throughout this step.

# Step 4: Operating Model & Technology Analyst

Read all prior outputs before completing this step.

## Outputs
- `outputs/{company}/tech_ops_footprint.md`
- `outputs/{company}/transformation_capacity.md`

## MANDATORY SECTION — DO NOT SKIP: Delivery Speed and Fulfillment Assessment
You MUST search for and report on ALL of the following. If you cannot find data, write NOT FOUND — discovery question required for each item:
1. Average delivery time from DC to end consumer (days)
2. Published delivery SLAs (standard, express, same-day)
3. Comparison vs Amazon, Zalando, or sector-specific fast-delivery competitors
4. Ship-from-store capabilities: yes/no/unknown with evidence
5. Microfulfillment centers: yes/no/unknown with evidence
6. Dark store operations: yes/no/unknown with evidence
7. Click-and-collect / BOPIS: yes/no/unknown with evidence
8. Number and location of distribution centers
9. Automated DC capabilities (AutoStore, robotics, etc.)
10. Last mile delivery partners and model (own fleet vs 3PL)

This section must produce a BODY READINESS SCORE: can the physical network support the speed that AI-enabled brain improvements would demand? If the body is too slow, flag this as a critical finding — brain-first AI without body modernization will not deliver competitive advantage.

THIS IS NOT OPTIONAL. If this section is missing from the output, the step has FAILED.

## Instructions
CRITICAL: Technology Implementation Discovery
Before completing the technology footprint, run specific web searches to uncover ongoing or recent technology implementations. Search for:

1. Search: [COMPANY] + each of these supply chain systems: Blue Yonder, Manhattan Associates, SAP TM, SAP EWM, SAP IBP, Oracle Transportation Management, Oracle WMS, Kinaxis, o9 Solutions, Coupa, Jaggaer, Ariba, GEP, project44, FourKites, Transporeon, Descartes, E2open, Körber, Honeywell Intelligrated, Locus Robotics, AutoStore, Ocado Solutions
2. Search: [COMPANY] + each of these ERP and enterprise systems: SAP S/4HANA, Oracle Cloud, Microsoft Dynamics, Salesforce, Workday, ServiceNow
3. Search: [COMPANY] + each of these AI and data platforms: Databricks, Snowflake, AWS SageMaker, Azure ML, Google Vertex AI, Palantir, C3.ai, DataRobot, H2O.ai, UiPath, Celonis, Alteryx
4. Search: [COMPANY] + each of these implementation partners: Accenture, Deloitte, McKinsey, BCG, Capgemini, TCS, Infosys, Wipro, IBM Consulting, PwC, EY, KPMG

For each search, look for: press releases, case studies, job postings mentioning specific systems, conference presentations, vendor customer references, and partner announcements.

Save all findings in a dedicated section called Technology Implementation Landscape within tech_ops_footprint.md. For each confirmed or likely implementation, note: system name, vendor, implementation partner if known, scope, timeline if available, and evidence source. Tag each as CONFIRMED, LIKELY, or UNCONFIRMED.

This is essential because knowing what systems are already being implemented changes the entire AI opportunity assessment — you cannot recommend AI in transport planning if the company is already mid-way through a TMS implementation.

1. Analyze the company’s tech stack and operating footprint.
2. Identify core systems, integration maturity, ownership model, and process standardization.
3. Assess transformation constraints: capital, contracts, labor, data maturity, outsourcing.
4. Recommend the sequencing posture: body-first, brain-first, or two-speed.
