FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo

RUN apt-get update && \
    apt-get install -y tzdata php php-mysql

COPY ./docker/app/mail.ini /etc/php/7.4/cli/conf.d/mail.ini

RUN apt install -yqq msmtp msmtp-mta

COPY ./docker/app/mailrc /etc/msmtprc

RUN apt install -y curl iputils-ping procps vim tree
