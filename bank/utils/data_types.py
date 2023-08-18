from dataclasses import dataclass


@dataclass
class RegisterInformation:
    account_name : str
    email : str
    name : str
    age : int
    phone_number : str
    description : str