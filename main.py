import uvicorn
from fastapi import FastAPI, HTTPException, Request, responses, staticfiles, templating
from kanji_selector import models, queries

app = FastAPI()
app.mount("/static", staticfiles.StaticFiles(directory="static", html=True), name="static")
templates = templating.Jinja2Templates(directory="templates")


@app.get("/app/", response_class=responses.HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})


@app.get("/random-kanji/")
async def get_random_kanji():
    return queries.get_random_kanji()


@app.get("/levels/")
async def get_levels() -> list[str]:
    return queries.get_level_names()


@app.get("/levels/{level_name}/")
async def get_level(level_name: str) -> models.Level:
    try:
        return queries.get_level(level_name)
    except queries.UnableToGetLevel as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/levels/{level_name}/{group_index}/")
async def get_level_group(level_name: str, group_index: int) -> models.Group:
    try:
        return queries.get_level_group(level_name, group_index)
    except (queries.UnableToGetLevel, queries.UnableToGetGroup) as e:
        raise HTTPException(status_code=404, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
