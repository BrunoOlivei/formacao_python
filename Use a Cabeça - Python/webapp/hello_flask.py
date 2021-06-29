from flask import Flask
from buscavogal import procura_letras

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/procuraletra')
def faz_pesquisa() -> str:
    return str(procura_letras('Life, the universe and everything', 'eiru'))

app.run()
