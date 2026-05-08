from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import uvicorn

from src.api.init import main_router


app = FastAPI()
app.include_router(main_router)


templates = Jinja2Templates(directory="src/templates")

@app.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={"request": request}
)

if __name__== "__main__":
    uvicorn.run("main:app" ,reload=True)

