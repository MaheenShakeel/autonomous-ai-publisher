# Autonomous AI Article Agent

## Project Overview

This project is an autonomous AI system designed to operate as a scheduled WordPress publisher. The pipeline systematically selects domain-specific topics focused on **Cloud and AI cost optimization for SMBs**. It uses an AI agent workflow to generate high-quality, structured articles, applies quality checks and SEO optimization, and automatically publishes them to a WordPress website.

The system is designed with a production-first mindset, emphasizing modular architecture, robust error handling, and comprehensive logging for operational visibility.

---

## Prerequisites

To run this project locally, ensure you have the following installed:

- **Python 3.13+**
- **Git**
- **Docker** (required for the local WordPress testing environment)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/MaheenShakeel/autonomous-ai-publisher.git
cd autonomous-ai-publisher
```

### 2. Set up the virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file and fill in your credentials:

```bash
cp .env.example .env
```

Your `.env` file must include:

```env
# Gemini AI
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=models/gemini-2.0-flash

# WordPress (old keys kept for Week 2 compatibility)
WP_URL=http://localhost:8080
WP_USERNAME=publisher-bot
WP_APP_PASSWORD=your-app-password

# WordPress (Week 3)
WORDPRESS_BASE_URL=http://localhost:8080
WORDPRESS_USERNAME=publisher-bot
WORDPRESS_APP_PASSWORD=your-app-password
WORDPRESS_POST_STATUS=draft

# Pipeline settings
DEFAULT_TOPIC=Cloud cost optimization for small businesses
DRY_RUN=false
```

### 5. Start the local WordPress instance

```bash
docker compose -f infra/docker-compose.yml up -d
```

Then visit `http://localhost:8080` in your browser to confirm WordPress is running.

---

## Running the Pipeline

### Full pipeline (generates article and publishes to WordPress)

```bash
python main.py
```

### Dry run (generates and validates article but does NOT publish)

Set `DRY_RUN=true` in your `.env` file, then run:

```bash
python main.py
```

### Test WordPress connection only (Week 2 test)

```bash
python -m publisher.test_publish
```

### Shut down Docker when done

```bash
docker compose -f infra/docker-compose.yml down
```

---

## Testing

### Run all unit tests

```bash
pytest src/tests/
```

### Test individual components

```bash
# Test config loads correctly
python -c "from src.config import get_config; c = get_config(); print('Config OK')"

# Test article generation
python -c "from src.article_generator import generate_article; a = generate_article('Cloud cost optimization'); print(a['title'])"

# Test article validation
python -c "from src.validator import validate_article; print(validate_article({'title':'Test','content':'x'*400,'slug':'test','excerpt':'test'}))"

# Test duplicate detection
python -c "from src.deduplicator import is_duplicate; print('Duplicate?', is_duplicate('test topic'))"

# Test WordPress connection
python -c "from src.wordpress_client import test_connection; test_connection()"
```

---

## Environment Variables

| Variable | Description | Example |
|---|---|---|
| `GEMINI_API_KEY` | Google AI Studio API key | `AIza...` |
| `GEMINI_MODEL` | Gemini model to use | `models/gemini-2.0-flash` |
| `WORDPRESS_BASE_URL` | Local WordPress URL | `http://localhost:8080` |
| `WORDPRESS_USERNAME` | WordPress username | `publisher-bot` |
| `WORDPRESS_APP_PASSWORD` | WordPress application password | `xxxx xxxx xxxx` |
| `WORDPRESS_POST_STATUS` | Post status on publish | `draft` or `publish` |
| `DEFAULT_TOPIC` | Topic to generate article about | `Cloud cost optimization` |
| `DRY_RUN` | Skip publishing if true | `true` or `false` |

---

## Folder Structure

```
autonomous-ai-publisher/
│
├── agents/                    # AI agent workflows (Topic Planner, Writer, Editor, SEO)
├── data/                      # Runtime data (posted_articles.json for duplicate tracking)
├── infra/                     # Docker Compose configuration
├── prompts/                   # Externalized system prompts for AI agents
├── publisher/                 # Week 2 WordPress REST API integration
├── scheduler/                 # Cron/APScheduler execution logic
├── src/                       # Week 3 core pipeline modules
│   ├── article_generator.py   # Calls Gemini AI to generate articles
│   ├── config.py              # Loads and validates environment variables
│   ├── deduplicator.py        # Prevents publishing duplicate topics
│   ├── prompts.py             # Article generation prompt template
│   ├── validator.py           # Checks article quality before publishing
│   ├── wordpress_client.py    # WordPress REST API client
│   └── tests/                 # Unit tests for all modules
├── storage/                   # SQLite database interactions
├── utils/                     # Shared utilities including structured logging
├── tests/                     # Top-level pytest test suite
├── main.py                    # Pipeline entry point
├── .env.example               # Example environment variable file
└── README.md                  # This file
```

---

## How It Works

```
main.py
   │
   ├── 1. Load config (.env)
   ├── 2. Check for duplicate topic
   ├── 3. Generate article via Gemini AI
   ├── 4. Validate article quality
   ├── 5. Publish to WordPress  ──(or)──  Simulate if DRY_RUN=true
   └── 6. Log results + record published topic
```