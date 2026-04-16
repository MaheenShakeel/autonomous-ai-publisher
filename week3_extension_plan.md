\# Week 3 Extension Plan



\## What Exists (Week 2)

\- `publisher/wp\_client.py` — WordPress API client (auth + post creation)

\- `publisher/test\_publish.py` — test script that creates a draft post

\- `utils/logger.py` — structured logging utility

\- `.env` — stores WordPress credentials

\- `infra/docker-compose.yml` — runs local WordPress + MySQL



\## What Will Be Added (Week 3)

\- `src/article\_generator.py` — calls OpenAI to generate articles

\- `src/prompts.py` — holds the prompt template

\- `src/validator.py` — checks article quality

\- `src/deduplicator.py` — prevents publishing same topic twice

\- `src/config.py` — loads and validates all env variables

\- Updated `main.py` — full pipeline from topic → publish



\## Reusable From Week 2

\- Logger utility

\- WordPress client

\- .env loading pattern



\## New Environment Variables Needed

\- OPENAI\_API\_KEY

\- OPENAI\_MODEL

\- WORDPRESS\_POST\_STATUS

\- DEFAULT\_TOPIC

\- DRY\_RUN

