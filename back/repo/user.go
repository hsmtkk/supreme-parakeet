package repo

import (
	"context"
	"fmt"
	"math/rand"
	"strconv"

	"cloud.google.com/go/firestore"
	"github.com/hsmtkk/supreme-parakeet/back/model"
	"google.golang.org/api/iterator"
)

const userCollection = "user"

type UserRepo interface {
	New(context.Context, model.NewUser) (model.User, error)
	Get(context.Context, int64) (model.User, error)
	List(context.Context) ([]model.User, error)
}

func NewUserRepo(client *firestore.Client) UserRepo {
	return &userRepoImpl{client}
}

type userRepoImpl struct {
	client *firestore.Client
}

func (r *userRepoImpl) New(ctx context.Context, newUser model.NewUser) (model.User, error) {
	id := rand.Int63()
	data := model.User{
		ID:   id,
		Name: newUser.Name,
	}
	if _, err := r.client.Collection(userCollection).Doc(strconv.FormatInt(id, 10)).Set(ctx, data); err != nil {
		return model.User{}, fmt.Errorf("failed to add data: %w", err)
	}
	return model.User{ID: id, Name: newUser.Name}, nil
}

func (r *userRepoImpl) Get(ctx context.Context, id int64) (model.User, error) {
	result := model.User{}
	dsnap, err := r.client.Collection(userCollection).Doc(strconv.FormatInt(id, 10)).Get(ctx)
	if err != nil {
		return result, fmt.Errorf("failed to get data: %w", err)
	}
	if err := dsnap.DataTo(&result); err != nil {
		return result, fmt.Errorf("failed to decode data: %w", err)
	}
	return result, nil
}

func (r *userRepoImpl) List(ctx context.Context) ([]model.User, error) {
	users := []model.User{}
	iter := r.client.Collection(userCollection).Documents(ctx)
	for {
		doc, err := iter.Next()
		if err == iterator.Done {
			break
		} else if err != nil {
			return nil, err
		}
		user := model.User{}
		if err := doc.DataTo(&user); err != nil {
			return nil, fmt.Errorf("failed to decode data: %w", err)
		}
		users = append(users, user)
	}
	return users, nil
}
