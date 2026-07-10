from fastapi import FastAPI
from app.quotes import quotes, get_random_quote

app = FastAPI(
    title="Motivational Quotes API",
    description="A simple API that serves motivational quotes",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "Welcome to the Motivational Quotes API! Hit /quote for inspiration."}

@app.get("/quote")
def random_quote():
    return get_random_quote()

@app.get("/quotes")
def all_quotes():
    return quotes