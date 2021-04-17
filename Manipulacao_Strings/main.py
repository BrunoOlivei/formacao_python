from ExtratorArgumentosUrl import ExtratorArugmentosUrl
import re
'''
url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"

argumentos_url = ExtratorArugmentosUrl(url)
moeda_origem, moeda_destino = argumentos_url.retorna_moedas()
valor = argumentos_url.extrai_valor()
print(moeda_origem, moeda_destino, valor)
'''

# Expressões Regulares
# Utilizando exemplo de um texto contendo um número de celular

texto1 = "Bom dia, gostaria de agendar uma consulta, Bruno Oliveira, 99850-8547"
texto2 = "Boa tarde, sou Bruno, 99850-8547, quero agendar uma consulta."
texto3 = "99850-8547 Digitou: Olá sou Bruno, gostaria de agendar uma consulta."
texto4 = "99850-8547"

padrao_celulares = "[0-9]{4,5}[-][0-9]{4}"

telefone = re.search(padrao_celulares, texto1)
print(telefone.group())
