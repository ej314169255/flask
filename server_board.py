from flask import Flask, jsonify, request
from flask.views import MethodView
from db import Session, Adv
from errors import HttpError
from schema import AdvCreate, AdvUpdate, validate

app = Flask("app")

@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    response = jsonify({"error": error.message})
    response.status_code = error.status_code
    return response


class AdvView(MethodView):
    def get(self, record_id: int):
        with Session() as session:
            record = session.get(Adv, record_id)
            if record is None:
                raise HttpError(404, "Record not found")
            return jsonify(record.dict())
        pass

    def post(self):
        json_data = validate(AdvCreate, request.json)

        with Session() as session:
            record = Adv(title=json_data["title"], descr=json_data["descr"],\
            owner=json_data["owner"])

            try:
                session.add(record)
                session.commit()
            except IntegrityError:
                raise HttpError(409, "User already exists")
            

            result = jsonify(record.dict() | {"message": "record created successfully"})
            result.status_code = 201
            return result
        pass


    def patch(self, record_id: int):

        json_data = validate(AdvUpdate, request.json)

        with Session() as session:
            record = session.get(Adv, record_id)
            if record is None:
                raise HttpError(404, "Record not found")

            if "owner" in json_data:
                record.onwer = json_data["owner"]
            if "title" in json_data:
                record.title = json_data["title"]
            if "descr" in json_data:
                record.descr = json_data["descr"]

            try:
                session.add(record)
                session.commit()
            except IntegrityError:
                raise HttpError(400, "Bad request")

            result = jsonify(record.id_dict() | {"message": "record edited successfully"})
            result.status_code = 200
            return result
        pass

    def delete(self, record_id: int):
        with Session() as session:
            record = session.get(Adv, record_id)

            if record is None:
                raise HttpError(404, "Record not found")
            result = jsonify(record.id_dict() | {"message": "deleted"})
            result.status_code = 200
            session.delete(record)
            session.commit()            
            return result

        pass



adv_view = AdvView.as_view("records")
app.add_url_rule("/records/<int:record_id>", view_func=adv_view, methods=["GET", "PATCH", "DELETE"])
app.add_url_rule("/records", view_func=adv_view, methods=["POST"])

app.run()
