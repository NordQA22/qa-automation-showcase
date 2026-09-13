import allure
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
@allure.title("Locked-out user cannot log in")
@allure.severity(allure.severity_level.NORMAL)
def test_locked_out_user(page: Page):
    """Заблокированный пользователь не может войти."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(LOCKED_OUT_USER["username"], LOCKED_OUT_USER["password"])

    login_page.expect_error("Sorry, this user has been locked out")


@allure.feature("Login")
@allure.story("Negative login")
@allure.title("Wrong password shows error message")
@allure.severity(allure.severity_level.NORMAL)
def test_wrong_password(page: Page):
    """Ошибка при неверном пароле."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(WRONG_PASSWORD_USER["username"], WRONG_PASSWORD_USER["password"])

    login_page.expect_error("Username and password do not match")
