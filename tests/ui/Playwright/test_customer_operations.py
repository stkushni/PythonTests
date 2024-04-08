import time
from playwright.sync_api import Page, expect
from models.ui.page_object.customer_account_page import CustomerAccountPage
from models.ui.page_object.transactions_page import TransactionsPage


def test_customer_operations(page: Page, customer_account_page):

    customer_account_page = CustomerAccountPage(page, customer_account_page)
    customer_account_page.click_transactions_button()

    transactions_page = TransactionsPage(page)
    expect(transactions_page.get_empty_table()).to_be_visible()
    transactions_page.click_back_button()

    # Deposit
    customer_account_page.click_deposit_button()
    page.get_by_placeholder("amount").click()
    page.get_by_placeholder("amount").fill("100")
    page.get_by_role("form").get_by_role("button", name="Deposit").click()
    expect(page.get_by_text("Deposit Successful")).to_be_visible()
    expect(page.locator("body")).to_contain_text(
        "Account Number : 1004 , Balance : 100 , Currency : Dollar"
    )
    time.sleep(1)

    # Check Deposit
    customer_account_page.click_transactions_button()
    expect(page.get_by_role("cell", name="Date-Time")).to_be_visible()
    # expect(page.get_by_role("cell", name="Apr 8, 2024 7:19:10 PM")).to_be_visible()
    expect(page.get_by_role("cell", name="Amount")).to_be_visible()
    expect(page.get_by_role("cell", name="100")).to_be_visible()
    expect(page.get_by_role("cell", name="Transaction Type")).to_be_visible()
    page.get_by_role("cell", name="Credit").click()
    transactions_page.click_back_button()

    # Withdrawl
    customer_account_page.click_withdrawl_button()
    page.get_by_placeholder("amount").click()
    page.get_by_placeholder("amount").fill("20")
    page.get_by_role("button", name="Withdraw", exact=True).click()
    expect(page.get_by_text("Transaction successful")).to_be_visible()
    expect(page.locator("body")).to_contain_text(
        "Account Number : 1004 , Balance : 80 , Currency : Dollar"
    )
    time.sleep(1)

    # Check Withdrawl
    customer_account_page.click_transactions_button()
    expect(page.get_by_role("cell", name="Date-Time")).to_be_visible()
    # expect(page.get_by_role("cell", name="Apr 8, 2024 7:20:13 PM")).to_be_visible()
    expect(page.get_by_role("cell", name="Amount")).to_be_visible()
    expect(page.get_by_role("cell", name="20", exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name="Credit")).to_be_visible()
    expect(page.get_by_text("Transaction Type")).to_be_visible()
    expect(page.get_by_role("cell", name="Transaction Type")).to_be_visible()
    page.get_by_role("cell", name="Debit").click()
    expect(page.get_by_role("cell", name="Debit")).to_be_visible()

    # expect(page.get_by_role("cell", name="Date-Time")).to_be_visible()
    # expect(page.get_by_role("cell", name="Amount")).to_be_visible()
    # expect(page.get_by_role("cell", name="Transaction Type")).to_be_visible()
    # expect(page.locator("div").filter(has_text="Date-Time Amount Transaction").nth(4)).to_be_visible()
    # expect(page.locator("body")).to_contain_text("Date-Time Amount Transaction Type")
