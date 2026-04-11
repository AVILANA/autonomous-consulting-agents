Autonomous Consulting Agents
Project Purpose and Mission
An automated outside-in executive research workflow that, given a company name, produces a full pursuit-ready dossier: financial snapshot, peer benchmarking, AI value mapping, operating model assessment, provocations, and client-ready deliverables with interactive visualizations.
The Real Mission
We are a consulting firm. We work exclusively with publicly listed companies. Our traditional approach requires workshops and 10-week discovery phases before we can say anything meaningful. This system changes that.
The mission is twofold:

Identify real opportunities before the first meeting. Using only public information (filings, transcripts, presentations, SEC data), build fact-based hypotheses about where AI, automation, and process reinvention can create value. The output will be top-down and assumption-heavy by nature — but public companies disclose enormous amounts of operational detail because investors demand it. That is our raw material.
Arrive with a strong preliminary picture, not a blank page. The difference between starting a conversation from zero ("tell us about your business") and arriving with a structured view ("here is what we believe matters, here is where we see gaps, here are the hypotheses we want to validate with you") is the difference between being one more consultant and being a trusted advisor from day one.

The output quality will not replace a proper discovery — but it compresses weeks of early-stage work into hours, and it gives our teams a fact-based foundation to build on. Questions will remain. Assumptions will need validation. But the starting position is radically stronger.
What "good" looks like

Every claim is tagged as fact, inference, or assumption
Every assumption generates a discovery question
The final memo reads like we already understand the business — not like we Googled it yesterday
Visuals make the analysis executive-ready and presentation-grade
The due diligence layer stress-tests our own thesis before we present it
Provocations are quantified, uncomfortable, and backed by peer evidence
The client presentation HTML is a standalone deliverable ready to open in any browser

Architecture Overview
Design Principle
This project runs entirely through Claude Code using custom command files and a PowerShell orchestrator.
No separate API keys needed. No Python API wrapper. No extra cost beyond the existing subscription.
Claude Code acts as both the orchestrator and the analyst — it searches the web, reads files, writes outputs, and executes each analytical phase.
How It Works — 7-Phase Automated Pipeline
User runs: .\run_analysis.ps1 -Company "Adidas"
                    │
                    ▼
      Orchestrator reads CLAUDE.md + memory.md
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│  PHASE 1: GATHER                                    │
│  The ONLY phase that uses web search.               │
│  Collects: financial data, tech/ops data,           │
│  peer data, current signals, source gate report.    │
│  Command: phase-01-gather.md                        │
│  Outputs: sources/financial_data.md,                │
│           sources/source_index.md,                  │
│           source_gate_report.md,                    │
│           tech_ops_raw.md, peer_raw_data.md,        │
│           current_signals.md                        │
│  → STOPS if source gate = FAIL                      │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│  PHASE 2: RESEARCH (no web search)                  │
│  Analyzes collected data into structured outputs.   │
│  Command: phase-02-research.md                      │
│  Outputs: company_snapshot.md,                      │
│           management_roadmap.md,                    │
│           sector_context.md                         │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│  PHASE 3: BENCHMARK (no web search)                 │
│  Peer set construction + P&L benchmarking.          │
│  Command: phase-03-benchmark.md                     │
│  Outputs: peer_set.md, benchmark_table.md           │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│  PHASE 4: DEEP ANALYSIS (no web search)             │
│  Operating model + AI value assessment.             │
│  Runs in two sub-sections: A (ops) then B (value).  │
│  Command: phase-04-deep-analysis.md                 │
│  Outputs: tech_ops_footprint.md,                    │
│           transformation_capacity.md,               │
│           value_levers.md, stream_ranking.md,       │
│           body_brain_diagnosis.md, moat_analysis.md │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│  PHASE 5: CHALLENGE (no web search)                 │
│  Due diligence + provocation generation.            │
│  Runs 4 jobs in order: routing → diligence →        │
│  raw provocations → compliance + self-evaluation.   │
│  Command: phase-05-challenge.md                     │
│  Outputs: routing_decisions.md,                     │
│           due_diligence.md, raw_provocations.md,    │
│           provocations.md,                          │
│           quality_evaluation.md,                    │
│           discovery_questions.md                    │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│  PHASE 6: PRODUCE (no web search)                   │
│  Final deliverables: client document (Track A),     │
│  internal memo (Track B), visual data.              │
│  Command: phase-06-produce.md                       │
│  Outputs: client_document.md,                       │
│           internal_memo.md,                         │
│           visuals_data.md                           │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│  PHASE 7: PRESENT (no web search)                   │
│  Standalone HTML client presentation.               │
│  Tailwind CSS + Plotly CDN. Three tabs:             │
│  Client Presentation, How We Built This,            │
│  Competitive Intelligence.                          │
│  Command: phase-07-client-html.md                   │
│  Outputs: client_presentation.html                  │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│  MEMORY UPDATE                                      │
│  Updates memory.md with execution history and       │
│  company-specific learnings.                        │
│  Command: update-memory.md                          │
└─────────────────────────────────────────────────────┘
Key Architectural Decisions

