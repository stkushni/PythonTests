from playwright.sync_api import expect

from models.ui.domain.transaction.transaction_type import TransactionType


class TransactionsPage:
    def __init__(self, page):
        self.page = page

    def click_back_button(self):
        self.page.get_by_role("button", name="Back").click()

    def get_empty_table(self):
        return (
            self.page.locator("div")
            .filter(has_text="Date-Time Amount Transaction")
            .nth(4)
        )

    def check_transaction(
        self,
        transaction_id: int,
        transaction_amount: int,
        transaction_type: TransactionType,
    ):
        rows = self.page.locator(f"tr#anchor{transaction_id} td")
        expect(rows.nth(1)).to_have_text(str(transaction_amount))
        expect(rows.nth(2)).to_have_text(transaction_type.value)
