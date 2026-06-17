"""ProductsPage — Page Object for the SauceDemo inventory page."""


class ProductsPage:
    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        return self.page.get_by_text("Products").is_visible()
        """Return True if the products page is showing."""
        # Hint: check the page has the "Products" title text
        raise NotImplementedError

    def add_to_cart(self, product_name):
        self.page.get_by_text(product_name).click()
        """Add a product to the cart by its visible name."""
        raise NotImplementedError

    def cart_count(self):
        badge = self.page.locator(".shopping_cart_badge")

        if badge.count() == 0:
            return 0

        return int(badge.text_content())
        """Return the number on the cart badge as an int (0 if empty)."""
        raise NotImplementedError
