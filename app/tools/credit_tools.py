from datetime import date

from fastmcp import FastMCP

from app.database import SessionLocal
from app.models import Credit


def register_credit_tools(mcp: FastMCP) -> None:
    @mcp.tool
    def add_credit(
        amount: float,
        source: str,
        description: str,
        credit_date: date,
    ) -> dict:
        with SessionLocal() as db:
            credit = Credit(
                amount=amount,
                source=source,
                description=description,
                credit_date=credit_date,
            )

            db.add(credit)
            db.commit()
            db.refresh(credit)

            return {
                "id": credit.id,
                "amount": float(credit.amount),
                "source": credit.source,
                "description": credit.description,
                "credit_date": credit.credit_date.isoformat(),
            }