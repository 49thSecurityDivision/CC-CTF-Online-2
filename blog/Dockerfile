FROM ubuntu:20.04

RUN /usr/sbin/useradd -m user

RUN apt update && apt -y install software-properties-common && apt -y install memcached libmemcached-tools

RUN add-apt-repository ppa:deadsnakes/ppa && apt install python3.8 && apt -y install python3-pip

RUN mkdir /home/user/blog

WORKDIR /home/user/blog

RUN mkdir templates

RUN pip3 install flask flask-session python-memcached pymemcache

COPY templates/* templates/

COPY app.py ./

COPY flag /home/user

RUN chown -R root:user /home/user && \
    chmod -R 750 /home/user && \
    chmod 740 /home/user/flag

CMD [ "./app.py" ]

EXPOSE 5000
EXPOSE 11211
