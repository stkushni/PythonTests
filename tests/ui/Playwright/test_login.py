from playwright.sync_api import Page, expect
from models.ui.domain.customer.customer_harry_potter import CustomerHarryPotter
from models.ui.page_object.customer_account_page import CustomerAccountPage
from models.ui.page_object.customer_login_page import CustomerLoginPage
from models.ui.page_object.login_page import LoginPage
from models.ui.page_object.manager_page import ManagerPage


def test_customer_login_page(
    login_page: LoginPage, customer_login_page: CustomerLoginPage
):
    login_page.navigate()
    login_page.customer_login_button_click()

    expect(customer_login_page.get_customer_select_label()).to_be_visible()
    expect(customer_login_page.get_customer_selector()).to_be_visible()
    expect(customer_login_page.get_login_button()).to_be_visible(visible=False)
    expect(customer_login_page.get_home_button()).to_be_visible()


def test_customer_harry_potter_login(
    customer_login_page: CustomerLoginPage, page: Page
):
    customer_login_page.navigate()

    customer = CustomerHarryPotter()
    customer_login_page.login_as_customer(customer)
    customer_account_page = CustomerAccountPage(page, customer)

    expect(customer_account_page.get_welcome_message_text()).to_be_visible()
    expect(customer_account_page.get_account_selector()).to_be_visible()
    expect(customer_account_page.get_default_account_info()).to_be_visible()
    expect(customer_account_page.get_transactions_button()).to_be_visible()
    expect(customer_account_page.get_deposit_button()).to_be_visible()
    expect(customer_account_page.get_withdrawl_button()).to_be_visible()


def test_manager_login(login_page: LoginPage, manager_page: ManagerPage):
    login_page.navigate()
    login_page.manager_login_button_click()

    expect(manager_page.get_add_customer_button()).to_be_visible()
    expect(manager_page.get_open_account_button()).to_be_visible()
    expect(manager_page.get_customers_button()).to_be_visible()
