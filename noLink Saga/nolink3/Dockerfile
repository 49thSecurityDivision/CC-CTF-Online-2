FROM debian:stable-slim
EXPOSE 8080

RUN apt-get update; exit 0
RUN apt-get install libev-dev python3 python3-pip -y
RUN python3 -m pip install bjoern falcon

COPY ./webserver.py /opt/webserver.py
COPY ./RobotoMono-Regular.ttf /opt/RobotoMono-Regular.ttf
WORKDIR /opt

CMD ["python3", "webserver.py"]