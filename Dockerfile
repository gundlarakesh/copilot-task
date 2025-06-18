# Stage 1: build dependencies
FROM python:3.10-slim AS build

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y build-essential libpq-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Stage 2: final runtime image
COPY . .

# Expose the port your app will run on
EXPOSE 8000

# Run gunicorn
CMD ["gunicorn", "it_chatbot_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
