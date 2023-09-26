from behave import given, when, then
from pages.login_page import LoginPage  # Importe a classe LoginPage correspondente

@given('O usuário está na página de login')
def step_given_user_on_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to_login_page()

@when('O usuário insere as credenciais corretas')
def step_when_user_enters_correct_credentials(context):
    context.login_page.enter_username('seu_usuario')
    context.login_page.enter_password('sua_senha')

@when('O usuário clica no botão de login')
def step_when_user_clicks_login_button(context):
    context.login_page.click_login_button()

@then('O usuário deve ser redirecionado para a página de dashboard')
def step_then_user_redirected_to_dashboard(context):
    assert context.login_page.is_dashboard_page(), 'Redirecionamento para a página de dashboard falhou'


