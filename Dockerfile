FROM ubuntu:22.04
MAINTAINER Nikita Pronin
RUN apt-get update -y
COPY . /opt/gsom_project
WORKDIR /opt/gsom_project
RUN apt install -y python3-pip
RUN pip3 install -r requirements.txt
CMD python3 app.py