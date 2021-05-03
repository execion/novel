FROM python:3.9.4
LABEL maintainer="execion"
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src /src

WORKDIR /src
VOLUME /src