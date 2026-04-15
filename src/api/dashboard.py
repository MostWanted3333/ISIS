
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates



router =APIRouter()

templates = Jinja2Templates(directory="src/templates")

@router.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"request": request}
    )