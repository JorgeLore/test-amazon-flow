import logging

async def search_amazon(page):
    # 2. Search TV
    boton = page.get_by_role("button", name="Abrir el menú de Todas las")
    await boton.wait_for(state="visible")
    await boton.hover()
    await page.wait_for_timeout(500)
    await boton.click()
    
    await page.get_by_role("button", name="Electrónicos").click()
    await page.get_by_role("link", name="Televisión y Video").nth(1).click()
    await page.get_by_role("link", name="Todo en Televisiones").click()
    await page.get_by_role("link", name="\" y Más").first.click()