import pytest
import time

from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestUserAddToCartFromProductPage(object):
    @pytest.mark.need_review
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user(email, password)
        time.sleep(10)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_backet()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_backet()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()


def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_backet()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_dissapeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_backet()
    page.should_be_disappeared_success_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_link()
    cart_page.should_be_empty_cart()
    cart_page.should_be_message_empty()
