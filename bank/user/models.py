from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from typing import Any

from bank.user.manager import UserManager
from bank.utils.models import BaseModel


class AccountsDetail(BaseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    last_login = models.DateTimeField(null=True, blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} - {self.phone_number}"


class Accounts(BaseModel, AbstractBaseUser, PermissionsMixin):
    account_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    details = models.ForeignKey(
        to=AccountsDetail,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="account",
    )
    balance = models.FloatField(default=0.0)

    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("is staff"), default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[Any] = []

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self) -> str:
        return f"{self.account_name} - {self.email}"
