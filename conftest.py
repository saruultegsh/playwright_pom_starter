"""Shared fixtures. pytest-playwright provides the `page` fixture automatically."""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.goto()
    return lp


@pytest.fixture
def products_page(page):
    return ProductsPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)
