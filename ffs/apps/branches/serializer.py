from rest_framework import serializers

from apps.branches.models import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'address', 'phone', 'description', 'owner',
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']
