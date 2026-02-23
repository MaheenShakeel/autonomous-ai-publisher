from dotenv import load_dotenv
import os
from utils.logger import get_logger

# Load environment variables
load_dotenv()

logger = get_logger("MAIN")

def main():
    logger.info("System initializing...")

    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        masked_key = api_key[:4] + "****"
        logger.info(f"OPENAI_API_KEY loaded: {masked_key}")
    else:
        logger.error("OPENAI_API_KEY not found!")

    topic = "Sample Topic: Reducing AWS EC2 Costs"
    logger.info(f"Selected topic: {topic}")

    logger.info("System exited successfully.")

if __name__ == "__main__":
    main()