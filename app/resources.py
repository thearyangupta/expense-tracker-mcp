import json
from pathlib import Path

from fastmcp import FastMCP


def register_resources(mcp: FastMCP) -> None:
    @mcp.resource("expense://categories")
    def expense_categories() -> dict:
        categories_file = Path("categories.json")

        with categories_file.open("r", encoding="utf-8") as file:
            return json.load(file)