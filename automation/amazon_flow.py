# Amazon flow to buy a TV
from automation.amazon_bot import AmazonBot
import logging

async def run_amazon_flow(email: str, password: str, mode: bool):
    logging.info(f"Starting Amazon flow for {email} in {mode} headless mode")
    async with AmazonBot(email, password, mode) as bot:
        await bot.login_amazon()
        await bot.search_amazon()
        await bot.add_to_cart_amazon()
        checkout_amazon_text = await bot.checkout_amazon()
        logging.info("Flow fully completed")
        
        return checkout_amazon_text # Checkout text whether the bot reaches the payment page or not
