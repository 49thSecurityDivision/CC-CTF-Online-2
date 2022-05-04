FROM ubuntu:20.04
RUN /usr/sbin/useradd -m 49sd
RUN /usr/sbin/useradd -m hacker
RUN apt update && apt -y install software-properties-common && apt -y install openssh-server && apt-get -y install sudo && apt-get -y install less && apt-get -y install git && apt-get -y install zip && apt-get -y install unzip
RUN git config --global user.email "49sd@rootme.org"
RUN git config --global user.name "49sd"
RUN mkdir /home/49sd/repos
RUN mkdir /root/49sd_main_repo
RUN chmod 733 /home/49sd/repos
COPY 49sd-note /home/49sd/
COPY addto49sdrepo.sh /root
RUN mkdir /opt/backup
COPY addto49sdrepo.sh /opt/backup/addto49sdrepo.sh.bak
RUN chmod +x /root/addto49sdrepo.sh
RUN echo "hacker ALL=(49sd) NOPASSWD: /bin/less" >> /etc/sudoers
RUN echo "49sd ALL=(root) NOPASSWD: /root/addto49sdrepo.sh" >> /etc/sudoers
COPY user.txt /home/49sd/
COPY root.txt /root/
RUN echo 'hacker:hacker' | chpasswd
ENTRYPOINT service ssh restart && /bin/bash
