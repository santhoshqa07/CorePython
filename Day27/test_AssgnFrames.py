import pytest
from playwright.sync_api import Page, expect

def test_assgn_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames = page.frames
    print("Number of frames on a page:", len(frames))  # 7

    frame3 = page.frame(url= "https://ui.vision/demo/webtest/frames/frame_3")
    frame3_Inptbox = frame3.locator("[name='mytext3']")
    frame3_Inptbox.fill("Santhosh Kumar")


    child_frames = frame3.child_frames
    print("Number of childframes on frame3:", len(child_frames))

    inner_frame = child_frames[0]

    #Check radio
    radio = inner_frame.get_by_label("I am a human")
    radio.click()
    expect(radio).to_be_checked()

    page.wait_for_timeout(3000)

    #Check Checkboxes How do you plan to use the software?

    checkbox1 = inner_frame.get_by_label("Form Autofilling")
    checkbox1.click()

    page.wait_for_timeout(3000)

    #click on the next button

    Nxt_Btn = inner_frame.get_by_role("button", name="Next")
    Nxt_Btn.click()

    page.wait_for_timeout(3000)

    #Enter a short text
    Shrt_txt = inner_frame.locator("input[type='text']")
    Shrt_txt.fill("Welcome to my Area")

    page.wait_for_timeout(2000)

    # Enter a long answer
    long_answer = inner_frame.locator("textarea[aria-label='Your answer']")
    long_answer.fill("Python is both the structured oriented and object oriented programming language")
    page.wait_for_timeout(2000)

    # click on submit button
    #sub_btn = inner_frame.get_by_label("Submit")
    #span[class='NPEfkd RveJvd snByac']
    sub_btn = inner_frame.locator("div[aria-label='Submit']")
    sub_btn.click()
    page.wait_for_timeout(2000)

    #Entering into Frame5
    frame5 = page.frame(url= "https://ui.vision/demo/webtest/frames/frame_5")
    frame5_InputBox = frame5.locator("[name='mytext5']")
    frame5_InputBox.fill("Sankar Narayana")

    expect(frame5_InputBox).to_have_value("Sankar Narayana")

    #Clicking on the link in frame 5
    frame5.locator("a[href='https://a9t9.com']").click()
    page.wait_for_timeout(2000)

    #Verify the logo present in the page or not.

    logo_UIVision= frame5.get_by_alt_text("Ui.Vision by a9t9 software")

    expect(logo_UIVision).to_be_visible()


