# Amazon bot to navigate from login to checkout
from automation.utils import click_if_visible, wait_for_button_and_clic
from playwright.async_api import async_playwright

AMAZON_URL = "https://www.amazon.com.mx/"

class AmazonBot:
    def __init__(self, email: str, password: str, mode: bool):
        self.email = email
        self.password = password
        self.mode = mode
        self.page = None
        self.browser = None
    
    async def __aenter__(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=self.mode)
        self.page = await self.browser.new_page()
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
        await click_if_visible(self.page, "Ver opciones")
        await wait_for_button_and_clic(self.page, "Agregar al Carrito")
        await click_if_visible(self.page, "No, gracias")
        await self.page.evaluate("window.scrollTo(0, 0)")
        await self.page.wait_for_timeout(500)
        await self.page.get_by_role("link", name="artículo en el carrito").click()
        
    async def checkout_amazon(self):
        # 4. Checkout
        await self.page.get_by_role("button", name="Proceder al pago Finalizar la").click()
        # Get whether the bot gets to Amazon checkout page
        try:
            checkout_locator = self.page.locator("#nav-checkout-title-header-text")
            await checkout_locator.wait_for(state="visible")
            checkout_text = await checkout_locator.inner_text()
        except:
            checkout_text = "Error reaching the payment page "
        # 5. Postcondition: eliminate the TV added to test this flow multiple times
        await self.page.get_by_label("Volver al carrito").click()
        await self.page.get_by_text("Eliminar").click()
        
        return checkout_text.strip()