from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from kanji_selector import queries

app = FastAPI()

app.mount("/app", StaticFiles(directory="app", html=True), name="app")


@app.get("/random-kanji/")
def get_random_kanji():
    return queries.get_random_kanji()


@app.get("/levels/")
def get_levels():
    return queries.get_levels()
