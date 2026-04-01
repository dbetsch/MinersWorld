from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.routes import dashboard, ores, inventory, imports, settings

BASE_DIR = Path(__file__).parent

app = FastAPI(title="MinersWorld")

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

app.include_router(dashboard.router)
app.include_router(ores.router)
app.include_router(inventory.router)
app.include_router(imports.router)
app.include_router(settings.router)
