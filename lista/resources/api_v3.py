'''
#from lista.schemas.schemas import ItemSchema,ItemModel,UsuarioModel,UsuarioSchema,ListaModel,ListaSchema,ItemLista
from flask_restful import Resource, reqparse, abort
from flask import request


#Esta classe representa um recurso na arquitetura REST.
#Ela implementa os métodos GET,POST,PUT e DELETE

class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('item',
                        type=str,
                        required=True,
                        help="O nome do Item não pode estar em branco."
                        )

    def get(self,item):
        json = ''
        try:
            item = ItemModel.encontrar_pelo_nome(item)
            if item:
                schema = ItemSchema(exclude=['listas'])
                json = schema.dump(item).data
            else:
                abort(404, message="Item {} não está na lista".format(item))
        except Exception as e:
            print(e)
            abort(404, message="Item {} não está na lista".format(item))

        return json,201


    def post(self):
        json = ''
        try:
            data = ItemResource.parser.parse_args()
            print(data)
            nome = data['item']
            item = ItemModel.encontrar_pelo_nome(nome)
            if item :
                return {"message":"Item {} já está na lista".format(nome)}
            else:
                item = ItemModel(nome=nome)
                item.adicionar()
                item = ItemModel.encontrar_pelo_nome(nome)
                schema = ItemSchema(exclude=['listas'])
                json = schema.dump(item).data
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    def delete(self,item):
        json = []
        try:
            item = ItemModel.encontrar_pelo_nome(item)
            if item:
                item.remover()
                lista = ItemModel.listar()
                schema = ItemSchema(many=True,exclude=['listas'])
                json = schema.dump(lista).data
            else:
                return {"message":"Item {} não está na lista".format(item)},404
        except Exception as e:
            print(e)
        return json, 201

    def put(self):
        json = ''
        try:
            data = ItemResource.parser.parse_args()
            nome = data['item']

            item = ItemModel.encontrar_pelo_nome(nome)
            if item :
                return {"message":"Item {} já está na lista".format(item)},200
            else:
                item = ItemModel(nome=nome)
                item.adicionar()
                schema = ItemSchema(many=True)
                item = ItemModel.encontrar_pelo_nome(nome)
                json = schema.dump(item).data
        except Exception as e:
            print(e)
        return json, 201



class ListaResource (Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("itens",
                        type=dict, location='json', action='append',
                        required=True,
                        help="O nome do Item não pode estar em branco."
                        )
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="O nome do Item não pode estar em branco."
                        )
    def post(self):
        json = ''
        try:
            data = ListaResource.parser.parse_args()
            if not data:
                return {"mensagem": "A requisição não tem dados JSON"}, 400
            lista = ListaModel.encontrar_pelo_nome(nome=data["nome"])
            if lista:
                return {"mensagem": "Uma lista já existe com esse nome"}, 400

            itens_lista = data['itens']
            nome = data['nome']
            lista = ListaModel(nome=nome,usuario_id=1)

            for i in itens_lista:
                il =ItemLista(preco="20 reais")
                item_temp = ItemModel.encontrar_pelo_nome(i['nome'])
                if item_temp:
                    il.item = item_temp
                else:
                    il.item = ItemModel(nome=i['nome'])
                lista.itens.append(il)
            lista.adicionar()
            lista = ListaModel.encontrar_pelo_nome(data["nome"])
            schema = ListaSchema()
            json = schema.dump(lista).data
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    def get(self,nome):
        json = ""
        try:
            item = ListaModel.encontrar_pelo_nome(nome)
            if item:
                schema = ItemSchema(many=False)
                json = schema.dump(item).data
            else:
                abort(404, message="Item {} não está na lista".format(item))
        except Exception as e:
            print(e)
            abort(404, message="Item {} não está na lista".format(item))

        return json, 201
class UsuarioResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("nome",
                        type=str,
                        required=True,
                        help="O nome do Usuario não pode estar em branco."
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="O email do Usuario não pode estar em branco."
                        )
    def get(self):
        json = ''
        return json, 200
    def post(self):
        try:
            data = UsuarioResource.parser.parse_args()
            if not data:
                return {"message": "Requisição sem JSON"}, 400

            if UsuarioModel.encontrar_pelo_nome(data['nome']):
                return {"message": "Usuário ja existe"}, 400
            else:
                usuario = UsuarioModel(data['nome'], data['email'])
                usuario.adicionar()
                usuario = UsuarioModel.encontrar_pelo_nome(data['nome'])

                user_schema = UsuarioSchema(exclude=['listas'])
                json = user_schema.dump(usuario).data
                return json, 201

        except Exception as ex:
            print(ex)
            return {"message": "erro"}, 500

    def put(self):
        json = ''
        return json, 201
class UsuariosResource(Resource):
    def get(self):
        json = ""
        try:
            usuarios = UsuarioModel.listar()
            schema = UsuarioSchema(many=True,exclude=['listas'])
            json = schema.dump(usuarios).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de usuarios."}, 500
        return json, 200

class ListasResource(Resource):

    def get(self):
        json = ""
        try:
            listas = ListaModel.listar()
            schema = ListaSchema(many=True)
            json = schema.dump(listas).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de compras."}, 500
        return json, 200



class ItensResource(Resource):
    def get(self):
        json = []
        try:
            itens = ItemModel.listar()
            schema = ItemSchema(many=True,exclude=['listas'])
            json = schema.dump(itens).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de compras."}, 500
        return json,201
'''