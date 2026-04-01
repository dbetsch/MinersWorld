from typing import Optional
from pydantic import BaseModel

class Ore(BaseModel):
    id: int
    name: str
    rarity: str
    tier: int
    value: float
    source: str
    image_url: Optional[str] = None

SAMPLE_ORES: list[Ore] = [
    Ore(id=1, name="Coal",     rarity="Common",    tier=1, value=1.0,   source="Underground"),
    Ore(id=2, name="Iron",     rarity="Common",    tier=1, value=3.0,   source="Underground"),
    Ore(id=3, name="Gold",     rarity="Uncommon",  tier=2, value=10.0,  source="Deep Mines"),
    Ore(id=4, name="Diamond",  rarity="Rare",      tier=3, value=50.0,  source="Deep Mines"),
    Ore(id=5, name="Emerald",  rarity="Rare",      tier=3, value=45.0,  source="Jungle Caves"),
    Ore(id=6, name="Ruby",     rarity="Epic",      tier=4, value=120.0, source="Volcanic Depths"),
    Ore(id=7, name="Sapphire", rarity="Epic",      tier=4, value=115.0, source="Glacier Caves"),
    Ore(id=8, name="Obsidian", rarity="Legendary", tier=5, value=500.0, source="The Void"),
]
