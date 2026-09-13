import allure
import pytest
from playwright.sync_api import Page, expect
from config.credentials import STANDARD_USER, LOCKED_OUT_USER, WRONG_PASSWORD_USER
from pages.login_page import LoginPage


@allure.feature("Login")
@allure.story("Successful login")
@allure.title("User can log in with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_login(page: Page):
    """Проверяем успешный вход standard_user."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


@allure.feature("Login")
@allure.story("Negative login")
@allure.title("Login fails with invalid credentials")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("user,expected_error", [
    (LOCKED_OUT_USER, "Sorry, this user has been locked out"),
    (WRONG_PASSWORD_USER, "Username and password do not match"),
])
def test_login_errors(page: Page, user, expected_error):
    """Параметризованная проверка ошибок входа."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(user["username"], user["password"])

    login_page.expect_error(expected_error)
