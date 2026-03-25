from main import app
from flask import render_template, jsonify, redirect, url_for
from models import db, Progresso

@app.route("/")
def homepage():
    return render_template("index.html")

# Rotas das fases
@app.route("/fase1")
def fase1(): return render_template("main1.html")

@app.route("/fase2")
def fase2(): return render_template("main2.html")

@app.route("/fase3")
def fase3(): return render_template("main3.html")

@app.route("/fase4")
def fase4(): return render_template("main4.html")

@app.route("/fase5")
def fase5(): return render_template("main5.html")

@app.route("/fase6")
def fase6(): return render_template("main6.html")

@app.route("/fase7")
def fase7(): return render_template("main7.html")

@app.route("/fase8")
def fase8(): return render_template("main8.html")

@app.route("/fase9")
def fase9(): return render_template("main9.html")

@app.route("/fase10")
def fase10(): return render_template("main10.html")

@app.route("/completed")
def completed():
    return render_template("completed.html")

# Lógica de IA/Monitoramento: Registra erros no banco via JS
@app.route("/registrar_erro")
def registrar_erro():
    prog = Progresso.query.first()
    if not prog:
        prog = Progresso()
        db.session.add(prog)
    
    prog.erros += 1
    db.session.commit()
    return jsonify({"total_erros": prog.erros})

@app.route("/relatorio")
def relatorio():
    # Busca o progresso no banco de dados
    prog = Progresso.query.first()
    
    # Se ainda não houver dados, cria um objeto vazio para não dar erro na tela
    if not prog:
        prog = {'fase_atual': 1, 'erros': 0, 'concluido': False}
        
    return render_template("relatorio.html", dados=prog)