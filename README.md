# DemoQA Playwright Test Automation

A simple Playwright pytest project demonstrating automated UI testing on [demoqa.com](https://demoqa.com/).

## Features

- **Page Object Model** design pattern for maintainable test code
- **pytest** framework with Playwright integration
- **Automated screenshot capture** on test failures
- **HTML test reports** for easy result analysis

## Test Scenarios

### Text Box (`test_text_box.py`)
- Form filling and submission
- Output validation
- Element visibility checks

### Buttons (`test_buttons.py`)
- Double-click interactions
- Right-click (context menu) interactions
- Single-click events
- Multiple button types in sequence

### Web Tables (`test_web_tables.py`)
- Adding new table records
- Search functionality
- Table data validation

### Accessibility (`test_accessibility.py`)
- Page title and heading hierarchy
- Form labels and ARIA attributes
- Keyboard navigation and focus management
- Color contrast and semantic HTML
- Accessibility tree validation
- Screen reader compatibility

### Responsive Design (`test_responsive.py`)
- Mobile viewports (iPhone SE, iPhone 12/13)
- Tablet viewports (iPad portrait/landscape)
- Laptop screens (1366x768, 1440x900)
- Desktop displays (Full HD, 2K)
- Cross-device form accessibility
- Layout adaptation and scroll behavior

### Alerts & JavaScript Dialogs (`test_alerts.py`)
- Simple JavaScript alerts
- Timed alerts (delayed appearance)
- Confirm dialogs (OK/Cancel)
- Prompt dialogs with text input
- Alert message validation
- Sequential dialog handling

## Project Structure

```
Python-demo/
├── tests/
│   ├── test_text_box.py       # Text box form tests
│   ├── test_buttons.py        # Button interaction tests
│   ├── test_web_tables.py     # Web table CRUD tests
│   ├── test_accessibility.py  # Accessibility & a11y tests
│   ├── test_responsive.py     # Responsive design tests
│   └── test_alerts.py         # JavaScript alerts & dialogs
├── pages/
│   ├── text_box_page.py       # Text box page object
│   ├── buttons_page.py        # Buttons page object
│   ├── web_tables_page.py     # Web tables page object
│   ├── accessibility_page.py  # Accessibility page object
│   ├── responsive_page.py     # Responsive design page object
│   └── alerts_page.py         # Alerts handling page object
├── conftest.py                # pytest configuration & fixtures
├── pytest.ini                 # pytest settings
└── requirements.txt           # Project dependencies
```

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## Running Tests

**Run all tests (headed mode with slow motion):**
```bash
pytest
```

**Run specific test file:**
```bash
pytest tests/test_buttons.py
```

**Run in headless mode:**
```bash
pytest --headless
```

**Generate HTML report:**
```bash
pytest --html=reports/report.html --self-contained-html
```

**Run with different browser:**
```bash
pytest --browser firefox
pytest --browser webkit
```

**Run responsive tests only:**
```bash
pytest tests/test_responsive.py -v
```

## Configuration

Default settings in `pytest.ini`:
- Base URL: `https://demoqa.com`
- Browser: Chromium (headed mode)
- Slow motion: 500ms (easier to observe test execution)

Modify these settings via command line or update `pytest.ini`.

## Requirements

- Python 3.8+
- pytest 8.3.4+
- playwright 1.49.1+
- pytest-playwright 0.6.2+
