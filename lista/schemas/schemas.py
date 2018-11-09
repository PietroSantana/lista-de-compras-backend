from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields, post_dump
#from lista.models.dao_v2 import ItemModel,ListaModel,UsuarioModel,ItemLista
from lista.models.item_model import ItemModel
from lista.models.usuario_model import UsuarioModel
from lista.models.lista_model import ListaModel
from lista.models.item_lista_model import ItemLista

class ItemSchema(ModelSchema):
    listas = fields.Nested("ListaSchema",many=True, exclude=('itens','usuario'))
    class Meta:
        model = ItemModel

class ListaSchema(ModelSchema):
    itens = fields.Nested('ItemListaSchema', many=True)
    usuario = fields.Nested('UsuarioSchema', many=False, only=['nome'])
    class Meta:
        model = ListaModel

class ItemListaSchema(ModelSchema):
    item = fields.Nested("ItemSchema", many=False, only=['nome'])
    #preco = fields.Str()
    class Meta:
        model: ItemLista
        
class UsuarioSchema(ModelSchema):
    listas = fields.Nested('ListaSchema',many=True, only=['nome'])
    class Meta:
        model = UsuarioModel
