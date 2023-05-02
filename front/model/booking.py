import dataclasses


@dataclasses.dataclass
class NewBooking:
    user_id: int
    room_id: int
    reserved_num: int
    begin_date_time: str
    end_date_time: str


@dataclasses.dataclass
class Booking(NewBooking):
    id: int
