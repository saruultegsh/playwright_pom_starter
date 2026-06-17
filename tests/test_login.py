"""Sample test to show the pattern. Add the remaining required scenarios.

Required (>=6 total): valid login, wrong password error, empty username error,
add 1 -> badge 1, add 2 -> badge 2, open cart -> correct items listed.
"""
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_open_cart_shows_item(login_page):
    login_page.login("standard_user", "secret_sauce")

    products = ProductsPage(login_page.page)

    products.page.get_by_role(
        "button",
        name="Add to cart"
    ).first.click()

    cart = CartPage(login_page.page)

    cart.open()

    assert len(cart.items()) > 0


def test_valid_login(login_page):
    login_page.login("standard_user", "secret_sauce")
    assert ProductsPage(login_page.page).is_loaded()

# TODO: add the other 5 scenarios.
def test_wrong_password(login_page):
    login_page.login("standard_user", "wrong_password")
    assert "Username and password do not match" in login_page.get_error()
def test_empty_username(login_page):
    login_page.login("", "secret_sauce")
    assert "Username is required" in login_page.get_error()

def test_add_one_item(login_page):
    login_page.login("standard_user", "secret_sauce")

    products = ProductsPage(login_page.page)

    products.page.get_by_role(
        "button",
        name="Add to cart"
    ).first.click()

    assert products.cart_count() == 1

def test_add_two_items(login_page):
    login_page.login("standard_user", "secret_sauce")

    products = ProductsPage(login_page.page)

    buttons = products.page.get_by_role(
        "button",
        name="Add to cart"
    )

    buttons.nth(0).click()
    buttons.nth(1).click()

    assert products.cart_count() == 2