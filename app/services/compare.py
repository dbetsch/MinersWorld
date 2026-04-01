from typing import List
from app.models.inventory import InventoryItem


def get_missing_items(inventory: List[InventoryItem]) -> List[InventoryItem]:
    return [item for item in inventory if item.missing > 0]


def get_sellable_items(inventory: List[InventoryItem]) -> List[InventoryItem]:
    return [item for item in inventory if item.is_sellable]


def compute_inventory_stats(inventory: List[InventoryItem]) -> dict:
    missing_items = get_missing_items(inventory)
    sellable_items = get_sellable_items(inventory)
    return {
        "total_ores": len(inventory),
        "missing_count": len(missing_items),
        "sellable_count": len(sellable_items),
        "missing_items": missing_items,
        "sellable_items": sellable_items,
    }
