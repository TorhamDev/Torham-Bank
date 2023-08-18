from django.contrib import admin
from bank.user.models import Accounts, AccountsDetail


class AccountsAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "account_name",
        "email",
        "is_active",
        "is_staff",
    )

    search_fields = (
        "account_name",
        "email",
    )


class AccountsDetailAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "age",
        "phone_number",
        "last_login",
    )

    search_fields = (
        "name",
        "age",
        "phone_number",
    )


admin.site.register(Accounts, AccountsAdmin)
admin.site.register(AccountsDetail, AccountsDetailAdmin)
