# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Install system dependencies required for Playwright
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libwayland-client0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium firefox webkit

# Install browser dependencies
RUN playwright install-deps

# Copy the entire project
COPY . .

# Create directories for outputs if they don't exist
RUN mkdir -p screenshots reports

# Update pytest.ini to remove --headed flag for Docker (headless by default)
RUN sed -i 's/--headed//g' pytest.ini && sed -i 's/--slowmo=500//g' pytest.ini

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command to run tests (headless mode is default without --headed flag)
CMD ["pytest", "--html=report.html", "--self-contained-html"]
