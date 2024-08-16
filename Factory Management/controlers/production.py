from flask import request, jsonify
from schemas.productionSchema import production_schema, productions_schema
from services import productionService
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        # Validate and deserialize the request data
        production_data = production_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Call the save service with the production data
    production_save = productionService.save(production_data)
    # Check to see that the production_save is a production and not None
    if production_save is not None:
        # Serialize the production data and return with a 201 success
        return production_schema.jsonify(production_save), 201
    else:
        return jsonify({"Message": "production_save is None"}), 400
    
@cache.cached(timeout=20)
def find_all():
    productions = productionService.find_all()
    return productions_schema.jsonify(productions), 200
    