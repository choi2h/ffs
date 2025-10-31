from datetime import date

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class Gender(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'

class Role(models.TextChoices):
    PLATFORM_ADMIN = 'platform_admin', '전체 관리자'
    BRANCH_ADMIN = 'branch_admin', '지점 관리자'
    TRAINER = 'trainer', '트레이너'
    MEMBER = 'member', '회원'

class MatchingStatus(models.TextChoices):
    PENDING = 'PENDING', '대기중'
    ACTIVE = 'ACTIVE', '매칭중'
    REJECTED = 'REJECTED', '거절',
    DISCONNECTED = 'DISCONNECTED', '매칭종료'


class ServiceUserManager(BaseUserManager):
    def create_user(self, email: str, name: str, birth: date, gender: Gender,
        password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email= self.normalize_email(email),
            birth = birth,
            name = name,
            gender = gender,
            phone = extra_fields.pop('phone', None),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, birth, gender, password=None,
        **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.create_user(
            email=email,
            name=name,
            birth=birth,
            gender=gender,
            password=password,
            **extra_fields
        )

        return user


class ServiceUser(AbstractUser):
    username = None

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    birth = models.DateField()
    gender = models.CharField(max_length=6,
                              choices=Gender.choices,
                              default=Gender.MALE)
    phone = models.CharField(max_length=11, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'birth', 'phone']

    objects = ServiceUserManager()

    class Meta:
        app_label = 'users'
        db_table = 'user'

class UserBranchMembership(models.Model):
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=15, choices=Role.choices,
                            default=Role.MEMBER)

    class Meta:
        unique_together = ['user', 'branch']
        ordering = ['-joined_at']
        app_label = 'users'
        db_table = 'membership'
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    user_id=models.F('branch__owner_id'),
                    role='branch_admin'
                ) | ~models.Q(role='branch_admin'),
                name='admin_must_be_owner'
            )
        ]

class Matching(models.Model):
    member = models.ForeignKey(ServiceUser, on_delete=models.CASCADE,
                               related_name='member')
    trainer = models.ForeignKey(ServiceUser, on_delete=models.CASCADE,
                                related_name='trainer')
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=MatchingStatus.choices,)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['member', 'trainer', 'branch']
        app_label = 'users'
        db_table = 'matching'