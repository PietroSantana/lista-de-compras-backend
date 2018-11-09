from datetime import datetime

class Usuario(object):
    def __init__(self, nome, email,listas):
        self.nome = nome
        self.email = email
        self.dataCriacao = datetime.now()
        self.listas = listas
