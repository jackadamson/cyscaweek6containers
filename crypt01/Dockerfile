FROM myubuntu:v1

RUN apt install -y schroot
RUN apt install -y debootstrap
RUN apt install -y python3

RUN groupadd -g 1004 crypt1
RUN useradd -u 2003 -g 1004 crypt1

RUN mkdir /cysca
WORKDIR /cysca

COPY --chown=2003:1004 ./server.py ./
COPY --chown=2003:1004 ./helpers.py ./

RUN mkdir -p /chroots/2003/dev

RUN mknod /chroots/2003/dev/urandom c 1 8

COPY ./flag.txt /chroots/2003/flag.txt

ENTRYPOINT ["python3", "./server.py"]