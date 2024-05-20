# Estrutura da Pasta "scripts"

A pasta `scripts` contém o arquivo [base.py](base.md) que contém a classe abstrata `BaseScript` que é utilizada para criar os scripts que serão executados pelas aplicações.

Todos os scripts devem herdar da classe `BaseScript` e implementar os métodos abstratos `help` e `run`.	

Exemplo de script:

```python
class HelloWorld(BaseScript):
    """
    Script para execução das tipologias de matriz de pessoa jurídica.
    """

    def help(self):
        return "Hello World"

    def run(self):
        print("Hello World")
```