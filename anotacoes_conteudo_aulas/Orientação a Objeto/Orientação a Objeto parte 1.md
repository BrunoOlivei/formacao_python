Introdução:
===========

O python utiliza o método `class` para definir um objeto na linguagem.

Dentro dele é usual definir uma função nomeada com uma função _dunder_ no caso `__init__` para atribuir as características do objeto ou seja os **atributos:**

```python
class Conta:
    
    def __init__(self):
				print("Criando Objeto...")

```

Nos códigos escritos sob o paradigma da orientação a objeto, é muito comum encontrar uma variável recebendo como valor o nome de uma determinada class (objeto). Quando isso ocorre os programadores dizem que a variável é a **referencia** do objeto.

```python
conta = Conta()
```

Isso por que o objeto Conta tem um endereço na memória do computador, mas cada vez que a classe é chamada ele cria um novo endereço. Então para que não percamos a referência desse endereço de memória toda vez que precisemos utilizar aquele objeto ele é atribuído a uma variável que no caso se torna uma **referencia** .

---

(Self)
------

O que o self representa dentro da função `__init__`?

Se observarmos o próprio **init** é uma função que recebe também um atributo dentro dos seus parênteses.

No caso aqui vamos pedir para imprimir o self no console e verificar o que se trata:

```python
class Conta:
    
    def __init__(self):
				print("Criando Objeto... {}".format(self))

>>> conta = Conta()
Construindo Objeto... <conta.Conta object at 0x00000173C013FF70>
>>> conta
<conta.Conta object at 0x00000173C013FF70>
```

`self` é a referência que sabe encontrar o objeto construído em memória.

---

Criando um Construtor:
======================

Definida a classe e a função que inicializa automaticamente a criação da classe, chegada a hora de criar os atributos que serão as características deste objeto e receberão os valores. Podemos fazer uma analogia a um carro, que possui suas características como potência do motor, tipo de combustível utilizado, autonomia, torque etc.

```python
class Conta:

		def __init__(self, numero, titular, saldo, limite):
          print("Criando Objeto... {}".format(self))
					self.numero = numero
					self.titular = titular
					self.saldo = saldo
					self.limite = limite
```

No `self.numero` o ponto (.) é um comando de "ida" ao objeto e `numero`, `titular`, `saldo` e `limite` são os atributos.

O que queremos dizer aqui é que a função `__init__()` acesse, crie ou altere os valores dos atributos.

Ao atribuirmos para cada objeto `self.` um "valor" precisamos atribuir como parâmetro na função `__init()__` para que o objeto seja acessado e alterado.

Agora é só testar:

```python
>>> from conta import Conta

>>> conta = Conta(123, "Bruno", 100.0, 1000.0)
Construindo objeto ... <conta.Conta object at 0x11077bcc0>

>>> conta2 = Conta(321, "Marco", 55.0, 1000.0)
Construindo objeto ... <conta.Conta object at 0x1109e1da0>
```

---

Acessando atributos
===================

Com os objetos e seus atributos criados, será que é possível acessá-los tanto para consultas como para tarefas mais complexas como usar em uma outra função que execute determinado operação?

Utilizando a linhagem UML que serve para descrever de forma visual através de gráficos e desenhos um sistema por exemplo, temos o seguinte:

![[2.7_2_diagramas+de+classe+com+atributos.png]]

Estrutura:
----------

