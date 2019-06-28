from pages.login_page import LoginPage


LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_guest_should_see_login_in_url(browser):
    link = LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_guest_should_see_login_form(browser):
    link = LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    link = LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
