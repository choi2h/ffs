import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class Gender(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'

class ServiceUserManager(BaseUserManager):
    def create_user(self, email, name, birth, gender, password=None, **extra_fields):
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

    def create_superuser(self, email, name, birth, gender, password=None):
        user = self.create_user(
            email,
            password,
            birth = birth,
            gender = gender,
        )

        user.is_admin = True
        user.save(using=self._db)
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