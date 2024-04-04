from playwright.sync_api import Page, expect


def test_click_button(page: Page):
    page.goto('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    page.get_by_role('button', name='Customer login').click()
    expect(page.get_by_text('Your Name :')).to_be_visible()