from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement

from locators import LocatorsBasePageNavBar


class BasePage:
    """Base page class."""

    def __init__(self, driver: Remote):
        """Initialize main class.
        :param driver: Remote.
        """
        self._driver = driver

    def get_my_account(self) -> WebElement:
        """Method get 'My account' WebElement.
        :return: WebElement
        """
        return self._driver.find_element(*LocatorsBasePageNavBar.MY_ACCOUNT)

    def click_account_and_go_to_login(self):
        """Method which click on link and go to Login page.
        :return: None
        """
        my_account = self.get_my_account()
        my_account.click()
        my_account.find_element(*LocatorsBasePageNavBar.LOGIN).click()

    def click_account_and_go_to_register(self):
        """Method which click on link and go to Register page.
        :return: None
        """
        my_account = self.get_my_account()
        my_account.click()
        my_account.find_element(*LocatorsBasePageNavBar.REGISTER).click()
