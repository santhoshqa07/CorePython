from playwright.sync_api import expect

from AI_Testing.demo_home_page import DemoBlazeHomePage
from AI_Testing.demo_login_page import DemoBlazeLoginPage


def test_demo_login_logout(page):
    home_page = DemoBlazeHomePage(page)
    login_page = DemoBlazeLoginPage(page)

    home_page.open()
    home_page.click_login()

    login_page.login("pavanol", "test@123")

    expect(home_page.logout_link).to_be_visible()
    home_page.assert_welcome_message("pavanol")

    home_page.click_logout()

    expect(home_page.login_link).to_be_visible()
