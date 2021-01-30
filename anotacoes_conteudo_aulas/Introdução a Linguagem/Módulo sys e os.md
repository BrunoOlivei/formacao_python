Introdução:
===========

Estes módulos são bastante úteis para obter informações precisas sobre o ambiente de desenvolvimento, desde o sistema operacional na qual estamos trabalhando, a versão do python que está sendo utilizada até o diretório na qual o projeto está inserido.

---

Módulo sys:
===========

Para utilizar o módulo sys, primeiro é necessário importar da biblioteca padrão do python, basta utilizar os comandos `import sys.`

Este módulo possui algumas funções uteis, como por exemplo `.platform` que retorna o sistema operacional subjacente.

![[25_sys_platform.jpg]]

No meu caso sistema operacional subjacente é o win32

---

Nós também podemos consultar a versão do python que está sendo executada com o comando `sys.version`, assim como o comando `python --version` no prompt do windows:

![[26_sys_version.jpg]]

---

Módulo os:
===========

Os módulos os são bastante úteis também para basicamente trabalhar com diretórios, porém ele possui funcionalidades muito mais avançadas.

## .getcwd()

Utilizando a função `getcwd()` do módulo os nós recebemos como resultado o diretório onde está sendo executado o programa em questão.
Quando executamos este comando direto no console python o resultado será o caminho para a pasta onde a linguagem e o console estão instalados:

![[27_so.getcwd.jpg]]

---

## .chdir(*'endereço'*)

Esta função move nosso ambiente de trabalho para outro diretório, exige um argumento que é uma string e essa é o endereço no qual desejamos acessar:

![[28_os_chdir.jpg]]

Se novamente executarmos a função `os.getcwd()` iremos receber agora como resultado o endereço que passamos na função `os.chdir()`

![[29_os_getcwd.jpg]]

---

## .listdir()

O `os.listdir()` retorna uma lista contendo os nomes dos arquivos na qual estamos inseridos. 
Esta função pode receber também como argumento algum outro endereço na forma de uma string.

![[30_os_listdir.jpg]]

---

## .mkdir('*nome*')

A função `os.mkdir()` é o mesmo que a que utilizamos nos terminais e consoles windows, mac os ou linux. Ela cria uma nova pasta com o nome que for usado dentro dos parenteses como argumento em formato de string, ou seja entre aspas simples ou duplas. 

![[31_os_mkdir.jpg]]

Agora se utilizarmos novamente a função `os.listdir()` para listar as pastas e documentos dentro do nosso diretório poderemos ver que a pasta **teste** que criamos também está lá.

![[32_os_listdir.jpg]]
