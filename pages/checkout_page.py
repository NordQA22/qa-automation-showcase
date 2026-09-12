from playwright.sync_api import Page, expect
from locators.checkout_locators import CheckoutLocators


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator(CheckoutLocators.FIRST_NAME)
        self.last_name = page.locator(CheckoutLocators.LAST_NAME)
        self.postal_code = page.locator(CheckoutLocators.POSTAL_CODE)
        self.continue_button = page.locator(CheckoutLocators.CONTINUE_BUTTON)
        self.finish_button = page.locator(CheckoutLocators.FINISH_BUTTON)
        self.complete_header = page.locator(CheckoutLocators.COMPLETE_HEADER)

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_to_overview(self):
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def expect_order_complete(self):
        expect(self.complete_header).to_have_text("Thank you for your order!")
