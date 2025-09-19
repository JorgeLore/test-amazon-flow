# Amazon flow to buy a TV
from playwright.async_api import async_playwright
import logging

AMAZON_URL = "https://www.amazon.com.mx/"

async def run_amazon_flow(email: str, password: str, mode: bool):
    logging.info("Iniciando flujo de Amazon")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        await page.goto(AMAZON_URL)
        logging.info("Finaliza flujo")
        
        return "Flujo completado"
