from flask import Flask, render_template, request, escape
from buscavogal import procura_letras

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('procura_letras_log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/procuraletra', methods=['POST'])
def faz_pesquisa() -> str:
    frase = request.form['frase']
    letras = request.form['letras']
    title = 'Aqui está o resultado:'
    resultado = str(procura_letras(frase, letras))
    log_request(request, resultado)
    return render_template('result.html', the_phrase=frase, the_letters=letras, the_result=resultado, the_title=title,)


@app.route('/')
@app.route('/entry')
def pagina_inicial() -> 'html':
    return render_template('entry.html', the_title="Bem vindo ao procure letras!")


@app.route('/viewlog')
def view_log() -> 'html':
    conteudos = []
    with open('procura_letras_log') as log:
        for linha in log:
            conteudos.append([])
            for item in linha.split('|'):
                conteudos[-1].append(escape(item))
    titulos = ('Informacoes Formulario', 'Endereço Remoto', 'Navegador e SO', 'Resultados')
    return render_template('viewlog.html', the_title="Log", the_row_titles=titulos, the_data=conteudos,)


if __name__ == '__main__':
    app.run(debug=True)
