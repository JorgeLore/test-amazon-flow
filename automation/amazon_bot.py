# Amazon bot to navigate from login to checkout
from automation.utils import click_if_visible, wait_for_button_and_clic
from playwright.async_api import async_playwright
import logging

AMAZON_URL = "https://www.amazon.com.mx/"

class AmazonBot:
    """
    This class encapsulates browser setup, navigation, login, and interaction logic
    for simulating a purchase on Amazon. 
    Attributes:
        email (str): Amazon account email.
        password (str): Amazon account password.
        mode (bool): Execution mode. True for headless, False for headed.
    """

    def __init__(self, email: str, password: str, mode: bool):
        self.email = email
        self.password = password
        self.mode = mode
        self.page = None
        self.browser = None
        self.context = None
    
    async def __aenter__(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=self.mode)
        self.context = await self.browser.new_context(viewport={"width": 1920, "height": 1080})
        self.page = await self.context.new_page()
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.browser.close()
        await self.playwright.stop()
    
    async def login_amazon(self):
        await self.page.goto(AMAZON_URL)
        # Initial page before login - not always
        await click_if_visible(self.page, "Continuar a Compras")
        # 1. Login 
        await self.page.get_by_role("link", name="Hola, identifícate Cuenta y").click()
        await self.page.get_by_role("textbox", name="Ingresa tu número de celular").fill(self.email)
        await self.page.get_by_role("button", name="Continuar").click()
        await self.page.get_by_role("textbox", name="Contraseña").fill(self.password)
        await self.page.get_by_role("button", name="Iniciar sesión").click()

    async def search_amazon(self):
    # 2. Search TV
        await wait_for_button_and_clic(self.page, "Abrir el menú de Todas las")
        await self.page.get_by_role("button", name="Electrónicos").click()
        await self.page.get_by_role("link", name="Televisión y Video").nth(1).click()
        await self.page.get_by_role("link", name="Todo en Televisiones").click()
        await self.page.get_by_role("link", name="\" y Más").first.click()
    
    async def add_to_cart_amazon(self):
    # 3. Select first result and add to cart
        await self.page.locator(".a-size-base-plus").first.click()
        await self.page.get_by_role("button", name="Agregar al Carrito").click()
        await click_if_visible(self.page, "No, gracias")
        await self.page.evaluate("window.scrollTo(0, 0)")
        await self.page.wait_for_timeout(500)
        await self.page.get_by_role("link", name="artículo en el carrito").click()
        logging.info("Product added to the cart")
        
    async def checkout_amazon(self):
        # 4. Checkout
        await self.page.get_by_role("button", name="Proceder al pago Finalizar la").click()
        # Get whether the bot gets to Amazon checkout page
        try:
            checkout_locator = self.page.locator("#nav-checkout-title-header-text")
            await checkout_locator.wait_for(state="visible")
            checkout_text = await checkout_locator.inner_text()
            await self.page.wait_for_timeout(1000)
            await self.page.screenshot(path=f"./logs/test_result_{self.mode}_headless_mode.png")
        except Exception as e:
            logging.error("Error accessing the payment page")
            checkout_text = "Error accessing the payment page"
            raise
        # 5. Postcondition: eliminate the TV added to test this flow multiple times
        logging.info("Access to payment page successfully")
        await self.page.get_by_label("Volver al carrito").click()
        await self.page.get_by_text("Eliminar").click()
        
        return checkout_text.strip()