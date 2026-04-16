import requests
import os
from dotenv import load_dotenv
from utils.logger import get_logger
from requests.auth import HTTPBasicAuth

load_dotenv()

logger = get_logger("WP_CLIENT")

class WordPressClient:
    def __init__(self):
        self.base_url = os.getenv("WP_URL")
        self.username = os.getenv("WP_USERNAME")
        self.app_password = os.getenv("WP_APP_PASSWORD")

        if not all([self.base_url, self.username, self.app_password]):
            raise ValueError("Missing WordPress credentials in .env")

    def get_category_id_by_name(self, category_name: str):
        logger.info(f"Searching for category ID: {category_name}")
        url = f"{self.base_url}/wp-json/wp/v2/categories"
        
        # Make the GET request to WordPress
        response = requests.get(
            url,
            auth=HTTPBasicAuth(self.username, self.app_password)
        )
        
        if response.status_code == 200:
            categories = response.json()
            # Loop through the list of categories WordPress sent back
            for cat in categories:
                # Compare names in lowercase so it matches perfectly
                if cat['name'].lower() == category_name.lower():
                    logger.info(f"Found '{category_name}' with ID: {cat['id']}")
                    return cat['id']
            
            logger.error(f"Category '{category_name}' does not exist in WordPress.")
            return None
        else:
            logger.error(f"Failed to fetch categories. Status: {response.status_code}")
            return None		


    def create_post(self, title, content, categories=None, tags=None):
        url = f"{self.base_url}/wp-json/wp/v2/posts"

        payload = {
            "title": title,
            "content": content,
            "status": "draft"
        }

        if categories:
            payload["categories"] = categories

        if tags:
            payload["tags"] = tags

        try:
            response = requests.post(
                url,
                json=payload,
                auth=HTTPBasicAuth(self.username, self.app_password)
            )

            logger.info(f"Status Code: {response.status_code}")

            if response.status_code == 201:
                logger.info("Post created successfully")
                return response.json()
            else:
                logger.error(f"Failed: {response.text}")
                return None

        except Exception as e:
            logger.error(f"Exception occurred: {str(e)}")
            return None