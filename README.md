# Treinamento Python

## Introdução
- O objetivo deste projeto é criar um tamplete de projeto em Python para facilitar o desenvolvimento de novos projetos.

## Como usar:

1. Clone o repositório:
```bash
git clone https://git.tcmnet.tcm/cieg/projeto_padrao_python.git nome_do_projeto
``` 

2. Acesse a pasta do projeto:
```bash
cd nome_do_projeto
```

3. Crie um ambiente virtual:
```bash
python -m venv .venv
```

4. Ative o ambiente virtual:
```bash
.venv\Scripts\activate
```

5. Instale as dependências:
```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

6. abra o projeto no vscode:
```bash
code .
```
7. Renomeia pasta `package` para o nome do seu projeto, o vscode irá perguntar se deseja renomear todas as referências, clique em `yes`.

8. Altere todos os arquivos de documentação como o pyproject.toml, README.md, mkdocs.yml, e os arquivos de docs, que contenham o nome do projeto `package` para o nome do seu projeto.

9. Instale o pacote localmente.
```bash
pip install -e .
```

10. Execute o comando `startproject` para criar a estrutura do projeto.
```bash
seu_projeto startproject
```

11. Desenvolva seu projeto.