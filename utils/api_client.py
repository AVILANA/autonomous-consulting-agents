"""
Autonomous Consulting Agents — API Client
Handles all communication with the Anthropic Claude API.
Every call automatically prepends the Master Prompt (Prompt 0).
Supports both heavy (Opus) and light (Sonnet) model routing.
"""

import json
import time
from anthropic import Anthropic
from tenacity import retry, stop_after_attempt, wait_fixed
from rich.console import Console

import config

# Rich console for pretty terminal output
console = Console()

# Initialize the Anthropic client (uses ANTHROPIC_API_KEY from .env automatically)
client = Anthropic(api_key=config.ANTHROPIC_API_KEY)


def get_model(module_name: str) -> str:
    """
    Returns the right model for a given module.
    Heavy modules (deep analysis) use Opus.
    Light modules (data collection) use Sonnet.
    """
    assignment = config.MODEL_ASSIGNMENT.get(module_name, "heavy")
    if assignment == "heavy":
        return config.MODEL_HEAVY
    return config.MODEL_LIGHT


@retry(stop=stop_after_attempt(config.MAX_RETRIES), wait=wait_fixed(config.RETRY_DELAY))
def call_claude(
    prompt: str,
    module_name: str,
    system_prompt: str = None,
    expect_json: bool = True,
    web_search: bool = False,
) -> dict | str:
    """
    Send a prompt to Claude and get a response.

    Args:
        prompt: The user message to send (the specific analysis request)
        module_name: Which module is calling (determines Opus vs Sonnet)
        system_prompt: Optional override for system prompt (default: Master Prompt)
        expect_json: If True, parse the response as JSON
        web_search: If True, enable web search tool for this call

    Returns:
        Parsed JSON dict if expect_json=True, otherwise raw text string
    """
    model = get_model(module_name)
    system = system_prompt or config.MASTER_PROMPT

    console.print(f"\n[bold blue]📡 Calling Claude ({model})[/bold blue]")
    console.print(f"[dim]Module: {module_name} | JSON expected: {expect_json} | Web search: {web_search}[/dim]")

    start_time = time.time()

    # Build the API call parameters
    api_params = {
        "model": model,
        "max_tokens": config.MAX_TOKENS,
        "system": system,
        "messages": [
            {"role": "user", "content": prompt}
        ],
    }

    # Add web search tool if requested
    if web_search:
        api_params["tools"] = [
            {
                "type": "web_search_20250305",
                "name": "web_search",
            }
        ]

    # Make the API call
    response = client.messages.create(**api_params)

    elapsed = round(time.time() - start_time, 1)

    # Extract text from response (may contain multiple content blocks)
    text_parts = []
    for block in response.content:
        if block.type == "text":
            text_parts.append(block.text)
    full_text = "\n".join(text_parts)

    # Log usage
    tokens_in = response.usage.input_tokens
    tokens_out = response.usage.output_tokens
    console.print(f"[green]✓ Response received[/green] — {elapsed}s | Tokens: {tokens_in} in / {tokens_out} out")

    # Parse JSON if expected
    if expect_json:
        return parse_json_response(full_text)

    return full_text


def parse_json_response(text: str) -> dict:
    """
    Safely parse a JSON response from Claude.
    Handles cases where Claude wraps JSON in markdown code blocks.
    """
    # Remove markdown code fences if present
    cleaned = text.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    if cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        console.print(f"[bold red]⚠ JSON parse error:[/bold red] {e}")
        console.print("[yellow]Returning raw text instead. The module should handle this.[/yellow]")
        return {"_raw_text": cleaned, "_parse_error": str(e)}


def call_claude_with_context(
    prompt_template: str,
    context: dict,
    module_name: str,
    expect_json: bool = True,
    web_search: bool = False,
) -> dict | str:
    """
    Higher-level function that fills a prompt template with context from prior modules,
    then calls Claude.

    Args:
        prompt_template: The prompt text with {PLACEHOLDERS}
        context: Dict of prior artifacts to inject into the prompt
        module_name: Which module is calling
        expect_json: If True, parse response as JSON
        web_search: If True, enable web search

    Returns:
        Parsed response (dict or string)
    """
    # Replace {COMPANY} and other placeholders
    filled_prompt = prompt_template
    for key, value in context.items():
        placeholder = "{" + key.upper() + "}"
        if placeholder in filled_prompt:
            if isinstance(value, dict):
                filled_prompt = filled_prompt.replace(placeholder, json.dumps(value, indent=2))
            else:
                filled_prompt = filled_prompt.replace(placeholder, str(value))

    # Replace any {ALL_PRIOR_ARTIFACTS} or {ALL_ARTIFACTS} with full context dump
    if "{ALL_PRIOR_ARTIFACTS}" in filled_prompt or "{ALL_ARTIFACTS}" in filled_prompt:
        artifacts_dump = json.dumps(context, indent=2, default=str)
        filled_prompt = filled_prompt.replace("{ALL_PRIOR_ARTIFACTS}", artifacts_dump)
        filled_prompt = filled_prompt.replace("{ALL_ARTIFACTS}", artifacts_dump)

    return call_claude(
        prompt=filled_prompt,
        module_name=module_name,
        expect_json=expect_json,
        web_search=web_search,
    )


def test_connection() -> bool:
    """
    Quick test to verify the API connection works.
    Returns True if successful, False otherwise.
    """
    try:
        console.print("\n[bold]🔌 Testing API connection...[/bold]")
        response = call_claude(
            prompt="Reply with exactly this JSON: {\"status\": \"connected\", \"message\": \"API working\"}",
            module_name="source_collector",  # Uses light model for the test
            expect_json=True,
            web_search=False,
        )
        if response.get("status") == "connected":
            console.print("[bold green]✅ API connection successful![/bold green]\n")
            return True
        else:
            console.print(f"[bold yellow]⚠ Unexpected response: {response}[/bold yellow]\n")
            return True  # Still connected, just unexpected format
    except Exception as e:
        console.print(f"[bold red]❌ API connection failed: {e}[/bold red]\n")
        return False