from playwright.sync_api import Page, expect


class CartPage:
    """Page Object для страницы корзины."""

    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.cart_items = page.locator(".cart_item")

    def expect_opened(self):
        expect(self.page).to_have_url(self.URL)

    def expect_items_count(self, count: int):
        expect(self.cart_items).to_have_count(count)

    def proceed_to_checkout(self):
        self.checkout_button.click()
        