# MinersWorld — Roblox Miner's World Community Tracker

A web-based community tracker for the Roblox game **Miner's World**. Track your ores, manage your inventory, plan crafting recipes, identify missing items, and spot surplus resources you can sell.

---

## Features

- **Ore List Viewer** — Browse all available ores with rarity, tier, value, and source information.
- **Inventory Tracker** — See what you own vs. what you need; instantly identify missing items and surplus stock.
- **Crafting / Recipe Support** — View crafting recipes and the ingredients required.
- **Missing Items** — At-a-glance list of ores you still need to collect.
- **Surplus / Sellable** — Know exactly which ores you have in excess and can sell or trade.
- **CSV / XLSX Import** — Upload your ore list or inventory from a spreadsheet.
- **Roblox Sync (placeholder)** — Future feature to sync inventory directly from your Roblox account.

---

## Setup

**Requirements:** Python 3.10+

```bash
# 1. Clone the repository
git clone https://github.com/your-org/MinersWorld.git
cd MinersWorld

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate.bat       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the development server
uvicorn app.main:app --reload

# 5. Open your browser
#    http://127.0.0.1:8000
```

---

## Project Structure

```
MinersWorld/
├─ app/
│  ├─ main.py            # FastAPI application entry point
│  ├─ routes/            # Page routers (dashboard, ores, inventory, imports, settings)
│  ├─ models/            # Pydantic data models (Ore, InventoryItem, Recipe)
│  ├─ services/          # Business logic (compare, importers, roblox_sync)
│  ├─ templates/         # Jinja2 HTML templates (Bootstrap 5)
│  └─ static/            # CSS and static assets
├─ data/
│  ├─ sample_ores.csv        # Sample ore data for import testing
│  └─ sample_inventory.csv   # Sample inventory data for import testing
├─ tests/
│  └─ test_main.py       # pytest test suite
└─ requirements.txt
```

---

## Running Tests

```bash
python -m pytest tests/ -v
```

---

## Roblox Sync (Future)

The **Settings** page contains a placeholder for Roblox account sync. Once a stable Roblox inventory API (e.g. Open Cloud) is available, this will allow players to automatically pull their in-game inventory without manual uploads. Until then, use the CSV/XLSX import feature.
