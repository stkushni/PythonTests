import time

from playwright.sync_api import expect


class CustomerAccountPage:
    def __init__(self, page, customer):
        self.page = page
        self.customer = customer

    def get_welcome_message_text(self):
        return self.page.get_by_text(f"Welcome {self.customer.name} !!")

    def get_account_selector(self):
        return self.page.locator("#accountSelect")

    def get_default_account_number(self):
        return self.page.get_by_text(
            f"Account Number : {self.customer.account_default_id} ,"
        )

    def get_transactions_button(self):
        return self.page.get_by_role("button", name="Transactions")

    def get_deposit_button(self):
        return self.page.get_by_role("button", name="Deposit")

    def get_withdrawl_button(self):
        return self.page.get_by_role("button", name="Withdrawl")

    def click_logout_button(self):
        self.page.get_by_role("button", name="Logout").click()

    def click_home_button(self):
        self.page.get_by_role("button", name="Home").click()

    def click_transactions_button(self):
        self.page.get_by_role("button", name="Transactions").click()

    def click_deposit_button(self):
        self.page.get_by_role("button", name="Deposit").click()

    def click_withdrawl_button(self):
        self.page.get_by_role("button", name="Withdrawl").click()

    def make_deposit(self, amount: int):
        self.page.get_by_placeholder("amount").click()
        self.page.get_by_placeholder("amount").fill(str(amount))
        self.page.get_by_role("form").get_by_role("button", name="Deposit").click()
        time.sleep(1)

    def make_withdrawl(self, amount: int):
        self.page.get_by_placeholder("amount").click()
        self.page.get_by_placeholder("amount").fill(str(amount))
        self.page.get_by_role("form").get_by_role("button", name="Withdraw").click()
        time.sleep(1)

    def get_deposit_success_message(self):
        return self.page.get_by_text("Deposit Successful")

    def get_withdrawl_success_message(self):
        return self.page.get_by_text("Transaction successful")

    def check_balance(self, amount: int):
        expect(self.page.locator("body")).to_contain_text(
            f"Account Number : 1004 , Balance : {amount} , Currency : Dollar"
        )
