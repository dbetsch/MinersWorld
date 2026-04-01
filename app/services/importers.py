from __future__ import annotations

import io
from typing import List

import pandas as pd

from app.models.ore import Ore
from app.models.inventory import InventoryItem


def import_csv(file_content: bytes) -> List[dict]:
    df = pd.read_csv(io.BytesIO(file_content))
    return df.where(pd.notna(df), None).to_dict(orient="records")


def import_xlsx(file_content: bytes) -> List[dict]:
    df = pd.read_excel(io.BytesIO(file_content), engine="openpyxl")
    return df.where(pd.notna(df), None).to_dict(orient="records")


def parse_ore_import(rows: List[dict]) -> List[Ore]:
    ores: List[Ore] = []
    for row in rows:
        ores.append(
            Ore(
                id=int(row.get("id", 0)),
                name=str(row.get("name", "")),
                rarity=str(row.get("rarity", "Common")),
                tier=int(row.get("tier", 1)),
                value=float(row.get("value", 0.0)),
                source=str(row.get("source", "")),
                image_url=row.get("image_url"),
            )
        )
    return ores


def parse_inventory_import(rows: List[dict]) -> List[InventoryItem]:
    items: List[InventoryItem] = []
    for row in rows:
        owned = int(row.get("owned", row.get("quantity", 0)))
        items.append(
            InventoryItem(
                ore_id=int(row.get("ore_id", 0)),
                ore_name=str(row.get("ore_name", "")),
                quantity=int(row.get("quantity", owned)),
                required=int(row.get("required", 0)),
                owned=owned,
            )
        )
    return items
