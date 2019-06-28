from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import time


# MAIN_PAGE = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"


def guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_link()
    cart_page.should_be_empty_cart()
    cart_page.should_be_message_empty()
