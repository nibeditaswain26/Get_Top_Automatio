from behave import Given, When, Then


@Then('User can see a left clickable button and right clickable button.')
def verify_left_right_arrow(context):
    context.app.product_page.verify_left_right_arrow()


@Then("Verify user can see the product's user ratting between product name and price of the product.")
def verify_user_ratting(context):
    context.app.product_page.verify_user_ratting()


@When('Click on ADD TO CART button.')
def click_add_to_product(context):
    context.app.product_page.click_add_to_product()


@Then('Verify that price in top nav menu is correct.')
def verify_price(context):
    context.app.product_page.verify_price()


@Then('verify that amount of items shown in top nav menu are correct')
def verify_amount_of_product(context):
    context.app.product_page.verify_amount_of_product()


@Then('verify correct products and subtotal shown')
def verify_product_subtotal(context):
    context.app.product_page.verify_product_subtotal()


@Then('Verify user can click on "View Cart" and is taken to cart page')
def verify_view_cart_clickable(context):
    context.app.product_page.verify_view_cart_clickable()


@Then('Verify user can click on "Checkout" and is taken to checkout page')
def verify_check_out_btn_clickable(context):
    context.app.product_page.verify_check_out_btn_clickable()


@Then('Verify user can remove a product.')
def verify_remove_product(context):
    context.app.product_page.verify_remove_product()
