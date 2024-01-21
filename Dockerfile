FROM python:3.11-bookworm as runtime

WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip3 install -r /requirements.txt

COPY . .