# Estrutura de Dados

Imagine que você tenha uma quantidade demasiada de dados para trabalhar e deseja usar python para isso. a principio você estaria tentado a atribuir cada dado em uma variável diferente, mas a linguagem python possui uma algumas funcionalidades que nos ajudam a organizar e trabalhar com quantidades de dados grandes.

Elas são chamadas de estruturas de dados. A biblioteca padrão do python entrega nativamente (sem a necessidade de importar) alguns tipos de estruturas.

Cada estrutura possui sua característica o que facilita muitos trabalhos e também caracteriza melhor onde e quando, determinada estrutura de dados será melhor aplicada.

> Imagine uma lista de compras de supermercado, ou uma lista de nomes e CPF, imagine um histórico de valores de uma determinada ação de uma empresa desde o momento em que ela entrou na bolsa, ou um estoque.

Por diversas vezes vamos nos deparar com algum tipo de estrutura de dados na vida real portanto não seria vantajoso usarmos uma linguagem de programação que fosse não fosse intuitiva a ponto de oferecer algumas estruturas para que possamos trabalhar com dados da vida real.

---

# Números, strings etc...

Antes de começarmos a nos aprofundarmos mais em estruturas de dados, precisamos entende alguns conceitos da linguagem para compreender o que caracteriza um dado. Portanto primeiramente vamos olhar para o dado em si no singular.

As variáveis que criamos geralmente recebem um dado:

```python
>>> nome = 'Python'
>>> idade = 30
>>> status_ativo = True
>>> nota = 9.5

```

Acima criamos diversas variáveis onde cada uma recebeu um dado, cada dado destes é um tipo, nós podemos checar qual o tipo de dado se encontra em cada variável utilizando a função `type(*nome_variável*)`

```python
>>> print(type(nome))
<class 'str'>
>>> print(type(idade))
<class 'int'>
>>> print(type(status_ativo))
<class 'bool'>
>>> print(type(nota))
<class 'float'>
```

Mas o que significa cada um desse tipo (class)?

---

## String ('str')

Podemos dizer que strings são os dados do tipo texto. Uma string é sempre definida pelas aspas simples ( ' ' ) ou aspas duplas ( " " ), todo o conteúdo entre as aspas é uma string.

Ela não necessariamente precisa ser apenas caracteres alfabéticos, podendo também receber números, ou caracteres especiais como por exemplo %, $, &, +, etc. desde que estejam entre aspas.

```python
	>>> texto = "Desmatamento na Amazônia é o maior dos últimos dez anos. Crescimento foi de 30% em 2020 em comparação com 2019; 8 mil quilômetros de floresta foram destruídos entre janeiro e dezembro do ano passado. É como se a cidade de São Paulo desaparecesse, cinco vezes."
>>> numero = '42'
>>> numero_decimal = '3.14'
>>> verdadeiro = "True"
```

Todos os exemplos acima são 'strings'.

Observe também que em nenhum momento, ao definir valor a uma variável, foi necessário informar a linguagem que o conteúdo seria do tipo string como se pede em algumas linguagens de programação.

Em python as definições a variáveis são dinâmicas a partir do momento que um valor é atribuído a uma variável, ela reconhece o tipo de dado e assume este tipo.

---

## Inteiro ('int')

Inteiro são os números do conjunto inteiro, ou seja os números fracionados não entram neste tipo.

Diferentemente das strings, os números são definidos por si só, não necessitando de aspas ou qualquer outro caractere especial:

```python
>>> numero = 42
>>> numero2 = 30
>>> numero3 = -15
>>> numero4 = 8000
```

Uma das características da linguagem python é a possibilidade de atribuir valores e tipos diferentes para uma mesma variável no momento que for interessante, observe:
![[01_definindo_valor_variavel.jpg]]

1.  Definimos o valor da variável numero uma `string` '42';
2.  Imprimimos o tipo da variável numero;
3.  Resultado, como esperado é uma `string`;
4.  Definimos agora a variável numero um `inteiro` 42;
5.  Imprimimos o tipo da variável numero;
6.  Resultado, como esperado é uma `int`.

