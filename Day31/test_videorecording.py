
from playwright.sync_api import Playwright, sync_playwright, expect


def test_record_video(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)

    context=browser.new_context(
           record_video_dir="videos/",
           record_video_size={"width":1024,"height":768}
    )
    page=context.new_page()

    page.on("request", lambda r: print(">>", r.method, r.url))
    page.on("response", lambda r: print("<<", r.status, r.url))

    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()

    username = page.locator("#loginusername")
    username.click()
    username.press_sequentially("pavanol", delay=150)

    password = page.locator("#loginpassword")
    password.click()
    password.press_sequentially("test@123", delay=150)

    page.keyboard.press("Tab")





    #page.locator('#loginusername').fill('pavanol')
    #page.locator('#loginpassword').fill('test@123')
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Log in").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator('#nameofuser')).to_contain_text('Welcome pavanol')

    context.close()
    browser.close()


