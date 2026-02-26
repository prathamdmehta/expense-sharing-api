FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app/expense_sharing

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy & install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ENTIRE project (manage.py will be in /app/)
COPY . .

# Run migrations first, then server
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]