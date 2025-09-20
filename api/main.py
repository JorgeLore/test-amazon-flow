# Script for the API
from fastapi import FastAPI, HTTPException
from automation.amazon_flow import run_amazon_flow
from config.data_model import PurchaseRequest
from config.logger import setup_logger
import logging

# Initialize logger
setup_logger()

# Initialize FastAPI app
app = FastAPI(title="Amazon Bot")

# Test Endpoint
@app.get("/")
def hello_world():
    return {"hello": "world"}

# Main Endpoint for Amazon flow
@app.post("/simulate-amazon-flow")
async def simulate_amazon_flow(data: PurchaseRequest):
    logging.info("Calling API ...")
    try:
        result = await run_amazon_flow(
            email=data.email,
            password=data.password,
            mode=data.headless
        )
        return {"status": "success", "details": result}
    except Exception as e:
        logging.error(f"Simulation Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Purchase simulation error")
        