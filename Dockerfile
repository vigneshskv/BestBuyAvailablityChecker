FROM python:3.8.0-buster

# Make directory for application
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY /app .

# Run the application
CMD ["python", "/app/scrape.py"]