from behave import Given, When, Then


@Then('User can see a left clickable button and right clickable button.')
def verify_left_right_arrow(context):
    context.app.product_page.verify_left_right_arrow()