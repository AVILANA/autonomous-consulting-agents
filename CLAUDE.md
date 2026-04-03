# Autonomous Consulting Agents

## Project Purpose and Mission
An automated outside-in executive research workflow that, given a company name, produces a full pursuit-ready dossier: financial snapshot, peer benchmarking, AI value mapping, operating model assessment, and a final executive memo with visualizations.

### The Real Mission
We are a consulting firm. We work exclusively with publicly listed companies. Our traditional approach requires workshops and 10-week discovery phases before we can say anything meaningful. This system changes that.

The mission is twofold:
1. **Identify real opportunities before the first meeting.** Using only public information (filings, transcripts, presentations, SEC data), build fact-based hypotheses about where AI, automation, and process reinvention can create value. The output will be top-down and assumption-heavy by nature — but public companies disclose enormous amounts of operational detail because investors demand it. That is our raw material.
2. **Arrive with a strong preliminary picture, not a blank page.** The difference between starting a conversation from zero ("tell us about your business") and arriving with a structured view ("here is what we believe matters, here is where we see gaps, here are the hypotheses we want to validate with you") is the difference between being one more consultant and being a trusted advisor from day one.

The output quality will not replace a proper discovery — but it compresses weeks of early-stage work into hours, and it gives our teams a fact-based foundation to build on. Questions will remain. Assumptions will need validation. But the starting position is radically stronger.

### What "good" looks like
- Every claim is tagged as fact, inference, or assumption
- Every assumption generates a discovery question
- The final memo reads like we already understand the business — not like we Googled it yesterday
- Visuals make the analysis executive-ready and presentation-grade
- The due diligence layer stress-tests our own thesis before we present it

## Architecture Overview

### Design Principle
This project runs entirely through **Claude Code** using custom slash commands.
No separate API keys needed. No Python API wrapper. No extra cost beyond the existing subscription.
Claude Code acts as both the orchestrator and the analyst — it searches the web, reads files, writes outputs, and executes each analytical step.

### How It Works
```
User types: /project:analyze-company Maersk
                    │
                    ▼
      Claude Code reads CLAUDE.md (this file)
      + reads the command instructions
                    │
                    ▼
┌─────────────────────────┐
│  STEP 1: COLLECT SOURCES │  → Searches SEC EDGAR, corporate websites, news
│  /project:step-01        │  → Saves found sources to outputs/{company}/sources/
│                          │  → Produces source_gate_report.md
│                          │  → STOPS if mandatory sources are missing
└──────────┬───────────────┘
           │
           ▼
┌─────────────────────────┐
│  STEP 2: COMPANY         │  → Financial snapshot, management roadmap, sector context
│  RESEARCH ANALYST        │  → Saves: company_snapshot.md, management_roadmap.md,
│  /project:step-02        │          sector_context.md
└──────────┬───────────────┘
           │
           ▼
┌─────────────────────────┐
│  STEP 3: PEER &          │  → Peer set construction + P&L benchmarking
│  BENCHMARK ANALYST       │  → Saves: peer_set.md, benchmark_table.md
│  /project:step-03        │
└──────────┬───────────────┘
           │
           ▼
┌─────────────────────────┐
│  STEP 4: OPERATING       │  → Tech stack, process standardization, ownership model
│  MODEL & TECH ANALYST    │  → Transformation capacity, debt as constraint
│  /project:step-04        │  → Saves: tech_ops_footprint.md, transformation_capacity.md
└──────────┬───────────────┘
           │
           ▼
┌─────────────────────────┐
│  STEP 5: AI VALUE &      │  → 5 value levers, value stream ranking,
│  REINVENTION ANALYST     │     body vs brain diagnosis, moat analysis
│  /project:step-05        │  → Saves: value_levers.md, stream_ranking.md,
│                          │          body_brain_diagnosis.md, moat_analysis.md
└──────────┬───────────────┘
           │
           ▼
┌─────────────────────────┐
│  STEP 6: CURRENT         │  → News, leadership changes, hiring signals,
│  SIGNALS ANALYST         │     partnerships, competitor moves (last 90 days)
│  /project:step-06        │  → Saves: current_signals.md
└──────────┬───────────────┘
           │
           ▼
┌─────────────────────────┐
│  STEP 7: DUE DILIGENCE   │  → Kill my thesis + prioritized discovery questions
│  /project:step-07        │  → Saves: due_diligence.md, discovery_questions.md
└──────────┬───────────────┘
           │
           ▼
┌─────────────────────────┐
│  STEP 8: FINAL MEMO      │  → Executive pursuit memo + visual data for charts
│  + VISUALS               │  → Saves: final_memo.md, visuals_data.md
│  /project:step-08        │
└──────────────────────────┘
```

### Execution Modes
1. **Full run:** User types `/project:analyze-company [COMPANY NAME]` — Claude Code runs all 8 steps sequentially
2. **Step by step:** User types individual step commands (e.g., `/project:step-02 Maersk`) — useful for re-running a specific step or continuing after a pause
3. **Resume after manual upload:** If Step 1 stops (missing sources), user places files in `inputs/{company}/manual/`, then types `/project:step-01 Maersk` again to re-validate

### Source Quality Gate (MANDATORY)
The Source Collector (Step 1) is the foundation of the entire workflow. Before any analytical step runs, Claude Code MUST validate that minimum source requirements are met.

