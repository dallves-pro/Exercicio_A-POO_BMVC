class User_account:
    # Simulacao de banco de dados 
    users_db = {"admin": "1234", "davi": "senha123"}

    @classmethod
    def authenticate(cls, username, password):
        return cls.users_db.get(username) == password