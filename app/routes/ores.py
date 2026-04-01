from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.models.ore import SAMPLE_ORES

router = APIRouter(tags=["ores"])
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))


@router.get("/ores", response_class=HTMLResponse)
async def ores(request: Request):
    return templates.TemplateResponse(
        request,
        "ores.html",
        context={"ores": SAMPLE_ORES},
    )
