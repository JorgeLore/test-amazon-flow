from automation.utils import click_if_visible, wait_for_button_and_clic

# Mexican Amazon url
AMAZON_URL = "https://www.amazon.com.mx/"

async def login_amazon(page, email, password):
    await page.goto(AMAZON_URL)
    
    # Initial page before login - not always
    await click_if_visible(page, "Continuar a Compras")

    # 1. Login 
    await page.get_by_role("link", name="Hola, identifícate Cuenta y").click()
    await page.get_by_role("textbox", name="Ingresa tu número de celular").fill(email)
    await page.get_by_role("button", name="Continuar").click()
    await page.get_by_role("textbox", name="Contraseña").fill(password)
    await page.get_by_role("button", name="Iniciar sesión").click()