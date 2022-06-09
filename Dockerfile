FROM python:3.9.9-bullseye

ARG APP_DIR=/var/envelope-maker
WORKDIR $APP_DIR

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY . $APP_DIR
