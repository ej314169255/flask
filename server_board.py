from flask import Flask, jsonify, request
from flask.views import MethodView

from db import Session, Adv

app = Flask("app")


class AdvView(MethodView):
    def get(self, record_id: int):
        with Session() as session:
            record = session.get(Adv, record_id)
            if record is None:
                http_response = jsonify({"error": "Record not found"})
                http_response.status_code = 404
                return http_response
            return jsonify(record.dict())
        pass

    def post(self):
        json_data = request.json
        if "title" not in json_data or "descr" not in json_data\
            or "owner" not in json_data:
            http_response = jsonify({"error": "Bad request"})
            http_response.status_code = 400
            return http_response

        with Session() as session:
            record = Adv(title=json_data["title"], descr=json_data["descr"],\
            owner=json_data["owner"], status=json_data["status"])
            session.add(record)
            session.commit()
            return jsonify(record.id_dict())

    def patch(self, record_id: int):
        json_data = request.json
        with Session() as session:
            record = session.get(Adv, record_id)
            if record is None:
                http_response = jsonify({"error": "User not found"})
                http_response.status_code = 404
                return http_response
            if "title" in json_data:
                record.title = json_data["title"]
            if "descr" in json_data:
                record.descr = json_data["descr"]
            session.add(record)
            session.commit()
            return jsonify(record.id_dict())

        pass

    def delete(self, record_id: int):
        with Session() as session:
            record = session.get(Adv, record_id)
            if record is None:
                http_response = jsonify({"error": "Record not found"})
                http_response.status_code = 404
                return http_response
            record.status = "deleted"
            session.add(record)
            #session.delete(record)
            session.commit()
            return jsonify({"status": "deleted"})



adv_view = AdvView.as_view("records")
app.add_url_rule(
    "/records/<int:record_id>", view_func=adv_view, methods=["GET", "PATCH", "DELETE"]
)
app.add_url_rule("/records", view_func=adv_view, methods=["POST"])

app.run()
