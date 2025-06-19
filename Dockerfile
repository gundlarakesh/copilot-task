# Stage 1: Build Dependencies
FROM python:3.10-slim AS build

WORKDIR /app

# Install system dependencies for building Python packages
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt

# Copy the application code
COPY . .

# Collect static files (optional at build)
RUN python manage.py collectstatic --noinput

# Stage 2: Runtime image
# FROM python:3.10-slim

# WORKDIR /app

# # Copy installed Python packages from build stage
# COPY --from=build /install /usr/local
# # Copy application code
# COPY --from=build /app /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Final container startup command
CMD ["gunicorn", "it_chatbot_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
