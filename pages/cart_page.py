"""CartPage — Page Object for the SauceDemo cart page."""


class CartPage:
    
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.locator(".shopping_cart_link").click()

    def items(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def go_to_checkout(self):
        self.page.get_by_role("button", name="Checkout").click()
        """Click the Checkout button."""
        raise NotImplementedError
