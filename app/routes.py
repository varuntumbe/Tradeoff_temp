from app import app, db
from flask import request
from app.models import db_table
from json import dumps


# first route for taking post data
@app.route("/", methods=["GET"])
def index():
    return "<h1>Hello !!</h1>"


# second route to recieve data
@app.route("/api", methods=["GET", "POST"])
def api():
    # one route hanles both get and post req
    if request.method == "GET":
        return "<h1>post your data</h1>"
    else:
        if request.is_json:
            json_data = request.get_json()
            # converting dict object to class object
            obj = db_table(
                id=json_data["id"],
                title=json_data["title"],
                descr=json_data["desc"],
                end=json_data["end"],
            )
            # # here i am stroing local obj to databse
            db.session.add(obj)
            db.session.commit()
        return "<h1>completed</h1>"


# Third route to fatch data from db
@app.route("/getdata/<id>")
def get_data(id):
    json_data = dict()
    obj = db_table.query.filter(db_table.id == id).first()
    print(obj)
    json_data["id"] = obj.id
    json_data["title"] = obj.title
    json_data["desc"] = obj.descr
    json_data["end"] = obj.end

    return dumps(json_data)
