from pages.inventory_page import InventoryPage


def test_add_one_item_to_cart(inventory_page: InventoryPage):
    """Добавляем один товар и проверяем счётчик корзины."""
    inventory_page.expect_opened()
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.expect_cart_count(1)


def test_add_two_items_to_cart(inventory_page: InventoryPage):
    """Добавляем два товара и проверяем счётчик."""
    inventory_page.expect_opened()
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bike Light")
    inventory_page.expect_cart_count(2)
