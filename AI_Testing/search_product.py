import pytest
from playwright.sync_api import Page, expect


def test_shared_hosting_navigation(page: Page):
    # Step 1: Open the website
    page.goto('https://www.inmotionhosting.com/', wait_until='load')
    page.wait_for_load_state('networkidle')

    # Step 2: Click the Products menu item
    products = page.locator('text=Products')
    if products.count() > 0:
        products.first.click(timeout=5000)
    else:
        page.locator("button[aria-label*='menu']").first.click(timeout=5000)

    # Step 3: Click Shared Hosting
    shared_hosting = page.locator('text=Shared Hosting')
    if shared_hosting.count() > 0:
        shared_hosting.first.click(timeout=8000)
    else:
        page.goto('https://www.inmotionhosting.com/shared-hosting', wait_until='load')

    # Step 4: Check if the page heading is visible
    expected_text = 'Scalable Hosting With Everything You Need'
    expect(page.get_by_text(expected_text)).to_be_visible(timeout=15000)


