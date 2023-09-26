from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Browser:
    def __init__(self, driver):
        self.driver = driver

    def start_browser(self):
        chrome_options = Options()
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_window_size(width=800, height=600)

    def close_browser(self):
        if self.driver:
            self.driver.quit()
