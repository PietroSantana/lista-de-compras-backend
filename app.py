from flask import Flask
from flask_cors import CORS
from flask_restful import Api
#from lista.resources.api_v2 import Item,ItemList
from lista.resources.api_v3 import ItemResource,ItensResource, UsuarioResource, ListaResource, ListasResource,\
    UsuariosResource
app = Flask(__name__)
#Configurações relativas ao sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

app.secret_key = b'\xc4]gW\x0f\x8d\xc8\x05ocG\xf1\xb1j,{'

#fim configurações relativas ao sqlalchemy
api = Api(app)
CORS(app,resources={r"/*": {"origins": "*"}}) #O uso do cors
#cria as tabelas do banco de dados, caso elas não estejam criadas
@app.before_first_request
def create_tables():
    print("oi create tables!")
    db.create_all()
#fim criaçaõ de tabelas


api.add_resource(ItensResource, '/itens')
api.add_resource(ItemResource, '/item', '/item/<string:item>')
api.add_resource(ListasResource, '/listas')
api.add_resource(ListaResource, '/lista','/lista/<string:lista>')
api.add_resource(UsuarioResource,'/usuario','/usuario/<string:usuario>')
api.add_resource(UsuariosResource, '/usuarios')

if __name__ == '__main__':
    from dao import db
    db.init_app(app)
    app.run(port=5000,debug=True)
