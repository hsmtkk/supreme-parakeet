package repo

import (
	"context"
	"fmt"
	"math/rand"
	"strconv"

	"cloud.google.com/go/firestore"
	"github.com/hsmtkk/supreme-parakeet/back/model"
)

const roomCollection = "room"

type RoomRepo interface {
	New(context.Context, model.NewRoom) (model.Room, error)
	Get(context.Context, int64) (model.Room, error)
}

func NewRoomRepo(client *firestore.Client) RoomRepo {
	return &roomRepoImpl{client}
}

type roomRepoImpl struct {
	client *firestore.Client
}

func (r *roomRepoImpl) New(ctx context.Context, newRoom model.NewRoom) (model.Room, error) {
	id := rand.Int63()
	data := model.Room{
		ID:       id,
		Name:     newRoom.Name,
		Capacity: newRoom.Capacity,
	}
	if _, err := r.client.Collection(roomCollection).Doc(strconv.FormatInt(id, 10)).Set(ctx, data); err != nil {
		return model.Room{}, fmt.Errorf("failed to add data: %w", err)
	}
	return model.Room{ID: id, Name: newRoom.Name}, nil
}

func (r *roomRepoImpl) Get(ctx context.Context, id int64) (model.Room, error) {
	result := model.Room{}
	dsnap, err := r.client.Collection(roomCollection).Doc(strconv.FormatInt(id, 10)).Get(ctx)
	if err != nil {
		return result, fmt.Errorf("failed to get data: %w", err)
	}
	if err := dsnap.DataTo(&result); err != nil {
		return result, fmt.Errorf("failed to decode data: %w", err)
	}
	return result, nil
}
