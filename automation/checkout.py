import logging

async def checkout_amazon(page):
    # 4. Checkout
    await page.get_by_role("button", name="Proceder al pago Finalizar la").click()
    
    # 5. Postcondition: eliminate the TV added to test this flow multiple times
    await page.get_by_label("Volver al carrito").click()
    await page.get_by_text("Eliminar").click()