# Estrutura da Pasta "core"

A pasta core é uma das principais pastas do projeto. Ela contém os módulos que implementam a lógica central do projeto e definição dos comandos que executam os ecripts.

Dentro da pasta core, encontramos as seguintes subpastas:

## Subpasta `management`: 

Contém o arquivo `base.py` contendo as classes abstratas para criar os comandos e a subpasta `command` com a implementação de comando a serem usados pela aplicação CLI.

## Subpasta `management/command`: 

Contém a implementação dos commandos a serem usados pelo CLI.

Exemplos:

* start_project: comando que executa a criação da estrutura base do projeto.
* run: Comando que executa o script principal do projeto.