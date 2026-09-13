from playwright.sync_api import Page, expect
from locators.cart_locators import CartLocators
from config.settings import SAUCEDEMO_CART_URL


class CartPage:
    """Page Object для страницы корзины."""

    URL = SAUCEDEMO_CART_URL

    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator(CartLocators.CHECKOUT_BUTTON)
        self.cart_items = page.locator(CartLocators.CART_ITEMS)

    def expect_opened(self):
        expect(self.page).to_have_url(self.URL)

    def expect_items_count(self, count: int):
        expect(self.cart_items).to_have_count(count)

    def proceed_to_checkout(self):
        self.checkout_button.click()