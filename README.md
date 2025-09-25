# Amazon Purchase Flow Automation with Playwright

This project simulates a purchase flow on Amazon by using Playwright with Python. The flow includes:
- Amazon login
- Search for the first TV result
- Add to cart
- Checkout simulation

This project uses a API Rest with FastAPI to execute the flow, the data input are:
- Email
- Password
- Headless mode (True or False)

## Technology

- [Python ≥ 3.8](https://www.python.org/)
- [Playwright](https://playwright.dev/python/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)
- [pytest-playwright](https://pypi.org/project/pytest-playwright/)

## Initial Setup

Initial project setup, configs and installation of dependencies:

#### 1. Clone this repository
```bash
git clone https://github.com/JorgeLore/test-amazon-flow
cd test-amazon-flow
```
#### 2. Create and activate a virtual enviroment
```bash
python -m venv venv
venv\Scripts\activate
```
#### 3. Install dependencies or libraries
```bash
pip install -r requirements.txt
```
#### 4. Install Playwright drivers
```bash
playwright install
```
#### 5. Copy the .env.example to a .env and add your Amazon credentials

## Deployment

To deploy this project run:

#### 1. Start the API
```bash
uvicorn api.main:app
```
#### 2. Execute pytest file (test_amazon_flow.py) with:
```bash
pytest -v
```

## Notes

This project doesn't perform actual purchases, it only simulates the flow.

## Author

Project developed by [@JorgeLore](https://github.com/JorgeLore)
