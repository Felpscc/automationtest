Feature: Teste de login no site

  Scenario: Login bem-sucedido
    Given O usuário está na página de login
    When O usuário insere as credenciais corretas
    And O usuário clica no botão de login
    Then O usuário deve ser redirecionado para a página de dashboard

 Scenario: Registro de Novo Usuário
    Given O usuário está na página de registro
    When O usuário preenche o formulário de registro com informações válidas
    And O usuário clica no botão de registro
    Then O usuário deve ser redirecionado para a página de boas-vindas

 Scenario: Registro de Novo Usuário com Senha Fraca
    Given O usuário está na página de registro
    When O usuário preenche o formulário de registro com uma senha fraca
    And O usuário clica no botão de registro
    Then O usuário deve ver uma mensagem de erro informando sobre a senha fraca

 Scenario: Login com Credenciais Incorretas
    Given O usuário está na página de login
    When O usuário insere credenciais incorretas
    And O usuário clica no botão de login
    Then O usuário deve ver uma mensagem de erro de login

 Scenario: Esqueceu a Senha
    Given O usuário está na página de login
    When O usuário clica no link "Esqueceu a senha?"
    And O usuário preenche seu e-mail de recuperação
    And O usuário clica no botão de recuperação de senha
    Then O usuário deve ver uma mensagem de sucesso de recuperação de senha
    
 Scenario: Navegação no Menu Principal
    Given O usuário está logado na página de dashboard
    When O usuário clica em "Perfil" no menu principal
    Then O usuário deve ser redirecionado para a página de perfil do usuário
    And O usuário clica em "Configurações" no menu principal
    Then O usuário deve ser redirecionado para a página de configurações

 Scenario: Pesquisa no Site
    Given O usuário está na página inicial do site
    When O usuário insere um termo de pesquisa no campo de busca
    And O usuário clica no botão de pesquisa
    Then O usuário deve ver os resultados da pesquisa

 Scenario: Adição de Produto ao Carrinho
    Given O usuário está na página de detalhes do produto
    When O usuário clica no botão "Adicionar ao Carrinho"
    Then O usuário deve ver uma mensagem de confirmação de adição ao carrinho
    And O usuário verifica o carrinho e vê o produto adicionado

 Scenario: Checkout de Compra
    Given O usuário está no carrinho de compras
    When O usuário clica no botão "Finalizar Compra"
    And O usuário preenche as informações de entrega e pagamento
    And O usuário confirma a compra
    Then O usuário deve ver uma mensagem de sucesso de compra

 Scenario: Atualização do Perfil do Usuário
    Given O usuário está logado na página de perfil do usuário
    When O usuário atualiza as informações do perfil
    And O usuário clica no botão "Salvar Alterações"
    Then O usuário deve ver uma mensagem de sucesso de atualização do perfil
   
   
   
   
