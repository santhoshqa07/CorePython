from playwright.sync_api import Playwright, Page, expect
#
# def test_login_functionality(playwright: Playwright):
#     # Create a new browser context
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#
#     # Create a new page
#     page = context.new_page()
#
#     # Navigate to the login page
#     page.goto("https://www.demoblaze.com/")
#
#     # Click on the login link
#     page.locator("#login2").click()
#
#     # Fill in the username and password fields
#     page.locator("#loginusername").fill("testuser")
#     page.locator("#loginpassword").fill("testpassword")
#
#     # Click the login button
#     page.locator("button[onclick='logIn()']").click()
#
#     # Wait for some time to observe the result (optional)
#     page.wait_for_timeout(5000)
#
#     # Close the browser context and browser
#     context.close()
#     browser.close()
from playwright.sync_api import Playwright, Page, expect
#
# def test_login_functionality(playwright: Playwright):
#     # Create a new browser context
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#
#     # Create a new page
#     page = context.new_page()
#
#     # Navigate to the login page
#     page.goto("https://www.demoblaze.com/")
#
#     # Click on the login link
#     page.locator("#login2").click()
#
#     # Fill in the username and password fields
#     page.locator("#loginusername").fill("testuser")
#     page.locator("#loginpassword").fill("testpassword")
#
#     # Click the login button
#     page.locator("button[onclick='logIn()']").click()
#
#     # Wait for some time to observe the result (optional)
#     page.wait_for_timeout(5000)
#
#     # Close the browser context and browser
#     context.close()
#     browser.close()

def test_verifyPageUrl(page: Page):
    page.goto("https://www.automationpractice.pl/index.php")
    #Q: Verify the URL of the application
    myurl=page.url

    print("URL of the application", myurl)
    expect(page).to_have_url("https://www.automationpractice.pl/index.php")
