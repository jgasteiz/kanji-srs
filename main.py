from fastapi import FastAPI, Request, responses, staticfiles, templating

from kanji_selector import queries

app = FastAPI()
app.mount(
    "/static", staticfiles.StaticFiles(directory="static", html=True), name="static"
)
templates = templating.Jinja2Templates(directory="templates")


@app.get("/app/", response_class=responses.HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})


@app.get("/random-kanji/")
async def get_random_kanji():
    return queries.get_random_kanji()


@app.get("/levels/")
async def get_levels():
    return queries.get_levels()
