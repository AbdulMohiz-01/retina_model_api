# Use a slim Python 3.9 image as the base
FROM python:3.9-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file initially to leverage Docker cache
COPY requirements.txt .

# Install dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port on which your Flask app will run (replace 5000 with your port)
EXPOSE 5000

# Specify the command to run your Flask application
CMD ["python", "app.py"]
