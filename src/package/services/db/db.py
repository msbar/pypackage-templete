from decouple import config
from sqlalchemy import create_engine

from package.conf.settings import CRYPTON_TOKEN_PATH
from package.services.criptografia.crypton import Crypton


class ConnBuilder:
    """Classe para construir uma conexão com o banco de dados.
    A conexão pode ser feita com credenciais ou com autenticação do Windows.

    Args:
        db (str): Nome do banco de dados.
        host (str): Endereço do servidor.
        user (str, optional): Usuário do banco de dados. Defaults to None.
        password (str, optional): Senha do banco de dados. Defaults to None.
    """

    def __init__(self, db: str, host: str, user: str = None, password: str = None, crypt=True) -> None:
        """Inicializa a classe."""
        self.crypt = crypt
        if self.crypt and user and password:
            crypton = Crypton(Crypton.read_token_file(CRYPTON_TOKEN_PATH))
            self.user = crypton.decrypt_content(user)
            self.password = crypton.decrypt_content(password)
        else:
            self.user = user
            self.password = password

        self.db = db
        self.host = host

    def get_engine(self, pool_reset_on_return=None, echo: bool = False):
        """Retorna um objeto de conexão com o banco de dados."""
        if self.user and self.password:
            return create_engine(
                self.credentials_connection_string(),
                pool_reset_on_return=pool_reset_on_return,
                fast_executemany=True,
                echo=echo,
            )

        return create_engine(self.trusted_connection_string())

    def credentials_connection_string(self):
        """Retorna uma string de conexão com o banco de dados."""
        return f"mssql+pyodbc://{self.user}:{self.password}@{self.host}/{self.db}?driver=ODBC+Driver+17+for+SQL+Server"

    def trusted_connection_string(self):
        """Retorna uma string de conexão com o banco de dados."""
        return f"mssql+pyodbc://{self.host}/{self.db}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"


class ConnBigDataCieg:
    """Classe para conexão com o banco de dados BIG_DATA_CIEG."""

    def __init__(self, crypt=True) -> None:
        """Inicializa a classe."""
        self.crypt = crypt
        self.host = config("DB_HOST_BIG_DATA_CIEG")
        self.db = config("DB_NAME_BIG_DATA_CIEG")
        self.user = config("DB_USER_BIG_DATA_CIEG", default=None)
        self.password = config("DB_PASSWORD_BIG_DATA_CIEG", default=None)
        self.engine = None

    def get_engine(self):
        """Retorna um objeto de conexão com o banco de dados."""
        if self.engine:
            return self.engine

        cb = ConnBuilder(self.db, self.host, self.user, self.password, crypt=self.crypt)
        self.engine = cb.get_engine()
        return self.engine


class ConnCiegDev:
    """Classe para conexão com o banco de dados CIEG_DEV."""

    def __init__(self, crypt=True) -> None:
        """Inicializa a classe."""
        self.crypt = crypt
        self.host = config("DB_HOST_CIEG_DEV")
        self.db = config("DB_NAME_CIEG_DEV")
        self.user = config("DB_USER_CIEG_DEV", default=None)
        self.password = config("DB_PASSWORD_CIEG_DEV", default=None)
        self.engine = None

    def get_engine(self):
        """Retorna um objeto de conexão com o banco de dados."""
        if self.engine:
            return self.engine

        cb = ConnBuilder(self.db, self.host, self.user, self.password)
        self.engine = cb.get_engine()
        return self.engine


class ConnTrilhasAuditoria:
    """Classe para conexão com o banco de dados TRILHAS_AUDITORIA."""

    def __init__(self, crypt=True) -> None:
        """Inicializa a classe."""
        self.crypt = crypt
        self.host = config("DB_HOST_TRILHAS_AUDITORIA")
        self.db = config("DB_NAME_TRILHAS_AUDITORIA")
        self.user = config("DB_USER_TRILHAS_AUDITORIA", default=None)
        self.password = config("DB_PASSWORD_TRILHAS_AUDITORIA", default=None)
        self.engine = None

    def get_engine(self):
        """Retorna um objeto de conexão com o banco de dados."""
        if self.engine:
            return self.engine

        cb = ConnBuilder(self.db, self.host, self.user, self.password)
        self.engine = cb.get_engine()
        return self.engine


class SqliteConn:
    """Classe para conexão com o banco de dados."""

    def __init__(self, db: str = "db.sqlite") -> None:
        """Inicializa a classe."""
        self.db = db
        self.engine = None

    def get_engine(self, echo: bool = False):
        """Retorna um objeto de conexão com o banco de dados."""
        if self.engine:
            return self.engine

        self.engine = create_engine(f"sqlite:///{self.db}", echo=echo)
        return self.engine


class SqliteMemoryTestConn:
    """Classe para conexão com o banco de dados."""

    def __init__(self) -> None:
        """Inicializa a classe."""
        self.engine = None

    def get_engine(self, echo: bool = False):
        """Retorna um objeto de conexão com o banco de dados."""
        if self.engine:
            return self.engine

        self.engine = create_engine("sqlite:///:memory:", echo=echo)
        return self.engine
