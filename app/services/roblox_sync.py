# Placeholder for future Roblox inventory sync integration.
# When the Roblox Open Cloud / third-party API becomes available,
# replace the stub below with real HTTP calls.

from dataclasses import dataclass, field


@dataclass
class RobloxSyncConfig:
    enabled: bool = False
    api_base_url: str = ""


def fetch_inventory_by_username(username: str) -> dict:
    raise NotImplementedError(
        "Roblox sync is not yet implemented. "
        "Upload your inventory manually or wait for a future update."
    )


def get_sync_status() -> dict:
    return {
        "enabled": False,
        "message": (
            "Roblox sync is not yet available. "
            "This feature will be implemented in a future version."
        ),
    }
