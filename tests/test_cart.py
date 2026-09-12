from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_one_item_to_cart(page: Page):
    """Добавляем один товар и проверяем счётчик корзины."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.expect_opened()
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.expect_cart_count(1)


def test_add_two_items_to_cart(page: Page):
    """Добавляем два товара и проверяем счётчик."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bike Light")
    inventory_page.expect_cart_count(2)
