"""Module for the 'Login' page."""

from selenium.webdriver import Remote

from components import RegisterPageRightMenuComponent, LoginComponent
from locators import LocatorsLoginPage
from pages.base_page import BasePage
from pages.register_page import RegisterPage


class LoginPage(BasePage):
    """This class describes methods that we need to work with 'Login' page."""

    def __init__(self, driver: Remote):
        """Initialize driver and objects to works with 'Login' page.
        :param driver: Remote
        """
        super().__init__(driver)
        self.right_menu = RegisterPageRightMenuComponent(self._driver)
        self.login_form = LoginComponent(self._driver)

    def click_login_button(self) -> object:
        """Click 'Login' button.

        :return: page
        """
        self._driver.find_element(
            *LocatorsLoginPage.LOGIN_BUTTON
        ).click()
        return LoginPage(self._driver)
