from typing import TypedDict, ClassVar

from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class JWTPayload(TypedDict):
    user_id: int
    exp: int

class AuthenticationService:
    JWT_SECRET_KEY: ClassVar[str] = settings.SECRET_KEY
    JWT_ALGORITHM: ClassVar[str] = "HS256"

    @staticmethod
    def get_token(user):
        token = TokenObtainPairSerializer.get_token(user)
        refresh = str(token)
        access = str(token.access_token)
        return {
            "access_token": access,
            "refresh_token": refresh,
        }