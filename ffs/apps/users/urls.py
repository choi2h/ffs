from ninja import Router

from apps.users.authentication import authentication_service
from apps.users.exceptions import UserNotFoundException, InvalidLoginException
from apps.users.request import LoginUserRequest, JoinUserRequest
from apps.common.response import response, ObjectResponse, ErrorResponse, \
    error_response
from apps.users.response import UserTokenResponse, UserDetailResponse
from apps.users.services import signup_user, login_user, get_user_detail

router = Router(tags=["users"])

@router.post("/signup")
def signup_user_handler(request, body: JoinUserRequest):
    signup_user(body)
    return 200

@router.post("/login",
             response={
                 200: ObjectResponse[UserTokenResponse],
                 404: ObjectResponse[ErrorResponse],
             })
def login_user_handler(request, body: LoginUserRequest):
    try:
        user = login_user(body)
        token = authentication_service.encode_token(user.id)
    except InvalidLoginException as ex :
        return 404, error_response(msg=ex.message)

    return 200, response({"token": token})

@router.get("/{user_id}",
            response={
                200: ObjectResponse[UserDetailResponse],
                404: ObjectResponse[ErrorResponse],
            })
def user_detail_handler(request, user_id: int):
    try:
        user_detail = get_user_detail(user_id)
    except UserNotFoundException as ex :
        return 404, error_response(msg=ex.message)
    return 200, response(user_detail)
