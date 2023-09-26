from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from behave import __main__ as behave_executable
from base.browser import Browser

if __name__ == '__main__':

    chrome_options = Options()

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(width=800, height=600)


    browser = Browser(driver)
    browser.start_browser()


    behave_executable.main(['--no-capture'])


    browser.close_browser()
