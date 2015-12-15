TARGET = flask-app

run: build
	docker run -d -p 8000:8000 $(TARGET)

build:
	docker build -t $(TARGET) .