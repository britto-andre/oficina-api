FROM python:3.12-slim
ARG SOURCE_FOLDER
WORKDIR /application

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src/app/ ./src/app/