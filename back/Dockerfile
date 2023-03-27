# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev nginx && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files
COPY . .

# Expose the port the app runs on
EXPOSE 80 8000

# Copy the Nginx configuration file
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

# Start Gunicorn and Nginx using a script
COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]