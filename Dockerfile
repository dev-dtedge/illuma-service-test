FROM ubuntu:latest
MAINTAINER Jeremy Whittington "jeremy.whittington@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential curl
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]