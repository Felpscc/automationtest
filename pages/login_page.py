from selenium.webdriver.common.by import By
from utils import Utils

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://google.com'
        self.username_input = (By.NAME, 'username')
        self.password_input = (By.NAME, 'password')
        self.login_button = (By.NAME, 'loginButton')
        self.dashboard_url = ''

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def is_dashboard_page(self):
        return self.driver.current_url == self.dashboard_url
