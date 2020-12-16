from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import LocatorsYourPersonalDetailsComponent, \
    LocatorsYourPasswordComponent, LocatorsNewsletterComponent, \
    LocatorsPrivacyPolicyComponent, LocatorsShoppingCartButton, \
    LocatorsRightMenuRegisterPage, LocatorsLoginComponent


class InputFieldComponent:
    """An input field to fill with data from user."""

    def __init__(self, driver: Remote, input_field_locator: tuple,
                 parent_element: WebElement = None
                 ) -> None:
        """Initialize the input field.
        :param driver: Remote
        :param input_field_locator: tuple
        :return: None
        """
        self._driver = driver
        self.input_field_locator = input_field_locator
        self.parent_element = parent_element
        self.error_message = ErrorMessageComponent(
            self._driver, self.input_field_locator
        )

    def _find_input_field(self) -> None:
        """Find input field by parent element or driver.
        :return: None
        """
        if self.parent_element:
            self.input_field = self.parent_element.find_element(
                *self.input_field_locator
            )
        else:
            self.input_field = self._driver.find_element(
                *self.input_field_locator
            )

    def clear_and_fill_input_field(self, data: str) -> None:
        """Clear and fill input field with data.
        :param data: str
        :return: None
        """
        self._find_input_field()
        self.input_field.clear()
        self.input_field.send_keys(data)


class YourPersonalDetailsComponent:
    """Your personal details form consists four fields to fill."""

    def __init__(self, driver: Remote, parent_element: WebElement) -> None:
        """Initialize input fields first name, last name, email, telephone.
        :param driver: Remote.
        :param parent_element: WebElement
        """
        self._driver = driver
        self._parent_element = parent_element

        self.first_name_field = \
            InputFieldComponent(
                self._driver,
                LocatorsYourPersonalDetailsComponent.FIRST_NAME_FIELD,
                self._parent_element
            )

        self.last_name_field = \
            InputFieldComponent(
                self._driver,
                LocatorsYourPersonalDetailsComponent.LAST_NAME_FIELD,
                self._parent_element
            )

        self.email_field = \
            InputFieldComponent(
                self._driver,
                LocatorsYourPersonalDetailsComponent.EMAIL_FIELD,
                self._parent_element
            )

        self.telephone_field = \
            InputFieldComponent(
                self._driver,
                LocatorsYourPersonalDetailsComponent.TELEPHONE_FIELD,
                self._parent_element
            )


class YourPasswordComponent:
    """Your password form consists two fields to fill."""

    def __init__(self, driver: Remote, parent_element: WebElement) -> None:
        """Initialize input fields password field, password confirm field.
        :param driver: Remote
        :param parent_element: WebElement
        :return: None
        """
        self._driver = driver
        self._parent_element = parent_element
        self.password_field = \
            InputFieldComponent(
                self._driver,
                LocatorsYourPasswordComponent.PASSWORD_FIELD,
                self._parent_element)

        self.password_confirm_field = \
            InputFieldComponent(
                self._driver,
                LocatorsYourPasswordComponent.PASSWORD_CONFIRM_FIELD,
                self._parent_element
            )


class NewsletterComponent:
    """Two radio buttons to subscribe or unsubscribe from newsletter."""

    def __init__(self, driver: Remote) -> None:
        """Initialize driver.
        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.subscribe_radio_button_labels = \
            self._driver.find_elements(
                *LocatorsNewsletterComponent.SUBSCRIBE_RADIO_BUTTONS
            )


class PrivacyPolicyComponent:
    """Checkbox Privacy Policy to agree with it."""

    def __init__(self, driver: Remote) -> None:
        """Initialize driver and privacy policy checkbox.
        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.privacy_policy_checkbox_input = \
            self._driver.find_element(
                *LocatorsPrivacyPolicyComponent.PRIVACY_POLICY_CHECKBOX
            )

    def agree_with_privacy_policy(self) -> None:
        """Agree with Privacy Policy.
        :return: None
        """
        self.privacy_policy_checkbox_input.click()

    def get_status_privacy_policy(self) -> str:
        """Check status: the user agrees with the policy or not.
        :return: str
        """
        if self.privacy_policy_checkbox_input.get_attribute('checked'):
            return 'I have read and agree to the Privacy Policy.'
        else:
            return 'I don\'t agree to the Privacy Policy.'


class ErrorMessageComponent:
    """Error message for inputs ."""

    def __init__(self, driver: Remote, element_locator: tuple) -> None:
        """Initialize element locator to find error message for it.
        :param driver: Remote
        :param element_locator: tuple
        :return: None
        """
        self._driver = driver
        self.element_locator = element_locator

    def get_error_message(self):
        """Get error message.

        :return: str or None
        """
        try:
            if '@data-date-format' in self.element_locator[1]:
                error_message_locator = \
                    f'{self.element_locator[1]}' \
                    f'/../following-sibling::div[@class="text-danger"]'
            else:
                error_message_locator = \
                    f'{self.element_locator[1]}' \
                    f'/following-sibling::div[@class="text-danger"]'

            error_message = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    error_message_locator
                )))
            return error_message.text
        except TimeoutException:
            return ''


