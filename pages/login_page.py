from playwright.sync_api import Page, expect
from locators.login_locators import LoginLocators
from config.settings import SAUCEDEMO_URL


class LoginPage:
    """Page Object для страницы входа saucedemo.com."""

    URL = SAUCEDEMO_URL

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator(LoginLocators.USERNAME_INPUT)
        self.password_input = page.locator(LoginLocators.PASSWORD_INPUT)
        self.login_button = page.locator(LoginLocators.LOGIN_BUTTON)
        self.error_message = page.locator(LoginLocators.ERROR_MESSAGE)

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_error(self, text: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(text)
