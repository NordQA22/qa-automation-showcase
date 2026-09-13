import allure
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@allure.feature("Cart")
@allure.story("Empty cart")
@allure.title("Cart is empty by default")
@allure.severity(allure.severity_level.NORMAL)
def test_cart_is_empty_by_default(inventory_page: InventoryPage):
    """Корзина пуста по умолчанию."""
    inventory_page.go_to_cart()

    cart_page = CartPage(inventory_page.page)
    cart_page.expect_opened()
    cart_page.expect_items_count(0)


@allure.feature("Cart")
@allure.story("Empty cart")
@allure.title("Empty cart has no badge")
@allure.severity(allure.severity_level.MINOR)
def test_empty_cart_has_no_badge(inventory_page: InventoryPage):
    """При пустой корзине счётчик отсутствует."""
    from playwright.sync_api import expect
    expect(inventory_page.cart_badge).not_to_be_visible()
