from typing import Optional

from assertpy import assert_that
from playwright.sync_api import expect
import time
from models.ui.domain.customer.customer import Customer
from test_data.urls import ui_tests_base_url


class CustomerListPage:
    def __init__(self, page):
        self.page = page

    def has_customer(self, customer: Customer) -> bool:
        self.page.wait_for_selector("table tbody tr")
        rows = self.page.locator("table tbody tr")
        for i in range(rows.count()):
            values = rows.nth(i).locator("td")
            if (
                values.nth(0).inner_text() == customer.name
                and values.nth(1).inner_text() == customer.lastname
                and values.nth(2).inner_text() == customer.postcode
            ):
                return True
        return False

    def get_customer_default_account_id(self, customer) -> Optional[int]:
        self.page.wait_for_selector("table tbody tr")
        rows = self.page.locator("table tbody tr")
        for i in range(rows.count()):
            values = rows.nth(i).locator("td")
            if (
                values.nth(0).inner_text() == customer.name
                and values.nth(1).inner_text() == customer.lastname
                and values.nth(2).inner_text() == customer.postcode
            ):
                return int(values.nth(3).inner_text().split(" ")[0])
        return None

    def delete_customer(self, customer):
        self.page.get_by_role(
            "row", name=f"{customer.name} {customer.lastname} {customer.postcode}"
        ).get_by_role("button").click()
