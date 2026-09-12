from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object для страницы входа saucedemo.com."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_error(self, text: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(text)
        