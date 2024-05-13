from assertpy import assert_that
from playwright.sync_api import expect

from models.ui.domain.customer.customer import Customer
from test_data.urls import ui_tests_base_url


class OpenAccountPage:
    def __init__(self, page):
        self.page = page

    def get_customer_selector(self):
        return self.page.locator("#userSelect")

    def create_account(self, customer: Customer):
        self.get_customer_selector().select_option(
            value=f"{customer.name} {customer.lastname}"
        )
        self.page.locator("#currency").select_option("Dollar")
        self.page.get_by_role("button", name="Process").click()

    def check_url(self):
        expect(self.page).to_have_url(f"{ui_tests_base_url}/manager/openAccount")
