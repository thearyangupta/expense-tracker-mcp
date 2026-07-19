# Expense Tracker MCP Server

A local MCP (Model Context Protocol) server built with **FastMCP** and **PostgreSQL**.

This project exposes expense management tools that can be used by MCP clients such as Claude Desktop.

## Features

- ➕ Add Expense
- 📋 List Expenses
- 📊 Summarize Expenses
- ✏️ Edit Expense
- 🗑️ Delete Expense
- 💰 Add Credit
- 📂 Expense Categories Resource

## Tech Stack

- Python
- FastMCP
- PostgreSQL
- SQLAlchemy
- Psycopg 3
- Pydantic Settings
- UV

## Project Structure

```text
expense-tracker-mcp/
│
├── app/
│   ├── tools/
│   │   ├── expense_tools.py
│   │   └── credit_tools.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   └── resources.py
│
├── categories.json
├── main.py
├── .env.example
├── pyproject.toml
└── README.md
```

## MCP Tools

| Tool | Description |
|------|-------------|
| `add_expense` | Add a new expense |
| `list_expenses` | List all expenses |
| `summarize_expenses` | Show expense summary |
| `edit_expense` | Update an existing expense |
| `delete_expense` | Delete an expense |
| `add_credit` | Add income/credit |

## MCP Resource

```
expense://categories
```

Returns the predefined expense categories.

## Setup

Clone the repository:

```bash
git clone https://github.com/thearyangupta/expense-tracker-mcp.git
cd expense-tracker-mcp
```

Install dependencies:

```bash
uv sync
```

Create a `.env` file:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/expense_tracker
```

Run the server:

```bash
uv run python main.py
```

## Example Prompts

```
Add a Food expense of ₹250 for Lunch.

Show all expenses.

Summarize my expenses.

Update expense 3.

Delete expense 5.

Add a credit of ₹20,000 from Freelancing.
```

## Future Improvements

- Expense filtering
- Monthly reports
- Export to CSV
- Budget tracking
- AI-powered expense insights

---

Built using FastMCP and PostgreSQL.