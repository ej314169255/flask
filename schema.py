import pydantic

from errors import HttpError


class UserBase(pydantic.BaseModel):
    name: str
    password: str

    @pydantic.field_validator("password")
    @classmethod
    def secure_password(cls, v):
        if len(v) < 8:
            raise ValueError(f"Minimal length of password is 8")
        return v


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):

    name: str | None = None
    password: str | None = None


def validate(schema: type[UserCreate | UserUpdate], json_date: dict):
    try:
        schema_instance = schema(**json_date)
        return schema_instance.model_dump(exclude_none=True)
    except pydantic.ValidationError as err:
        errs = err.errors()
        for error in errs:
            error.pop("ctx", None)
        raise HttpError(400, errs)
