from pydantic import BaseModel, parse_obj_as


class UserModel(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
