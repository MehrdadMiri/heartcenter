# Base image
FROM python:3.10-slim-bullseye

# Set work directory
WORKDIR /app

RUN apt update
RUN apt install -y gettext
# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Copy project files
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Run migrations and start Django
CMD ["python", "manage.py", "migrate"] && \
    ["python", "manage.py", "runserver", "0.0.0.0:8000"]