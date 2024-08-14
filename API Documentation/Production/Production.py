from flask import jsonify, request

from production import app
from production.models import Production
from production import db
from production.schemas import ProductionSchema

Production_schema = ProductionSchema()


@app.route('/Production', methods=['POST'])
def add_Production():
    """
    Add Production . Example POST data format
    {
    "Production_name": "abc",
    "Artst_name": "abc",
    :Genre": "abd"
    }
    :return: success or error message
    """
    try:
        data = request.get_json()
        errors = Production_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        Artist_name = data.get("Artist_name")
        Genre = data.get("Genre")
        # Check if the Production already exists based on Artist_name or Record_lable
        existing_Production = Production.query.filter(
            (Production.Artist_name == Artist_name) | (Production.Genre == Genre)
        ).first()

        if existing_Production:
            return jsonify({"message": f"Production already existed"})
        Song = Song(Song_name=data["Song_name"], Artist_name=data["Artist_name"],
                            Genre=data["Genre"])

        # Add the new customer to the database
        db.session.add(Production)
        db.session.commit()

        return jsonify({"message": "Production added successfully"})
    except Exception as e:
        return jsonify({"Error": f"Production not added. Error {e}"})


@app.route('/Production/<int:Song_id>', methods=['GET'])
def get_Song(Song_id):
    """
    Get Production data based on ID provided
    :param Production_id: ID of the registered Song.
    :return: Song details oif found else Error message
    """
    try:
        Song = Production.query.get(Production_id)

        if Production:
            Production_data = {
                "Production_id": Production.Production_id,
                "Production_name": Production.Production_name,
                "Artist": Artist.Artist_Name,
                "Record_lable": Production.Record_lable
            }
            return jsonify(Production_data)
        else:
            return jsonify({"message": "Production not found"})

    except Exception as e:
        print(f"Error in getting Production. Error Message: {e}")
        return jsonify(
            {"message": f"Error while fetching Production with ID: {Production_id}. Error: {e}"})


@app.route('/Production/<int:Production_id>', methods=['PUT'])
def update_user(Production_id):
    """
    Update the Production details.
    example PUT data to update;
    {
    "Production_name": "name",
    "Artist": "Artist_Name",
    "Genre": "Genre_Name"
    }
    :param Production_id:
    :return:
    """
    try:
        Production = Production.query.get(Production_id)

        if Production:
            data = request.get_json()
            error = Production_schema.validate(data)
            if error:
                return jsonify(error), 400
            Production.Production_name = data.get('Production_name', Production.Production_name)
            Production.Artist_Name = data.get('Artist', Artist.Artist_Name)
            Production.Genre = data.get('phone_number', Genre.Genre_Name)

            db.session.commit()
            return jsonify({"message": "Production updated successfully"})
        else:
            return jsonify({"message": "Production Not Found!!!"})
    except Exception as e:
        return jsonify({"message": f"error in updating Production. Error: {e}"})


@app.route('/Production/<int:Production_id>', methods=['DELETE'])
def delete_user(Production_id):
    """
    Delete user based on the ID provided
    :param Production_id: ID of the Production to delete
    :return: success message if user deleted successfully else None
    """

    try:
        Production = Production.query.get(Production_id)

        if Production:
            # Delete the Production from the database
            db.session.delete(Production)
            db.session.commit()
            return jsonify({"message": "Production deleted successfully"})
        else:
            return jsonify({"message": "Production not found"})

    except Exception as e:
        return jsonify({"message": f"error in deleting Production. Error: {e}"})
