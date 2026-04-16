import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    config = {
        "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
        "GEMINI_MODEL": os.getenv("GEMINI_MODEL", "gemini-2.0-flash"),
        "WORDPRESS_BASE_URL": os.getenv("WORDPRESS_BASE_URL"),
        "WORDPRESS_USERNAME": os.getenv("WORDPRESS_USERNAME"),
        "WORDPRESS_APP_PASSWORD": os.getenv("WORDPRESS_APP_PASSWORD"),
        "WORDPRESS_POST_STATUS": os.getenv("WORDPRESS_POST_STATUS", "draft"),
        "DEFAULT_TOPIC": os.getenv("DEFAULT_TOPIC", "Cloud cost optimization"),
        "DRY_RUN": os.getenv("DRY_RUN", "false").lower() == "true",
    }

    # Validate required fields
    required = ["GEMINI_API_KEY", "WORDPRESS_BASE_URL", "WORDPRESS_USERNAME"]
    for key in required:
        if not config[key]:
            raise ValueError(f"Missing required environment variable: {key}")

    return config
