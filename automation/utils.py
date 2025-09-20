import logging

async def wait_for_button_and_clic(page, btn_name):
    btn = page.get_by_role("button", name=btn_name).first
    await btn.wait_for(state="visible")
    await btn.hover()
    await page.wait_for_timeout(500)
    await btn.click()

async def click_if_visible(page, btn_name):
    btn = page.get_by_role("button", name=btn_name)
    if await btn.is_visible():
        await btn.click()
        await page.wait_for_timeout(1000)
    else:
        logging.info(f"'{btn_name}' button not present")
