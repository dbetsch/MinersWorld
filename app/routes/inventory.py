from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.models.inventory import SAMPLE_INVENTORY
from app.services.compare import get_missing_items, get_sellable_items

router = APIRouter(tags=["inventory"])
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))


@router.get("/inventory", response_class=HTMLResponse)
async def inventory(request: Request):
    return templates.TemplateResponse(
        request,
        "inventory.html",
        context={
            "inventory": SAMPLE_INVENTORY,
            "missing_items": get_missing_items(SAMPLE_INVENTORY),
            "sellable_items": get_sellable_items(SAMPLE_INVENTORY),
        },
    )
