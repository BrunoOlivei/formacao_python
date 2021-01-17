# Criando uma funcionalidade dinâmica entre a palavra secreta e a lista de letras acertadas:



Utilizando List Comprehension:

```python
lista = ["_" for letra in palavra_secreta]
```

O que o sistema diz nesse código é usar este caractere ("_") dentro da palavra secreta.

Essa linha de código substitui facilmente um bloco de laço for como a seguir:

```python
lista = []
palavra_secreta = "banana"

for letra in palavra_secreta:
    lista.append("_")
```



Podemos utilizar também condições if para criar listas específicas, por exemplo uma lista de números pares baseadas em uma outra lista, por exemplo:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = []

for n in numeros:
    if n % 2 == 0:
        numeros_pares.append(n)
        
print(numeros_pares)
```

O resultado esperado é uma lista apenas com os números pares.

Utilizando o lista comprehension, podemos fazer:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = [n for n in numeros if n % 2 == 0]

print(numeros_pares)
```

