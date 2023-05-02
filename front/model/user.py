import dataclasses


@dataclasses.dataclass
class NewUser:
    name: str


@dataclasses.dataclass
class User(NewUser):
    id: int
