from behave import Given, When, Then


@Given('Open Get top')
def open_get_top(context):
    context.app.main_page.open_get_top()


@When('Hover over the mouse to {btn_name}.')
def hover_to_iphone(context, btn_name):
    context.app.header.hover_over_to_iphone_btn(btn_name)


@When('Hover the mouse to "iphone 12" button and click on it.')
def click_on_iphone_12(context):
    context.app.drop_down_field.click_on_iphone_12()


@Then('Verify user goes to the page of the {product_page}.')
def verify_product_page(context, product_page):
    context.app.product_page.verify_product_page(product_page)

