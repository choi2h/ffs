import logging
from django.contrib.auth.hashers import check_password

from apps.users.authentication import AuthenticationService
from apps.users.exceptions import UserNotFoundException, InvalidLoginException
from apps.users.models import ServiceUser
import apps.users.serializer as serializers

logger = logging.getLogger('django.logger')

def signup_user(serializer: serializers.SignupSerializer):
    return serializer.save()

def login_user(serializer: serializers.LoginUserSerializer):
    logger.debug("Login user. input={}".format(serializer.data['email']))

    try:
        user = ServiceUser.objects.get(email=serializer.data['email'])
    except ServiceUser.DoesNotExist:
        raise InvalidLoginException()

    if not check_password(serializer.data['password'], user.password):
        raise InvalidLoginException()

    return AuthenticationService.get_token(user)

def get_user_detail(user_id: int):
    try:
        user = ServiceUser.objects.get(id=user_id)
    except ServiceUser.DoesNotExist:
        raise UserNotFoundException()

    return serializers.UserDetailSerializer(user)
