Company: {COMPANY}

Search for the latest publicly available sources for the target company.

Required output:
- List of mandatory sources with URL or file location: annual reports / 10-K, quarterly reports / 10-Q, SEC filings or 20-F, DEF 14A proxy statement
- List of important supporting sources with URL or file location: earnings call transcripts, investor presentations, investor day / capital markets day
- Gate status: PASS, PARTIAL, or FAIL
- If FAIL: explain exactly what is missing and where to find it, including the path to place manual uploads in `inputs/{COMPANY}/manual/`
- If PARTIAL: identify gaps and continue with warning

Format the answer as markdown with sections for Sources Found, Sources Missing, and Gate Status.
