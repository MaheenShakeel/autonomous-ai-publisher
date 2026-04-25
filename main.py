import sys
from dotenv import load_dotenv
from src.config import get_config
from src.article_generator import generate_article
from src.validator import validate_article
from src.deduplicator import is_duplicate, record_published
from src.wordpress_client import create_post
from utils.logger import get_logger

load_dotenv()
logger = get_logger("MAIN")

def main():
    logger.info("=== Autonomous Article Pipeline Started ===")

    # Step 1: Load config
    try:
        config = get_config()
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        sys.exit(1)

    topic = config["DEFAULT_TOPIC"]
    dry_run = config["DRY_RUN"]
    logger.info(f"Topic: {topic}")
    logger.info(f"Dry Run Mode: {dry_run}")

    # Step 2: Duplicate check
    if is_duplicate(topic):
        logger.warning(f"Duplicate topic detected: '{topic}' — skipping.")
        sys.exit(0)

    # Step 3: Generate article via Gemini
    logger.info("Generating article via Gemini AI...")
    try:
        article = generate_article(topic)
        logger.info(f"Generated title: {article['title']}")
        logger.info(f"Slug: {article['slug']}")
    except Exception as e:
        logger.error(f"Article generation failed: {e}")
        sys.exit(1)

    # Step 4: Validate article
    is_valid, errors = validate_article(article)
    if not is_valid:
        logger.error(f"Article failed validation: {errors}")
        sys.exit(1)
    logger.info("Article passed validation ✅")

    # Step 5: Publish or simulate
    if dry_run:
        logger.info("--- DRY RUN MODE — Article will NOT be published ---")
        logger.info(f"Title    : {article['title']}")
        logger.info(f"Slug     : {article['slug']}")
        logger.info(f"Excerpt  : {article['excerpt']}")
        logger.info("--- End of Dry Run ---")
    else:
        logger.info("Publishing article to WordPress...")
        try:
            result = create_post(article)
            record_published(topic, result["post_id"], result["url"])
            logger.info(f"✅ Published successfully!")
            logger.info(f"Post ID  : {result['post_id']}")
            logger.info(f"URL      : {result['url']}")
            logger.info(f"Status   : {result['status']}")
        except Exception as e:
            logger.error(f"Publishing failed: {e}")
            sys.exit(1)

    logger.info("=== Pipeline Complete ===")

if __name__ == "__main__":
    main()