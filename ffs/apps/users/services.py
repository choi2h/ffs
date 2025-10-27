from django.contrib.auth import authenticate

from apps.users.exceptions import UserNotFoundException, InvalidLoginException
from apps.users.request import JoinUserRequest, LoginUserRequest

from apps.users.models import ServiceUser
from apps.users.response import UserDetailResponse


def signup_user(request: JoinUserRequest):
    user = ServiceUser.objects.create_user(
        name=request.name,
        email=request.email,
        password=request.password,
        birth=request.birth,
        gender=request.gender,
        phone=request.phone,
    )

    user.save()
    return user

def login_user(request: LoginUserRequest):
    user = authenticate(email=request.email, password=request.password)

    if user is None:
        raise InvalidLoginException()

    return user

def get_user_detail(user_id: int):
    try:
        user = ServiceUser.objects.get(id=user_id)
    except ServiceUser.DoesNotExist:
        raise UserNotFoundException("회원 정보를 찾을 수 없습니다.")

    return UserDetailResponse.from_orm(user)
