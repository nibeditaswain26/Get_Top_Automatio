from behave import Given, When, Then


@Then('User can see a left clickable button and right clickable button.')
def verify_left_right_arrow(context):
    context.app.product_page.verify_left_right_arrow()


@Then("Verify user can see the product's user ratting between product name and price of the product.")
def verify_user_ratting(context):
    context.app.product_page.verify_user_ratting()