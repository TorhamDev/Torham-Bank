from django.db import models
from django.contrib.auth.models import PermissionsMixin, Group
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from typing import Any

from bank.user.manager import UserManager
from bank.utils.models import BaseModel


class AccountsType(BaseModel):
    accounts_types_code = models.CharField(primary_key=True, max_length=10)
    accounts_types_description = models.TextField()


class AccountsDetail(BaseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    last_login = models.DateTimeField(null=True, blank=True)
    description = models.TextField()


class Accounts(BaseModel, AbstractBaseUser, PermissionsMixin):
    account_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    details = models.ForeignKey(to=AccountsDetail, on_delete=models.CASCADE)
    account_types_code = models.ForeignKey(to=AccountsType, on_delete=models.CASCADE)
    # account_wallet = ... #TODO : create wallet for users

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[Any] = []

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
