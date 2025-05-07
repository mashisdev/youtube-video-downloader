FROM python:3.12-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install -r requirements.txt

RUN mkdir -p downloads

CMD ["python", "main.py"]