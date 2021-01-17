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



