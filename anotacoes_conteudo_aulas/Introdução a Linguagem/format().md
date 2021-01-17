# Função format()
A função format é muito útil quando queremos, por exemplo, inserir os valores de váriáveis dentro de uma string. 

Um exemplo prático:
```py
valor = 3.50
quantidade = 7

print("O valor é", valor, "Há em estoque: ", quantidade)

O valor é 3.5 Há em estoque:  7
```

Nós podemos deixar o código visualmente melhor utilizando a função format(). 

```py
valor = 3.50
quantidade = 7

print("O valor é {}. Há em estoque: {}".format(valor, quantidade))

O valor é 3.5. Há em estoque: 7
```
Podemos observar que utilizando chaves {} podemos criar campos que serão preenchidos pelos valores das variáveis conforme a ordem em que foram declaradas na função format.

É possível utilizar argumentos dentro das chaves {} que indicarão qual valor receber da função format:

```py
valor = 3.50
quantidade = 7

print("O valor é {1}. Há em estoque: {0}".format(valor, quantidade))

O valor é 7. Há em estoque: 3.5
```

A função format também é muito útil para deixar a visualização mais agradável:

Suponhamos que você queira visualizar uma lista de valores diversos:

```py
valor1 = 1.59
valor2 = 69.90
valor3 = 1400.00
```

Vamos tentar imprimir o valor para que fiquem com o ponto que separa as casa decimais alinhados verticalmente.

```py
print("R$ ", valor1)  
print("R$ ", valor2)  
print("R$ ", valor3)
```

O resultado é:

```
R$ 1.59
R$ 69.9
R$ 1400.0
```

Repare que em valores decimais como 90, 10, 20 etc, a linguagem omite o 0.
Agora vamos conhecer alguns argumentos que podemos passar utilizando a função format():

```py
print("R$ {:f}".format(valor2))
```

O {:f} configura as casas decimais após o ponto. O f aqui significa float, que é um tipo de dado utilizado em python para números decimais (reais). O resultado que obtemos é o seguinte:

```
R$ 69.900000
```

O que queremos é que os valores decimais tenham duas casas sempre, independente de serem multiplos de 10 ou se tenham mais de 2 casa decimais (como nos valores de preços de combustível):

Para isso basta acrescentar um ponto (.) entre os dois pontos e o f e informar a quantidade de casas que desejamos apresentar:

```py
print("R$ {:.2f}".format(valor2))
```

Teremos o seguinte resultado:

```
R$ 69.90
```

Nós também podemos criar campos na parte esquerda para alinharmos por exemplo os números e ter uma visualização melhor. Podemos alinhar com os pontos decimais por exemplos:

```py
print("R$ {:7.2f}".format(valor1))  
print("R$ {:7.2f}".format(valor2))  
print("R$ {:7.2f}".format(valor3))
```

Os resultados são:
```
R$    4.59
R$   69.90
R$ 1400.00
```

Bem melhor para visualização.

Também podemos preencher os espaços criados ao lado esquerdo do número:

```py
print("R$ {:07.2f}".format(valor1))
print("R$ {:07.2f}".format(valor2))
print("R$ {:07.2f}".format(valor3))
```

O resultado é:
```
R$ 0004.59
R$ 0069.90
R$ 1400.00
```

Também podemos fazer essas definições de formatação para numeros inteiros. No caso ao invés de utilizarmos o f, a linguagem python pede que utiliza a letra d:

```py
print("R$ {:7d}".format(6))
```

O resultado:
```
R$       6
```

Um outro exemplo interessante de utilização dessa função é para imprimir datas:

```py
print("Data {:02d}/{:02d}".format(9,4))
print("Data {:02d}/{:02d}".format(19,11))
```

O resultado:

```
Data 09/04
Data 19/11
```

___

# Python 2 x Python 3
A interpolação foi alterada de uma versão para a outra:

No python 3 utilizamos `"{} {}".format(1, 2)`, já no python 2 não era utilizada a função format para tal, utilizava-se o caracetere `%`:

```
"%d %d" % (1, 2)
```

___

# Atualização Python 3.6

A partir desta versão, foi criado um novo recurso para realização da interpolação de strings, chamado de *f-strings* ou *formatted string literals*

Basicamente ele acrescenta a letra f antes da string (caracterizada pelas aspas duplas ou simples):

```py
print(f"O valor é: {valor1}.")
```

O interessante deste recurso é que podemos passar funções dentro das {}:

```py
print(f"O valor é: {valor1 * valor2}.")
```

---

# Conclusão
Existem inumeras funcionalidades com a interpolação que é uma ferramenta poderosa para a formatação dos dados, sejam ele obtidos pelo usuário, seja através de outros serviços. O importante aqui é saber que existe a possibilidade e quando for necessário saber como e onde buscar essas informações, seja para relembrar, seja para pesquisar se existe a possibilidade de realizar o que você deseja.

