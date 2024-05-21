from assertpy import assert_that
from playwright.sync_api import Page, expect

from models.ui.domain.customer.customer import Customer
from models.ui.page_object.add_customer_page import AddCustomerPage
from models.ui.page_object.customer_account_page import CustomerAccountPage
from models.ui.page_object.customer_list_page import CustomerListPage
from models.ui.page_object.customer_login_page import CustomerLoginPage
from models.ui.page_object.login_page import LoginPage
from models.ui.page_object.manager_page import ManagerPage
from models.ui.page_object.open_account_page import OpenAccountPage
from test_data.urls import ui_tests_base_url


def test_manager_operations(
    page: Page, login_page: LoginPage, manager_page: ManagerPage
) -> None:
    login_page.navigate()
    login_page.manager_login_button_click()

    manager_page.add_customer_button_click()
    add_customer_page = AddCustomerPage(page)
    add_customer_page.check_url()

    customer = Customer(
        name="Sara", lastname="Connor", postcode="11111", account_id="1016"
    )

    add_customer_page.create_customer(customer)
    add_customer_page.check_url()

    manager_page.click_home_button()

    login_page.customer_login_button_click()
    customer_login_page = CustomerLoginPage(page)
    customer_login_page.login_as_customer(customer)
    customer_account_page = CustomerAccountPage(page, customer)
    expect(customer_account_page.get_welcome_message_text()).to_be_visible()
    customer_account_page.click_home_button()

    # Login as a manager and create account for new User
    login_page.manager_login_button_click()
    manager_page.open_account_click()

    open_account_page = OpenAccountPage(page)
    open_account_page.create_account(customer)

    # As a manager check created user
    manager_page.customers_click()
    customer_list_page = CustomerListPage(page)
    assert_that(customer_list_page.has_customer(customer)).is_true()
    account_default_id = customer_list_page.get_customer_default_account_id(customer)

    # Logout
    manager_page.click_home_button()

    # Login as a user and Check account
    customer_login_page.navigate()
    customer_login_page.login_as_customer(customer)
    customer_account_page.check_default_account_number(account_default_id)
    customer_account_page.click_home_button()

    # Login as a Manager and delete customer
    login_page.manager_login_button_click()
    manager_page.customers_click()
    customer_list_page.delete_customer(customer)
    assert_that(customer_list_page.has_customer(customer)).is_false()
