## Arquivo `settings.py`

O arquivo `settings.py` é um componente fundamental para a configuração do projeto. Ele define diversas variáveis e constantes que especificam caminhos de diretórios, nomes de arquivos e outras configurações relevantes.

```python
from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

DOTENV_PATH = Path(".env")
STATIC = Path("./static")

HOST = config("HOST", default=None)
DB = config("DB")
TYPE_ENV = config("TYPE_ENV", default=None)
```