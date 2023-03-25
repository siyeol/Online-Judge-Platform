# # Use the official Python image as the base image
# FROM python:3.8-slim

# RUN mkdir /app

# # Set the working directory
# WORKDIR /app

# # Install build dependencies
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends gcc python3-dev && \
#     rm -rf /var/lib/apt/lists/*

# # Copy the requirements file into the container
# COPY requirements.txt .

# # Install the required packages
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code
# COPY . .

# # Expose the port the app will run on
# EXPOSE 8000

# ENV PYTHONPATH /app

# # Start the application
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "back.oj.wsgi:application"]


# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]