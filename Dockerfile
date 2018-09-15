FROM ubuntu:latest
LABEL Author="ronaldtheodoro"
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt:en
ENV LC_ALL pt_BR.UTF-8
RUN mkdir /app
WORKDIR /app
RUN apt update && apt install python3 python3-pip -y && apt clean
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
RUN chmod +x entrypoint.sh
RUN pytest
