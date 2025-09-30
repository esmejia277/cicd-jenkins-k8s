# Use a Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your code
COPY . /app/

# Create a virtual environment and install dependencies
RUN python -m venv venv && venv/bin/pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# Start your application by calling the executable directly
CMD ["/app/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
