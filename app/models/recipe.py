from typing import List
from pydantic import BaseModel

class RecipeIngredient(BaseModel):
    """A single ingredient line in a crafting recipe."""

    ore_id: int
    ore_name: str
    quantity: int

class Recipe(BaseModel):
    """A crafting recipe that turns ingredients into an output ore/item."""

    id: int
    output_ore_id: int
    output_ore_name: str
    output_quantity: int
    ingredients: List[RecipeIngredient]

SAMPLE_RECIPES: list[Recipe] = [
    Recipe(
        id=1,
        output_ore_id=2,
        output_ore_name="Iron Ingot",
        output_quantity=1,
        ingredients=[
            RecipeIngredient(ore_id=2, ore_name="Iron", quantity=5),
        ],
    ),
    Recipe(
        id=2,
        output_ore_id=3,
        output_ore_name="Gold Ingot",
        output_quantity=1,
        ingredients=[
            RecipeIngredient(ore_id=3, ore_name="Gold", quantity=3),
        ],
    ),
    Recipe(
        id=3,
        output_ore_id=2,
        output_ore_name="Steel",
        output_quantity=1,
        ingredients=[
            RecipeIngredient(ore_id=2, ore_name="Iron Ingot", quantity=3),
            RecipeIngredient(ore_id=1, ore_name="Coal",       quantity=2),
        ],
    ),
]
