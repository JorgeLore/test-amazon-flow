# Script for the API
from fastapi import FastAPI, Request
from automation.amazon_flow import run_amazon_flow
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="log.log",
    filemode="w"
)

app = FastAPI(title="Amazon Bot")

@app.get("/")
def hello_world():
    return {"hola": "mundo"}

@app.post("/simulate-amazon-flow")
async def simulate_amazon_flow(request: Request):
    logging.info("Call API")
    data = await request.json()
    try:
        result = await run_amazon_flow(
            email=data.get("email"),
            password=data.get("correo"),
            mode=data.get("headless")
        )
        return {"status": "success", "details": result}
    except Exception as e:
        logging.error(f"Error en la simulación: {str(e)}")