# First stage: build
FROM python:3.12-alpine

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD [ "python3", "./main.py" ]