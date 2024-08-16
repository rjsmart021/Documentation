from flask import request, jsonify
from schemas.employeeSchema import employee_schema, employees_schema
from services import employeeService
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        # Validate and deserialize the request data
        employee_data = employee_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Call the save service with the employee data
    employee_save = employeeService.save(employee_data)
    # Check to see that the employee_save is a employee and not None
    if employee_save is not None:
        # Serialize the employee data and return with a 201 success
        return employee_schema.jsonify(employee_save), 201
    else:
        return jsonify({"Message": "employee_save is None"}), 400
    
@cache.cached(timeout=20)
def find_all():
    employees = employeeService.find_all()
    return employees_schema.jsonify(employees), 200
    