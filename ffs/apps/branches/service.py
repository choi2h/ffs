from apps.branches.serializer import BranchSerializer
from apps.users.models import ServiceUser, Role, UserBranchMembership

from apps.branches.models import Branch
from apps.users.services import create_membership


def add_branch(user_id: int, serializer: BranchSerializer):
    user = ServiceUser.objects.get(id=user_id)
    validated_data = serializer.validated_data
    validated_data['owner'] = user
    branch = Branch.objects.create(**validated_data)
    create_membership(user, branch, Role.BRANCH_ADMIN)

    return branch