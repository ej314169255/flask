from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

from db import Session, User
from errors import HttpError
from schema import UserCreate, UserUpdate, validate

app = Flask("app")
bcrypt = Bcrypt(app)


def hash_password(password: str):
    password = password.encode()
    password = bcrypt.generate_password_hash(password)
    password = password.decode()
    return password


@app.before_request
def before_request():
    session = Session()
    request.session = session


@app.after_request
def after_request(response):
    request.session.close()
    return response


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    response = jsonify({"error": error.message})
    response.status_code = error.status_code
    return response


def get_user(user_id: int):
    user = request.session.get(User, user_id)
    if user is None:
        raise HttpError(404, "User not found")
    return user


def add_user(user: User):
    try:
        request.session.add(user)
        request.session.commit()
    except IntegrityError:
        raise HttpError(409, "User already exists")


class UserView(MethodView):

    @property
    def session(self):
        return request.session

    def get(self, user_id: int):
        user = get_user(user_id)
        return jsonify(user.dict())

    def post(self):
        json_data = validate(UserCreate, request.json)
        user = User(
            name=json_data["name"], password=hash_password(json_data["password"])
        )
        add_user(user)
        return jsonify(user.id_dict())

    def patch(self, user_id: int):
        json_data = validate(UserUpdate, request.json)
        user = get_user(user_id)
        if "name" in json_data:
            user.name = json_data["name"]
        if "password" in json_data:
            user.password = hash_password(json_data["password"])
        add_user(user)
        return jsonify(user.id_dict())

        pass

    def delete(self, user_id: int):
        user = get_user(user_id)
        self.session.delete(user)
        self.session.commit()
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
