import logging
from abc import ABC, abstractmethod

from package.services.db.db import ConnCiegDev


class AbstractScript(ABC):
    """Classe abstrata para scripts de linha de comando."""

    @abstractmethod
    def help(self):
        """Retorna a descrição do script."""
        pass

    @abstractmethod
    def run(self, *args, **kwargs):
        """Executa o script."""
        pass


class BaseScript(AbstractScript):
    """
    Classe base para scripts de linha de comando.

    Args:
        engine (sqlalchemy.engine.base.Connection): Conexão com o banco de dados.
    """

    def __init__(self, engine=None, *args, **kwargs):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.engine = ConnCiegDev().get_engine() if engine is None else engine

    def help(self):
        """Retorna a descrição do script."""
        raise NotImplementedError

    def run(self, *args, **kwargs):
        """Executa o script."""
        raise NotImplementedError

    def __exit__(self, exc_type, exc_value, traceback):
        """Executa ao finalizar"""
        if self.engine:
            self.engine.dispose()
