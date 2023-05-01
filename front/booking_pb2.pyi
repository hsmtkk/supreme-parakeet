from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Booking(_message.Message):
    __slots__ = ["begin_date_time", "end_date_time", "id", "reserved_num", "room_id", "user_id"]
    BEGIN_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RESERVED_NUM_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    begin_date_time: str
    end_date_time: str
    id: int
    reserved_num: int
    room_id: int
    user_id: int
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., room_id: _Optional[int] = ..., reserved_num: _Optional[int] = ..., begin_date_time: _Optional[str] = ..., end_date_time: _Optional[str] = ...) -> None: ...

class GetBookingRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetBookingResponse(_message.Message):
    __slots__ = ["booking"]
    BOOKING_FIELD_NUMBER: _ClassVar[int]
    booking: Booking
    def __init__(self, booking: _Optional[_Union[Booking, _Mapping]] = ...) -> None: ...

class GetRoomRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetRoomResponse(_message.Message):
    __slots__ = ["room"]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    room: Room
    def __init__(self, room: _Optional[_Union[Room, _Mapping]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class NewBooking(_message.Message):
    __slots__ = ["begin_date_time", "end_date_time", "reserved_num", "room_id", "user_id"]
    BEGIN_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESERVED_NUM_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    begin_date_time: str
    end_date_time: str
    reserved_num: int
    room_id: int
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., room_id: _Optional[int] = ..., reserved_num: _Optional[int] = ..., begin_date_time: _Optional[str] = ..., end_date_time: _Optional[str] = ...) -> None: ...

class NewBookingRequest(_message.Message):
    __slots__ = ["booking"]
    BOOKING_FIELD_NUMBER: _ClassVar[int]
    booking: NewBooking
    def __init__(self, booking: _Optional[_Union[NewBooking, _Mapping]] = ...) -> None: ...

class NewBookingResponse(_message.Message):
    __slots__ = ["booking"]
    BOOKING_FIELD_NUMBER: _ClassVar[int]
    booking: Booking
    def __init__(self, booking: _Optional[_Union[Booking, _Mapping]] = ...) -> None: ...

class NewRoom(_message.Message):
    __slots__ = ["capacity", "name"]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    capacity: int
    name: str
    def __init__(self, name: _Optional[str] = ..., capacity: _Optional[int] = ...) -> None: ...

class NewRoomRequest(_message.Message):
    __slots__ = ["room"]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    room: NewRoom
    def __init__(self, room: _Optional[_Union[NewRoom, _Mapping]] = ...) -> None: ...

class NewRoomResponse(_message.Message):
    __slots__ = ["room"]
    ROOM_FIELD_NUMBER: _ClassVar[int]
    room: Room
    def __init__(self, room: _Optional[_Union[Room, _Mapping]] = ...) -> None: ...

class NewUser(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class NewUserRequest(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: NewUser
    def __init__(self, user: _Optional[_Union[NewUser, _Mapping]] = ...) -> None: ...

class NewUserResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class Room(_message.Message):
    __slots__ = ["capacity", "id", "name"]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    capacity: int
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., capacity: _Optional[int] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
