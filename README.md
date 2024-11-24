
# Fan Theory Aggregator

This project is an automated pipeline for gathering, curating, and presenting fan theories about popular animanga. Using AI-powered agents and Reddit data, it extracts fan-generated content, evaluates their relevance and uniqueness, and generates engaging articles.

## Key Features

- **Reddit Integration**: Search and retrieve recent Reddit posts from specified subreddits.
- **Modular Agents**: Specialized agents for data gathering, curation, and writing.
- **Task Automation**: Seamless pipeline to manage workflows from data ingestion to article generation.

---

## Project Structure

```plaintext
Fan-Theory-Aggregator/
├── Agents.py          # Agent definitions for tasks like research and curation
├── Tools.py           # Custom tools for Reddit search
├── Test.py            # Example task execution with CrewAI
├── requirements.txt   # Python dependencies
├── .env               # Environment variables (excluded from version control)
└── README.md          # Project documentation
```

---

## Getting Started

### Prerequisites

1. **Python 3.8+**
2. **Dependencies**:
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```
3. **Reddit API Access**:
   - Obtain Reddit API credentials and add them to a `.env` file:
     ```plaintext
     REDDIT_CLIENT_ID=<your_client_id>
     REDDIT_CLIENT_SECRET=<your_client_secret>
     ```

### Running the Code

1. Define your inputs (e.g., `query` and `subreddit`) in `Test.py`.
2. Run the test script:
   ```bash
   python Test.py
   ```
3. The results will include Reddit posts relevant to the specified query.

---

## Usage

### Agents

1. **Theory Finder**:
   - **Role**: Researcher.
   - **Goal**: Find relevant Reddit posts discussing fan theories for a given animanga.
   - **Tool**: `my_tool` (RedditSearcher).

2. **Theory Curator** (Planned Expansion):
   - **Role**: Curator.
   - **Goal**: Identify the most compelling and well-supported fan theories.

3. **Article Writer** (Planned Expansion):
   - **Role**: Writer.
   - **Goal**: Transform curated theories into engaging narratives.

### Tools

- **RedditSearcher**:
  - A custom tool for searching Reddit posts based on user-provided parameters like query, subreddit, and time filter.

---
