from production import db


class Employe(db.Model):
    """
    Customer Relation Model.
    Attributes are:
    1. Customer_id: integer and primary key. It will have auto increment
    2. Customer_name: string of max length 100 and null is not allowed
    3. Artist: string of max length 100 and null is not allowed
    4. Genre: string of max length 10 and null is not allowed
    """
    Customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Customer_name = db.Column(db.String(100), nullable=False)
    Artist = db.Column(db.String(100), nullable=False)
    Genre = db.Column(db.String(20), nullable=False)


class production(db.Model):
    """
        production Relation Model.
        Attributes are:
        1. production_id: integer and primary key. It will have auto increment
        2. production_name: string of max length 100 and null is not allowed
        3. production_price: float and null is not allowed
        4. stock_available: Integer and null is not allowed
        """
    production_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    production_name = db.Column(db.String(100), nullable=False)
    production_price = db.Column(db.Float, nullable=False)
    stock_available = db.Column(db.Integer, nullable=False)


class Orders(db.Model):
    """
    Order Relation.
    """
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    expected_date = db.Column(db.Date, nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('Employe.Customer_id'), nullable=False)


class OrderItem(db.Model):
    """
    Order Item relation.
    It refers to order and production table.
    It will have all the list of production for a particular order.
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    production_id = db.Column(db.Integer, db.ForeignKey('production.production_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
