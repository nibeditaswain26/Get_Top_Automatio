from behave import Given, When, Then


@When('User can click right and left arrows to see top banners.')
def right_left_arrow_banner(context):
    context.app.main_page.left_right_arrow_banner()


@When('User can click bottom dots to see top banner.')
def click_bottom_dots(context):
    context.app.main_page.click_bottom_dots()


@When('User can click on product banner,Then verify it is taken to correct category page.')
def product_banners_clickable(context):
    context.app.main_page.product_banners_clickable()


