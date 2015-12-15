TARGET = flask-app

run: build
	docker run -d -p 8090:5000 $(TARGET)

build:
	docker build -t $(TARGET) .