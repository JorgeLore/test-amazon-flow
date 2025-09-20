from automation.utils import click_if_visible, wait_for_button_and_clic

async def add_to_cart_amazon(page):
    # 3. Select first result and add to cart
    await click_if_visible(page, "Ver opciones")
    await wait_for_button_and_clic(page, "Agregar al Carrito")
    await click_if_visible(page, "No, gracias")
    
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(500)
    
    await page.get_by_role("link", name="artículo en el carrito").click()