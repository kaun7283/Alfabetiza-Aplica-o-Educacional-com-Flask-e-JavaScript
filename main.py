from flask import Flask
import os

app = Flask(__name__)

# Configuração do Banco de Dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'alfabetiza.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db
db.init_app(app)

with app.app_context():
    db.create_all()

from views import *

if __name__ == "__main__":
    app.run(debug=True)