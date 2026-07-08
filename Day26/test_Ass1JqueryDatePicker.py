from multiprocessing.pool import MaybeEncodingError

from playwright.sync_api import Page, expect


def select_date_field(page, tar_year, tar_month, tar_day):
    current_month = page.locator('.ui-datepicker-month option[selected="selected"]').text_content()
    current_year = page.locator('.ui-datepicker-year option[selected="selected"]').text_content()

    print("The current month is: ", current_month)
    print("The current year is: ", current_year)


    while True:
        if current_month != tar_month and current_year !=tar_year:
            Select_month = page.locator(".ui-datepicker-month")
            Select_month.select_option(label="May")

            Select_Year = page.locator(".ui-datepicker-year")
            Select_Year.select_option(label="2027")
            break
        else:
            print("f, The current month {current_month} and the current year {current_year} have already been selected")





    #select date

    all_dates = page.locator(".ui-datepicker-calendar td a").all()

    for dt in all_dates:
        date= dt.inner_text()
        if date == tar_day:
            dt.click()
            break




def test_Ass1_JqueryDatePicker(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    date_field= page.locator("#txtDate")

    date_field.click()

    tar_year = 2027
    tar_month = "May"
    tar_day = 25

    select_date_field(page, tar_year, tar_month, tar_day)









