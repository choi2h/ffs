from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.branches.models import Branch
from apps.branches.serializer import BranchSerializer
from apps.branches.service import add_branch

""" 
POST 지점 등록
GET 지점 목록 조회
"""
class BranchListCreateView(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication, ]

    def perform_create(self, serializer):
        user_id = self.request.user.id
        add_branch(user_id, serializer)

""" GET 단일 지점 조회"""
class BranchDetailView(RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication, ]
