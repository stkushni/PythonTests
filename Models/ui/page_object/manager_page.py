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
