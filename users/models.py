from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, email, fullname, password=None):
        if not email:
            raise ValueError('User must provide email!')

        user = self.model(
            email=self.normalize_email(email),
            fullname=fullname
        )

        user.set_password(password)
        user.is_active = True
        user.save(using=self.db)

        return user

    def create_superuser(self, email, fullname, password=None):
        user = self.create_user(email=email, fullname=fullname, password=password)

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self.db)

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True, verbose_name="Email Address")
    fullname = models.CharField(max_length=30)
    is_instructor = models.BooleanField(default=False, blank=True)
    date_join = models.DateTimeField(auto_now_add=True, verbose_name="Date Joined")
    last_login = models.DateTimeField(auto_now=True, verbose_name="Last Login")

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["fullname"]


