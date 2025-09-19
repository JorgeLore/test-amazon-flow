import logging

async def add_to_cart_amazon(page):
    # 3. Select first result and add to cart
    see_options_btn = page.get_by_role("link", name="Ver opciones")
    if await see_options_btn.is_visible():
        await see_options_btn.click()
        await page.wait_for_timeout(1000)
    else:
        logging.info("'Ver opciones' button not present")

    add_to_cart_btn = page.get_by_role("button", name="Agregar al Carrito").first 
    await add_to_cart_btn.wait_for(state="visible")
    await page.wait_for_timeout(500)    
    await add_to_cart_btn.click()
    
    no_warranty_btn = page.get_by_role("button", name="No, gracias")
    if await no_warranty_btn.is_visible():
        await no_warranty_btn.click()
        await page.wait_for_timeout(1000)
    else:
        logging.info("Extra warranty not available")
    #await page.locator("#sw-gtc").get_by_role("link", name="Ir al carrito").click()
    
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(500)
    
    await page.get_by_role("link", name="artículo en el carrito").click()