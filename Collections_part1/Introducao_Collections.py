"""
A ideia das coleções é que tenhamos mais de um elemento, suponhamos que temos um sistema que receba a idade dos usuários
a cada nova entrada de idade, precisariamos criar uma nova variável para receber essa nova idade
"""

idade1 = 32
idade2 = 30
idade3 = 45
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

'''
Para casos como esse existem as listas (list) onde podemos inserir os valores entre colchetes. É comum e uma boa prática
trabalharmos com listas que contenham valores do mesmo TIPO, isso quer dizer somente números inteiros ou somente 
strings por exemplo.
'''

idades = [32, 30, 45, 18]

'''
As listas são a implementação de uma "ideia" para uma sequencia de acesso aleatório onde podemos solicitar o acesso ao
elemento da segunda posição ou da quarta por exemplo, as listas em python podem ser comumente comparadas as *arrays* em 
outras linguagens, porém no python listas e arrays são coisas distintas.

Existem diversos métodos que podem ser utilizados com e para a lista. Um deles é o len()
'''

print(len(idades))

'''
Como dito anteriormente podemos também consultar elementos específicos dentro das listas baseando em suas posições, 
lembrando que em python a contagem começa sempre a partir de 0 então para encontrar o primeiro elemento pedimos a 
posição 0
'''

print(idades[0])

'''
As listas são dinamicas, podendo aumentar ou diminuir sob demanda. Isso quer dizer que podemos acrescentar elementos
a uma lista pré-existente ou remover. Como dito anteriormente as listas possuem diversos métodos pré definidos que podem
ser utilizados para manipular os elementos. Para "chamar" um método utilizamos a **notação de ponto**, um exemplo é o 
`append()` que acrescenta um novo elemento **sempre ao final da lista**.
'''

idades.append(15)
print(idades)

'''
Se tentarmos acessar agora a posição 4, teremos como resultado o valor 15. Agora e se tentarmos acessar a posição 5 por
exemplo
'''
# print(idades[5])
'''
Temos como retorno um erro de indice "IndexError: list index out of range"
'''

'''
Podemos também iterar sobre os elementos da lista, utilizando o laço for
'''
for idade in idades:
    print(idade)

'''
Podemos também remover elementos da lista, utilizando o método remove que também é usado através da notação de ponto. 
Diferentemente do método append, que insere um novo elemento sempre ao final da lista, o método remove retira um 
elemento informado dentro dos parênteses como argumento. Caso a lista contenha mais de um elemento com mesmo valor, o 
o método remove a primeira aparição (ocorrência) do elemento, da esquerda para a direita. Caso o método não encontre o 
elemento passado como argumento, ele retorna um ValueError.
'''

idades.remove(15)
print(idades)

'''
Para remover todos os elementos da lista de uma só vez, podemos utilizar o método `clear()` que limpa toda a lista, 
removendo todos os elementos de uma só vez. 
'''

idades.clear()
print(idades)
