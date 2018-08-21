FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y schroot
RUN apt-get install -y debootstrap
RUN apt-get install -y python

RUN groupadd -g 1005 crypt2
RUN useradd -u 2004 -g 1005 crypt2

RUN mkdir /cysca
WORKDIR /cysca

COPY --chown=2004:1005 ./server.py ./
COPY --chown=2004:1005 ./helpers.py ./

RUN mkdir -p /chroots/2004/dev

RUN mknod /chroots/2004/dev/urandom c 1 8


RUN apt-get install -y python-pip
RUN pip install pycrypto

COPY ./flag.txt /chroots/2004/flag.txt

EXPOSE 9999

ENTRYPOINT ["python", "./server.py"]