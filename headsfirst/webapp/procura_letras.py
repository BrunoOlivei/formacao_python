from flask import Flask, render_template
from buscavogal import procura_letras

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/procuraletra', methods=['POST'])
def faz_pesquisa() -> str:
    return str(procura_letras('Life, the universe and everything', 'eiru'))


@app.route('/entry')
def pagina_inicial() -> 'html':
    return render_template('entry.html', the_title="Bem vindo ao procure letras!")


app.run(debug=True)
