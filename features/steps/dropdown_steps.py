from behave import Given, When, Then


@Given('Open Get top')
def open_get_top(context):
    context.app.main_page.open_get_top()


@When('Hover over the mouse to {button_name}.')
def hover_to_header_btn(context, button_name):
    context.app.header.hover_over_to_header_btn(button_name)


@When('Hover the mouse to {product_name} button and click on it.')
def click_on_drop_down_btn(context, product_name):
    context.app.drop_down_field.click_on_drop_down_btn(product_name)


@Then('Verify user goes to the page of the {product_page}.')
def verify_product_page(context, product_page):
    context.app.product_page.verify_product_page(product_page)

