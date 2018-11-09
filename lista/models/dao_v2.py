from dao import db,Base
from datetime import datetime
from sqlalchemy.ext.associationproxy import association_proxy

class ItemModel(Base):
    __tablename__ = 'itens'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), unique=True)
    data_criacao = db.Column(db.DateTime)
    listas = db.relationship("ItemLista", back_populates="item")

    def __init__(self, nome):
        self.nome = nome
        self.data_criacao = datetime.now()

    def adicionar(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def encontrar_pelo_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def encontrar_pelo_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def listar(cls):
        return cls.query.all()

    def remover(self):
        db.session.delete(self)
        db.session.commit()
        
class ItemLista(Base):
    __tablename__ = 'itenslistas'
    lista_id = db.Column(db.Integer, db.ForeignKey('listas.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('itens.id'), primary_key=True)
    preco = db.Column(db.String(100))
    item = db.relationship("ItemModel", back_populates="listas", uselist=False)
    lista = db.relationship("ListaModel", back_populates="itens", uselist = False)
    def __init__(self, preco):
        self.preco = preco

class ListaModel(Base):
    __tablename__ = 'listas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), unique=True)
    usuario_id = db.Column(db.Integer,db.ForeignKey("usuarios.id"))
    usuario = db.relationship("UsuarioModel", back_populates="listas")

    dataCadastro = db.Column(db.DateTime)
    itens = db.relationship("ItemLista", back_populates="lista")
    def __init__(self,nome,usuario_id):
        self.nome = nome
        self.usuario_id = usuario_id
        self.dataCadastro = datetime.now()

    def adicionar(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def encontrar_pelo_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def encontrar_pelo_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def listar(cls):
        return cls.query.all()

    def remover(self):
        db.session.delete(self)
        db.session.commit()



class UsuarioModel(Base):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200),unique=True)
    email = db.Column(db.String(200),unique=True)
    dataCadastro = db.Column(db.DateTime)
    listas = db.relationship("ListaModel",back_populates="usuario")

    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
        self.dataCadastro = datetime.now()

    def adicionar(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def encontrar_pelo_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def encontrar_pelo_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def listar(cls):
        return cls.query.all()

    def remover(self):
        db.session.delete(self)
        db.session.commit()

