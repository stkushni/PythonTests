from selene import browser, config
from selene.support.jquery_style_selectors import s


config.base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#"


def test_login():
    # Открываем страницу логина
    browser.open("/login")

    s('[type="customer_login"]').click()

    # # Вводим логин и пароль и нажимаем кнопку входа
    # s('[name="username"]').type('your_username')
    # s('[name="password"]').type('your_password')
    # s('[type="submit"]').click()
    #
    # # Проверяем, что мы успешно вошли (предполагая, что после успешного входа появится какой-то элемент)
    # s('.welcome-message').should_be.visible()
