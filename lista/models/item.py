'''
from datetime import datetime
class Item(object):
    def __init__(self, _id, nome):
        self.id = _id
        self.nome = nome
        self.dataCriacao = datetime.now()
'''