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

# Install only Chromium browser and its dependencies for faster builds
RUN playwright install --with-deps chromium

# Copy the entire project
COPY . .

# Create directories for outputs if they don't exist
RUN mkdir -p screenshots reports

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command to run tests using CI config (headless mode)
CMD ["pytest", "-c", "pytest-ci.ini", "--html=report.html", "--self-contained-html"]
