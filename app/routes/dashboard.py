from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.models.inventory import SAMPLE_INVENTORY
from app.models.ore import SAMPLE_ORES
from app.services.compare import compute_inventory_stats

router = APIRouter(tags=["dashboard"])
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))


@router.get("/dashboard", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    stats = compute_inventory_stats(SAMPLE_INVENTORY)
    return templates.TemplateResponse(
        request,
        "dashboard.html",
        context={"stats": stats, "ore_count": len(SAMPLE_ORES)},
    )
