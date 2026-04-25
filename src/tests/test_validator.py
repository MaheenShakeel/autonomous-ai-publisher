from src.validator import validate_article

def test_valid_article():
    article = {
        "title": "How to Cut AWS Costs",
        "content": "a" * 400,
        "slug": "how-to-cut-aws-costs",
        "excerpt": "A guide to saving money on AWS."
    }
    valid, errors = validate_article(article)
    assert valid is True
    assert errors == []

def test_missing_title():
    article = {"title": "", "content": "a" * 400, "slug": "test", "excerpt": "test"}
    valid, errors = validate_article(article)
    assert valid is False
    assert any("Title" in e for e in errors)

def test_short_content():
    article = {"title": "Test", "content": "short", "slug": "test", "excerpt": "test"}
    valid, errors = validate_article(article)
    assert valid is False