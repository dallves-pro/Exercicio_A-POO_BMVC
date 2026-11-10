from bottle import request, response, template, redirect
from models.user_account import User_account

class PortalController:
    def __init__(self, app):
        self.app = app
        self.app.route('/portal', method='GET', callback=self.portal_get)
        self.app.route('/portal', method='POST', callback=self.portal_post)

    def portal_get(self):
        return template('views/portal.html')

    def portal_post(self):
        username = request.forms.get('username')
        password = request.forms.get('password')
        
        if User_account.authenticate(username, password):
            # Definicao do cookie de autenticacao com chave secreta
            response.set_cookie('auth', username, secret='bmvc-chave-secreta')
            redirect('/banco')
        else:
            return "<h3>Falha no login. <a href='/portal'>Tente novamente</a></h3>"