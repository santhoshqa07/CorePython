from playwright.sync_api import Page, expect

from AI_Testing.base_page import BasePage


class DemoBlazeLoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#loginusername")
        self.password_input = page.locator("#loginpassword")
        self.login_button = page.get_by_role("button", name="Log in")
        self.modal = page.locator("#logInModal")

    def login(self, username: str, password: str):
        expect(self.modal).to_be_visible()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
