from bottle import request, template, redirect
from models.transacao import Transacao

class BancoController:
    def __init__(self, app):
        self.app = app
        # API CRUD para requisicoes via cURL 
        self.app.route('/api/banco', method='POST', callback=self.create)
        self.app.route('/api/banco', method='GET', callback=self.read_api)
        self.app.route('/api/banco/<id:int>', method='PUT', callback=self.update)
        self.app.route('/api/banco/<id:int>', method='DELETE', callback=self.delete)
        
        # Endpoint visual ("Read" interno)
        self.app.route('/banco', method='GET', callback=self.read_web)

    def _verificar_autenticacao(self):
        usuario = request.get_cookie('auth', secret='bmvc-chave-secreta')
        if not usuario:
            redirect('/portal')
        return usuario

    def read_web(self):
        usuario = self._verificar_autenticacao()
        transacoes = Transacao.get_all()
        return template('views/banco.html', usuario=usuario, transacoes=transacoes)
        
    def create(self):
        dados = request.json
        nova_transacao = Transacao.create(dados['descricao'], dados['valor'])
        return {"status": "sucesso", "id": nova_transacao.id}
        
    def read_api(self):
        return {"transacoes": [t.__dict__ for t in Transacao.get_all()]}
        
    def update(self, id):
        dados = request.json
        if Transacao.update(id, dados.get('descricao'), dados.get('valor')):
            return {"status": "Atualizado com sucesso"}
        return {"erro": "Transacao nao encontrada"}
        
    def delete(self, id):
        if Transacao.delete(id):
            return {"status": "Deletado com sucesso"}
        return {"erro": "Transacao nao encontrada"}