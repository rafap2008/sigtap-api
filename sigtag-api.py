import os
from flask import Flask #, request, render_template
from flask_cors import CORS

from src.fb import getSelect

os.system('color')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def get_index():
    return "Server is online!"    

@app.route("/teste", methods=["GET"])
def get_teste():
    print(getSelect("SELECT * FROM TAREFAS"))
    return "Query executed, check console for results."

if __name__ == "__main__" :
    _host = "0.0.0.0"
    _port = 99
    host = str(os.environ.get("HOST",_host))
    port = int(os.environ.get("PORT",_port))
    app.run(host=host, port=port)