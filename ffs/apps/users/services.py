import logging

from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import ValidationError

from apps.branches.models import Branch
from apps.users.authentication import AuthenticationService
from apps.users.exceptions import UserNotFoundException, InvalidLoginException
from apps.users.models import ServiceUser, UserBranchMembership, Role
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

def add_membership(serializer: serializers.MembershipRegisterSerializer):
    user_id = int(serializer.data['user_id'])
    branch_id = int(serializer.data['branch_id'])

    if UserBranchMembership.objects.get(user_id=user_id, branch_id=branch_id):
        raise ValidationError('이미 존재하는 멤버십 정보가 있습니다.')

    try:
        user = ServiceUser.objects.get(id=user_id)
    except ServiceUser.DoesNotExist:
        raise UserNotFoundException()

    try:
        branch = Branch.objects.get(id=branch_id)
    except Branch.DoesNotExist:
        raise ValidationError('지점 정보를 찾을 수 없습니다')

    return create_membership(user, branch, serializer.data['role'])

def create_membership(user: ServiceUser, branch: Branch, role: Role):
    return UserBranchMembership.objects.create(
        user=user,
        branch=branch,
        role=role,
    )


def get_memberships(user: ServiceUser):
    try:
        memberships = UserBranchMembership.objects.filter(user=user)
    except UserBranchMembership.DoesNotExist:
        return []

    return memberships