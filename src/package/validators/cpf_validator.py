from typing import List

from package.validators.base import BaseValidator


class CpfValidator(BaseValidator):
    """
    Validador de CPF.
    """

    def __init__(self) -> None:
        """
        Inicializa a classe.

        Args:
            lazy: Se True, a validação será feita apenas quando o método validate for chamado.
        """
        super().__init__(lazy=True)
        self._seq_mult_first_digit = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        self._seq_mult_second_digit = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    def help(self) -> str:
        """Retorna uma descrição do validador."""
        return "Valida um CPF."

    def _get_blacklist(self) -> List:
        """
        Retorna uma lista de CPFs inválidos.
        ["00000000000", ..., "99999999999"]
        """
        return [str(digit) * 11 for digit in range(10)]

    def sanitize_cpf(self, cpf: str) -> str:
        """
        Remove caracteres não numéricos do CPF,
        preenche com zeros à esquerda e retorna o CPF.
        """
        cpf = "".join(filter(str.isdigit, str(cpf)))
        return cpf.zfill(11)

    def _calculate_first_digit(self, digits: int) -> int:
        """Calcula o primeiro dígito verificador do CPF."""
        total = sum([digit * weight for digit, weight in zip(digits, self._seq_mult_first_digit)])
        digit = total % 11
        return 0 if digit < 2 else 11 - digit

    def _calculate_second_digit(self, digits: int) -> int:
        """Calcula o segundo dígito verificador do CPF."""
        total = sum([digit * weight for digit, weight in zip(digits, self._seq_mult_second_digit)])
        digit = total % 11
        return 0 if digit < 2 else 11 - digit

    def validate(self, cpf) -> bool:
        """Executa o validador com os argumentos e argumentos de palavra-chave fornecidos."""
        if len(cpf) < 10:
            return False

        cpf = self.sanitize_cpf(cpf)
        if cpf in self._get_blacklist():
            return False

        digits = [int(digit) for digit in cpf]
        first_digit = self._calculate_first_digit(digits)
        second_digit = self._calculate_second_digit(digits)
        return digits[9] == first_digit and digits[10] == second_digit


class CpfListValidator(BaseValidator):
    """
    Validador de lista de CPFs.

    Args:
        cpf_list (list): Lista de CPFs.
        sanitize (bool): Remove caracteres não numéricos dos CPFs da lista.
    """

    def __init__(self, cpf_list: List[str | int], sanitize: bool = True, *args, **kwargs) -> None:
        """
        Inicializa a classe.

        Args:
            cpf_list: Lista de CPFs.
            sanitize: Remove caracteres não numéricos dos CPFs da lista.
        """
        self.cpf_list = set(cpf_list)
        self._invalid_cpfs = []
        self._valid_cpfs = []
        self._cpf_validator = CpfValidator()
        self._sanitize = sanitize
        if self._sanitize:
            self._sanitize_cpf_list()
        super().__init__(*args, **kwargs)

    def help(self) -> str:
        """Retorna uma descrição do validador."""
        return "Valida uma lista de CPFs."

    def _sanitize_cpf_list(self) -> None:
        """Remove caracteres não numéricos dos CPFs da lista."""
        self.cpf_list = [self._cpf_validator.sanitize_cpf(cpf) for cpf in self.cpf_list]

    def validate(self) -> bool:
        """Executa o validador com os argumentos e argumentos de palavra-chave fornecidos."""
        if len(self.cpf_list) == 0:
            return False
        for cpf in self.cpf_list:
            if self._cpf_validator.validate(cpf):
                self._valid_cpfs.append(cpf)
            else:
                self._invalid_cpfs.append(cpf)
        return len(self._invalid_cpfs) == 0

    def get_valid_cpfs(self) -> list:
        """Retorna uma lista de CPFs válidos."""
        return self._valid_cpfs

    def get_invalid_cpfs(self) -> list:
        """Retorna uma lista de CPFs inválidos."""
        return self._invalid_cpfs

    def __str__(self) -> str:
        """Retorna uma representação de string do objeto."""
        return f"""Lista de CPFs válidos: {self._valid_cpfs}\nLista de CPFs inválidos: {self._invalid_cpfs}"""

    def __repr__(self) -> str:
        """Retorna uma representação de string do objeto."""
        return f"""Lista de CPFs válidos: {self._valid_cpfs}\nLista de CPFs inválidos: {self._invalid_cpfs}"""
