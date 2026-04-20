import json
import re
from google import genai
from src.config import get_config
from src.prompts import get_article_prompt

def generate_article(topic: str) -> dict:
    config = get_config()

    client = genai.Client(api_key=config["GEMINI_API_KEY"])

    prompt = get_article_prompt(topic)

    response = client.models.generate_content(
        model=config["GEMINI_MODEL"],
        contents=prompt
    )

    raw_text = response.text.strip()

    # Remove markdown fences if present
    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]
    raw_text = raw_text.strip()

    article = json.loads(raw_text)
    return normalize_article(article)


import re

def normalize_article(article: dict) -> dict:
    # Clean whitespace
    article["title"] = article.get("title", "").strip()
    article["content"] = article.get("content", "").strip()
    article["excerpt"] = article.get("excerpt", "").strip()

    # Generate slug if missing
    if not article.get("slug"):
        slug = article["title"].lower()
        slug = re.sub(r"[^a-z0-9\s-]", "", slug)
        slug = re.sub(r"\s+", "-", slug).strip("-")
        article["slug"] = slug

    # Truncate excerpt if too long
    if len(article["excerpt"]) > 160:
        article["excerpt"] = article["excerpt"][:157] + "..."

    return article