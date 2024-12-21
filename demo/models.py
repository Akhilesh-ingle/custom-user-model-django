from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from demo.managers import Usermanager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    contact = models.CharField(max_length=20)
    address = models.TextField()

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = Usermanager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'User'
