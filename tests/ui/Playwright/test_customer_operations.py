from playwright.sync_api import Page, expect
from models.ui.domain.transaction.transaction_type import TransactionType
from models.ui.page_object.customer_account_page import CustomerAccountPage
from models.ui.page_object.transactions_page import TransactionsPage


def test_customer_operations(page: Page, customer_account_page: CustomerAccountPage):
    deposit_amount = 100
    withdrawal_amount = 20
    customer_account_page.click_transactions_button()

    transactions_page = TransactionsPage(page)
    expect(transactions_page.get_empty_table()).to_be_visible()
    transactions_page.click_back_button()

    customer_account_page.check_balance(0)
    customer_account_page.click_deposit_button()
    customer_account_page.make_deposit(deposit_amount)
    expect(customer_account_page.get_deposit_success_message()).to_be_visible()
    customer_account_page.check_balance(deposit_amount)

    customer_account_page.click_transactions_button()
    transactions_page.check_transaction(0, deposit_amount, TransactionType.CREDIT)
    transactions_page.click_back_button()

    customer_account_page.check_balance(deposit_amount)
    customer_account_page.click_withdrawl_button()
    customer_account_page.make_withdrawl(withdrawal_amount)
    expect(customer_account_page.get_withdrawl_success_message()).to_be_visible()
    customer_account_page.check_balance(80)

    customer_account_page.click_transactions_button()
    transactions_page.check_transaction(1, withdrawal_amount, TransactionType.DEBIT)
    transactions_page.click_back_button()
