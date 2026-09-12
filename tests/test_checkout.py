from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_full_checkout_flow(inventory_page: InventoryPage):
    """Полный сценарий: логин → товар → корзина → оформление → заказ."""
    inventory_page.expect_opened()
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.expect_cart_count(1)
    inventory_page.go_to_cart()

    cart_page = CartPage(inventory_page.page)
    cart_page.expect_opened()
    cart_page.expect_items_count(1)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(inventory_page.page)
    checkout_page.fill_customer_info("Ivan", "Taran", "123456")
    checkout_page.continue_to_overview()
    checkout_page.finish_order()
    checkout_page.expect_order_complete()
