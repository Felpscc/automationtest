from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_registration_page(self):
        
        self.driver.get('url_da_pagina_de_registro')

    def enter_registration_info(self, nome, email, senha):
        nome_input = self.driver.find_element(By.ID, 'nome_id')  
        email_input = self.driver.find_element(By.ID, 'email_id') 
        senha_input = self.driver.find_element(By.ID, 'senha_id')  
        registro_button = self.driver.find_element(By.ID, 'registro_id') 

        nome_input.send_keys(nome)
        email_input.send_keys(email)
        senha_input.send_keys(senha)
        registro_button.click()

    def is_welcome_page(self):
      
       
        return "/welcome" in self.driver.current_url
