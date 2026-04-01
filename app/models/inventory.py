from pydantic import BaseModel, computed_field

class InventoryItem(BaseModel):
    """An ore entry in the player's inventory.

    ``owned`` reflects the current count in-game; ``quantity`` mirrors
    ``owned`` when imported from a spreadsheet. ``required`` is the
    target amount needed for crafting or quest completion.
    """

    ore_id: int
    ore_name: str
    quantity: int
    required: int
    owned: int

    @computed_field
    @property
    def missing(self) -> int:
        return max(0, self.required - self.owned)

    @computed_field
    @property
    def surplus(self) -> int:
        return max(0, self.owned - self.required)

    @computed_field
    @property
    def is_sellable(self) -> bool:
        return self.surplus > 0

SAMPLE_INVENTORY: list[InventoryItem] = [
    InventoryItem(ore_id=1, ore_name="Coal",     quantity=80,  required=50,  owned=80),
    InventoryItem(ore_id=2, ore_name="Iron",     quantity=20,  required=40,  owned=20),
    InventoryItem(ore_id=3, ore_name="Gold",     quantity=15,  required=10,  owned=15),
    InventoryItem(ore_id=4, ore_name="Diamond",  quantity=3,   required=10,  owned=3),
    InventoryItem(ore_id=5, ore_name="Emerald",  quantity=5,   required=5,   owned=5),
    InventoryItem(ore_id=6, ore_name="Ruby",     quantity=0,   required=3,   owned=0),
    InventoryItem(ore_id=7, ore_name="Sapphire", quantity=2,   required=3,   owned=2),
    InventoryItem(ore_id=8, ore_name="Obsidian", quantity=1,   required=1,   owned=1),
]
