# Motivational Quotes API

A simple REST API built with **FastAPI** that serves random motivational quotes.

## Endpoints

| Method | Route     | Description              |
|--------|-----------|--------------------------|
| GET    | `/`       | Welcome message          |
| GET    | `/quote`  | Get a random quote       |
| GET    | `/quotes` | Get all available quotes |

## Setup

```bash
pip install -r requirements.txt
python run.py
```

The server runs at `http://localhost:8000`.

Interactive API docs available at `http://localhost:8000/docs`.

## Project Structure

```
motivational-quotes-api/
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI app and routes
│   └── quotes.py      # Quotes data and helper functions
├── run.py             # Entry point
├── requirements.txt
└── Readme.md
```

## Tech Stack

- Python
- FastAPI
- Uvicorn