# Smart Loadshedding Advisor

A starter project for the Smart Loadshedding Advisor using FastAPI, Streamlit, PostgreSQL, and LangChain.

## Requirements

- Python 3.11 (see `python-version`).
- PostgreSQL (configure connection details in your environment).

## Environment Variables

Create a `.env` file with the following keys:

```
ESKOM_TOKEN_KEY=your_eskom_token
OPENAI_KEY=your_openai_key
```

They are loaded at startup via `python-dotenv`.

## Running the API

Install dependencies and start the FastAPI server:

```bash
uvicorn main:app --reload
```

Test the health check:

```
GET http://127.0.0.1:8000/health
```

## Running the Streamlit UI

```bash
streamlit run main.py
```

You should see a placeholder UI for the Streamlit frontend.
