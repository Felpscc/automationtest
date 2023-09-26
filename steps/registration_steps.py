from behave import given, when, then
from pages.registration_page import RegistrationPage  # Importe a classe RegistrationPage correspondente

@given('O usuário está na página de registro')
def step_given_user_on_registration_page(context):
    context.registration_page = RegistrationPage(context.driver)
    context.registration_page.navigate_to_registration_page()

@when('O usuário preenche o formulário de registro com informações válidas')
def step_when_user_enters_valid_registration_info(context):
    context.registration_page.enter_registration_info('nome', 'email', 'senha')

@when('O usuário clica no botão de registro')
def step_when_user_clicks_registration_button(context):
    context.registration_page.click_registration_button()

@then('O usuário deve ser redirecionado para a página de boas-vindas')
def step_then_user_redirected_to_welcome_page(context):
    assert context.registration_page.is_welcome_page(), 'Redirecionamento para a página de boas-vindas falhou'


