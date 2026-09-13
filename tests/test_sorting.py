import allure
from pages.inventory_page import InventoryPage


@allure.feature("Sorting")
@allure.story("Sort by name")
@allure.title("Sort products A to Z")
@allure.severity(allure.severity_level.NORMAL)
def test_sort_by_name_asc(inventory_page: InventoryPage):
    """Сортировка по имени от A до Z."""
    inventory_page.sort_by("az")
    names = inventory_page.get_item_names()
    assert names == sorted(names)


@allure.feature("Sorting")
@allure.story("Sort by name")
@allure.title("Sort products Z to A")
@allure.severity(allure.severity_level.NORMAL)
def test_sort_by_name_desc(inventory_page: InventoryPage):
    """Сортировка по имени от Z до A."""
    inventory_page.sort_by("za")
    names = inventory_page.get_item_names()
    assert names == sorted(names, reverse=True)


@allure.feature("Sorting")
@allure.story("Sort by price")
@allure.title("Sort products by price low to high")
@allure.severity(allure.severity_level.NORMAL)
def test_sort_by_price_asc(inventory_page: InventoryPage):
    """Сортировка по цене от низкой к высокой."""
    inventory_page.sort_by("lohi")
    prices = inventory_page.get_item_prices()
    assert prices == sorted(prices)


@allure.feature("Sorting")
@allure.story("Sort by price")
@allure.title("Sort products by price high to low")
@allure.severity(allure.severity_level.NORMAL)
def test_sort_by_price_desc(inventory_page: InventoryPage):
    """Сортировка по цене от высокой к низкой."""
    inventory_page.sort_by("hilo")
    prices = inventory_page.get_item_prices()
    assert prices == sorted(prices, reverse=True)
    