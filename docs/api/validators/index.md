# Estrutura da Pasta "validators"

Pasta que contém os arquivos Python que implementam as validações dos dados.

## Arquivo [base.py](base.md)

Arquivo que contém a classe abstrata `AbstractValidator` e a classe base `BaseValidator` que é utilizada para criar os validadores que serão executados pelas aplicações.

Todos os validadores devem herdar da classe `BaseValidator` e implementar os métodos abstratos `help` e `validate`.

Exemplo de validador:

```python
from pymrf.validators.base import BaseValidator

class TelValidator(BaseValidator):

    def help(self):
        return "Valida o campo telefone."
    
    def validate(self, value):
        if value is None:
            return False
        if len(value) < 10:
            return False
        return True
```