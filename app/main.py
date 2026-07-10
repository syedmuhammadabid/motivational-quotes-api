from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.quotes import quotes, get_random_quote

app = FastAPI(
    title="Motivational Quotes API",
    description="A simple API that serves motivational quotes",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/quote")
def random_quote():
    return get_random_quote()


@app.get("/quotes")
def all_quotes():
    return quotes