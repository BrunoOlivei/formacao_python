import re
# Expressões Regulares
# Utilizando exemplo de um texto contendo um número de celular

email_1 = "Meu número é 1234-1234"
email_2 = "Fale comigo em 1234-1234, esse é meu telefone"
email_3 = "1234-1234 é o meu celular"

padrao = "[0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"

retorno = re.search(padrao, email_1)
print(retorno.group())
