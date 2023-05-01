import datetime
import os
import typing

import booking_pb2
import booking_pb2_grpc
import grpc
import streamlit as st


def run() -> None:
    back_host = os.environ["BACK_HOST"]
    back_port = os.environ["BACK_PORT"]
    back_address = f"{back_host}:{back_port}"

    page: str = st.sidebar.selectbox("Choose your page", ["bookings", "users", "rooms"])
    page_map: typing.Dict = {
        "bookings": show_booking,
        "users": show_user,
        "rooms": show_room,
    }
    page_map[page](back_address)


def get_users(back_address: str) -> typing.List[booking_pb2.User]:
    with grpc.insecure_channel(back_address) as channel:
        stub = booking_pb2_grpc.BookingServiceStub(channel)
        response = stub.GetUsers(booking_pb2.GetUsersRequest())
    return response.users


def get_rooms(back_address: str) -> typing.List[booking_pb2.Room]:
    with grpc.insecure_channel(back_address) as channel:
        stub = booking_pb2_grpc.BookingServiceStub(channel)
        response = stub.GetRooms(booking_pb2.GetRoomsRequest())
    return response.rooms


def show_booking(back_address: str) -> None:
    st.title("予約登録")

    users = get_users(back_address)
    users_dict: typing.Dict[str, int] = {}
    for user in users:
        users_dict[user.name] = user.id

    rooms = get_rooms(back_address)
    rooms_dict: typing.Dict[str, typing.Dict[str, int]] = {}
    for room in rooms:
        rooms_dict[room.name] = {"id": room.id, "capacity": room.capacity}
    st.write(rooms_dict)

    with st.form(key="booking"):
        user_id: int = 0
        room_id: int = 0
        reserved_num: int = st.number_input("予約人数", step=1)
        date: datetime.date = st.date_input("日付を入力", min_value=datetime.date.today())
        begin_time = st.time_input("開始時刻", value=datetime.time(hour=9))
        end_time = st.time_input("終了時刻", value=datetime.time(hour=20))
        begin_date_time = datetime.datetime(
            year=date.year,
            month=date.month,
            day=date.day,
            hour=begin_time.hour,
            minute=begin_time.minute,
        ).isoformat()
        end_date_time = datetime.datetime(
            year=date.year,
            month=date.month,
            day=date.day,
            hour=end_time.hour,
            minute=end_time.minute,
        ).isoformat()
        submit_button = st.form_submit_button(label="送信")

    if submit_button:
        with grpc.insecure_channel(back_address) as channel:
            stub = booking_pb2_grpc.BookingServiceStub(channel)
            response = stub.NewBooking(
                booking_pb2.NewBookingRequest(
                    booking=booking_pb2.NewBooking(
                        user_id=user_id,
                        room_id=room_id,
                        reserved_num=reserved_num,
                        begin_date_time=begin_date_time,
                        end_date_time=end_date_time,
                    )
                )
            )
        st.write(response)


def show_room(back_address: str) -> None:
    st.title("会議室登録")

    with st.form(key="room"):
        name: str = st.text_input("会議室名", max_chars=12)
        capacity: int = st.number_input("定員", step=1)
        submit_button = st.form_submit_button(label="送信")

    if submit_button:
        with grpc.insecure_channel(back_address) as channel:
            stub = booking_pb2_grpc.BookingServiceStub(channel)
            response = stub.NewRoom(
                booking_pb2.NewRoomRequest(
                    room=booking_pb2.NewRoom(
                        name=name,
                        capacity=capacity,
                    )
                )
            )
        st.write(response)


def show_user(back_address: str) -> None:
    st.title("ユーザー登録")

    with st.form(key="user"):
        name: str = st.text_input("ユーザー名", max_chars=12)
        submit_button = st.form_submit_button(label="送信")

    if submit_button:
        with grpc.insecure_channel(back_address) as channel:
            stub = booking_pb2_grpc.BookingServiceStub(channel)
            response = stub.NewUser(
                booking_pb2.NewUserRequest(user=booking_pb2.NewUser(name=name))
            )
        st.write(response)


run()
