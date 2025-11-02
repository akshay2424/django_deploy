# Use official Python image as base
FROM python:3.10-slim

# Set work directory inside container
WORKDIR /app

# Prevent Python from buffering output (good for logs)
ENV PYTHONUNBUFFERED=1

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Default command to run Django
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "drf_demo.wsgi:application", "--bind", "0.0.0.0:8000"]

