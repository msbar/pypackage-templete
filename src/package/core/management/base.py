import logging
from abc import ABC, abstractmethod


class AbstractCommand(ABC):
    """Classe abstrata para comandos de linha de comando."""

    @abstractmethod
    def help(self):
        """Retorna a descrição do comando."""
        pass

    @abstractmethod
    def handle(self, *args, **options):
        """Executa o comando."""
        pass


class BaseCommand(AbstractCommand):
    """Classe abstrata para comandos de linha de comando."""

    def __init__(self, *args, **kwargs):
        """Inicializa a classe."""
        self._logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def help(self):
        """Retorna a descrição do comando."""
        pass

    @abstractmethod
    def add_arguments(self, parser):
        """Adiciona argumentos ao comando."""
        pass

    @abstractmethod
    def handle(self, *args, **options):
        """Executa o comando."""
        pass
