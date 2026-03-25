from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo de Dados para o Progresso (Aula 6)
class Progresso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fase_atual = db.Column(db.Integer, default=1)
    erros = db.Column(db.Integer, default=0)
    concluido = db.Column(db.Boolean, default=False)