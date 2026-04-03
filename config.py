"""
Autonomous Consulting Agents — Configuration
Central configuration for all modules, paths, and API settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================
# PATHS
# ============================================================
# Project root = the folder where this config.py lives
PROJECT_ROOT = Path(__file__).parent

# Where prompts templates are stored
PROMPTS_DIR = PROJECT_ROOT / "prompts"

# Where outputs are saved (one subfolder per run)
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

# Where the user can place manually downloaded files
INPUTS_DIR = PROJECT_ROOT / "inputs"

# ============================================================
# API CONFIGURATION
# ============================================================
# Anthropic API key — loaded from .env file, never hardcoded
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Models — use Opus for deep analysis, Sonnet for mechanical tasks
MODEL_HEAVY = "claude-opus-4-6"       # Benchmarking, moat, strategy, kill thesis, memo
MODEL_LIGHT = "claude-sonnet-4-6"     # Source collection, data extraction, formatting

# Which modules use which model
MODEL_ASSIGNMENT = {
    "source_collector":  "light",   # Fetching and organizing — Sonnet is enough
    "company_research":  "heavy",   # Deep financial and strategic analysis
    "peer_benchmark":    "heavy",   # Comparative reasoning across companies
    "operating_model":   "heavy",   # Technology and transformation assessment
    "ai_value":          "heavy",   # Value lever mapping — needs strong reasoning
    "current_signals":   "light",   # News search and synthesis
    "red_team":          "heavy",   # Kill my thesis — needs the best reasoning
    "memo_composer":     "heavy",   # Final executive output — quality matters most
}

# Max tokens for API responses (higher = longer, more detailed answers)
MAX_TOKENS = 8000

# ============================================================
# SOURCE COLLECTOR SETTINGS
# ============================================================
# Minimum years of mandatory filings required to proceed
MIN_YEARS_MANDATORY = 3

# Ideal years of filings to collect
IDEAL_YEARS = 5

# SEC EDGAR base URL
SEC_EDGAR_BASE = "https://efts.sec.gov/LATEST"

# User agent for SEC EDGAR (required by SEC — use your real email)
SEC_USER_AGENT = "AutonomousConsultingAgents research@example.com"

# ============================================================
# SOURCE QUALITY GATE
# ============================================================
# Mandatory sources — workflow STOPS if these are not met
MANDATORY_SOURCES = {
    "annual_reports_10k": {"min_years": 3, "ideal_years": 5},
    "quarterly_reports_10q": {"min_quarters": 4, "ideal_quarters": 12},
    "sec_filings": {"min_years": 3, "ideal_years": 5},
    "proxy_def14a": {"min_years": 1, "ideal_years": 3},
}

# Important sources — workflow continues but flags gaps
IMPORTANT_SOURCES = [
    "earnings_transcripts",
    "investor_presentations",
    "investor_day",
]

# ============================================================
# INTERNAL INTELLIGENCE PLUGIN
# ============================================================
# Set to True when internal data sources are configured
INTERNAL_INTEL_ENABLED = False

# ============================================================
# WORKFLOW SETTINGS
# ============================================================
# Master prompt (Prompt 0) — prepended to every API call
MASTER_PROMPT = (
    "Act as a senior strategy, operations, and AI transformation analyst "
    "preparing an outside-in executive briefing for a client pursuit. "
    "Your job is to identify business facts, operating constraints, peer gaps, "
    "and AI value pools that could be influenced through process reinvention, "
    "network redesign, automation, ML, generative AI, or agentic AI. "
    "Use only public, verifiable sources. Distinguish clearly between facts, "
    "inferences, assumptions, and missing information. Be skeptical of corporate "
    "narrative and contrast claims with numbers. Output must be concise, "
    "structured, comparative, and executive-ready."
)

# Module execution order
MODULE_ORDER = [
    "source_collector",
    "source_gate",        # MANDATORY quality check
    "internal_intel",     # Optional — skipped if INTERNAL_INTEL_ENABLED is False
    "company_research",   # Prompts 1, 8, 9
    "peer_benchmark",     # Prompts 2, 3
    "operating_model",    # Prompts 11, 12
    "ai_value",           # Prompts 4, 5, 6, 7
    "current_signals",    # Prompt 13
    "red_team",           # Due Diligence: Kill My Thesis
    "memo_composer",      # Prompt 10 + visualizations
]

# ============================================================
# RETRY SETTINGS
# ============================================================
# How many times to retry a failed API call
MAX_RETRIES = 3

# Seconds to wait between retries
RETRY_DELAY = 5