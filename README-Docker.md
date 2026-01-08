# Running Tests with Docker

This guide explains how to run the Playwright tests using Docker.

> **Note**: Docker image is optimized for Chromium only. For multi-browser testing, use GitHub Actions or local pytest.

## Prerequisites

- Docker installed on your system
- Docker Compose (optional, but recommended)

## Quick Start

### Option 1: Using Docker Compose (Recommended)

Build and run tests:
```bash
docker-compose up --build
```

Run tests and remove container after:
```bash
docker-compose up --build --abort-on-container-exit
```

### Option 2: Using Docker CLI

Build the Docker image:
```bash
docker build -t playwright-tests .
```

Run all tests:
```bash
docker run --rm -v ${PWD}/screenshots:/app/screenshots -v ${PWD}/report.html:/app/report.html playwright-tests
```

Run specific test file:
```bash
docker run --rm -v ${PWD}/screenshots:/app/screenshots playwright-tests pytest tests/test_text_box.py
```

Run with custom pytest options:
```bash
docker run --rm playwright-tests pytest tests/ --browser firefox
```

## Accessing Test Results

After running tests, you can access:
- **HTML Report**: `report.html` in your project directory
- **Screenshots**: In the `screenshots/` directory (for failed tests)

## Advanced Usage

### Running Interactive Shell in Container

```bash
docker run --rm -it playwright-tests /bin/bash
```

### Running with Different Browsers

```bash
docker run --rm playwright-tests pytest --browser firefox
docker run --rm playwright-tests pytest --browser webkit
```

### Running Specific Tests

Run a single test file:
```bash
docker run --rm playwright-tests pytest tests/test_buttons.py
```

Run tests with specific markers or filters:
```bash
docker run --rm playwright-tests pytest -k "test_name"
```

## Troubleshooting

### Container Exits Immediately
Make sure the Dockerfile CMD or your docker run command includes the test execution command.

### Tests Fail with Browser Launch Errors
Ensure all browser dependencies are installed. The Dockerfile includes `playwright install-deps` to handle this.

### Permission Issues with Volumes
On Linux/Mac, you may need to adjust permissions for the mounted volumes:
```bash
chmod 777 screenshots/
```

## Notes

- Tests run in **headless mode** by default in Docker (no GUI)
- The pytest.ini configuration is modified during Docker build to remove `--headed` flag
- To run in headed mode, you would need to add `--headed` flag and configure X11 forwarding (advanced)
- All three browsers (Chromium, Firefox, WebKit) are pre-installed in the image
