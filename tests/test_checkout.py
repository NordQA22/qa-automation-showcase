from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_full_checkout_flow(page: Page):
    """Полный сценарий: логин → товар → корзина → оформление → заказ."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.expect_cart_count(1)
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.expect_opened()
    cart_page.expect_items_count(1)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_customer_info("Ivan", "Taran", "123456")
    checkout_page.continue_to_overview()
    checkout_page.finish_order()
    checkout_page.expect_order_complete()
