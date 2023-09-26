from selenium.webdriver.common.keys import Keys

class Utils:
    def __init__(self, driver):
        self.driver = driver

    def entrar(self, url):
        self.driver.get(url)
