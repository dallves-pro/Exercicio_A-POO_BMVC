# Exercício A/POO - BMVC

## Funcionalidades
1. **Recurso `Portal`**: Um painel de entrada exige a autenticação do usuário (integrada ao `user_account`), valida as credenciais e fornece acesso seguro (via cookies assinados).
2. **Recurso `Banco`**: Área privada onde os usuários autenticados podem visualizar as suas movimentações financeiras via interface web (Read).
3. **API RESTful Integrada**: Endpoints para executar o CRUD completo nas transações, desenvolvidos para aceitação de operações via terminal (cURL).

## Arquitetura
* **Models**: `user_account.py` (lógica de usuários) e `transacao.py` (representação e regras dos lançamentos financeiros).
* **Controllers**: `portal_controller.py` e `banco_controller.py` roteando os requests HTML e requisições cURL.
* **Views**: Formulários de login e exibição de saldos em arquivos HTML.

## Como rodar
1. Instale o framework: `pip install bottle`
2. Execute o servidor: `python3 app.py`
3. Acesse `http://localhost:8000/portal` (Login de teste: `admin`/`1234`).

## Comandos de cURL 
Exemplo de gerenciamento do sistema diretamente do terminal:

* **Adicionar despesa ou receita**:
  `curl -X POST http://localhost:8000/api/banco -H "Content-Type: application/json" -d '{"descricao": "Energia", "valor": -150.00}'`
* **Atualizar lançamento**:
  `curl -X PUT http://localhost:8000/api/banco/1 -H "Content-Type: application/json" -d '{"valor": -160.00}'`
* **Remover lançamento**:
  `curl -X DELETE http://localhost:8000/api/banco/1`
