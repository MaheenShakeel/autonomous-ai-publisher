def get_article_prompt(topic: str) -> str:
    return f"""
You are an expert technical writer specializing in Cloud and AI cost optimization for small and medium businesses (SMBs).

Write a complete, SEO-optimized article on the following topic:
Topic: {topic}

Your response must be a valid JSON object with exactly these fields:
{{
  "title": "The full article title (compelling, SEO-friendly)",
  "slug": "url-friendly-version-of-title-lowercase-with-hyphens",
  "excerpt": "A 1-2 sentence summary of the article (used as meta description)",
  "content": "The full article in HTML format with proper <h2>, <p>, <ul> tags"
}}

Requirements:
- Title must be clear and specific
- Slug must be lowercase, no spaces, hyphens only
- Excerpt must be under 160 characters
- Content must be at least 600 words
- Write for a non-technical SMB audience
- Include practical, actionable advice
- Do NOT include markdown code fences in your response, just the raw JSON
"""