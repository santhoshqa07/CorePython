
from playwright.sync_api import Page,expect

def select_date_of_birth(page, birth_year, birth_month, birth_date):
        Select_month = page.locator(".ui-datepicker-month")
        Select_month.select_option(label=birth_month)

        Select_Year = page.locator(".ui-datepicker-year")
        Select_Year.select_option(label= birth_year)

        all_dates = page.locator(".ui-datepicker-calendar td a").all()

        for dt in all_dates:
            date= dt.inner_text()
            if date == birth_date:
                dt.click()
                break


def select_departuredate(page, depart_year, depart_month, depart_date):
    Select_month = page.locator(".ui-datepicker-month")
    Select_month.select_option(label=depart_month)

    Select_Year = page.locator(".ui-datepicker-year")
    Select_Year.select_option(label=depart_year)

    all_dates = page.locator(".ui-datepicker-calendar td a").all()

    for dt in all_dates:
        date = dt.inner_text()
        if date == depart_date:
            dt.click()
            break





def test_Ass_DummyTicketBooking(page: Page):

    page.goto("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

    #Choose the correct option

    page.locator("#product_549").check()

    #Filling passenger Details.
    page.locator("#travname").fill("Akash")

    page.locator("#travlastname").fill("Ratore")

    #Select DOB
    # Select Date Of Birth
    birth_year = "2001"
    birth_month = "Mar"
    birth_date = "2"
    page.locator('#dob').click()
    select_date_of_birth(page, birth_year, birth_month, birth_date)

    page.wait_for_timeout(5000)


    #Select Sex
    page.locator("#sex_1").check()

    #Select travel type.

    page.get_by_label(" One Way").check()


    From_city = page.locator("#fromcity")
    From_city.fill("Toronto")

    To_city = page.locator("#tocity")
    To_city.fill("Mumbai")

    #select departure date
    depart_year = "2026"
    depart_month = "Nov"
    depart_date = "25"

    page.locator("#departon").click()

    select_departuredate(page, depart_year, depart_month, depart_date)

    #Additional information
    page.locator("#notes").fill("Need visa as soon as possible")

    #Select purpose of dummy ticket
    page.locator("#select2-reasondummy-container").click()

    purpose_option = "Other"

    Purpose_options = page.locator("#select2-reasondummy-results li").all()

    for option in Purpose_options:
        if option.inner_text() == purpose_option:
            option.click()
            break

    page.locator('#deliverymethod_1').check()

    #Billing Details

    page.locator('#billname').fill("Akash Rathore")

    page.locator("#billing_email").fill("abc.123@gmail.com")

    page.locator("#select2-billing_country-container").click()

    page.wait_for_timeout(5000)

    #select2-billing_country-results

    page.locator('.select2-results li:has-text("Canada")').click()

    #Enter Address
    page.locator("#billing_address_1").fill("123 Scott Street,")

    # Enter billing City
    page.locator("#billing_city").fill("Niagara Falls")

    #Select state
    page.locator("#select2-billing_state-container").click()
    page.locator("#select2-billing_state-results li:has-text('Ontario')").click()

    #Enter Zipcode
    page.locator("#billing_postcode").fill("L2C 6M1")

    page.locator("#billing_phone").fill("+12345678956")

    #Verify billing details
    expect(page.locator('#billname')).to_have_value('Akash Rathore')
    expect(page.locator("#billing_phone")).to_have_value('+12345678956')
    expect(page.locator('#billing_email')).to_have_value('abc.123@gmail.com')
    expect(page.locator('#select2-billing_country-container')).to_have_text('Canada')
    expect(page.locator('#billing_address_1')).to_have_value('123 Scott Street,')
    expect(page.locator("#billing_city")).to_have_value('Niagara Falls')
    expect(page.locator('#select2-billing_state-container')).to_have_text('Ontario')
    expect(page.locator('#billing_postcode')).to_have_value('L2C 6M1')

    #Verify product table- Prod name

    Prd_name= page.locator(".product-details")

    print("The selected product name is: " + Prd_name.inner_text())

    expect(Prd_name).to_have_text("Dummy ticket for Visa Application")


    ##Verify product table- order total
    order_total = page.locator(".shop_table.woocommerce-checkout-review-order-table tfoot tr:nth-child(2) td")
    print("The selected order total is: " + order_total.inner_text())
    expect(order_total).to_have_text("₹1,200")

    # Place order
    page.locator('#place_order').click()

    page.wait_for_timeout(5000)











