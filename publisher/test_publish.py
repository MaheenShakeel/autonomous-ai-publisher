from publisher.wp_client import WordPressClient
from utils.logger import get_logger

logger = get_logger("TEST_PUBLISH")

def main():
    logger.info("Starting publish test...")
    client = WordPressClient()
    
    # 1. Dynamically get the ID for the category you created in Step 1
    target_category = "Cloud Optimization"
    cat_id = client.get_category_id_by_name(target_category)
    
    if not cat_id:
        logger.error("Aborting publish: Category ID could not be found.")
        return # Fail fast!
        
    # 2. Pass that ID into your post creator as a list
    client.create_post(
        title="Dynamic Category Test",
        content="This post should automatically be assigned to the Cloud Optimization category.",
        categories=[cat_id]
    )

if __name__ == "__main__":
    main()