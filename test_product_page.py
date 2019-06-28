from pages.product_page import ProductPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

#@pytest.mark.parametrize('link', urls)
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_backet()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
#    time.sleep(10)

def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_to_backet()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

def test_message_dissapeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_to_backet()
    page.should_be_disappeared_success_message()