1.  **[conta.py](http://conta.py)**: é o módulo, em algumas linguagens pode ser reconhecido como `package` ou `namespace` dentro dele poderíamos ter mais de uma sintaxe.
    
2.  **Conta:** É a classe criada. ela está contida dentro do módulo [conta.py](http://conta.py)
    
    Por isso quando vamos executar no console python, precisamos fazer o import deste módulo e da classe conta, através do `from conta import Conta`
    
3.  **numero, titular, saldo e limite:** são os atributos da classe Conta
    

E cadê o **init()**?
--------------------

Ele não é exibido no diagrama de classes, porque se trata de uma função implícita, que é chamada automaticamente.

Quando chamamos a classe Conta(), por baixo dos panos o Python passará os valores para a função `__init()__`. Quando executamos a linha com a referência **conta,** em memória, o python irá gerar o objeto em que são guardados os valores:

![[2.7_3_+classe+Conta+adicionada.png]]

A partir daqui python criou um objeto conta com os atributos como numero, titular, saldo e limite definidos, a partir do momento que passamos estes valores dentro dos parênteses, em uma referencia com nome conta.

---

Acessando valores
=================

Com objeto criado, podemos acessar os seus valores utilizando os atributos:

A primeira conta criada tem como referencia a palavra 'conta':

```python
>>> conta = Conta(123, "Bruno", 55.0, 1000.0)
>>> conta2 = Conta(321, "Marco", 100.0, 1000.0)
```

Para acessar utilizamos a referencia seguida de ponto e o nome do atributo:

```python
>>> conta.titular
'Bruno'
>>> conta.saldo
55.0
>>> conta2.titular
'Marco'
>>> conta2.numero
321
```

---

Métodos
=======

Métodos basicamente são as funcionalidades que um objeto tem ou pode fazer. Podemos pensar em um carro, que só pode andar para frente ou para trás ou ficar parado.

Para definir uma funcionalidade (método):

```python
class Conta:

		def __init__(self, numero, titular, saldo, limite):
          print("Criando Objeto... {}".format(self))
					self.numero = numero
					self.titular = titular
					self.saldo = saldo
					self.limite = limite
		
		def extrato(self):
					print('Saldo {} do títuluar {}'.format(self.saldo, self.titular))

```

Dessa vez definimos um nome a função que será o método 'extrato', esse que irá imprimir na tela o valor de saldo do cliente.

`def extrato(self):`

Como parâmetro o self novamente é informado, isso se deve pois ele precisa acessar a referência da classe em que está inserida e todos os atributos que a classe possui.

Como retorno vamos imprimir uma string que receberá os saldo e o nome do titular, através da formatação do string.

`print('Saldo {} do títuluar {}'.format(self.saldo, self.titular))`

Mais uma vez o self aparece pelo mesmo motivo de buscar a própria referência.

Executando:
-----------

Executando o método extrato:

Novamente dentro do console, importamos a classe e criamos as contas de exemplo:

```python
>>> from conta import Conta

>>> conta = Conta(123, "Bruno", 55.0, 1000.0)
Construindo objeto... <conta.Conta object at 0x000001AE182B7280>

```

Agora para chamarmos o método extrato:

```python
>>> extrato()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'extrato' is not defined
```

Recebemos um erro dizendo que extrato não foi definido. Mas nós escrevemos corretamente, a criação da conta de exemplo ocorreu tudo bem o que falta?

> FALTA A REFERÊNCIA

Sim imagine se tivéssemos 10, 50, 100, Um milhão de contas criadas, ao executar o comando `extrato()` estamos solicitando o extrato de quem?

É ai que entra novamente a referência conforme vimos anteriormente quando queríamos acessar o nome do titular por exemplo. Então a sintaxe para execução do método "extrato" fica da seguinte maneira:

```python
>>> conta.extrato()
Saldo 55.0 do titular Nico.
```

Agora sim executada de forma correta.

---

Mais métodos:
-------------

Agora podemos criar alguns métodos que podem ser úteis para uma conta bancária, como por exemplo depósito e saque de valores.

```python
class Conta:

		def __init__(self, numero, titular, saldo, limite):
          print("Criando Objeto... {}".format(self))
					self.numero = numero
					self.titular = titular
					self.saldo = saldo
					self.limite = limite
		
		def extrato(self):
					print('Saldo {} do títuluar {}'.format(self.saldo, self.titular))

		def deposita(self, valor):
					self.saldo += valor

		def saca(self, valor):
					self.saldo -= valor
```

No caso destes 2 novos métodos, precisamos receber um valor como argumento para que possamos realizar as operações pertinentes para alterar o saldo.

No caso de depósitos o valor recebido como argumento será adicionado ao saldo, enquanto o método saca o valor irá subtrair do saldo. Para isso é necessário parametrizar em cada método, além do self, um valor que será utilizado para as operações.

```python
>>> from conta import Conta

>>> conta = Conta(123, "Nico", 55.5, 1000)
Construindo objeto... <conta.Conta object at 0x000002393068FF70>

>>> conta.extrato()
Saldo 55.5 do titular Nico.

>>> conta.deposita(15.0)
>>> conta.extrato()
Saldo 70.5 do titular Nico.

>>> conta.saca(10)
>>> conta.extrato()
Saldo 60.5 do titular Nico.

```

---

None e Coletor de Lixo
======================

Imagine a seguinte situação:

Suponhamos que dentro do nosso programa onde temos uma conta criada com a referência _'conta1'_ com todos os seus atributos como número da conta, tiular da conta, valor do saldo e o valor do limite.

Agora imagine que por algum motivo hipotético nós executamos a classe para uma referencia de mesmo nome _conta1_, com os mesmos valores para os atributos, algo como:

```python
>>> conta1 = Conta(123, "Nico", 55.0, 1000.0)
>>> conta1 = Conta(123, "Nico", 55.0, 1000.0)
```

Nós literalmente criamos 2 objetos com a mesma referencia. É isso mesmo que acontece, foram criados 2 objetos utilizando a mesma referencia. Só que esta referência não irá apontar para os 2 objetos ao mesmo tempo, um deles ficará perdido na memória ocupando espaço, sem uma referencia para que possamos acessá-la.

Ou seja:

O que temos é uma referencia com nome conta atribuída a um objeto na memória enquanto outro não possui nenhuma referencia.

Porém a linguagem python e muitas outras possui uma funcionalidade que automaticamente procura os objetos na memória que não possuem referencia, isso é chamado de _garbage collector_ (coletor de lixo)

![[coletor_lixo.png]]

Outra possibilidade seria querermos _"desatribuir"_ uma referencia a um objeto na memória, podemos fazer isso utilizando o `None`:

```python
>>> conta = None
```

Simples assim.

---