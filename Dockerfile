# Stage 1: build dependencies
FROM python:3.10-slim AS build

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y build-essential libpq-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Stage 2: final runtime image
FROM python:3.10-slim

WORKDIR /app
COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY . .

EXPOSE 8000
CMD ["gunicorn", "it_chatbot_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
