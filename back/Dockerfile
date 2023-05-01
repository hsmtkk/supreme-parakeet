FROM golang:1.20 AS builder
WORKDIR /app
COPY go.mod .
COPY go.sum .
RUN go mod download
COPY back/ /app/back/
WORKDIR /app/back
RUN CGO_ENABLED=0 go build -o back

FROM gcr.io/distroless/static-debian11 AS runtime
COPY --from=builder /app/back/back /app/back/back
ENTRYPOINT ["/app/back/back"]
