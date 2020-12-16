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

class LocatorsLoginPage:
    """Locators for 'Login' page."""

    FORGOTTEN_PASSWORD_BUTTON = (
        By.XPATH,
        '//div[@id="content"]//a[text()="Forgotten Password"]'
    )
    LOGIN_BUTTON = (By.XPATH, '//input[@value="Login"]')
    REGISTER_PAGE_BUTTON = (By.XPATH, '//a[text()="Continue"]')


class LocatorsRightMenuRegisterPage:
    """"Locators for right menu on Register and Login pages"""

    RIGHT_MENU = (By.CLASS_NAME, 'list-group')
    LOGIN = (By.XPATH, './/a[text()="Login"]')
    REGISTER = (By.XPATH, './/a[text()="Register"]')
    FORGOTTEN_PASSWORD = (By.XPATH, './/a[text()="Forgotten Password"]')
    MY_ACCOUNT = (By.XPATH, './/a[text()="My Account"]')
    EDIT_ACCOUNT = (By.XPATH, './/a[text()="Edit Account"]')
    PASSWORD = (By.XPATH, './/a[text()="Password"]')
    ADDRESS_BOOK = (By.XPATH, './/a[text()="Address Book"]')
    WISH_LIST = (By.XPATH, './/a[text()="Wish List"]')
    ORDER_HISTORY = (By.XPATH, './/a[text()="Order History"]')
    DOWNLOADS = (By.XPATH, './/a[text()="Downloads"]')
    RECURRING_PAYMENTS = (By.XPATH, './/a[text()="Recurring payments"]')
    REWARD_POINTS = (By.XPATH, './/a[text()="Reward Points"]')
    RETURNS = (By.XPATH, './/a[text()="Returns"]')
    TRANSACTIONS = (By.XPATH, './/a[text()="Transactions"]')
    NEWSLETTER = (By.XPATH, './/a[text()="Newsletter"]')
    LOGOUT = (By.XPATH, './/a[text()="Logout"]')


class LocatorsLoginComponent:
    """Locators for Login Component."""

    EMAIL_INPUT = (By.XPATH, '//input[@id="input-email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="input-password"]')
    FORGOTTEN_PASSWORD_BUTTON = (By.XPATH, '//a[text()="Forgotten Password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@type="submit"]')
