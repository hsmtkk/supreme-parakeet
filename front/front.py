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

    page: str = st.sidebar.selectbox("Choose your page", ["users", "rooms"])
    page_map: typing.Dict = {"users": show_user, "rooms": show_room}
    page_map[page](back_address)


def show_room(back_address: str) -> None:
    st.title("APIテスト画面 会議室")

    with st.form(key="room"):
        name: str = st.text_input("会議室名", max_chars=12)
        capacity: int = st.number_input("定員", step=1)
        submit_button = st.form_submit_button(label="送信")

    if submit_button:
        with grpc.insecure_channel(back_address) as channel:
            stub = booking_pb2_grpc.BookingServiceStub(channel)
            response = stub.NewRoom(
                booking_pb2.NewRoomRequest(
                    room=booking_pb2.NewRoom(name=name, capacity=capacity)
                )
            )
        st.write(response)


def show_user(back_address: str) -> None:
    st.title("APIテスト画面 ユーザー")

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
