from playwright.sync_api import Page, expect

from AI_Testing.base_page import BasePage


class DemoBlazeHomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_link = page.locator("#login2")
        self.logout_link = page.locator("#logout2")
        self.welcome_user = page.locator("#nameofuser")

    def open(self):
        super().open("https://www.demoblaze.com/index.html")

    def click_login(self):
        self.login_link.click()

    def is_login_link_visible(self):
        return self.login_link.is_visible()

    def is_logout_link_visible(self):
        return self.logout_link.is_visible()

    def get_welcome_text(self):
        return self.welcome_user.inner_text()

    def assert_welcome_message(self, username: str):
        expect(self.welcome_user).to_contain_text(f"Welcome {username}")

    def click_logout(self):
        self.logout_link.click()
