from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

# from models.order import Order
# from models.production import Production

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)

    # One-to-Many Relationship with Orders, Production
    orders: Mapped[List['Order']] = db.relationship(back_populates='product')
    production: Mapped[List['Production']] = db.relationship(back_populates='product')
    