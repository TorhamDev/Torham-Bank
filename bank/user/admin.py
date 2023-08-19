from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.safestring import SafeString

from bank.user.models import Accounts, AccountsDetail


class AccountsAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "account_name",
        "email",
        "_account_details_link",
        "is_active",
        "is_staff",
    )

    search_fields = (
        "account_name",
        "email",
    )

    def _account_details_link(self, obj) -> SafeString | str:
        if obj.details:
            reversed_url = reverse(
                "admin:user_accountsdetail_change", args=[obj.details.pk]
            )
            return mark_safe(f'<a href="{reversed_url}">{obj.details.__str__()}</a>')

        else:
            return "-"


class AccountsDetailAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "age",
        "phone_number",
        "_account_link",
        "last_login",
    )

    search_fields = (
        "name",
        "age",
        "phone_number",
    )

    def _account_link(self, obj) -> SafeString | str:
        if obj.account:
            account = obj.account.all().first()
            reversed_url = reverse("admin:user_accounts_change", args=[account.pk])
            return mark_safe(f'<a href="{reversed_url}">{account.__str__()}</a>')

        else:
            return "-"


admin.site.register(Accounts, AccountsAdmin)
admin.site.register(AccountsDetail, AccountsDetailAdmin)
