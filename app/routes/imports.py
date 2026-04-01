from pathlib import Path

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.services.importers import import_csv, import_xlsx, parse_inventory_import

router = APIRouter(tags=["imports"])
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))


@router.get("/imports", response_class=HTMLResponse)
async def imports_page(request: Request):
    return templates.TemplateResponse(request, "imports.html", context={})


@router.post("/imports/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    try:
        content = await file.read()
        filename = file.filename or ""
        if filename.endswith(".xlsx"):
            rows = import_xlsx(content)
        else:
            rows = import_csv(content)
        items = parse_inventory_import(rows)
        return templates.TemplateResponse(
            request,
            "imports.html",
            context={
                "message": f"Successfully imported {len(items)} inventory items.",
                "items": items,
            },
        )
    except Exception as exc:
        return templates.TemplateResponse(
            request,
            "imports.html",
            context={"error": str(exc)},
            status_code=400,
        )