Phase 1 is the only phase with web search. All other phases work offline from collected data. This makes phases 2-7 faster, more reliable, and deterministic.
Each phase runs in a fresh Claude Code session via claude -p. This avoids context window overflow.
Phases 2-7 explicitly disable web search (--allowedTools "Read,Write,Edit") to prevent hallucinated searches.
Conditional routing in Phase 5 adapts provocation strategy based on company condition (financial distress, high growth, standout peer, body constraint).
Phase 6 produces content, Phase 7 produces presentation. Phase 6 writes the markdown deliverables (client document, internal memo, chart data). Phase 7 takes all of that and renders the polished HTML with interactive charts and professional styling.

Execution Modes

Full automated run: .\run_analysis.ps1 -Company "Adidas" — runs all 7 phases + memory update sequentially. Output: complete dossier with HTML ready to open in browser.
Individual phase: Run any phase command directly in Claude Code or via claude -p for re-runs or iteration.
Resume after manual upload: If Phase 1 stops (source gate FAIL), user places files in inputs/{company}/manual/, then re-runs Phase 1.

Source Quality Gate (MANDATORY)
The Source Collector (Phase 1) is the foundation of the entire workflow. Before any analytical phase runs, Claude Code MUST validate that minimum source requirements are met.
Mandatory sources (workflow STOPS if not available — minimum 3 years, ideal 5 years):
Source TypeDescriptionMinimumIdealAnnual Reports / 10-KFull annual filings3 years5 yearsQuarterly Reports / 10-QQuarterly filingsLast 4 quarters3 yearsSEC Filings (20-F for non-US)Regulatory filings3 years5 yearsProxy Statement (DEF 14A)Executive compensation, board composition, strategic incentive structures1 year (latest)3 years
Important sources (workflow continues but flags gaps):
Source TypeDescriptionAction if missingEarnings call transcriptsQuarterly investor callsFlag; continueInvestor presentationsQuarterly/annual presentationsFlag; continueInvestor Day / Capital Markets DayDeep-dive strategy presentationsFlag; continue
Gate behavior:

FAIL: Any mandatory source missing or below minimum → STOP, tell user what to download, ask user to place files in inputs/{company}/manual/
PARTIAL: All mandatory met but important sources have gaps → WARN user, list gaps, continue automatically
PASS: All sources available → continue automatically

