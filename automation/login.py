import logging

# Mexican Amazon url
AMAZON_URL = "https://www.amazon.com.mx/"

async def login_amazon(page, email, password):
    await page.goto(AMAZON_URL)
    
    # Initial page before login - not always
    initial_btn = page.get_by_role("button", name="Continuar a Compras")
    if await initial_btn.is_visible():
        await initial_btn.click()
        await page.wait_for_timeout(1000)
    else:
        logging.info("'Continuar a Compras' button not present")

    # 1. Login 
    await page.get_by_role("link", name="Hola, identifícate Cuenta y").click()
    await page.get_by_role("textbox", name="Ingresa tu número de celular").fill(email)
    await page.get_by_role("button", name="Continuar").click()
    await page.get_by_role("textbox", name="Contraseña").fill(password)
    await page.get_by_role("button", name="Iniciar sesión").click()