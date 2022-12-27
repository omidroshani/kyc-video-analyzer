FROM python:3.8-slim

ENV PYTHONUNBUFFERED True

# Copy requirements.txt to the docker image and install packages
COPY requirements.txt /
RUN pip install -r requirements.txt

# Set the WORKDIR to be the folder
COPY . /app

# Expose port 5000
EXPOSE 8080
ENV PORT 8080
WORKDIR /app

# Use gunicorn as the entrypoint
CMD exec gunicorn --bind :$PORT main_v1:app --workers 1 --threads 1 --timeout 60