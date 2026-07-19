from datetime import date

from fastmcp import FastMCP
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Expense


def register_expense_tools(mcp: FastMCP) -> None:
    @mcp.tool
    def add_expense(
        amount: float,
        category: str,
        description: str,
        expense_date: date,
    ) -> dict:
        with SessionLocal() as db:
            db: Session

            expense = Expense(
                amount=amount,
                category=category,
                description=description,
                expense_date=expense_date,
            )

            db.add(expense)
            db.commit()
            db.refresh(expense)

            return {
                "id": expense.id,
                "amount": float(expense.amount),
                "category": expense.category,
                "description": expense.description,
                "expense_date": expense.expense_date.isoformat(),
            }
        
    @mcp.tool
    def list_expenses() -> list[dict]:
        with SessionLocal() as db:
            expenses = db.query(Expense).order_by(Expense.expense_date.desc()).all()

            return [
                {
                    "id": expense.id,
                    "amount": float(expense.amount),
                    "category": expense.category,
                    "description": expense.description,
                    "expense_date": expense.expense_date.isoformat(),
                }
                for expense in expenses
            ]
        
    @mcp.tool
    def summarize_expenses() -> dict:
        with SessionLocal() as db:
            expenses = db.query(Expense).all()

            total = sum(float(expense.amount) for expense in expenses)

            category_summary = {}

            for expense in expenses:
                category = expense.category
                category_summary[category] = (
                    category_summary.get(category, 0)
                    + float(expense.amount)
                )

            return {
                "total_expenses": total,
                "total_transactions": len(expenses),
                "category_breakdown": category_summary,
            }
        
    @mcp.tool
    def edit_expense(
        expense_id: int,
        amount: float,
        category: str,
        description: str,
        expense_date: date,
    ) -> dict:
        with SessionLocal() as db:
            expense = (
                db.query(Expense)
                .filter(Expense.id == expense_id)
                .first()
            )

            if expense is None:
                return {"error": "Expense not found"}

            expense.amount = amount
            expense.category = category
            expense.description = description
            expense.expense_date = expense_date

            db.commit()
            db.refresh(expense)

            return {
                "message": "Expense updated successfully",
                "expense": {
                    "id": expense.id,
                    "amount": float(expense.amount),
                    "category": expense.category,
                    "description": expense.description,
                    "expense_date": expense.expense_date.isoformat(),
                },
            }
        
    @mcp.tool
    def delete_expense(expense_id: int) -> dict:
        with SessionLocal() as db:
            expense = (
                db.query(Expense)
                .filter(Expense.id == expense_id)
                .first()
            )

            if expense is None:
                return {"error": "Expense not found"}

            db.delete(expense)
            db.commit()

            return {
                "message": "Expense deleted successfully",
                "expense_id": expense_id,
            }