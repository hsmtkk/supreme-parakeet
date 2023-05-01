package repo

import (
	"context"
	"fmt"
	"math/rand"
	"strconv"

	"cloud.google.com/go/firestore"
	"github.com/hsmtkk/supreme-parakeet/back/model"
)

const bookingCollection = "booking"

type BookingRepo interface {
	New(context.Context, model.NewBooking) (model.Booking, error)
	Get(context.Context, int64) (model.Booking, error)
}

func NewBookingRepo(client *firestore.Client) BookingRepo {
	return &bookingRepoImpl{client}
}

type bookingRepoImpl struct {
	client *firestore.Client
}

func (r *bookingRepoImpl) New(ctx context.Context, newBooking model.NewBooking) (model.Booking, error) {
	id := rand.Int63()
	data := model.Booking{
		UserID:        newBooking.UserID,
		RoomID:        newBooking.RoomID,
		ReservedNum:   newBooking.ReservedNum,
		BeginDateTime: newBooking.BeginDateTime,
		EndDateTime:   newBooking.EndDateTime,
	}
	if _, err := r.client.Collection(bookingCollection).Doc(strconv.FormatInt(id, 10)).Set(ctx, data); err != nil {
		return model.Booking{}, fmt.Errorf("failed to add data: %w", err)
	}
	return model.Booking{ID: id, UserID: newBooking.UserID, RoomID: newBooking.RoomID, ReservedNum: newBooking.ReservedNum, BeginDateTime: newBooking.BeginDateTime, EndDateTime: newBooking.EndDateTime}, nil
}

func (r *bookingRepoImpl) Get(ctx context.Context, id int64) (model.Booking, error) {
	result := model.Booking{}
	dsnap, err := r.client.Collection(bookingCollection).Doc(strconv.FormatInt(id, 10)).Get(ctx)
	if err != nil {
		return result, fmt.Errorf("failed to get data: %w", err)
	}
	if err := dsnap.DataTo(&result); err != nil {
		return result, fmt.Errorf("failed to decode data: %w", err)
	}
	return result, nil
}
