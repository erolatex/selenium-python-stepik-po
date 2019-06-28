from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from .locators import ProductPageLocators

from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_to_backet(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BACKET), "Backet button isn't presented"
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BACKET)
        button.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), ("Product name isn't presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), ("Adding message isn't presented")

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text

        assert product_name in message, "Message should have product name"
        assert message == product_name + " has been added to your basket.", "Message should have product name"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), ("Message should have backet total")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), ("Message should have product price")

        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert product_price in message_basket_total, "Message should have total amount"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"
