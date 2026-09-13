import allure
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def _go_to_checkout(inventory_page: InventoryPage) -> CheckoutPage:
    """Хелпер: добавляет товар и открывает страницу checkout."""
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(inventory_page.page)
    cart_page.proceed_to_checkout()

    return CheckoutPage(inventory_page.page)


@allure.feature("Checkout")
@allure.story("Negative scenarios")
@allure.title("Checkout fails when first name is empty")
@allure.severity(allure.severity_level.NORMAL)
def test_checkout_without_first_name(inventory_page: InventoryPage):
    """Ошибка при пустом имени."""
    checkout_page = _go_to_checkout(inventory_page)
    checkout_page.fill_customer_info("", "Taran", "123456")
    checkout_page.continue_to_overview()

    checkout_page.expect_error("Error: First Name is required")


@allure.feature("Checkout")
@allure.story("Negative scenarios")
@allure.title("Checkout fails when last name is empty")
@allure.severity(allure.severity_level.NORMAL)
def test_checkout_without_last_name(inventory_page: InventoryPage):
    """Ошибка при пустой фамилии."""
    checkout_page = _go_to_checkout(inventory_page)
    checkout_page.fill_customer_info("Ivan", "", "123456")
    checkout_page.continue_to_overview()

    checkout_page.expect_error("Error: Last Name is required")


@allure.feature("Checkout")
@allure.story("Negative scenarios")
@allure.title("Checkout fails when postal code is empty")
@allure.severity(allure.severity_level.NORMAL)
def test_checkout_without_postal_code(inventory_page: InventoryPage):
    """Ошибка при пустом индексе."""
    checkout_page = _go_to_checkout(inventory_page)
    checkout_page.fill_customer_info("Ivan", "Taran", "")
    checkout_page.continue_to_overview()

    checkout_page.expect_error("Error: Postal Code is required")
