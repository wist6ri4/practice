FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php && \
    apt-get update && \
    apt-get install -y php8.3 php8.3-mysql

COPY ./docker/app/mail.ini /etc/php/8.3/cli/conf.d/mail.ini

RUN apt-get install -yqq msmtp msmtp-mta

COPY ./docker/app/mailrc /etc/msmtprc

RUN apt-get install -y curl iputils-ping procps vim tree