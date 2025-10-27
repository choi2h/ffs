from ninja import Schema, ModelSchema

from apps.users.models import ServiceUser


class JoinUserRequest(ModelSchema):
    class Meta:
        model = ServiceUser
        fields = [
            'email',
            'name',
            'password',
            'birth',
            'gender',
            'phone',
        ]



class LoginUserRequest(Schema):
    email: str
    password: str