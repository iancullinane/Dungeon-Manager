FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y python-dev build-essential

ADD https://bootstrap.pypa.io/get-pip.py .
RUN python get-pip.py;

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]