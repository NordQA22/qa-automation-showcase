from playwright.sync_api import Page, expect


class InventoryPage:
    """Page Object для страницы товаров (каталога) saucedemo.com."""

    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def expect_opened(self):
        """Проверяем, что страница каталога открыта."""
        expect(self.page).to_have_url(self.URL)
        expect(self.title).to_have_text("Products")

    def add_to_cart(self, item_name: str):
        """Добавляем товар в корзину по его названию."""
        item = self.page.locator(".inventory_item", has_text=item_name)
        item.locator("button").click()

    def expect_cart_count(self, count: int):
        """Проверяем количество товаров на иконке корзины."""
        expect(self.cart_badge).to_have_text(str(count))

    def go_to_cart(self):
        """Переходим в корзину."""
        self.cart_link.click()
        