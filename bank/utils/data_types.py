from dataclasses import dataclass, field


@dataclass
class RegisterInformation:
    account_name: str
    email: str
    name: str
    age: int
    phone_number: str
    description: str
    balance: float = field(default_factory=float)
