from flask import jsonify, request

from production import app
from production.models import customer
from production import db
from production.schemas import CustomerSchema

Customer_schema = CustomerSchema()


@app.route('/customer', methods=['POST'])
def add_Customer():
    """
    Add customer . Example POST data format
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
        # Check if the customer already exists based on Artist_name or Record_lable
        existing_Customer = customer.query.filter(
            (customer.Artist_name == Artist_name) | (customer.Genre == Genre)
        ).first()

        if existing_Customer:
            return jsonify({"message": f"customer already existed"})
        Song = Song(Song_name=data["Song_name"], Artist_name=data["Artist_name"],
                            Genre=data["Genre"])

        # Add the new customer to the database
        db.session.add(customer)
        db.session.commit()

        return jsonify({"message": "customer added successfully"})
    except Exception as e:
        return jsonify({"Error": f"customer not added. Error {e}"})


@app.route('/customer/<int:Song_id>', methods=['GET'])
def get_Song(Song_id):
    """
    Get customer data based on ID provided
    :param Customer_id: ID of the registered Song.
    :return: Song details oif found else Error message
    """
    try:
        Song = customer.query.get(Customer_id)

        if customer:
            Customer_data = {
                "Customer_id": customer.Customer_id,
                "Customer_name": customer.Customer_name,
                "Artist": Artist.Artist_Name,
                "Record_lable": customer.Record_lable
            }
            return jsonify(Customer_data)
        else:
            return jsonify({"message": "customer not found"})

    except Exception as e:
        print(f"Error in getting customer. Error Message: {e}")
        return jsonify(
            {"message": f"Error while fetching customer with ID: {Customer_id}. Error: {e}"})


@app.route('/customer/<int:Customer_id>', methods=['PUT'])
def update_user(Customer_id):
    """
    Update the customer details.
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
        customer = customer.query.get(Customer_id)

        if customer:
            data = request.get_json()
            error = Customer_schema.validate(data)
            if error:
                return jsonify(error), 400
            customer.Customer_name = data.get('Customer_name', customer.Customer_name)
            customer.Artist_Name = data.get('Artist', Artist.Artist_Name)
            customer.Genre = data.get('phone_number', Genre.Genre_Name)

            db.session.commit()
            return jsonify({"message": "customer updated successfully"})
        else:
            return jsonify({"message": "customer Not Found!!!"})
    except Exception as e:
        return jsonify({"message": f"error in updating customer. Error: {e}"})


@app.route('/customer/<int:Customer_id>', methods=['DELETE'])
def delete_user(Customer_id):
    """
    Delete user based on the ID provided
    :param Customer_id: ID of the customer to delete
    :return: success message if user deleted successfully else None
    """

    try:
        customer = customer.query.get(Customer_id)

        if customer:
            # Delete the customer from the database
            db.session.delete(customer)
            db.session.commit()
            return jsonify({"message": "customer deleted successfully"})
        else:
            return jsonify({"message": "customer not found"})

    except Exception as e:
        return jsonify({"message": f"error in deleting customer. Error: {e}"})
