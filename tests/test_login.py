from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_successful_login(page: Page):
    """Проверяем успешный вход standard_user."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_locked_out_user(page: Page):
    """Заблокированный пользователь не может войти."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    login_page.expect_error("Sorry, this user has been locked out")


def test_wrong_password(page: Page):
    """Ошибка при неверном пароле."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")

    login_page.expect_error("Username and password do not match")
