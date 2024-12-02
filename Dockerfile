# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the templates folder into the container
COPY templates/ /app/templates/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run Gunicorn WSGI server with the Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "ResourceSemaphoreService:app"]
