class Transacao:
    db = {}
    _id_counter = 1

    def __init__(self, id, descricao, valor):
        self.id = id
        self.descricao = descricao
        self.valor = float(valor)

    @classmethod
    def create(cls, descricao, valor):
        t = cls(cls._id_counter, descricao, valor)
        cls.db[t.id] = t
        cls._id_counter += 1
        return t

    @classmethod
    def get_all(cls):
        return list(cls.db.values())

    @classmethod
    def update(cls, id, descricao, valor):
        if id in cls.db:
            if descricao: 
                cls.db[id].descricao = descricao
            if valor is not None: 
                cls.db[id].valor = float(valor)
            return cls.db[id]
        return None

    @classmethod
    def delete(cls, id):
        if id in cls.db:
            del cls.db[id]
            return True
        return False

# Dados iniciais para o "Read" 
Transacao.create("Salário Mensal", 5000.0)