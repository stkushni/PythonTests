import pytest
from playwright.sync_api import Page
from models.ui.domain.customer.customer_harry_potter import CustomerHarryPotter
from models.ui.page_object.customer_account_page import CustomerAccountPage
from models.ui.page_object.customer_login_page import CustomerLoginPage
from models.ui.page_object.login_page import LoginPage
from models.ui.page_object.manager_page import ManagerPage


@pytest.fixture
def customer_account_page(
    page: Page, customer_login_page: CustomerLoginPage
) -> CustomerAccountPage:
    customer_login_page.navigate()

    customer = CustomerHarryPotter()
    customer_login_page.login_as_customer(customer)
    return CustomerAccountPage(page, customer)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def customer_login_page(page: Page) -> CustomerLoginPage:
    return CustomerLoginPage(page)


@pytest.fixture()
def manager_page(page: Page, login_page: LoginPage) -> ManagerPage:
    login_page.navigate()
    login_page.manager_login_button_click()
    return ManagerPage(page)
