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
valor2 = 69.75
valor3 = 1034.78
```

Vamos tentar imprimir o valor para que fiquem com o ponto que separa as casa decimais alinhados verticalmente.

```py
print("R$ ", valor1)  
print("R$ ", valor2)  
print("R$ ", valor3)
```

O resultado é:

```
R$ 4.59
R$ 69.9
R$ 1400.0
```

Agora vamos conhecer alguns argumentos que podemos passar utilizando a função format():

