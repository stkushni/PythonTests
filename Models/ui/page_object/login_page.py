from test_data.urls import ui_tests_base_url


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(f"{ui_tests_base_url}/login")

    def customer_login_button_click(self):
        self.page.get_by_role("button", name="Customer login").click()

    def manager_login_button_click(self):
        self.page.get_by_role("button", name="Bank Manager login").click()

    def get_customer_login_button(self):
        return self.page.get_by_role("button", name="Customer login")

    def get_manager_login_button(self):
        return self.page.get_by_role("button", name="Bank Manager login")