**Mandatory sources (workflow STOPS if not available — minimum 3 years, ideal 5 years):**
| Source Type | Description | Minimum | Ideal |
|-------------|-------------|---------|-------|
| Annual Reports / 10-K | Full annual filings | 3 years | 5 years |
| Quarterly Reports / 10-Q | Quarterly filings | Last 4 quarters | 3 years |
| SEC Filings (20-F for non-US) | Regulatory filings | 3 years | 5 years |
| Proxy Statement (DEF 14A) | Executive compensation, board composition, strategic incentive structures | 1 year (latest) | 3 years |

**Important sources (workflow continues but flags gaps):**
| Source Type | Description | Action if missing |
|-------------|-------------|-------------------|
| Earnings call transcripts | Quarterly investor calls | Flag if only audio available; continue with available text |
| Investor presentations | Quarterly or annual presentations to investors | Flag if missing; continue |
| Investor Day / Capital Markets Day | Deep-dive strategy presentations | Flag if missing; continue |

**Gate behavior:**
- **FAIL:** Any mandatory source missing or below minimum → STOP, tell the user exactly what is missing and where to download it, ask user to place files in `inputs/{company}/manual/`
- **PARTIAL:** All mandatory met but important sources have gaps → WARN user, list gaps, continue automatically
- **PASS:** All sources available → continue automatically

**Why DEF 14A matters:**
The proxy statement reveals what executives are incentivized to achieve (revenue targets, margin goals, ESG metrics, transformation milestones tied to compensation). This tells us what leadership actually cares about vs. what they say publicly.

## Project Structure
```
autonomous-consulting-agents/
├── CLAUDE.md                        # This file — project brain
├── .claude/
│   └── commands/                    # Custom slash commands
│       ├── analyze-company.md       # Master orchestrator: /project:analyze-company
│       ├── step-01-sources.md       # Source collection + quality gate
│       ├── step-02-research.md      # Company research analyst (Prompts 1, 8, 9)
│       ├── step-03-benchmark.md     # Peer & benchmark analyst (Prompts 2, 3)
│       ├── step-04-operating.md     # Operating model & tech analyst (Prompts 11, 12)
│       ├── step-05-ai-value.md      # AI value & reinvention analyst (Prompts 4, 5, 6, 7)
│       ├── step-06-signals.md       # Current signals analyst (Prompt 13)
│       ├── step-07-diligence.md     # Due diligence: kill my thesis (Bonus)
│       └── step-08-memo.md          # Final memo + visuals (Prompt 10)
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
├── inputs/                          # Manual file uploads when source collector can't access
│   └── {company_name}/manual/       # User places downloaded files here
├── outputs/                         # Generated per run
│   └── {company_name}/             # One folder per company
│       ├── sources/                 # Raw source files and links
│       ├── source_gate_report.md
│       ├── company_snapshot.md
│       ├── management_roadmap.md
│       ├── sector_context.md
│       ├── peer_set.md
│       ├── benchmark_table.md
│       ├── tech_ops_footprint.md
│       ├── transformation_capacity.md
│       ├── value_levers.md
│       ├── stream_ranking.md
│       ├── body_brain_diagnosis.md
│       ├── moat_analysis.md
│       ├── current_signals.md
│       ├── due_diligence.md
│       ├── discovery_questions.md
│       ├── final_memo.md
│       └── visuals_data.md
└── venv/                            # Python virtual environment (for future visualization scripts)
```

## Master Prompt (Prompt 0)
This instruction shapes ALL analytical work. Claude Code must follow this persona and these rules in every step:

"Act as a senior strategy, operations, and AI transformation analyst preparing an outside-in executive briefing for a client pursuit. Your job is to identify business facts, operating constraints, peer gaps, and AI value pools that could be influenced through process reinvention, network redesign, automation, ML, generative AI, or agentic AI. Use only public, verifiable sources. Distinguish clearly between facts, inferences, assumptions, and missing information. Be skeptical of corporate narrative and contrast claims with numbers. Output must be concise, structured, comparative, and executive-ready."

## Internal Intelligence Plugin
- Not yet active — will be added as a future step
- When ready: searches configured internal sources (Google Drive, SharePoint, CRM export)
- Interface: input = company_name, output = internal_context.md
- Does not block the core workflow

## Coding Standards
- All analytical outputs in English
- Every claim tagged as [FACT], [INFERENCE], or [ASSUMPTION]
- Every assumption must generate a corresponding discovery question
- Outputs saved as Markdown (.md) for readability and portability
- File names use snake_case
- Each step reads prior outputs from the outputs/{company}/ folder before starting

## Key Design Decisions
1. **Claude Code native execution.** No separate API keys, no Python API wrapper. Claude Code is the engine. Custom slash commands are the interface.
2. **Source quality gate is non-negotiable.** No analytical step runs until mandatory sources (10-K, 10-Q, SEC filings, DEF 14A) are validated. The workflow stops and asks the user for manual uploads if minimum thresholds are not met.
3. **Sequential execution.** Each step runs after the previous one completes. Each step reads all prior artifacts.
4. **All outputs to files.** Every step writes its results to `outputs/{company}/` so nothing is lost if a conversation ends.
5. **Web search enabled.** Claude Code uses web search to find filings, news, corporate information, and current signals.
6. **Hybrid model strategy.** Claude Code uses Opus for deep analytical steps and can use Sonnet for lighter tasks, following the /model command or automatic model selection.
7. **Resumable workflow.** If a step fails or the session ends, the user can re-run any individual step. Each step checks what prior outputs exist and builds on them.