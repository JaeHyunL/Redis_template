FROM python:3.12.0

COPY app /app/

WORKDIR /app

RUN pip install redis

CMD ["sleep", "infinity"]
