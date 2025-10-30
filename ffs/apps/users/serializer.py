from rest_framework import serializers

from apps.users.models import ServiceUser
from config.validator import validate_password, validate_phone_number

class SignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(validators=[validate_password], write_only=True)
    phone = serializers.CharField(validators=[validate_phone_number])

    class Meta:
        model = ServiceUser
        fields = ["id", "email", "name", "password", "confirm_password",
                  "birth", "gender", "phone"]
        read_only_fields = ["id"]
        write_only_fields = ["password", "confirm_password"]

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError(
                {"confirm_password": "비밀번호가 일치하지 않습니다."}
            )
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return ServiceUser.objects.create_user(**validated_data)


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class UserDetailSerializer(serializers. ModelSerializer):
    class Meta:
        model = ServiceUser
        fields = ['id', 'email', 'name',
                  'gender', 'phone', 'created_at', 'updated_at']