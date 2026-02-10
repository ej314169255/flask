import pydantic

from errors import HttpError


class AdvBase(pydantic.BaseModel):
    title: str
    descr: str
    owner: str
    

    @pydantic.field_validator("descr")
    @classmethod
    def contain_description(cls, v):
        if len(v) < 16:
            raise ValueError(f"Minimal length of description is 16")
        return v


class AdvCreate(AdvBase):
    title: str
    descr: str
    owner: str


class AdvUpdate(AdvBase):

    title: str
    descr: str
    owner: str


def validate(schema: type[AdvCreate | AdvUpdate], json_date: dict):
    try:
        schema_instance = schema(**json_date)
        return schema_instance.model_dump(exclude_none=True)
    except pydantic.ValidationError as err:
        errs = err.errors()
        for error in errs:
            error.pop("ctx", None)
        raise HttpError(400, errs)
