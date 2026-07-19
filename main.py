from fastmcp import FastMCP

from app.database import Base, engine
from app.tools.credit_tools import register_credit_tools
from app.tools.expense_tools import register_expense_tools


Base.metadata.create_all(bind=engine)

mcp = FastMCP("Expense Tracker MCP")

register_expense_tools(mcp)
register_credit_tools(mcp)


if __name__ == "__main__":
    mcp.run()