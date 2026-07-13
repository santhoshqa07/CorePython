
from playwright.sync_api import Page, expect
import pytest
import openpyxl
import uuid

reg_data=[]

workbook=openpyxl.load_workbook("testdata/Demo_reg.xlsx")
sheet=workbook.active

for row in sheet.iter_rows(min_row=2, values_only=True):
    reg_data.append(row)

@pytest.mark.parametrize("Gender,FirstName, LastName, Email, Password, ConfirmPassword",reg_data)
def test_login_data_driven_excel(Gender,FirstName, LastName, Email, Password, ConfirmPassword,page:Page):
    page.goto("https://demowebshop.tricentis.com/register")

    if Gender=="Male":
        radio_male= page.locator("#gender-male")
        radio_male.check()

    else:
        radio_female= page.locator("#gender-female")
        radio_female.check()

    Email= f"{uuid.uuid4().hex[:8]}@gmail.com"


    #fill teh login form
    page.locator("#FirstName").fill(FirstName)   # email id
    page.locator("#LastName").fill(LastName)  #password
    page.locator("#Email").fill(Email)
    page.locator("#Password").fill(Password)
    page.locator("#ConfirmPassword").fill(ConfirmPassword)

    page.locator("#register-button").click()

    #Assertion


    success_msg= page.locator("div.result")
    expect(success_msg).to_have_text("Your registration completed")






