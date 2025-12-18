from flask import Flask, jsonify, request
from flask.views import MethodView

from db import Session, User

app = Flask("app")


class UserView(MethodView):
    def get(self, user_id: int):
        with Session() as session:
            user = session.get(User, user_id)
            if user is None:
                http_response = jsonify({"error": "User not found"})
                http_response.status_code = 404
                return http_response
            return jsonify(user.dict())
        pass

    def post(self):
        json_data = request.json
        if "name" not in json_data or "password" not in json_data:
            http_response = jsonify({"error": "Bad request"})
            http_response.status_code = 400
            return http_response

        with Session() as session:
            user = User(name=json_data["name"], password=json_data["password"])
            session.add(user)
            session.commit()
            return jsonify(user.id_dict())

    def patch(self, user_id: int):
        json_data = request.json
        with Session() as session:
            user = session.get(User, user_id)
            if user is None:
                http_response = jsonify({"error": "User not found"})
                http_response.status_code = 404
                return http_response
            if "name" in json_data:
                user.name = json_data["name"]
            if "password" in json_data:
                user.password = json_data["password"]
            session.add(user)
            session.commit()
            return jsonify(user.id_dict())

        pass

    def delete(self, user_id: int):
        with Session() as session:
            user = session.get(User, user_id)
            if user is None:
                http_response = jsonify({"error": "User not found"})
                http_response.status_code = 404
                return http_response
            session.delete(user)
            session.commit()
            return jsonify({"status": "deleted"})


def hello_world(some_id: int):
    qs = request.args
    json_data = request.json
    headers = request.headers
    print(f"{qs=}")
    print(f"{json_data=}")
    print(f"{headers=}")
    response = jsonify({"message": "Hello, World!"})
    return response


user_view = UserView.as_view("users")
app.add_url_rule("/hello/world/<int:some_id>", view_func=hello_world, methods=["POST"])
app.add_url_rule(
    "/users/<int:user_id>", view_func=user_view, methods=["GET", "PATCH", "DELETE"]
)
app.add_url_rule("/users", view_func=user_view, methods=["POST"])

app.run()
