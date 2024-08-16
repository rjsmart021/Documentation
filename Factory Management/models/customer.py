from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

# from models.order import Order

class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    email: Mapped[str] = mapped_column(db.String(100), nullable=False)
    phone: Mapped[str] = mapped_column(db.String(20), nullable=False)

    # One-to-Many Relationship with Orders
    orders: Mapped[List['Order']] = db.relationship(back_populates='customer')