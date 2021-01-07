# O que faz:
Print imprime o valor desejado no console ou terminal:

![[9_print_ola_mundo.jpg]]

# Sintaxe
<pre><code>print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)</code></pre>

A sintaxe básica do print é a palavra-chave, seguida de parenteses de abertura, o valor (letras, palavras, números) e parenteses de fechamento.

```
print("Olá Mundo")
```

Na documentação da função print temos outros argumentos que podem ser utilizados:
- Value, ...: É o argumento, valor que se deseja imprimir, as reticencias indicam que pode se passar mais de um valor.
- sep=' ': Dentro da aspas simples, podemos passar um argumento que será utilizado para separar os valores (values) que passamos na função. Por padrão ele utiliza um espaço em branco.
- end='\n': Indica o que deve ser feito ou impresso ao final, por padrão o python coloca como argumento que a função finalize com uma nova linha que é o \n dentro das aspas.
- file=sys.stdout: Indica qual arquivo irá ser impresso o valor (value), passado. Por padrão é o próprio console python.
- flush=False: Flush força o resultado da função, em determinados casos extremos é interessante utilizar. Por padrão ele não faz essa força.

---

#python #python3 #primeirospassos #funçaoprint #iniciante 