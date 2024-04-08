from test_data.urls import ui_tests_base_url


class CustomerLoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(f"{ui_tests_base_url}/customer")

    def get_customer_select_label(self):
        return self.page.get_by_text("Your Name :")

    def get_customer_selector(self):
        return self.page.locator("#userSelect")

    def get_login_button(self):
        return self.page.get_by_role("button", name="Login")

    def get_home_button(self):
        return self.page.get_by_role("button", name="Home")

    def select_customer(self, customer):
        self.get_customer_selector().select_option(value=customer.name)

    def login_as_customer(self, customer):
        self.select_customer(customer)
        self.page.get_by_role("button", name="Login").click()
