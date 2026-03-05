# **Autonomous AI Article Agent**

### 

### Project Overview



This project is an autonomous AI system designed to operate as a scheduled WordPress publisher. The pipeline is built to systematically select domain-specific topics focused on Cloud and AI cost optimization for SMBs. It utilizes an AI agent workflow to generate high-quality, structured articles, applies quality checks and SEO optimization, and automatically publishes them to a WordPress website.



The system is designed with a production-first mindset, emphasizing modular architecture, robust error handling, and comprehensive logging for operational visibility.



### **Prerequisites**



To run this project locally, ensure you have the following installed:

* **Python 3.13+** 
* **Git**
* **Docker** (Required for the local WordPress testing environment) 



### **Setup Instructions**



#### 1\. Clone the repository:

```bash

git clone \[https://github.com/MaheenShakeel/autonomous-ai-publisher.git](https://github.com/MaheenShakeel/autonomous-ai-publisher.git)

cd autonomous-ai-publisher



#### 2\. Set up the virtual environment:



```bash

python -m venv venv

venv\\Scripts\\activate  # On Windows

\# source venv/bin/activate  # On Mac/Linux



#### 3\. Install dependencies:



```bash

pip install -r requirements.txt



#### 4\. Configure environment variables:



Copy the example environment file and populate it with your credentials:



```bash

cp .env.example .env

Your .env file must include:



OPENAI\_API\_KEY: Your OpenAI API key.



WP\_URL: The local Docker WordPress URL (e.g., http://localhost:8080).



WP\_USERNAME: Your WordPress administrator username.



WP\_APP\_PASSWORD: Your WordPress Application Password.



#### 5\. Start the local infrastructure:



Use Docker to spin up the local WordPress and database containers.



```bash

docker compose up -d

Usage / Running the Pipeline

Currently, the system is configured to test the WordPress REST API integration. It will dynamically fetch category IDs and publish a draft post to your local WordPress instance.



To run the publisher test:



```bash

python -m publisher.test\_publish





**To shut down the local infrastructure when you are done:**



```bash

docker compose down

Folder Structure





###### The codebase follows a modular design, separating discrete system components:





* agents/ - AI agent workflows (Topic Planner, Writer, Editor, SEO)



* publisher/ - WordPress REST API integration logic



* scheduler/ - Cron/APScheduler execution logic



* storage/ - SQLite database interactions and state tracking



* utils/ - Shared utilities, including structured logging



* tests/ - Automated unit tests via pytest



* infra/ - Infrastructure configuration (Docker Compose files)



* prompts/ - Externalized system prompts for AI agents





