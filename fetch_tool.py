# fetch_tool.py
import requests
from bs4 import BeautifulSoup


def fetch_webpage(url: str, max_chars: int = 4000) -> str:
    """

    Using the fetch_tool to read, summarise, or analyse the contents
    of a web page. The model then decides how to use the returned text
    (e.g. summarise, extract key points, answer questions).
    """
    # Basic validation
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError("URL must start with http:// or https://")

    # Fetch the page
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()

    content_type = resp.headers.get("Content-Type", "")

    # If it's not HTML, just return (truncated) raw text/bytes decoded
    if "text/html" not in content_type:
        # Best effort decode
        text = resp.text
        if len(text) > max_chars:
            text = text[:max_chars] + "\n\n[Truncated non-HTML content]"
        return text

    # Parse HTML and strip scripts/styles
    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Extract visible text
    text = soup.get_text(separator="\n")

    # Normalise whitespace: strip and drop empty lines
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]
    text = "\n".join(lines)

    # Truncate to max_chars to avoid overloading the model context
    if len(text) > max_chars:
        text = text[:max_chars] + "\n\n[Truncated page content]"
    return text
