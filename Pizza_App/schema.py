""" schema.py """

from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id : Optional[int]
    username : str
    email : str
    password : str
    is_staff : Optional[bool]
    is_active : Optional[bool]

    class config:
        orm_mode = True
        schema_extra = {
            'example' : {
                'username': "johndoe",
                'email': "johndoe@skiff.com",
                'password': "hunter2",
                'is_staff' : False,
                'is_active' : True
            }
        }
