import asyncio

from fastmcp import Client

from main import mcp


async def main() -> None:
    async with Client(mcp) as client:
        add_result = await client.call_tool(
            "add_expense",
            {
                "amount": 300,
                "category": "Food",
                "description": "Dinner",
                "expense_date": "2026-07-19",
            },
        )

        expense_id = add_result.data["id"]
        print("CREATED:", add_result.data)

        edit_result = await client.call_tool(
            "edit_expense",
            {
                "expense_id": expense_id,
                "amount": 350,
                "category": "Food",
                "description": "Dinner with dessert",
                "expense_date": "2026-07-19",
            },
        )
        print("EDITED:", edit_result.data)

        delete_result = await client.call_tool(
            "delete_expense",
            {
                "expense_id": expense_id,
            },
        )
        print("DELETED:", delete_result.data)


if __name__ == "__main__":
    asyncio.run(main())