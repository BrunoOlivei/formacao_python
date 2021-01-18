# Escrevendo em um arquivo e o lendo

O que queremos aprender aqui é como utilizar o python para criar um arquivo de texto, escrever um conteúdo para ele e que nosso código leia este conteúdo e utilize para o jogo forca.

Para isso utilizaremos algumas funções built-in disponibilizadas pela linguagem.

A primeira função que aprenderemos é a open(), ela devolve um objeto arquivo, e frequentemente é usada com dois argumentos `open(nome_do_arquivo, modo)`.

O primeiro argumento (nome_do_arquivo) é uma string contendo o nome do arquivo. O segundo argumento também é uma string, contendo alguns caracteres que descrevem como o arquivo será usado, por exemplo `"r"` que é quando o arquivo será apenas lido.

| Caractere | Função                                                       |
| --------- | ------------------------------------------------------------ |
| "r"       | Abre para leitura (padrão)                                   |
| "w"       | Abre para escrita, truncando o arquivo primeiro (removendo tudo o que estiver contido no mesmo) ou seja deleta tudo e escreve em cima. |
| "x"       | Abre para criação exclusiva, falhando caso o arquivo já exista |
| "a"       | Abre para escrita, anexando ao final do arquivo caso o mesmo já exista e tenha algum conteúdo. |
| "b"       | Abre o conteúdo do arquivo em binário, ideal para arquivos que não possuam texto |
| "t"       | Modo texto (padrão)                                          |
| "+"       | Abre para atualização (leitura e escrita)                    |

O sinal de '+' é sempre utilizado com alguma outra letra que corresponde a algum modo para abertura de arquivo, no caso do r ele combina a abertura para leitura e escrita

Utilizando o r, o comando write substituirá o que já estiver escrito no documento.

Utilizando o modo a+ para abertura de arquivo, podemos acessar o documento e adicionar conteúdo sem apagar o que já estava escrito.

Para que possamos utilizar o conteúdo do arquivo é uma boa prática abrimos o mesmo em uma variável:

<img src="C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\13_open.jpg" alt="13_open" style="zoom: 80%;" />

Agora podemos escrever no arquivo, para isto utilizamos a função built-in `.write()`:

Utilizando a variável que contem o arquivo, chamamos a função e passamos como argumento dentro dos parênteses uma string que será o nosso conteúdo:

<img src="C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\14_write_1.jpg" alt="14_write_1" style="zoom:80%;" />

Repare que o comando retornou o número 6 que é a quantidade de caracteres inseridos através da função.

Podemos escrever mais palavras seguidas vezes:

<img src="C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\15_write_2.jpg" alt="15_write_2" style="zoom:80%;" />

Após trabalhar com arquivos é uma boa prática fecha-lo, isso é importante pois o sistema operacional cria um caminho de comunicação, em alguns casos esse caminho pode bloquear outros acessos, impossibilitando por exemplo que você ou outro colaborador consiga acessar o arquivo de outra forma para editar ou apenas visualizar. Por isso a importância de encerrar esse caminho de comunicação, para isso utilizamos a função `close()`

<img src="C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\16_close.jpg" alt="16_close" style="zoom:80%;" />

---



# Lendo o arquivo:

Agora como acessar esse arquivo dentro da IDLE do python? No comando prompt já sabemos, mas será que conseguimos acessar este arquivo diretamente do prompt? Vamos ver:

Utilizando o comando `dir` direto no prompt: 

![17_dir](C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\17_dir.jpg)

Não vemos nenhum arquivo com nome "palavras.txt", como poderemos encontra-lo?

É ai que entra o módulo OS no python, vamos importá-lo e usar o comando `os.getcwd()` para saber onde estamos trabalhando:

<img src="C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\18_os.getcwd.jpg" alt="18_os.getcwd"  />

A função `os.getcwd()` retorna o diretório onde estamos trabalhando, portanto se acessarmos ele através do prompt do windows, poderemos ver o arquivo criado, dentro do prompt utilizando o comando `cd` acesse o caminho informado no terminal python:

![19_cd](C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\19_cd.jpg)

Utilizando o comando `dir` para listar os arquivos contidos neste diretório:

![20_dir](C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\20_dir.jpg)

Agora podemos enxergar o arquivo e uma vez trabalhando na pasta, podemos inclusive lê-lo dentro do terminal do windows, para isso, basta acessar o python neste ambiente.

Inicializando o python no terminal, importando o módulo OS e comande o `os.getcwd()`:

![21.python](C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\21.python.jpg)

Veja que estamos no mesmo ambiente que a IDLE do python onde se encontra o arquivo "palavras.txt". Agora utilizando os mesmos comandos para abrir o arquivo vamos acessá-lo para conseguirmos le-lo:

![22_open_read](C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\22_open_read.jpg)

Repare o que nos retornou: **bananamelancia** não era bem isso que queríamos. Por que isso ocorreu?

A função write não distingue uma palavra da outra, além disso o cursor para escrita se encontrava logo após a letra "a" final da palavra banana, para que isso não ocorra, quando formos passar uma string dentro da função `.write()` devemos colocar um espaço ao final ou início da palavra ou se quisermos colocar uma palavra abaixo da outra, podemos utilizar dentro das aspas \n que caracteriza uma nova linha.

Lembrando do que aprendemos anteriormente dos 'modos' como podemos abrir os arquivos, podemos reabri-lo para escrevermos encima do que já foi escrito, agora da forma correta. Então para isso vamos acessá-lo novamente utilizando o comando `open()` agora passando o modo "w", escreva no terminal a linha abaixo e execute:

```python
>>> arquivo = open("palavras.txt", "w")
```

Agora vamos escrever no arquivo algumas frutas novas e ao final da string adicionar \n para que cada fruta seja escrita uma abaixo da outra:

```python
>>> arquivo.write("banana\n")
7
>>> arquivo.write("melancia\n")
9
>>> arquivo.write("morango\n")
8
>>> arquivo.write("maça\n")
5
```

Pronto agora que escrevemos todas as frutas, vamos acessar o arquivo novamente de forma que possamos visualizá-lo, para isso precisamos utilizar novamente o comando `open()` passando o modo "r" que é para leitura, como ele é padrão da linguagem podemos omitir, para leitura basta utilizar o comando `.read()`

```python
>>> arquivo = open("palavras.txt")
>>> arquivo.read()
```

O resultado:

![23_read](C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\23_read.jpg)

Será que está realmente formatado como queremos? Vamos acessar o arquivo diretamente através do explorador de arquivos do computador, antes disso vamos encerrar a comunicação do python com o arquivo utilizando o comando:

```python
>>> arquivo.close()
```

Buscando o arquivo dentro do nosso explorador de arquivos do windows temos:

<img src="C:\Users\bruol\OneDrive\Formação Python\formacao_python\anotacoes_conteudo_aulas\Introdução a Linguagem\Images\24_palavras_txt.jpg" alt="24_palavras_txt" style="zoom:80%;" />

Tudo certo com nosso arquivo. 

