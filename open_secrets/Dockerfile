FROM ubuntu:20.04

RUN apt update -y
RUN apt upgrade -y
RUN apt intsall socat -y

COPY ./open_secrets /open_secrets
COPY ./script.sh /script.sh

ENTRYPOINT /script.sh
