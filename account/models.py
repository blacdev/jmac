import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
class myAccountmanagaer(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")
        if not password:
            raise ValueError("User must have a password")

        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class Accounts(AbstractBaseUser, PermissionsMixin):
    id               = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email            = models.EmailField(verbose_name="email", max_length=255, unique=True)
    username         = models.CharField(max_length=255, unique=True, db_index=True)
    date_joined      = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login       = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin         = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    is_staff         = models.BooleanField(default=False)
    is_superuser     = models.BooleanField(default=False)
    is_verified      = models.BooleanField(default=False)

    objects = myAccountmanagaer()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def token(self):
        tokens  = RefreshToken.for_user(self)
        return {
            "refesh": str(tokens),
            "access": str(tokens.access_token),
        }





    # interface User {
#   id: string;
#   name: string;
#   email: string;
#   password: string;
#
#   accounts: [
#     {
#       id: string;
#       bankName: string;
#     }
#   ];
# }