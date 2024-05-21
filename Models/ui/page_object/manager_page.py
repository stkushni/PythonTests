from models.ui.domain.customer.customer import Customer


class ManagerPage:
    def __init__(self, page):
        self.page = page

    def get_add_customer_button(self):
        return self.page.get_by_role("button", name="Add Customer")

    def get_open_account_button(self):
        return self.page.get_by_role("button", name="Open Account")

    def get_customers_button(self):
        return self.page.get_by_role("button", name="Customers")

    def click_home_button(self):
        self.page.get_by_role("button", name="Home").click()

    def add_customer_button_click(self):
        self.get_add_customer_button().click()

    def open_account_click(self):
        self.get_open_account_button().click()

    def customers_click(self):
        self.get_customers_button().click()
