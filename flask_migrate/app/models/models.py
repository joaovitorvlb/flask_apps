from app import db


class Users(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    cpf = db.Column(db.String(128))
    idade = db.Column(db.Integer)


class Products(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    peso = db.Column(db.String(128))
    quantidade = db.Column(db.String(128))
