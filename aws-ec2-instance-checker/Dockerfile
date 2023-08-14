# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy necessary files and directories
COPY app.py .
COPY templates ./templates

# Create flask_session directory
RUN mkdir flask_session 

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
