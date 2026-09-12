import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def logged_in_page(page):
    """Логинит standard_user и возвращает page."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return page


@pytest.fixture
def inventory_page(logged_in_page):
    """Возвращает InventoryPage после авторизации."""
    return InventoryPage(logged_in_page)
