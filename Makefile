TARGET = flask-app

flask:
	cd ../rest-service/ && python services.py

run: build
	docker run -d -p 8090:5000 $(TARGET)

test:
	echo "+----------------------------------------------+"
	echo "|                START TEST                    |"
	echo "+----------------------------------------------+"
	py.test -v

coverage:
	coverage erase
	coverage run -m unittest discover
	coverage html

run-local:
	python app.py

build:
	docker build -t $(TARGET) .