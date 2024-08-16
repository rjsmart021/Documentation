from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

# from models.customer import Customer
# from models.product import Product

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.ForeignKey('products.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    total_price: Mapped[float] = mapped_column(db.Float, nullable=False)

    # Many-to-One Relationship with Customers, Products
    customer: Mapped['Customer'] = db.relationship(back_populates='orders')
    product: Mapped['Product'] = db.relationship(back_populates='orders')