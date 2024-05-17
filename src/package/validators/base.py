from abc import ABC, abstractmethod


class AbstractValidator(ABC):
    """Classe abstrata base para validadores que podem ser executados no contexto do projeto."""

    @abstractmethod
    def help(self) -> str:
        """Retorna uma descrição do validador."""
        pass

    @abstractmethod
    def validate(self, *args, **kwargs) -> bool:
        """Executa o validador com os argumentos e argumentos de palavra-chave fornecidos."""
        pass


class BaseValidator(AbstractValidator):
    """
    Classe base para validadores que podem ser executados no contexto do projeto.

    Args:
        lazy: Se True, o validador não será executado no momento da inicialização.
    """

    def __init__(self, lazy: bool = False) -> None:
        super().__init__()
        self._lazy = lazy
        if not self._lazy:
            self.validate()

    @abstractmethod
    def help(self) -> str:
        """Retorna uma descrição do validador."""
        raise NotImplementedError

    def validate(self, *args, **kwargs) -> bool:
        """Executa o validador com os argumentos e argumentos de palavra-chave fornecidos."""
        raise NotImplementedError
