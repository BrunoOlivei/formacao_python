from flask import Flask, render_template, request
from buscavogal import procura_letras

app = Flask(__name__)


@app.route('/procuraletra', methods=['POST'])
def faz_pesquisa() -> str:
    frase = request.form['frase']
    letras = request.form['letras']
    title = 'Aqui está o resultado:'
    resultado = str(procura_letras(frase, letras))
    return render_template('result.html', the_phrase=frase, the_letters=letras, the_result=resultado, the_title=title,)


@app.route('/')
@app.route('/entry')
def pagina_inicial() -> 'html':
    return render_template('entry.html', the_title="Bem vindo ao procure letras!")


if __name__ == '__main__':
    app.run(debug=True)
