# O que é um Módulo?
Em python, basicamente módulo é um arquivo contendo um código python.
Existem inumeros módulos (bibliotecas) que possuem funções e funcionalidades que podem ser úteis nos projetos de diversas áreas, como por exemplo machine learning, data science, etc.

Um exemplo de módulo é o random, que possuem diversas funcionalidades.

Muitos destes módulos precisam ser importados para ser utilizado.

---

# random
Antes de utilizarmos as funções presentes no módulo random, precisamos importar para nosso projeto utilizando a função `import`.
Muitos módulos já vêem pré instalados no momento que você instala o python na sua máquina, random é um deles. Mas temos inumeros módulos disponíveis no site: [PyPi](https://pypi.org/)

![[11_import.jpg]]

Dessa forma importamos todas as funções existentes no módulo random. 

---

# random.random()
Agora podemos utilizar as funcionalidades, como a função que leva o nome de random(), está função retorna um valor aleatório entre 0,0 e 1,0. 

```py
print(random.random())
0.9681743450967373
```

---

# random.randrange(x,y, passo)
Retorna um valor aleatório entre um valor de série onde o número limite é excludente, isso significa que ele não é considerado. Exemplo:

```py
print(random.randrange(1,101))
42
```

Também é possível estabelecer regras para os número aleatórios como por exemplo apenas multiplos de 5 entre 0 e 100:

```py
print(random.randrange(0,101,5))
45
```


---

# random.randint(x, y)
Randint funciona básicamente da mesma forma que o randrange().

```py
print(random.randint(0,101))
24
```

---

# From x import y

É possível também importarmos apenas uma função especifica do módulo, usando `from`:

```py
from random import randint
```

Nesses casos somente a função randint fica disponível para utilização, qualquer tentativa de utilização de outra função do módulo random ocasionará erro no código:

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'random' is not defined
```

Importante também salientar que a chamada da função também muda, no caso de importação de funções específicas ela fica assim:

```py
print(randint(0,101))
```

Caso você utilize o random.randint() causará *NameError 'randon' is not defined*

---
