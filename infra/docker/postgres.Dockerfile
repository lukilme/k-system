FROM postgres:16

LABEL maintainer="knowledge-system"

ENV LANG=en_US.utf8

COPY ./database/schemas /docker-entrypoint-initdb.d/

EXPOSE 5432
