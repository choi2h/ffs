from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.branches.models import Branch
from apps.branches.serializer import BranchSerializer
from apps.branches.service import addBranch

class BranchListCreateView(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication, ]

    def perform_create(self, serializer):
        user_id = self.request.user.id
        addBranch(user_id, serializer)

class DetailBranchView(RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication, ]


