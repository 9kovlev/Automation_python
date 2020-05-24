from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class LoginPageLocators:
    LOGIN_BUTTON = (By.ID, "login_link")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    EMAIL_INPUT = (By.NAME, "registration-email")
    PASSWORD_INPUT = (By.NAME, "registration-password1")
    REPEAT_PASSWORD_INPUT = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class BasketLocators:
    BUTTON_ADD_TO_BASKET = (By.ID, "add_to_basket_form")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    ADDING_SUCCESS = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    ALERT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages>div:first-child .alertinner strong")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")



class CartPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "div#content_inner > p")
    FREE_BASKET = (By.XPATH, "//h3/a")
