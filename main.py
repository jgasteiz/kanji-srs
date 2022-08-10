from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from kanji_selector import data

app = FastAPI()

app.mount("/app", StaticFiles(directory="app", html=True), name="app")


@app.get("/random-kanji/")
async def get_random_kanji():
    return data.get_random_kanji()