Why DEF 14A matters:
The proxy statement reveals what executives are incentivized to achieve (revenue targets, margin goals, ESG metrics, transformation milestones tied to compensation). This tells us what leadership actually cares about vs. what they say publicly.
Project Structure
autonomous-consulting-agents/
├── CLAUDE.md                        # This file — project brain
├── memory.md                        # Accumulated learnings and quality standards
├── run_analysis.ps1                 # 7-phase automated orchestrator
├── app.py                           # Streamlit dashboard (internal showcase)
├── requirements.txt                 # Python dependencies for Streamlit
├── .claude/
│   └── commands/                    # Phase command files
│       ├── phase-01-gather.md       # Phase 1: Data collection (web search)
│       ├── phase-02-research.md     # Phase 2: Company analysis
│       ├── phase-03-benchmark.md    # Phase 3: Peer benchmarking
│       ├── phase-04-deep-analysis.md # Phase 4: Operating model + AI value
│       ├── phase-05-challenge.md    # Phase 5: Due diligence + provocations
│       ├── phase-06-produce.md      # Phase 6: Markdown deliverables
│       ├── phase-07-client-html.md  # Phase 7: HTML client presentation
│       ├── update-memory.md         # Post-run memory update
│       └── evaluate-step.md         # Quality evaluator
├── prompts/                         # Reference copy of all prompt templates
│   ├── prompt_00_master.md
│   ├── prompt_01_snapshot.md
│   ├── prompt_02_peer_set.md
│   ├── prompt_03_benchmark.md
│   ├── prompt_04_value_levers.md
│   ├── prompt_05_value_streams.md
│   ├── prompt_06_body_brain.md
│   ├── prompt_07_moat.md
│   ├── prompt_08_management.md
│   ├── prompt_09_industry.md
│   ├── prompt_10_memo.md
│   ├── prompt_11_tech_ops.md
│   ├── prompt_12_transformation.md
│   ├── prompt_13_current_signals.md
│   └── prompt_bonus_kill_thesis.md
├── inputs/                          # Manual file uploads
│   └── {company_name}/manual/       # User places downloaded files here
├── outputs/                         # Generated per run
│   └── {company_name}/             # One folder per company
│       ├── sources/                 # Source files and index
│       │   ├── source_index.md
│       │   └── financial_data.md
│       ├── source_gate_report.md    # Phase 1 gate result
│       ├── tech_ops_raw.md          # Phase 1 technology findings
│       ├── peer_raw_data.md         # Phase 1 peer data
│       ├── current_signals.md       # Phase 1 signals
│       ├── company_snapshot.md      # Phase 2
│       ├── management_roadmap.md    # Phase 2
│       ├── sector_context.md        # Phase 2
│       ├── peer_set.md              # Phase 3
│       ├── benchmark_table.md       # Phase 3
│       ├── tech_ops_footprint.md    # Phase 4A
│       ├── transformation_capacity.md # Phase 4A
│       ├── value_levers.md          # Phase 4B
│       ├── stream_ranking.md        # Phase 4B
│       ├── body_brain_diagnosis.md  # Phase 4B
│       ├── moat_analysis.md         # Phase 4B
│       ├── routing_decisions.md     # Phase 5 Job 1
│       ├── due_diligence.md         # Phase 5 Job 2
│       ├── raw_provocations.md      # Phase 5 Job 3A
│       ├── provocations.md          # Phase 5 Job 3B
│       ├── quality_evaluation.md    # Phase 5 Job 4
│       ├── discovery_questions.md   # Phase 5 Job 4
│       ├── client_document.md       # Phase 6 Track A
│       ├── internal_memo.md         # Phase 6 Track B
│       ├── visuals_data.md          # Phase 6 chart data
│       └── client_presentation.html # Phase 7 HTML deliverable
└── venv/                            # Python virtual environment
Master Prompt (Prompt 0)
This instruction shapes ALL analytical work. Claude Code must follow this persona and these rules in every phase:
"Act as a senior strategy, operations, and AI transformation analyst preparing an outside-in executive briefing for a client pursuit. Your job is to identify business facts, operating constraints, peer gaps, and AI value pools that could be influenced through process reinvention, network redesign, automation, ML, generative AI, or agentic AI. Use only public, verifiable sources. Distinguish clearly between facts, inferences, assumptions, and missing information. Be skeptical of corporate narrative and contrast claims with numbers. Output must be concise, structured, comparative, and executive-ready."
Coding Standards

All analytical outputs in English
Every claim tagged as [FACT], [INFERENCE], or [ASSUMPTION]
Every assumption must generate a corresponding discovery question
Outputs saved as Markdown (.md) except client_presentation.html
File names use snake_case
Each phase reads prior outputs from the outputs/{company}/ folder before starting
Simple language: explain every acronym the first time, no jargon without explanation
Provocations use conditional language for non-FACT claims (may, could, if so)

Key Design Decisions

7-phase pipeline with single web search phase. Phase 1 collects all data upfront. Phases 2-7 work offline — faster, more reliable, deterministic.
Claude Code native execution. No separate API keys, no Python API wrapper. Claude Code is the engine. PowerShell orchestrator calls claude -p for each phase in a fresh session.
Source quality gate is non-negotiable. No analytical phase runs until mandatory sources are validated. The workflow stops and asks the user for manual uploads if minimum thresholds are not met.
Conditional routing. Phase 5 adapts provocation strategy based on company financial condition, standout peers, and body-vs-brain diagnosis.
Dual-track output. Phase 6 produces both a client-facing document (Track A — no AI/agent language) and an internal memo (Track B — full analysis with agent architecture).
Content then presentation. Phase 6 produces markdown content. Phase 7 renders it into polished interactive HTML with Tailwind and Plotly. Separating these ensures the content is right before styling it.
Memory system. memory.md accumulates quality standards and learnings across executions. Every phase reads it first.
All outputs to files. Every phase writes results to outputs/{company}/ so nothing is lost if a session ends.
Resumable workflow. Any individual phase can be re-run. Each phase checks what prior outputs exist and builds on them.

Internal Intelligence Plugin

Not yet active — will be added as a future phase
When ready: searches configured internal sources (Google Drive, SharePoint, CRM export)
Interface: input = company_name, output = internal_context.md
Does not block the core workflow