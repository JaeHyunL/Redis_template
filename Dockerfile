FROM python:3.12.0

COPY app /app/

WORKDIR /app

RUN pip install redis redlock-py redis-om

CMD ["sleep", "infinity"]
