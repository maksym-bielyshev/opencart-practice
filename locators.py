from selenium.webdriver.common.by import By


class LocatorsBasePageNavBar:
    """Locators for top navbar links on base page"""

    NAVBAR = (By.CLASS_NAME, 'list-inline')
    MY_ACCOUNT = (By.XPATH, '//a[@title="My Account"]')
    CURRENCY = (By.XPATH, '//span[text()="Currency"]/../..')
    USD = (By.XPATH, './/button[@name="EUR"]')
    POUND = (By.XPATH, './/button[@name="GBP"]')
    EUR = (By.XPATH, './/button[@name="USD"]')
    CONTACT_US = (By.XPATH, './/li[1]/a')
    LOGIN = (By.XPATH, './/ul/li[2]/a')
    REGISTER = (By.XPATH, './/ul/li[1]/a')
    WISH_LIST = (By.XPATH, './/li[3]/a')
    SHOPPING_CART = (By.XPATH, './/li[4]/a')
    CHECKOUT = (By.XPATH, './/li[5]/a')


class LocatorsYourPersonalDetailsComponent:
    """Locators fot the 'Your Personal Details' component."""

    FIRST_NAME_FIELD = (By.XPATH, './/input[@name="firstname"]')
    LAST_NAME_FIELD = (By.XPATH, './/input[@name="lastname"]')
    EMAIL_FIELD = (By.XPATH, './/input[@name="email"]')
    TELEPHONE_FIELD = (By.XPATH, './/input[@name="telephone"]')


class LocatorsYourPasswordComponent:
    """Locators fot the 'Your Password' component."""

    PASSWORD_FIELD = (By.XPATH, './/*[@name="password"]')
    PASSWORD_CONFIRM_FIELD = (By.XPATH, './/*[@name="confirm"]')


class LocatorsRegisterPage:
    """Locators fot the 'Register' page."""

    YOUR_PERSONAL_DETAILS_PARENT = (By.XPATH, '//*[@id="content"]')
    CHECKBOX_PRIVACY_POLICY = (By.NAME, 'agree')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')


class LocatorsNewsletterComponent:
    """Locators fot the 'Newsletter' component."""

    SUBSCRIBE_RADIO_BUTTONS = (By.XPATH, '//label[@class="radio-inline"]')


class LocatorsPrivacyPolicyComponent:
    """Locators fot the 'Privacy Policy' component."""

    PRIVACY_POLICY_CHECKBOX = (By.XPATH, '//input[@name="agree"]')


class LocatorsShoppingCartButton:
    """Locators for a black shop cart button."""

    SHOP_CART_BUTTON = (By.XPATH, '//div[@id="cart"]/button')
    CART_ITEMS = (By.XPATH, '//div[@id="cart"]//table')
    VIEW_CART = (
        By.XPATH,
        '//ul[@class="dropdown-menu pull-right"]//li[2]//div//p//a[1]'
    )

    CHECKOUT = (
        By.XPATH,
        '//ul[@class="dropdown-menu pull-right"]//li[2]//div//p//a[2]'
    )
