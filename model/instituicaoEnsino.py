from flask_restful import fields
from helpers.database import db
from model.endereco import endereco_fields

instituicaoEnsino_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'telefone': fields.String,
  'endereco': fields.Nested(endereco_fields),
}


class InstituicaoEnsino(db.Model):
  __tablename__ = "instituicao_ensino"

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String, nullable=False)
  telefone = db.Column(db.String, nullable=False)
  id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'))

  aluno = db.relationship("Aluno", uselist=False, backref="instituicao_ensino")

  def __init__(self, nome, telefone, id_endereco):
    super().__init__()
    self.nome = nome
    self.telefone = telefone
    self.id_endereco = id_endereco

  def __repr__(self):
    return f'<Endereço>'