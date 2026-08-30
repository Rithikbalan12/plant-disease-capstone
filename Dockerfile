FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for image processing
RUN apt-get update && \
    apt-get install -y --no-install-recommends libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Render assigns the port via the PORT env variable
ENV PORT=8000
EXPOSE 8000

# Start the FastAPI server using the PORT env variable
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT