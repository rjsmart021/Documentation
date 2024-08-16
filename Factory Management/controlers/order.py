from flask import request, jsonify
from schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        # Validate and deserialize the request data
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Call the save service with the order data
    order_save = orderService.save(order_data)
    # Check to see that the order_save is a order and not None
    if order_save is not None:
        # Serialize the order data and return with a 201 success
        return order_schema.jsonify(order_save), 201
    else:
        return jsonify({"Message": "order_save is None"}), 400
    
# @cache.cached(timeout=20) # took this out for smoother testing
def find_all():
    # get pagination parameters (or set to default)
    args = request.args
    page = args.get('page', 1, type=int)
    per_page = args.get('per_page', 10, type=int)
    orders = orderService.find_all(page, per_page)
    return orders_schema.jsonify(orders), 200
    