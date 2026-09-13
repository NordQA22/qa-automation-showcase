from playwright.sync_api import Page, expect
from locators.inventory_locators import InventoryLocators
from config.settings import SAUCEDEMO_INVENTORY_URL


class InventoryPage:
    """Page Object для страницы товаров (каталога) saucedemo.com."""

    URL = SAUCEDEMO_INVENTORY_URL

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(InventoryLocators.TITLE)
        self.cart_badge = page.locator(InventoryLocators.CART_BADGE)
        self.cart_link = page.locator(InventoryLocators.CART_LINK)

    def expect_opened(self):
        expect(self.page).to_have_url(self.URL)
        expect(self.title).to_have_text("Products")

    def add_to_cart(self, item_name: str):
        item = self.page.locator(InventoryLocators.INVENTORY_ITEM, has_text=item_name)
        item.locator(InventoryLocators.ITEM_BUTTON).click()

    def expect_cart_count(self, count: int):
        expect(self.cart_badge).to_have_text(str(count))

    def go_to_cart(self):
        self.cart_link.click()
