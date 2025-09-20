import logging

async def checkout_amazon(page):
    # 4. Checkout
    await page.get_by_role("button", name="Proceder al pago Finalizar la").click()
    
    # Get wheter the bot gets to Amazon checkout page
    try:
        checkout_locator = page.locator("#nav-checkout-title-header-text")
        await checkout_locator.wait_for(state="visible")
        checkout_text = await checkout_locator.inner_text()
    except:
        checkout_text = "Error reaching the payment page "
    
    # 5. Postcondition: eliminate the TV added to test this flow multiple times
    await page.get_by_label("Volver al carrito").click()
    await page.get_by_text("Eliminar").click()
    
    return checkout_text.strip()