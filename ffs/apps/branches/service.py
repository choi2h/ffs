from apps.branches.serializer import BranchSerializer
from apps.users.models import ServiceUser

from apps.branches.models import Branch


def addBranch(user_id: int, serializer: BranchSerializer):
    user = ServiceUser.objects.get(id=user_id)

    validated_data = serializer.validated_data
    validated_data['owner'] = user

    return Branch.objects.create(**validated_data)