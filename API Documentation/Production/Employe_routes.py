from flask import jsonify, request

from production import app
from production.models import Employe
from production import db
from production.schemas import EmployeSchema

Employe_schema = EmployeSchema()


@app.route('/Employe', methods=['POST'])
def add_Employe():
    """
    Add Employe . Example POST data format
    {
    "Employe_name": "abc",
    "Artst_name": "abc",
    :Genre": "abd"
    }
    :return: success or error message
    """
    try:
        data = request.get_json()
        errors = Employe_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        Artist_name = data.get("Artist_name")
        Genre = data.get("Genre")
        # Check if the Employe already exists based on Artist_name or Record_lable
        existing_Employe = Employe.query.filter(
            (Employe.Artist_name == Artist_name) | (Employe.Genre == Genre)
        ).first()

        if existing_Employe:
            return jsonify({"message": f"Employe already existed"})
        Song = Song(Song_name=data["Song_name"], Artist_name=data["Artist_name"],
                            Genre=data["Genre"])

        # Add the new customer to the database
        db.session.add(Employe)
        db.session.commit()

        return jsonify({"message": "Employe added successfully"})
    except Exception as e:
        return jsonify({"Error": f"Employe not added. Error {e}"})


@app.route('/Employe/<int:Song_id>', methods=['GET'])
def get_Song(Song_id):
    """
    Get Employe data based on ID provided
    :param Employe_id: ID of the registered Song.
    :return: Song details oif found else Error message
    """
    try:
        Song = Employe.query.get(Employe_id)

        if Employe:
            Employe_data = {
                "Employe_id": Employe.Employe_id,
                "Employe_name": Employe.Employe_name,
                "Artist": Artist.Artist_Name,
                "Record_lable": Employe.Record_lable
            }
            return jsonify(Employe_data)
        else:
            return jsonify({"message": "Employe not found"})

    except Exception as e:
        print(f"Error in getting Employe. Error Message: {e}")
        return jsonify(
            {"message": f"Error while fetching Employe with ID: {Employe_id}. Error: {e}"})


@app.route('/Employe/<int:Employe_id>', methods=['PUT'])
def update_user(Employe_id):
    """
    Update the Employe details.
    example PUT data to update;
    {
    "Employe_name": "name",
    "Artist": "Artist_Name",
    "Genre": "Genre_Name"
    }
    :param Employe_id:
    :return:
    """
    try:
        Employe = Employe.query.get(Employe_id)

        if Employe:
            data = request.get_json()
            error = Employe_schema.validate(data)
            if error:
                return jsonify(error), 400
            Employe.Employe_name = data.get('Employe_name', Employe.Employe_name)
            Employe.Artist_Name = data.get('Artist', Artist.Artist_Name)
            Employe.Genre = data.get('phone_number', Genre.Genre_Name)

            db.session.commit()
            return jsonify({"message": "Employe updated successfully"})
        else:
            return jsonify({"message": "Employe Not Found!!!"})
    except Exception as e:
        return jsonify({"message": f"error in updating Employe. Error: {e}"})


@app.route('/Employe/<int:Employe_id>', methods=['DELETE'])
def delete_user(Employe_id):
    """
    Delete user based on the ID provided
    :param Employe_id: ID of the Employe to delete
    :return: success message if user deleted successfully else None
    """

    try:
        Employe = Employe.query.get(Employe_id)

        if Employe:
            # Delete the Employe from the database
            db.session.delete(Employe)
            db.session.commit()
            return jsonify({"message": "Employe deleted successfully"})
        else:
            return jsonify({"message": "Employe not found"})

    except Exception as e:
        return jsonify({"message": f"error in deleting Employe. Error: {e}"})
