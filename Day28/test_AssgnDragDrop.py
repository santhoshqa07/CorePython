import pytest
from playwright.sync_api import Page,expect

def test_DragAndDrop(page:Page):
    page.goto("https://demo.guru99.com/test/drag_drop.html")

    # Drag AND DROP dEBIT SIDE

    Source_Bank= page.locator("li[id='credit2'] a[class='button button-orange']")
    Target_Deb_Acc= page.locator("#bank li[class=placeholder]")

    Source_Bank.drag_to(Target_Deb_Acc)

    page.wait_for_timeout(3000)

    bank = page.locator("ol[id='bank'] li")
    text= bank.inner_text()


    expect(bank).to_have_text(text)

    source_Amt1 = page.locator("section[id='g-container-main'] li:nth-child(4) a")
    target_Amt1 = page.locator("ol[id='amt7'] li[class='placeholder']")

    source_Amt1.drag_to(target_Amt1)

    page.wait_for_timeout(3000)

    Amt1 = page.locator("ol[id='amt7'] li")
    text_Amt1 = Amt1.inner_text()

    expect(Amt1).to_have_text(text_Amt1)

    # Drag AND DROP CREDIT SIDE

    Source_Sales = page.locator("li[id='credit1'] a")
    Target_Cred_Acc = page.locator("ol[id='loan'] li[class='placeholder']")

    Source_Sales.drag_to(Target_Cred_Acc)

    page.wait_for_timeout(3000)

    sales = page.locator("ol[id='loan'] li")
    text_Sales = sales.inner_text()
    expect(sales).to_have_text(text_Sales)


    source_Amt2= page.locator("section[id='g-container-main'] li:nth-child(4) a")
    target_Amt2 = page.locator("ol[id='amt8'] li[class='placeholder']")

    source_Amt2.drag_to(target_Amt2)

    page.wait_for_timeout(3000)

    Amt2= page.locator("ol[id='amt8'] li")
    text_Amt2 = Amt2.inner_text()
    expect(Amt2).to_have_text(text_Amt2)


