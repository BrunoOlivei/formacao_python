# Lendo arquivos



[TOC]

## Introdução

Após aprendermos sobre abrir arquivos, criarmos, escrevermos ou até mesmo sobrescrevermos, é chegado a hora de lermos o seu conteúdo e utilizarmos dentro da linguagem python. 

Para isso é importante lembrarmos que no momento em que executamos a função `open()` precisamos parametrizar o modo no qual este arquivo será aberto, se será só leitura, se será só escrita, se será só criação e escrita, etc. 

No nosso caso iremos acessar um arquivo que já existe e não temos a intenção de edita-lo, sendo assim o modo que utilizaremos é o "r":

```python
>>> arquivo = open("palavras.txt", "r")

```



## .read()

A função read, como do inglês "ler", serve para lermos um arquivo de texto dentro da linguagem python. Para isso basta abrirmos um arquivo em uma variável e através desta chamarmos a função read:

```python
>>> arquivo = open("palavras.txt", "r")
>>> arquivo.read()
banana\nmelancia\nmorango\nmaça\n
```

 Conforme no artigo anterior, onde escrevemos as palavras acima em um arquivo txt, temos este resultado, que é a representação de cada palavra em linhas separadas.

Se quisermos ler novamente o texto o resultado é:

```python
>>> arquivo.read()

```

Sim nada. Isso se deve a posição do cursor, que depois de percorrer lendo todo o conteúdo do arquivo, fica aguardando novas instruções no final do arquivo. 

Tecnicamente precisaríamos fechar o arquivo dentro do python, reabri-lo e ler novamente. Porém, lembrando o read irá ler todo o conteúdo e aguardar novas instruções ao final. Se quisermos ler apenas 1 linha?

------



## .readline()

Está função built-in é usada para leitura de arquivos, com ela ao invés de lermos todo conteúdo de uma só vez, o python lê apenas a linha em que o cursor se encontra, por exemplo:

```python
>>> arquivo.readline()
banana\n
>>> arquivo.readline()
melancia\n
```

Está função irá ler o conteúdo de um arquivo até que ele encontre o `\n`, caso o retorno seja em branco a função atingiu o final do arquivo. Da mesma forma que o read, a readline executa lendo o conteúdo onde ela parar será o começo, caso a função seja executada novamente. 

------



## Iterando sobre o conteúdo de um arquivo

Podemos iterar o conteúdo de um arquivo de texto usando o laço for, por exemplo:

```python
>>> for linha in arquivo:
        print(linha)
banana

melancia

morango

maça

```

O resultado é cada palavra seguida do `\n` que aqui é lido como nova linha, pois a função print já traz imbutido o `\n` ao final de cada string.

Uma forma de contornar isso pode ser parametrizando o `end=` vazio:

```python
>>> for linha in arquivo:
        print(linha, end='')
banana
melancia
morango
maça
```

Da mesma forma que as outras funções, o laço for irá percorrer todo o conteúdo do arquivo e o cursor ficará aguardando ao final do arquivo, sendo assim não conseguiremos imprimir novamente o conteúdo, seja usando o laço seja usando uma das funções de leitura.

------



## Atribuição a variáveis

Além destas funcionalidades podemos também atribuir uma palavra, uma frase ou até mesmo um parágrafo inteiro a uma variável:

```python
>>> palavra1 = arquivo.readline()
>>> print(palavra1)
'banana\n'
```

Também podemos iterar em uma lista o conteúdo do arquivo:

```python
>>> lista = []
>>> for linha in arquivo:
        lista.append(linha)
>>> print(lista)
['banana\n', 'melancia\n', 'morango\n', 'maça\n']
```

Pode ser executado também utilizando a função `.readlines()`:

```python
>>> lista = arquivo.readlines()
>>> print(lista)
['banana\n', 'melancia\n', 'morango\n', 'maça\n']
```

------



## .strip()

Como visto apenas quando utilizamos a iteração sobre o conteúdo do arquivo com a função print parametrizada para ao final de cada string não conter o \n que conseguimos eliminar ele do conteúdo final de cada string, seja sozinho como resultado, seja atribuindo a uma variável ou até mesmo em uma lista.

Nós podemos utilizar a função `.strip()` para isso:

```python
>>> lista = []
>>> for linha in arquivo:
        lista.append(linha.strip())
>>> print(lista)
['banana', 'melancia', 'morango', 'maça']
```

Também funciona com:

```python
>>> palavra1 = arquivo.readline()
>>> print(palavra1.strip())
'banana'
```







