from behave import Given, When, Then


@When('Click on the cart icon.')
def click_on_cart_icon(context):
    context.app.header.click_on_cart_icon()


@Then('Verify empty cart page.')
def verify_empty_cart(context):
    context.app.cart_page.verify_empty_cart()


@When('Hover the mouse to cart icon.')
def hover_the_mouse_cart_btn(context):
    context.app.header.hover_to_cart_icon()


@Then('Verify a popup message"No products in the cart."')
def verify_message(context):
    context.app.header.verify_message()
