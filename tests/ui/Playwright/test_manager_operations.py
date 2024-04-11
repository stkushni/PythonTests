from playwright.sync_api import Page, expect


def test_manager_operations(page: Page) -> None:
    # Setup
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    page.get_by_role("button", name="Bank Manager Login").click()

    # Create customer
    page.get_by_role("button", name="Add Customer").click()
    page.get_by_placeholder("First Name").click()
    page.get_by_placeholder("First Name").fill("Sara")
    page.get_by_placeholder("Last Name").click()
    page.get_by_placeholder("Last Name").fill("Connor")
    page.get_by_placeholder("Post Code").click()
    page.get_by_placeholder("Post Code").fill("11111")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("form").get_by_role("button", name="Add Customer").click()

    # Check that user stays in Create customer page
    expect(page.get_by_placeholder("First Name")).to_be_visible()
    expect(page.get_by_placeholder("Last Name")).to_be_visible()
    expect(page.get_by_placeholder("Post Code")).to_be_visible()

    # Logout (teardown)
    page.get_by_role("button", name="Home").click()

    # Check created user, login
    page.get_by_role("button", name="Customer Login").click()
    expect(page.locator("#userSelect")).to_be_visible()
    expect(page.locator("#userSelect")).to_contain_text(
        "---Your Name--- Hermoine GrangerHarry PotterRon WeaslyAlbus DumbledoreNeville LongbottomSara Connor"
    )
    page.locator("#userSelect").select_option("6")
    page.get_by_role("button", name="Login").click()

    # Check created user page
    expect(page.get_by_text("Welcome Sara Connor !! Please")).to_be_visible()

    # Logout (teardown)
    page.get_by_role("button", name="Home").click()

    # Login as a manager and create account for new User
    page.get_by_role("button", name="Bank Manager Login").click()
    page.get_by_role("button", name="Open Account").click()
    page.locator("#userSelect").select_option("6")
    page.locator("#currency").select_option("Dollar")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Process").click()

    # As a manager check created user
    page.get_by_role("button", name="Customers").click()
    expect(page.get_by_role("cell", name="Sara")).to_be_visible()
    expect(page.get_by_role("cell", name="Connor")).to_be_visible()
    expect(page.get_by_role("cell", name="11111")).to_be_visible()
    expect(page.get_by_role("cell", name="1016")).to_be_visible()

    # Logout
    page.get_by_role("button", name="Home").click()

    # Login as a user and Check account
    page.get_by_role("button", name="Customer Login").click()
    page.locator("#userSelect").select_option("6")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Account Number : 1016 ,")).to_be_visible()
    expect(page.locator("#accountSelect")).to_be_visible()
    page.get_by_role("button", name="Home").click()

    # Login as a Manager and delete customer
    page.get_by_role("button", name="Bank Manager Login").click()
    page.get_by_role("button", name="Customers").click()
    page.get_by_role("row", name="Sara Connor 11111 1016 Delete").get_by_role(
        "button"
    ).click()
