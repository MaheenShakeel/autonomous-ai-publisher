"""
WordPress REST API Reference
============================
Endpoint: POST /wp-json/wp/v2/posts

Required Fields:
- title    : Article title (string)
- content  : HTML content (string)
- excerpt  : Short summary (string)
- slug     : URL slug (string)
- status   : 'draft' or 'publish'

Authentication: Basic Auth using WordPress username + application password
Response: 201 Created with post ID and URL on success
"""

import requests
from requests.auth import HTTPBasicAuth
from src.config import get_config


def get_auth():
    config = get_config()
    return HTTPBasicAuth(
        config["WORDPRESS_USERNAME"],
        config["WORDPRESS_APP_PASSWORD"]
    )


def test_connection():
    config = get_config()
    auth = get_auth()
    url = f"{config['WORDPRESS_BASE_URL']}/wp-json/wp/v2/users/me"
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        print("✅ WordPress connection successful")
        return True
    else:
        print(f"❌ Connection failed: {response.status_code} {response.text}")
        return False


def create_post(article: dict) -> dict:
    config = get_config()
    auth = get_auth()
    url = f"{config['WORDPRESS_BASE_URL']}/wp-json/wp/v2/posts"

    payload = {
        "title": article["title"],
        "content": article["content"],
        "excerpt": article["excerpt"],
        "slug": article["slug"],
        "status": config["WORDPRESS_POST_STATUS"],
    }

    response = requests.post(url, json=payload, auth=auth)

    if response.status_code == 201:
        data = response.json()
        return {
            "post_id": data["id"],
            "url": data["link"],
            "status": data["status"]
        }
    else:
        raise Exception(f"WordPress API error {response.status_code}: {response.text}")