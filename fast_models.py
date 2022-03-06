from pydantic import BaseModel,Field,EmailStr
from typing import List

class Admin(BaseModel):

    id :int

    admin_name :str

    email :str

    password :str

    class Config:
        orm_mode = True


class Events(BaseModel):

    id :int

    event_name :str

    seat_count :int

    event_summary :str

    booking_status :str

    class Config:
        orm_mode = True

class Users(BaseModel):

    id :int

    user_name :str

    email :str

    password :str

    class Config:
        orm_mode = True


class UserEvents(BaseModel):

    id :int

    event_name :str

    user_id :int

    class Config:
        orm_mode = True


