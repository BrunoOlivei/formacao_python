# .split()
Split divide os caracteres que estão separados por espaço dentro de uma única string, adicionando os como itens separados em uma lista.

```python
nome = "Bruno Oliveira"
print(nome.split())

['Bruno', 'Oliveira']

nome = "BrunoOliveir a"
print(nome.split())

['BrunoOliveir', 'a']
```

---
<br>

# .strip()
Esse método remove espaços no começo e/ou no fim de uma string, sem eliminar o espaço entre 2 palavras por exemplo.

```python
>>> nome = ' Bruno '

>>> print(nome)

' Bruno '

>>> nomme.strip()
>>> print(nome)

'Bruno'
```

---
<br>

# .title()
Retorna uma string com a primeira letra maiúscula (capitaliza), muito útil para formulários que contenham texto de input e as pessoas acidentalmente digitam o nome com a primeira letra minúscula.

```python
>>> nome = 'bruno'
>>> print(nome)

'bruno'

>>> nome.title()
>>> print(nome)

'Bruno'
```

---
<br>

# .join()
Esse métodos retorna um iterável um uma string novamente:

```python
>>> exemplo = ['B', 'r', 'u', 'n', 'o', ' ', 'O', 'l', 'i', 'v', 'e', 'i', 'r', 'a']
```

Usando o join para concatenar os elementos da lista:

Cria-se a variável que irá receber o resultado da concatenação, executa o .join() e imprime o resultado:

```python
>>> teste = ''

>>> teste = teste.join(exemplo)
>>> print(teste)
```

Se criarmos a variável com uma string vazia, ou seja um espaço o resultado não será desejado:

```python
>>> teste = ' '

>>> teste = teste.join(exemplo)
>>> print(teste)

B r u n o   O l i v e i r a
```

Podemos executar de outras maneiras, este resultado já imprime direto o resultado, sem armazenar em nenhuma variável:

```python
>>> print(''.join(exemplo))

Bruno Oliveira
```

Podemos acrescentar elementos entre as letras da string:

```python
>>> print('-'.join(exemplo))

B-r-u-n-o- -O-l-i-v-e-i-r-a
```

---
<br>

# .capitalize()
Retorna o primeiro caractére da string maiúsculo e o restante minusculo:

```python
>>> palavra = "banana"
>>> print(palavra.capitalize())
Banana

>>> palavra = "BANANA"
>>> print(palavra.capitilize())
Banana

```

---
<br>

# .find()
Está função busca dentro de uma string os caracteres que forem passados como argumentos, retornando a posição em que se encontra o caractere, caso não encontre, retorna -1

```py
>>> palavra = "banana"
>>> print(palavra.find("b"))
0

>>> print(palavra.find("n"))
2

>>> print(palavra.find("z"))
-1
```

Caso a palavra tenha letras repetidas, o .find retorna o indice em que o caractere ocorre primeiro, sempre da esquerda para a direita.

---
<br>

# Slice:
------

Este método não é exatamente uma função integrada, é mais como uma ferramenta que pode ser utilizada com qualquer iterável, incluindo as strings.

Os números utilizados dentro dos colchetes funcionam como índices, o primeiro elemento de um iterável sempre é 0.

```python
>>> print('Bruno Oliveira'[0:5])

Bruno
```

Dentro dos colchetes:

1.  O primeiro número sempre será onde o 'slice' irá iniciar
2.  Dois pontos :
3.  O segundo número sempre será onde o slice termina, excluindo o elemento na qual está o índice.
4.  Dois pontos :
5.  Ainda é possível adicionar um número negativo após tudo para que o slice seja feito de trás para frente

```python
>>> print('Bruno Oliveira'[-10:-15:-1])

onurB
```

---

