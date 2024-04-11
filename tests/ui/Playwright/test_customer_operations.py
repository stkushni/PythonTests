from playwright.sync_api import Page, expect
from models.ui.domain.transaction.transaction_type import TransactionType
from models.ui.page_object.customer_account_page import CustomerAccountPage
from models.ui.page_object.transactions_page import TransactionsPage


def test_customer_operations(page: Page, customer_account_page: CustomerAccountPage):
    customer_account_page.click_transactions_button()

    transactions_page = TransactionsPage(page)
    expect(transactions_page.get_empty_table()).to_be_visible()
    transactions_page.click_back_button()

    customer_account_page.check_balance(0)
    customer_account_page.click_deposit_button()
    customer_account_page.make_deposit(100)
    expect(customer_account_page.get_deposit_success_message()).to_be_visible()
    customer_account_page.check_balance(100)

    customer_account_page.click_transactions_button()
    transactions_page.check_transaction(0, 100, TransactionType.CREDIT)
    transactions_page.click_back_button()

    customer_account_page.check_balance(100)
    customer_account_page.click_withdrawl_button()
    customer_account_page.make_withdrawl(20)
    expect(customer_account_page.get_withdrawl_success_message()).to_be_visible()
    customer_account_page.check_balance(80)

    customer_account_page.click_transactions_button()
    transactions_page.check_transaction(1, 20, TransactionType.DEBIT)
    transactions_page.click_back_button()
