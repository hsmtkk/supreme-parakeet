# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\x12\x05proto\"\x17\n\x07NewUser\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\x04User\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\".\n\x0eNewUserRequest\x12\x1c\n\x04user\x18\x01 \x01(\x0b\x32\x0e.proto.NewUser\",\n\x0fNewUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.proto.User\"\x1c\n\x0eGetUserRequest\x12\n\n\x02id\x18\x01 \x01(\x03\",\n\x0fGetUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.proto.User\"\x11\n\x0fGetUsersRequest\".\n\x10GetUsersResponse\x12\x1a\n\x05users\x18\x01 \x03(\x0b\x32\x0b.proto.User\")\n\x07NewRoom\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61pacity\x18\x02 \x01(\x03\"2\n\x04Room\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61pacity\x18\x03 \x01(\x03\".\n\x0eNewRoomRequest\x12\x1c\n\x04room\x18\x01 \x01(\x0b\x32\x0e.proto.NewRoom\",\n\x0fNewRoomResponse\x12\x19\n\x04room\x18\x01 \x01(\x0b\x32\x0b.proto.Room\"\x1c\n\x0eGetRoomRequest\x12\n\n\x02id\x18\x01 \x01(\x03\",\n\x0fGetRoomResponse\x12\x19\n\x04room\x18\x01 \x01(\x0b\x32\x0b.proto.Room\"\x11\n\x0fGetRoomsRequest\".\n\x10GetRoomsResponse\x12\x1a\n\x05rooms\x18\x01 \x03(\x0b\x32\x0b.proto.Room\"t\n\nNewBooking\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x0f\n\x07room_id\x18\x02 \x01(\x03\x12\x14\n\x0creserved_num\x18\x03 \x01(\x03\x12\x17\n\x0f\x62\x65gin_date_time\x18\x04 \x01(\t\x12\x15\n\rend_date_time\x18\x05 \x01(\t\"}\n\x07\x42ooking\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07user_id\x18\x02 \x01(\x03\x12\x0f\n\x07room_id\x18\x03 \x01(\x03\x12\x14\n\x0creserved_num\x18\x04 \x01(\x03\x12\x17\n\x0f\x62\x65gin_date_time\x18\x05 \x01(\t\x12\x15\n\rend_date_time\x18\x06 \x01(\t\"7\n\x11NewBookingRequest\x12\"\n\x07\x62ooking\x18\x01 \x01(\x0b\x32\x11.proto.NewBooking\"5\n\x12NewBookingResponse\x12\x1f\n\x07\x62ooking\x18\x01 \x01(\x0b\x32\x0e.proto.Booking\"\x1f\n\x11GetBookingRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"5\n\x12GetBookingResponse\x12\x1f\n\x07\x62ooking\x18\x01 \x01(\x0b\x32\x0e.proto.Booking2\x88\x04\n\x0e\x42ookingService\x12:\n\x07NewUser\x12\x15.proto.NewUserRequest\x1a\x16.proto.NewUserResponse\"\x00\x12:\n\x07GetUser\x12\x15.proto.GetUserRequest\x1a\x16.proto.GetUserResponse\"\x00\x12=\n\x08GetUsers\x12\x16.proto.GetUsersRequest\x1a\x17.proto.GetUsersResponse\"\x00\x12:\n\x07NewRoom\x12\x15.proto.NewRoomRequest\x1a\x16.proto.NewRoomResponse\"\x00\x12:\n\x07GetRoom\x12\x15.proto.GetRoomRequest\x1a\x16.proto.GetRoomResponse\"\x00\x12=\n\x08GetRooms\x12\x16.proto.GetRoomsRequest\x1a\x17.proto.GetRoomsResponse\"\x00\x12\x43\n\nNewBooking\x12\x18.proto.NewBookingRequest\x1a\x19.proto.NewBookingResponse\"\x00\x12\x43\n\nGetBooking\x12\x18.proto.GetBookingRequest\x1a\x19.proto.GetBookingResponse\"\x00\x42*Z(github.com/hsmtkk/supreme-parakeet/protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(github.com/hsmtkk/supreme-parakeet/proto'
  _NEWUSER._serialized_start=24
  _NEWUSER._serialized_end=47
  _USER._serialized_start=49
  _USER._serialized_end=81
  _NEWUSERREQUEST._serialized_start=83
  _NEWUSERREQUEST._serialized_end=129
  _NEWUSERRESPONSE._serialized_start=131
  _NEWUSERRESPONSE._serialized_end=175
  _GETUSERREQUEST._serialized_start=177
  _GETUSERREQUEST._serialized_end=205
  _GETUSERRESPONSE._serialized_start=207
  _GETUSERRESPONSE._serialized_end=251
  _GETUSERSREQUEST._serialized_start=253
  _GETUSERSREQUEST._serialized_end=270
  _GETUSERSRESPONSE._serialized_start=272
  _GETUSERSRESPONSE._serialized_end=318
  _NEWROOM._serialized_start=320
  _NEWROOM._serialized_end=361
  _ROOM._serialized_start=363
  _ROOM._serialized_end=413
  _NEWROOMREQUEST._serialized_start=415
  _NEWROOMREQUEST._serialized_end=461
  _NEWROOMRESPONSE._serialized_start=463
  _NEWROOMRESPONSE._serialized_end=507
  _GETROOMREQUEST._serialized_start=509
  _GETROOMREQUEST._serialized_end=537
  _GETROOMRESPONSE._serialized_start=539
  _GETROOMRESPONSE._serialized_end=583
  _GETROOMSREQUEST._serialized_start=585
  _GETROOMSREQUEST._serialized_end=602
  _GETROOMSRESPONSE._serialized_start=604
  _GETROOMSRESPONSE._serialized_end=650
  _NEWBOOKING._serialized_start=652
  _NEWBOOKING._serialized_end=768
  _BOOKING._serialized_start=770
  _BOOKING._serialized_end=895
  _NEWBOOKINGREQUEST._serialized_start=897
  _NEWBOOKINGREQUEST._serialized_end=952
  _NEWBOOKINGRESPONSE._serialized_start=954
  _NEWBOOKINGRESPONSE._serialized_end=1007
  _GETBOOKINGREQUEST._serialized_start=1009
  _GETBOOKINGREQUEST._serialized_end=1040
  _GETBOOKINGRESPONSE._serialized_start=1042
  _GETBOOKINGRESPONSE._serialized_end=1095
  _BOOKINGSERVICE._serialized_start=1098
  _BOOKINGSERVICE._serialized_end=1618
# @@protoc_insertion_point(module_scope)
