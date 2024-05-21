from assertpy import assert_that
from playwright.sync_api import expect

from models.ui.domain.customer.customer import Customer
from test_data.urls import ui_tests_base_url


class AddCustomerPage:
    def __init__(self, page):
        self.page = page

    def create_customer(self, customer: Customer):
        self.page.get_by_placeholder("First Name").click()
        self.page.get_by_placeholder("First Name").fill(customer.name)
        self.page.get_by_placeholder("Last Name").click()
        self.page.get_by_placeholder("Last Name").fill(customer.lastname)
        self.page.get_by_placeholder("Post Code").click()
        self.page.get_by_placeholder("Post Code").fill(customer.postcode)
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.get_by_role("form").get_by_role("button", name="Add Customer").click()

    def check_url(self):
        expect(self.page).to_have_url(f"{ui_tests_base_url}/manager/addCust")
