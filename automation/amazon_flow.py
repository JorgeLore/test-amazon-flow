# Amazon flow to buy a TV
from playwright.async_api import async_playwright
from automation.login import login_amazon
from automation.search import search_amazon
from automation.cart import add_to_cart_amazon
from automation.checkout import checkout_amazon
import logging

async def run_amazon_flow(email: str, password: str, mode: bool):
    logging.info(f"Starting Amazon flow for {email} in {mode} headless mode")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=mode)
        context = await browser.new_context()
        page = await context.new_page()

        await login_amazon(page, email, password)
        await search_amazon(page)
        await add_to_cart_amazon(page)
        checkout_amazon_text = await checkout_amazon(page)
        
        logging.info("Flow fully completed")
        
        return checkout_amazon_text
