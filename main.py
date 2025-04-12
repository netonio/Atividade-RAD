from flask import Flask, render_template, request, redirect, url_for
from db import db
from models import Produtos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///estoque.db"
db.init_app(app)

# Criando funções para buscas

def buscar_produto_id(produto_id):
    return Produtos.query.get(produto_id)

def buscar_produto_nome(produto_nome):
   return Produtos.query.filter(Produtos.nome.ilike(f'%{produto_nome}%')).all()

# Criando rotas

@app.route("/")
def homepage():
   produtos = db.session.query(Produtos).all()
   return render_template("homepage.html", produtos = produtos)

@app.route("/adicionar", methods=['GET', 'POST'])
def adicionar():
   if request.method == 'GET':
      return render_template("adicionar.html")
   
   elif request.method == 'POST':

      nome = request.form['nomeForm']
      preco = float(request.form['precoForm'])
      quantidade = request.form['quantidadeForm']

      novo_produto = Produtos(nome = nome, preco = preco, quantidade = quantidade)
      db.session.add(novo_produto)
      db.session.commit()

      return redirect(url_for("homepage"))
   
@app.route("/editar/<int:id>", methods = ["GET", "POST"])
def editar(id):
   produto = db.session.query(Produtos).filter_by(id=id).first()

   if request.method == "GET":
      return render_template("editar.html", produto = produto)

   elif request.method == "POST":
      nome = request.form['nomeForm']
      preco = float(request.form['precoForm'])
      quantidade = request.form['quantidadeForm']

      produto.nome = nome
      produto.preco = preco
      produto.quantidade = quantidade
      db.session.commit()

      return redirect(url_for("homepage"))

@app.route("/remover/<int:id>", methods = ['GET', 'POST'])
def deletar(id):
   produto = db.session.query(Produtos).filter_by(id=id).first()
   db.session.delete(produto)
   db.session.commit()

   return redirect(url_for("homepage"))

@app.route("/pesquisar", methods=['GET'])
def pesquisar():
   pesquisa = request.args.get("pesquisa")

   if not pesquisa:
      return render_template("homepage.html", produtos=[])
   
   if pesquisa.isdigit():
      produto = buscar_produto_id(int(pesquisa))
      return render_template("homepage.html", produtos=[produto] if produto else [])
   else:
      produtos = buscar_produto_nome(pesquisa)
      return render_template("homepage.html", produtos=produtos)

if __name__ == "__main__":
   with app.app_context():
      db.create_all()

   app.run(debug=True)