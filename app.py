from bottle import Bottle, run
from controllers.portal_controller import PortalController
from controllers.banco_controller import BancoController

app = Bottle()

# Inicialização das rotas
PortalController(app)
BancoController(app)

if __name__ == '__main__':
    print("Servidor BMVC rodando em http://localhost:8000/portal")
    run(app, host='localhost', port=8000, debug=True, reloader=True)