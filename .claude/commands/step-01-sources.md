FIRST: Read memory.md in the project root. This contains accumulated quality standards and learnings from previous executions. Apply all quality standards listed there throughout this step.

# Step 1: Source Collection & Quality Gate

Search the web for and collect public sources for the target company. You MUST use web search actively — do NOT just check local files.
Collect links, raw documents, and filings and extract numbers from the underlying disclosures, not just summary pages.

## Required outputs
- `outputs/{company}/sources/source_index.md`
- `outputs/{company}/sources/financial_data.md`
- `outputs/{company}/source_gate_report.md`
- Raw links or uploaded files saved under `outputs/{company}/sources/`

## Mandatory sources (workflow STOP if missing)
- Annual Reports / 10-K / 20-F filings: minimum 3 years, ideal 5
- Quarterly Reports / 10-Q or interim reports: minimum last 4 quarters, ideal 3 years
- SEC filings (or equivalent regulatory filings for non-US companies): minimum 3 years, ideal 5 years
- Proxy Statement / DEF 14A (or equivalent governance document): latest year

## Important sources (continue but flag gaps)
- Earnings call transcripts
- Investor presentations
- Investor Day / Capital Markets Day presentations

## Instructions
1. Use web search as the PRIMARY research method. Performing at least 8 explicit web searches is mandatory.
2. The source inventory must be built from public web research first. Only after that use `inputs/{company}/manual/` as a secondary source for files already downloaded by the user.
3. Required explicit searches:
   - `"{company} investor relations annual report"`
   - `"{company} SEC EDGAR 20-F"` (for non-US companies) or `"{company} SEC EDGAR 10-K"` (for US companies)
   - `"{company} quarterly report Q4 2025"` and prior quarters
   - `"{company} earnings call transcript"`
   - `"{company} investor presentation"`
   - `"{company} proxy statement DEF 14A"`
   - `"{company} investor day"` or `"{company} capital markets day"`
   - Visit the company investor relations website directly and catalog what is available
4. For European or other non-US-listed companies, do NOT rely on SEC EDGAR as the first source. Search the company IR website for annual reports and interim results. Only search for `20-F` if the company has a US ADR listing or is otherwise US-reporting.
5. For every source found, save the URL, year, source type, and summary of key contents to `outputs/{company}/sources/source_index.md`.
6. Extract actual financial data from the source documents or web pages. For each annual report, filing, or investor release found, visit the document and capture:
   - Revenue
   - Net income
   - EBITDA
   - Gross margin
   - Operating margin
   - SG&A or total OPEX
   - Debt levels
   - Capex
   - Working capital components (inventory, receivables, payables)
7. Save the extracted financial metrics in `outputs/{company}/sources/financial_data.md` as a structured table covering each available year.
   - Without actual numbers, the analysis will be generic. Financial data extraction is as important as finding the sources.
8. If a document cannot be accessed directly, extract whatever financial figures are available from investor relations summaries, earnings releases, press releases, or financial aggregators.
9. Also check `inputs/{company}/manual/` for any manual uploads and include them in the source registry, but only after the web search inventory is complete.
10. Document every missing mandatory or important source in `outputs/{company}/source_gate_report.md`, including type, years searched, and reason not found.
11. Determine gate status in `outputs/{company}/source_gate_report.md`:
    - FAIL: any mandatory source missing or below minimum threshold
    - PARTIAL: all mandatory sources present but one or more important sources missing
    - PASS: all mandatory sources available
12. If FAIL, clearly list the exact documents the user must download and where to place them (`inputs/{company}/manual/`) and stop the workflow.
13. If PASS or PARTIAL, proceed to Step 2.

## Notes for non-US companies
- Search the company investor relations website for annual reports, interim reports, and equivalent regulatory filings first.
- Look for local filings or home-market disclosure documents (e.g. annual report, interim report, half-year report, annual general meeting materials).
- Only search for SEC `20-F` if the company is a US-reporting foreign issuer or has ADR listings in the United States.
- For governance documentation, use the local equivalent to DEF 14A where necessary, but prioritize the latest proxy or shareholder meeting report.
