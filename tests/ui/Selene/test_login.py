from selene import browser, config
from selene.support.jquery_style_selectors import s
from selene.support.conditions import be

config.base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#"


def test_login():
    # Открываем страницу логина
    browser.open_url("/login")

    # Тыкаем на кнопку "customer_login"
    s("//button[contains(@ng-click, 'customer()')]").click()

    # Проверяем, что открылась другая страница с лейблом
    s("/html/body/div/div/div[2]/div/form/div/label").should(be.visible)

    print("hello-how-are-you")
