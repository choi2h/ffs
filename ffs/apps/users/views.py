from django.core.exceptions import BadRequest
from rest_framework import status
from rest_framework.response import Response

import apps.users.serializer as serializers

from rest_framework.generics import CreateAPIView, GenericAPIView, \
    RetrieveAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.users.exceptions import InvalidLoginException
from apps.users.models import ServiceUser, UserBranchMembership
from apps.users.services import signup_user, login_user, add_membership, get_memberships

""" POST 회원 가입 """
class UserSignupView(CreateAPIView):
    serializer_class = serializers.SignupSerializer
    permission_classes = []

    def perform_create(self, serializer):
        signup_user(serializer)

""" POST 로그인 """
class UserLoginView(GenericAPIView):
    serializer_class = serializers.LoginUserSerializer
    permission_classes = []

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = serializers.LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            token = login_user(serializer)
            return Response(token, status=status.HTTP_200_OK)
        except InvalidLoginException :
            raise BadRequest('아이디 혹은 비밀번호가 올바르지 않습니다.')


""" GET 회원 목록 조회"""
class UserListView(ListAPIView):
    queryset = ServiceUser.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = []

""" GET 단일 회원 조회"""
class UserDetailView(RetrieveAPIView):
    queryset = ServiceUser.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAuthenticated] # 인증된 유저만 호출
    authentication_classes = [JWTAuthentication]

""" 멤버십 """
class MembershipRegisterView(ListCreateAPIView):
    serializer_class = serializers.MembershipRegisterSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.MembershipRegisterSerializer
        elif self.request.method == 'GET':
            return serializers.MembershipBranchSerializer
        return None

    """ POST 멤버십 추가 """
    def perform_create(self, serializer):
        add_membership(serializer)

    """ GET 멤버십 조회 """
    def get(self, request, *args, **kwargs):
        user = request.user
        memberships = get_memberships(user)
        serializer = serializers.MembershipBranchSerializer(memberships, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


