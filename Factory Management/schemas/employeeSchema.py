from marshmallow import fields
from schemas import ma


# Define the employee 
class EmployeeSchema(ma.Schema):
    id = fields.Integer(required=False) # id is autogenerated
    name = fields.String(required=True)
    position = fields.String(required=True)

    class Meta:
        fields = ("id", "name", "position")

# Create instances of the schema
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
