import os
from flask import Flask
from flask_cors import CORS

from src.fb import getSelect
from src.consultas import CabecalhoSql, getListaTabelas, getColunasTabela, getDadosTabela, getConsulta
from src.lib import getRotasApi, getHome

os.system('color')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def get_index():
    return getHome(app)

@app.route("/rotas", methods=["GET"])
def get_rotas_api():
    return getRotasApi(app)

@app.route("/lista-tabelas", methods=["GET"])
def get_lista_tabelas():
    return getListaTabelas()

@app.route("/colunas-tabela/<tabela>", methods=["GET"])
@app.route("/colunas-tabela/<tabela>/<cabecalho>", methods=["GET"])
def get_colunas_tabela(tabela, cabecalho=CabecalhoSql.UNICO):
    return getColunasTabela(tabela, cabecalho)

@app.route("/dados-tabela/<tabela>", methods=["GET"])
@app.route("/dados-tabela/<tabela>/<cabecalho>", methods=["GET"])
def get_dados_tabela(tabela, cabecalho=CabecalhoSql.UNICO):
    return getDadosTabela(tabela, cabecalho)

@app.route("/consulta/<script>", methods=["GET"])
@app.route("/consulta/<script>/<cabecalho>", methods=["GET"])
def get_consulta(script, cabecalho=CabecalhoSql.UNICO):
    return getConsulta(script, cabecalho)

if __name__ == "__main__" :
    _host = "0.0.0.0"
    _port = 99
    host = str(os.environ.get("HOST",_host))
    port = int(os.environ.get("PORT",_port))
    app.run(host=host, port=port)