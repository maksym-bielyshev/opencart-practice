"""Module for the testing 'Register' page."""


from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestLoginPage(BaseTest):
    """Class for the 'Login' page."""

    def setup(self) -> None:
        """Setup for the test.

        :return: None
        """
        self.driver.get(
            'https://demo.opencart.com/index.php?route=account/login'
        )
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self) -> None:
        """Check the 'Email' field with valid data on login page.

        :return: None
        """

        self.login_page.login_form.email_field.clear_and_fill_input_field(
            'aaaaa@a.com'
        )
        self.login_page.login_form.password_field.clear_and_fill_input_field(
            'aaaa'
        )
        self.login_page.click_login_button()
        assert self.driver.find_element_by_id("account-account")
