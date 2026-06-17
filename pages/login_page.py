"""LoginPage — Page Object for SauceDemo login.

The class structure is done for you. Fill in each method body
(remove the `raise NotImplementedError`). Use Playwright's auto-waiting —
never use time.sleep().
"""


class LoginPage:
    
    URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.get_by_role("button", name="Login").click()

    def get_error(self):
        return self.page.locator("[data-test='error']").text_content()