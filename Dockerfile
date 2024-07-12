FROM python:3.12-slim
ARG SOURCE_FOLDER
WORKDIR /application

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src/app/common ./src/app/common

COPY ./src/app/$SOURCE_FOLDER ./src/app/$SOURCE_FOLDER