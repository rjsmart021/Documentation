from flask import jsonify, request

from production import app
from production.models import Customer
from production import db
from production.schemas import CustomerSchema

Customer_schema = CustomerSchema()


@app.route('/Customer', methods=['POST'])
def add_Customer():
    """
    Add Customer . Example POST data format
    {
    "Customer_name": "abc",
    "Artst_name": "abc",
    :Genre": "abd"
    }
    :return: success or error message
    """
    try:
        data = request.get_json()
        errors = Customer_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        Artist_name = data.get("Artist_name")
        Genre = data.get("Genre")
        # Check if the Customer already exists based on Artist_name or Record_lable
        existing_Customer = Customer.query.filter(
            (Customer.Artist_name == Artist_name) | (Customer.Genre == Genre)
        ).first()

        if existing_Customer:
            return jsonify({"message": f"Customer already existed"})
        Song = Song(Song_name=data["Song_name"], Artist_name=data["Artist_name"],
                            Genre=data["Genre"])

        # Add the new customer to the database
        db.session.add(Customer)
        db.session.commit()

        return jsonify({"message": "Customer added successfully"})
    except Exception as e:
        return jsonify({"Error": f"Customer not added. Error {e}"})


@app.route('/Customer/<int:Song_id>', methods=['GET'])
def get_Song(Song_id):
    """
    Get Customer data based on ID provided
    :param Customer_id: ID of the registered Song.
    :return: Song details oif found else Error message
    """
    try:
        Song = Customer.query.get(Customer_id)

        if Customer:
            Customer_data = {
                "Customer_id": Customer.Customer_id,
                "Customer_name": Customer.Customer_name,
                "Artist": Artist.Artist_Name,
                "Record_lable": Customer.Record_lable
            }
            return jsonify(Customer_data)
        else:
            return jsonify({"message": "Customer not found"})

    except Exception as e:
        print(f"Error in getting Customer. Error Message: {e}")
        return jsonify(
            {"message": f"Error while fetching Customer with ID: {Customer_id}. Error: {e}"})


@app.route('/Customer/<int:Customer_id>', methods=['PUT'])
def update_user(Customer_id):
    """
    Update the Customer details.
    example PUT data to update;
    {
    "Customer_name": "name",
    "Artist": "Artist_Name",
    "Genre": "Genre_Name"
    }
    :param Customer_id:
    :return:
    """
    try:
        Customer = Customer.query.get(Customer_id)

        if Customer:
            data = request.get_json()
            error = Customer_schema.validate(data)
            if error:
                return jsonify(error), 400
            Customer.Customer_name = data.get('Customer_name', Customer.Customer_name)
            Customer.Artist_Name = data.get('Artist', Artist.Artist_Name)
            Customer.Genre = data.get('phone_number', Genre.Genre_Name)

            db.session.commit()
            return jsonify({"message": "Customer updated successfully"})
        else:
            return jsonify({"message": "Customer Not Found!!!"})
    except Exception as e:
        return jsonify({"message": f"error in updating Customer. Error: {e}"})


@app.route('/Customer/<int:Customer_id>', methods=['DELETE'])
def delete_user(Customer_id):
    """
    Delete user based on the ID provided
    :param Customer_id: ID of the Customer to delete
    :return: success message if user deleted successfully else None
    """

    try:
        Customer = Customer.query.get(Customer_id)

        if Customer:
            # Delete the Customer from the database
            db.session.delete(Customer)
            db.session.commit()
            return jsonify({"message": "Customer deleted successfully"})
        else:
            return jsonify({"message": "Customer not found"})

    except Exception as e:
        return jsonify({"message": f"error in deleting Customer. Error: {e}"})
