from automation.utils import click_if_visible, wait_for_button_and_clic

async def search_amazon(page):
    # 2. Search TV
    await wait_for_button_and_clic(page, "Abrir el menú de Todas las")
    
    await page.get_by_role("button", name="Electrónicos").click()
    await page.get_by_role("link", name="Televisión y Video").nth(1).click()
    await page.get_by_role("link", name="Todo en Televisiones").click()
    await page.get_by_role("link", name="\" y Más").first.click()