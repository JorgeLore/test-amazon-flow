# Script for the API
from fastapi import FastAPI, Request
from automation.amazon_flow import run_amazon_flow
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="log.log",
    filemode="w"
)

# Initialize FastAPI app
app = FastAPI(title="Amazon Bot")

# Test Endpoint
@app.get("/")
def hello_world():
    return {"hello": "world"}

# Main Endpoint for Amazon flow
@app.post("/simulate-amazon-flow")
async def simulate_amazon_flow(request: Request):
    logging.info("Call API")
    data = await request.json()
    try:
        result = await run_amazon_flow(
            email=data.get("email"),
            password=data.get("password"),
            mode=data.get("headless")
        )
        return {"status": "success", "details": result}
    except Exception as e:
        logging.error(f"Error en la simulación: {str(e)}")