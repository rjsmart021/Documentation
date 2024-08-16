from sqlalchemy.orm import Session
from database import db
from models.production import Production

# Creates new production
def save(production_data):
    with Session(db.engine) as session:
        with session.begin():
            new_production = Production(
                product_id=production_data['product_id'], 
                quantity_produced=production_data['quantity_produced'], 
                date_produced=production_data['date_produced'])
            session.add(new_production)
            session.commit()
        session.refresh(new_production)
        return new_production
    
    
# Get all productions in database
def find_all():
    query = db.select(Production)
    productions = db.session.execute(query).scalars().all()
    return productions