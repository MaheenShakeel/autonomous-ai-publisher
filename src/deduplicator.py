import json
import os

DATA_FILE = "data/posted_articles.json"

def load_published() -> list:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def is_duplicate(topic: str) -> bool:
    published = load_published()
    return topic.lower().strip() in [p["topic"].lower().strip() for p in published]

def record_published(topic: str, post_id: int, url: str):
    published = load_published()
    published.append({"topic": topic, "post_id": post_id, "url": url})
    with open(DATA_FILE, "w") as f:
        json.dump(published, f, indent=2)