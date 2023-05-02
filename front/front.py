import datetime
import os
import typing

import booking_pb2
import booking_pb2_grpc
import grpc
import model.booking
import model.room
import model.user
import pandas as pd
import streamlit as st


def run() -> None:
    back_host = os.environ["BACK_HOST"]
    if back_host == "":
        raise Exception("BACK_HOST env var is not defined")
    back_port = os.environ["BACK_PORT"]
    if back_port == "":
        raise Exception("BACK_PORT env var is not defined")
    back_address: str = f"{back_host}:{back_port}"

    page: str = st.sidebar.selectbox("Choose your page", ["bookings", "users", "rooms"])
    page_map: typing.Dict = {
        "bookings": show_booking,
        "users": show_user,
        "rooms": show_room,
    }
    page_map[page](back_address)


def new_booking(
    back_address: str, new_item: model.booking.NewBooking
) -> model.booking.Booking:
    with grpc.insecure_channel(back_address) as channel:
        stub = booking_pb2_grpc.BookingServiceStub(channel)
        response = stub.NewBooking(
            booking_pb2.NewBookingRequest(
                booking=booking_pb2.NewBooking(
                    user_id=new_item.user_id,
                    room_id=new_item.room_id,
                    reserved_num=new_item.reserved_num,
                    begin_date_time=new_item.begin_date_time,
                    end_date_time=new_item.end_date_time,
                )
            )
        )
    return model.booking.Booking(
        id=response.id,
        user_id=new_item.user_id,
        room_id=new_item.room_id,
        reserved_num=new_item.reserved_num,
        begin_date_time=new_item.begin_date_time,
        end_date_time=new_item.end_date_time,
    )


def new_room(back_address: str, new_item: model.room.NewRoom) -> model.room.Room:
    with grpc.insecure_channel(back_address) as channel:
        stub = booking_pb2_grpc.BookingServiceStub(channel)
        response = stub.NewRoom(
            booking_pb2.NewRoomRequest(
                room=booking_pb2.NewRoom(
                    name=new_item.name,
                    capacity=new_item.capacity,
                )
            )
        )
    return model.room.Room(
        id=response.id, name=new_item.name, capacity=new_item.capacity
    )


def new_user(back_address: str, new_item: model.user.NewUser) -> model.user.User:
    with grpc.insecure_channel(back_address) as channel:
        stub = booking_pb2_grpc.BookingServiceStub(channel)
        response = stub.NewUser(
            booking_pb2.NewUserRequest(user=booking_pb2.NewUser(name=new_item.name))
        )
    return model.user.User(id=response.id, name=new_item.name)


def get_rooms(back_address: str) -> typing.List[model.room.Room]:
    with grpc.insecure_channel(back_address) as channel:
        stub = booking_pb2_grpc.BookingServiceStub(channel)
        response = stub.GetRooms(booking_pb2.GetRoomsRequest())
    results = []
    for r in response.rooms:
        results.append(model.room.Room(id=r.id, name=r.name, capacity=r.capacity))
    return results


def get_users(back_address: str) -> typing.List[model.user.User]:
    with grpc.insecure_channel(back_address) as channel:
        stub = booking_pb2_grpc.BookingServiceStub(channel)
        response = stub.GetUsers(booking_pb2.GetUsersRequest())
    results = []
    for u in response.users:
        results.append(model.user.User(id=u.id, name=u.name))
    return results


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

    st.write("会議室一覧")
    df_rooms = pd.DataFrame(rooms)
    st.table(df_rooms)

    with st.form(key="booking"):
        user_name: str = st.selectbox("予約者名", users_dict.keys())
        room_name: str = st.selectbox("会議室名", rooms_dict.keys())
        reserved_num: int = st.number_input("予約人数", step=1, min_value=1)
        date: datetime.date = st.date_input("日付を入力", min_value=datetime.date.today())
        begin_time = st.time_input("開始時刻", value=datetime.time(hour=9))
        end_time = st.time_input("終了時刻", value=datetime.time(hour=20))

        user_id: int = users_dict[user_name]
        room_id: int = rooms_dict[room_name]["id"]
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
        booking = new_booking(
            back_address,
            model.booking.NewBooking(
                user_id=user_id,
                room_id=room_id,
                reserved_num=reserved_num,
                begin_date_time=begin_date_time,
                end_date_time=end_date_time,
            ),
        )
        st.write(booking)


def show_room(back_address: str) -> None:
    st.title("会議室登録")

    with st.form(key="room"):
        name: str = st.text_input("会議室名", max_chars=12)
        capacity: int = st.number_input("定員", step=1)
        submit_button = st.form_submit_button(label="送信")

    if submit_button:
        room = new_room(back_address, model.room.NewRoom(name=name, capacity=capacity))
        st.write(room)


def show_user(back_address: str) -> None:
    st.title("ユーザー登録")

    with st.form(key="user"):
        name: str = st.text_input("ユーザー名", max_chars=12)
        submit_button = st.form_submit_button(label="送信")

    if submit_button:
        user = new_user(back_address, model.user.NewUser(name=name))
        st.write(user)


run()