class ShopCartButtonComponent:
    """Component to find and click shopping cart button."""

    def __init__(self, driver: Remote):
        """Initialise shopping cart button.
        :param driver: Remote driver
        """
        self._driver = driver

    def click_shop_cart_button(self):
        """Click shopping cart button."""
        shop_cart_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                LocatorsShoppingCartButton.SHOP_CART_BUTTON
            ))
        shop_cart_button.click()
        cart_items = \
            self._driver.find_elements(
                *LocatorsShoppingCartButton.CART_ITEMS
            )
        if len(cart_items) == 0:
            return 'Your cart is empty!'
        else:
            return ShopCartDropdownComponent(self._driver)


class ShopCartDropdownComponent:
    """Component for black shopping cart drop-down button."""

    def __init__(self, driver: Remote) -> None:
        """Initialise shopping cart drop-down button.
        :param driver: Remote driver.
        """
        self._driver = driver

    def click_product_title(self, product_title: str) -> None:
        """Click on the provided product title.
        :return: None.
        """
        self._driver.find_element(
            By.XPATH,
            f'//*[@id="cart"]//td[2]//a[(text()="{product_title}")]'
        ).click()

    def click_remove_button(self, product_title: str) -> None:
        """Click on the remove from the shopping cart button.
        :return: None.
        """
        product_title = self._driver.find_element(
            By.XPATH,
            f'//*[@id="cart"]//td[2]//a[(text()="{product_title}")]'
        )

        self._driver.find_element(
            By.XPATH,
            f'{product_title}/../../td[5]/button'
        ).click()

    def click_view_cart_link(self) -> None:
        """Click on the 'View Cart' link.
        :return: None.
        """
        self._driver.find_element(
            *LocatorsShoppingCartButton.VIEW_CART
        ).click()

    def click_checkout_link(self) -> None:
        """Click on the 'Checkout' link.
        :return: None.
        """
        self._driver.find_element(*LocatorsShoppingCartButton.CHECKOUT).click()


class RegisterPageRightMenuComponent:
    """This class describes the right menu on register page."""

    def __init__(self, driver: Remote) -> None:
        """Initialise Right Menu Component on Register Page.
        :param driver: Remote driver.
        :return: None.
        """
        self._driver = driver
        self._right_menu = driver.find_element_by_class_name('list-group')

    def click_my_account(self) -> None:
        """Click 'My account' link in right menu.
        :return: None.
        """
        self._right_menu.find_element(
            *LocatorsRightMenuRegisterPage.MY_ACCOUNT
        ).click()

    def click_address_book(self) -> None:
        """Click 'Address book' link in right menu.
        :return: None.
        """
        self._right_menu.find_element(
            *LocatorsRightMenuRegisterPage.ADDRESS_BOOK
        ).click()

    def click_wish_list(self) -> None:
        """Click 'Wish List' link in right menu.
        :return: None.
        """
        self._right_menu.find_element(
            *LocatorsRightMenuRegisterPage.WISH_LIST
        ).click()

    def click_order_history(self) -> None:
        """Click 'Order history' link in right menu.
        :return: None.
        """
        self._right_menu.find_element(
            *LocatorsRightMenuRegisterPage.ORDER_HISTORY
        ).click()

    def click_downloads(self) -> None:
        """Click 'Downloads' link in right menu.
        :return: None.
        """
        self._right_menu.find_element(
            *LocatorsRightMenuRegisterPage.DOWNLOADS
        ).click()

    def click_recurring_payments(self) -> None:
        """Click 'Recurring payments' link in right menu.
        :return: None.
        """
        self._right_menu.find_element(
            *LocatorsRightMenuRegisterPage.RECURRING_PAYMENTS
        ).click()

    def click_reward_points(self) -> None:
        """Click 'Reward points' link in right menu.
        :return: None.
        """
        self._right_menu.find_element(
            *LocatorsRightMenuRegisterPage.REWARD_POINTS
        ).click()

    def click_returns(self) -> None:
        """Click 'Returns' link in right menu.
        :return: None.
        """
        self._right_menu.find_element(
            *LocatorsRightMenuRegisterPage.RETURNS
        ).click()

    def click_transactions(self) -> None:
        """Click 'Transactions' link in right menu.
        :return: None.
        """
        self._right_menu.find_element(
            *LocatorsRightMenuRegisterPage.TRANSACTIONS
        ).click()

    def click_newsletter(self) -> None:
        """Click 'Newsletter' link in right menu.
        :return: None.
        """
        self._right_menu.find_element(
            *LocatorsRightMenuRegisterPage.NEWSLETTER
        ).click()


class LoginComponent:
    """Login component consists two fields: E-Mail Address and Password."""

    def __init__(self, driver: Remote) -> None:
        """Initialize input form fields.
        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.email_field = InputFieldComponent(
            self._driver,
            LocatorsLoginComponent.EMAIL_INPUT
        )
        self.password_field = InputFieldComponent(
            self._driver,
            LocatorsLoginComponent.PASSWORD_INPUT
        )

    def click_forgotten_password(self) -> None:
        """Click forgotten password button to restore password.
        :return: None
        """
        self._driver.find_element(
            *LocatorsLoginComponent.FORGOTTEN_PASSWORD_BUTTON
        ).click()

    def click_login_button(self) -> None:
        """Click login button to return the user to the system.
        :return: None
        """
        self._driver.find_element(*LocatorsLoginComponent.LOGIN_BUTTON).click()
