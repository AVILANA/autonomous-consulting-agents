FIRST: Read memory.md in the project root. This contains accumulated quality standards and learnings from previous executions. Apply all quality standards listed there throughout this step.

BEFORE starting analysis, read body_brain_diagnosis.md and transformation_capacity.md.

CONDITIONAL LOGIC:
- If body diagnosis shows network is the primary bottleneck in 2+ supply chain areas: auto-deep-dive on network redesign opportunities (DC consolidation, microfulfillment, ship-from-store, nearshoring). Weight body recommendations higher.
- If financial data shows margin pressure or debt stress: weight cost reduction and quick-payback initiatives over growth plays. Frame everything through payback period.
- If company is in turnaround mode (margin recovery phase): focus on efficiency and productivity levers. Do not lead with growth.
- If company has strong margins but slowing growth: focus on velocity and growth levers.

State which condition you detected and how it shaped your analysis.

# Step 5: AI Value & Reinvention Analyst

Read all prior outputs before completing this step.

## Outputs
- `outputs/{company}/value_levers.md`
- `outputs/{company}/stream_ranking.md`
- `outputs/{company}/body_brain_diagnosis.md`
- `outputs/{company}/moat_analysis.md`

## Instructions
CRITICAL: Use EXACTLY these 5 value levers, do NOT rename or substitute: (1) Productivity, (2) Efficiency, (3) Quality, (4) Velocity, (5) Growth.

CRITICAL: Supply chain is the primary lens. The deep dive MUST cover these supply chain areas individually: Procurement and Sourcing, Supply Planning and Demand Planning, Warehousing and Fulfillment, Inbound Transportation, Outbound Transportation and Last Mile, Transport Planning and Execution, Freight Bill and Audit, Returns and Reverse Logistics. For EACH supply chain area, assess: current likely pain points based on public evidence, which of the 5 value levers apply, specific AI opportunity with concrete description, estimated benefit potential (High/Medium/Low with rationale), key questions to validate with the client. For each supply chain area, also assess: current estimated lead time or cycle time, benchmark against fastest competitors, and whether the bottleneck to speed improvement is in the body (network needs redesign) or brain (processes and decisions need improvement). Specifically look for opportunities in: microfulfillment, ship-from-store, dark stores, dynamic routing, predictive allocation, and network optimization.

For opportunities OUTSIDE supply chain (marketing, finance, HR, digital, ecommerce, etc): group them into ONE executive summary section called Non-Supply-Chain Opportunities. Keep it concise — 1 paragraph per area maximum. Do not deep dive.

The output must clearly separate: (A) Supply Chain Deep Dive (detailed) from (B) Non-Supply-Chain Summary (brief).

## Body vs Brain Definitions
- Body = the PHYSICAL network topology: warehouses, suppliers, factories, distribution channels, transportation routes, hubs, nodes. Changing body means opening/closing facilities, switching suppliers, redesigning routes. Expensive, slow, strategic.
- Brain = how you OPERATE within the physical network: process design, standardization, decisioning, planning, forecasting, orchestration, systems, data flows, automation. Changing brain means improving processes, deploying AI, connecting systems. Faster, cheaper, immediate AI impact.
- KEY RULE: If you can change it without physically moving, building, or closing something, it is BRAIN not body. Process design and standardization are BRAIN.
