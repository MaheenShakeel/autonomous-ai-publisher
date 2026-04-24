import re

def validate_article(article: dict) -> tuple[bool, list[str]]:
    errors = []

    # Check title exists
    if not article.get("title"):
        errors.append("Title is missing")

    # Check content length (minimum 300 characters as a safe threshold)
    content = article.get("content", "")
    if len(content) < 300:
        errors.append(f"Content too short: {len(content)} characters (minimum 300)")

    # Check for placeholder text
    placeholders = ["lorem ipsum", "[insert", "placeholder", "TODO", "FIXME"]
    for placeholder in placeholders:
        if placeholder.lower() in content.lower():
            errors.append(f"Placeholder text found: '{placeholder}'")

    # Check slug is valid
    slug = article.get("slug", "")
    if not slug:
        errors.append("Slug is missing")
    elif not re.match(r"^[a-z0-9-]+$", slug):
        errors.append(f"Slug has invalid characters: '{slug}'")

    is_valid = len(errors) == 0
    return is_valid, errors