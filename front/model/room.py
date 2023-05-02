import dataclasses


@dataclasses.dataclass
class NewRoom:
    name: str
    capacity: int


@dataclasses.dataclass
class Room(NewRoom):
    id: int
