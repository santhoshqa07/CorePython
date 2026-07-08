from playwright.sync_api import sync_playwright, expect, Playwright

def test_AssgnOrangeHrm(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.on("page", lambda page:page.wait_for_load_state())

    page.locator("a[href='http://www.orangehrm.com']").click()

    page.wait_for_timeout(5000)

    all_pages = context.pages

    print("The title of the parent page:" , all_pages[0].title())
    print("The Url of the parent page:", all_pages[0].url)

    print("The title of the child page:" , all_pages[1].title())
    print("The Url of the child page:", all_pages[1].url)

    parent_page = all_pages[0]

    Username = parent_page.locator("input[placeholder='Username']")
    Username.fill("admin")
    Password = parent_page.locator("input[placeholder='Password']")
    Password.fill("admin123")

    page.wait_for_timeout(5000)

    Login = parent_page.locator("button[type='submit']")
    Login.click()

    page.wait_for_load_state()

    child_page = all_pages[1]


    ContactSales =child_page.locator("a[href='/contact-sales']").all()

    ContactSales[0].click()

    page.wait_for_timeout(5000)


    context.close()
    browser.close()

    





