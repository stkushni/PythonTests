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
