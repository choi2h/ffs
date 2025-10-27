from ninja import Schema
from datetime import date, datetime

from apps.users.models import ServiceUser


class UserTokenResponse(Schema):
    token: str


class UserDetailResponse(Schema):
    id: int
    name: str
    email: str
    gender: str
    birth: date
    phone: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attribute = True

    @classmethod
    def from_model(cls, user: ServiceUser):
        return cls.from_attribute(user)