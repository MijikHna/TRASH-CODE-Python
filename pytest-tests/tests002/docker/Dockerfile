FROM postgres

RUN apt update && \
  apt dist-upgrade -y

RUN apt install -y vim

RUN apt autoremove -y

ENV POSTGRES_PASSWORD=password

COPY ./init.sql /docker-entrypoint-initdb.d/init.sql