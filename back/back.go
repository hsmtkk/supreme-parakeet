package main

import (
	"context"
	"fmt"
	"log"
	"net"
	"os"
	"strconv"

	"cloud.google.com/go/firestore"
	"github.com/hsmtkk/supreme-parakeet/back/model"
	"github.com/hsmtkk/supreme-parakeet/back/repo"
	"github.com/hsmtkk/supreme-parakeet/proto"
	"google.golang.org/grpc"
)

type service struct {
	proto.UnimplementedBookingServiceServer
	bookingRepo repo.BookingRepo
	roomRepo    repo.RoomRepo
	userRepo    repo.UserRepo
}

func newService(bookingRepo repo.BookingRepo, roomRepo repo.RoomRepo, userRepo repo.UserRepo) *service {
	return &service{bookingRepo: bookingRepo, roomRepo: roomRepo, userRepo: userRepo}
}

func (s *service) NewUser(ctx context.Context, in *proto.NewUserRequest) (*proto.NewUserResponse, error) {
	newUser := model.NewUser{Name: in.GetUser().GetName()}
	user, err := s.userRepo.New(ctx, newUser)
	if err != nil {
		return nil, err
	}
	return &proto.NewUserResponse{User: &proto.User{Id: user.ID, Name: user.Name}}, nil
}

func (s *service) GetUser(ctx context.Context, in *proto.GetUserRequest) (*proto.GetUserResponse, error) {
	user, err := s.userRepo.Get(ctx, in.GetId())
	if err != nil {
		return nil, err
	}
	return &proto.GetUserResponse{User: &proto.User{Id: user.ID, Name: user.Name}}, nil
}

func (s *service) NewRoom(ctx context.Context, in *proto.NewRoomRequest) (*proto.NewRoomResponse, error) {
	newRoom := model.NewRoom{Name: in.GetRoom().GetName(), Capacity: in.GetRoom().GetCapacity()}
	room, err := s.roomRepo.New(ctx, newRoom)
	if err != nil {
		return nil, err
	}
	return &proto.NewRoomResponse{Room: &proto.Room{Id: room.ID, Name: room.Name, Capacity: room.Capacity}}, nil
}

func (s *service) GetRoom(ctx context.Context, in *proto.GetRoomRequest) (*proto.GetRoomResponse, error) {
	room, err := s.roomRepo.Get(ctx, in.GetId())
	if err != nil {
		return nil, err
	}
	return &proto.GetRoomResponse{Room: &proto.Room{Id: room.ID, Name: room.Name, Capacity: room.Capacity}}, nil
}

func (s *service) NewBooking(ctx context.Context, in *proto.NewBookingRequest) (*proto.NewBookingResponse, error) {
	newBooking := model.NewBooking{
		UserID:        in.GetBooking().GetUserId(),
		RoomID:        in.GetBooking().GetRoomId(),
		ReservedNum:   in.GetBooking().GetReservedNum(),
		BeginDateTime: in.GetBooking().GetBeginDateTime(),
		EndDateTime:   in.GetBooking().GetEndDateTime(),
	}
	booking, err := s.bookingRepo.New(ctx, newBooking)
	if err != nil {
		return nil, err
	}
	return &proto.NewBookingResponse{Booking: &proto.Booking{Id: booking.ID, UserId: booking.UserID, RoomId: booking.RoomID, ReservedNum: booking.ReservedNum, BeginDateTime: booking.BeginDateTime, EndDateTime: booking.EndDateTime}}, nil
}

func (s *service) GetBooking(ctx context.Context, in *proto.GetBookingRequest) (*proto.GetBookingResponse, error) {
	booking, err := s.bookingRepo.Get(ctx, in.GetId())
	if err != nil {
		return nil, err
	}
	return &proto.GetBookingResponse{Booking: &proto.Booking{Id: booking.ID, UserId: booking.UserID, RoomId: booking.RoomID, ReservedNum: booking.ReservedNum, BeginDateTime: booking.BeginDateTime, EndDateTime: booking.EndDateTime}}, nil
}

func main() {
	portStr := os.Getenv("PORT")
	port, err := strconv.Atoi(portStr)
	if err != nil {
		log.Fatalf("failed to parse %s as int: %v", portStr, err)
	}
	projectID := os.Getenv("PROJECT_ID")

	ctx := context.Background()
	client, err := firestore.NewClient(ctx, projectID)
	if err != nil {
		log.Fatalf("failed to init firestore client: %v", err)
	}
	defer client.Close()

	bookingRepo := repo.NewBookingRepo(client)
	roomRepo := repo.NewRoomRepo(client)
	userRepo := repo.NewUserRepo(client)

	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	svc := newService(bookingRepo, roomRepo, userRepo)
	proto.RegisterBookingServiceServer(s, svc)

	log.Printf("server is listening: %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
