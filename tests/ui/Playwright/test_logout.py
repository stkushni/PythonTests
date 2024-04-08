from playwright.sync_api import Page, expect

from models.ui.page_object.customer_account_page import CustomerAccountPage
from models.ui.page_object.customer_login_page import CustomerLoginPage
from models.ui.page_object.login_page import LoginPage
from models.ui.page_object.manager_page import ManagerPage


def test_customer_logout(
    customer_login_page: CustomerLoginPage, customer_account_page: CustomerAccountPage
):
    customer_account_page.click_logout_button()
    expect(customer_login_page.get_customer_select_label()).to_be_visible()
    expect(customer_login_page.get_customer_selector()).to_be_visible()


def test_customer_logout_to_home_page(
    login_page: LoginPage, customer_account_page: CustomerAccountPage
):
    customer_account_page.click_home_button()
    expect(login_page.get_customer_login_button()).to_be_visible()
    expect(login_page.get_manager_login_button()).to_be_visible()


def test_manager_logout_to_home_page(login_page: LoginPage, manager_page: ManagerPage):
    manager_page.click_home_button()
    expect(login_page.get_customer_login_button()).to_be_visible()
    expect(login_page.get_manager_login_button()).to_be_visible()
