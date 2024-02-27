from selene.support.jquery_style_selectors import s

s("//button[contains(@ng-click, 'customer()')]").type("customer_login")
s('//input[@name="username"]').type("your_username")
s('//input[@name="password"]').type("your_password")
s('//button[text()="Submit"]').click()
