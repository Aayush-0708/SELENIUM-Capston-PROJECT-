# Selenium Capstone Project

This project contains Selenium automation tests for an e-commerce purchase flow on the Demo e-commerce website.

## Project Overview

The automation validates:
- User login
- Product search
- Add to cart
- Cart quantity update
- Final checkout flow verification

## Tech Stack
- Python
- Selenium WebDriver
- Pytest
- ChromeDriver

## Project Structure

```text
Selenium_Capstone_project/
├── tests/
│   ├── test_login.py
│   └── test_ecommerce.py
├── test_data/
│   ├── __init__.py
│   ├── config.py
│   └── test_data.json
├── screenshots/
├── reports/
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure Chrome/Chromedriver is installed and available in PATH.

## Run Tests

```bash
pytest -q
```

You can also run a specific test file:

```bash
pytest tests/test_ecommerce.py -q
```

## Notes

- Test data is stored in `test_data/test_data.json`.
- Screenshots are saved under the `screenshots/` folder.
- Reports are generated in the `reports/` folder.

## Author

Aayush Mahi
