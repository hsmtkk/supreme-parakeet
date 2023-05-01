package model

type NewBooking struct {
	UserID        int64
	RoomID        int64
	ReservedNum   int64
	BeginDateTime string
	EndDateTime   string
}

type Booking struct {
	ID            int64
	UserID        int64
	RoomID        int64
	ReservedNum   int64
	BeginDateTime string
	EndDateTime   string
}
