from datetime import datetime
class Lista(object):
    def __init__(self,_id,nome,usuario,itens):
        self.id = _id
        self.usuario = usuario
        self.itens = itens
        self.dataCriacao = datetime.now()
        self.nome = nome

