from bank.utils.data_types import RegisterInformation
from bank.user.models import AccountsDetail, Accounts


def create_account(register_info: RegisterInformation) -> Accounts:
    account_detail = AccountsDetail.objects.create(
        name=register_info.name,
        age=register_info.age,
        phone_number=register_info.phone_number,
        description=register_info.description,
    )

    account = Accounts.objects.create(
        account_name=register_info.account_name,
        email=register_info.email,
        details=account_detail,
    )

    return account
