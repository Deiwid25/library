
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt



RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .


EXPOSE 8000

CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000