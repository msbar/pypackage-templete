from typing import List

from package.validators.base import BaseValidator


class CnpjValidator(BaseValidator):
    """
    Validador de CNPJ.
    """

    def __init__(self) -> None:
        """Inicializa a classe."""
        super().__init__(lazy=True)
        self._seq_mult_first_digit = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        self._seq_mult_second_digit = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    def help(self) -> str:
        """Retorna uma descrição do validador."""
        return "Valida um CNPJ."

    def _get_blacklist(self) -> List:
        """
        Retorna uma lista de CNPJs inválidos.
        ["00000000000000", ..., "11111111111111"]
        """
        return [str(digit) * 14 for digit in range(10)]

    def sanitize_cnpj(self, cnpj: str) -> str:
        """
        Remove caracteres não numéricos do CNPJ,
        preenche com zeros à esquerda e retorna o CNPJ.
        """
        cnpj = "".join(filter(str.isdigit, str(cnpj)))
        return cnpj.zfill(14)

    def _calculate_first_digit(self, digits: int) -> int:
        """Calcula o primeiro dígito verificador do CNPJ."""
        total = sum([digit * weight for digit, weight in zip(digits, self._seq_mult_first_digit)])
        digit = total % 11
        return 0 if digit < 2 else 11 - digit

    def _calculate_second_digit(self, digits: int) -> int:
        """Calcula o segundo dígito verificador do CNPJ."""
        total = sum([digit * weight for digit, weight in zip(digits, self._seq_mult_second_digit)])
        digit = total % 11
        return 0 if digit < 2 else 11 - digit

    def validate(self, cnpj) -> bool:
        """Executa o validador com os argumentos e argumentos de palavra-chave fornecidos."""
        if len(cnpj) < 13:
            return False
        cnpj = self.sanitize_cnpj(cnpj)
        if cnpj in self._get_blacklist():
            return False

        digits = [int(digit) for digit in cnpj]
        first_digit = self._calculate_first_digit(digits)
        second_digit = self._calculate_second_digit(digits)
        return digits[12] == first_digit and digits[13] == second_digit


class CnpjListValidator(BaseValidator):
    """
    Validador de lista de CNPJs.

    Args:
        cnpj_list (list): Lista de CNPJs a ser validada.
        sanitize (bool, optional): Remove caracteres não numéricos dos CNPJs da lista. Defaults to True.
    """

    def __init__(self, cnpj_list: List[str | int], sanitize: bool = True, *args, **kwargs) -> None:
        """Inicializa a classe."""
        self.cnpj_list = set(cnpj_list)
        self._invalid_cnpjs = []
        self._valid_cnpjs = []
        self._cnpj_validator = CnpjValidator()
        self._sanitize = sanitize
        if self._sanitize:
            self._sanitize_cnpj_list()
        super().__init__(*args, **kwargs)

    def help(self) -> str:
        """Retorna uma descrição do validador."""
        return "Valida uma lista de CNPJs."

    def _sanitize_cnpj_list(self) -> None:
        """Remove caracteres não numéricos dos CNPJs da lista."""
        self.cnpj_list = [self._cnpj_validator.sanitize_cnpj(cnpj) for cnpj in self.cnpj_list]

    def validate(self) -> bool:
        """Executa o validador com os argumentos e argumentos de palavra-chave fornecidos."""
        if len(self.cnpj_list) == 0:
            return False
        for cnpj in self.cnpj_list:
            if self._cnpj_validator.validate(cnpj):
                self._valid_cnpjs.append(cnpj)
            else:
                self._invalid_cnpjs.append(cnpj)
        return len(self._invalid_cnpjs) == 0

    def get_valid_cnpjs(self) -> list:
        """Retorna uma lista de CNPJs válidos."""
        return self._valid_cnpjs

    def get_invalid_cnpjs(self) -> list:
        """Retorna uma lista de CNPJs inválidos."""
        return self._invalid_cnpjs

    def __str__(self) -> str:
        """Retorna uma representação de string do objeto."""
        return f"""Lista de CNPJs válidos: {self._valid_cnpjs}\nLista de CNPJs inválidos: {self._invalid_cnpjs}"""

    def __repr__(self) -> str:
        """Retorna uma representação de string do objeto."""
        return f"""Lista de CNPJs válidos: {self._valid_cnpjs}\nLista de CNPJs inválidos: {self._invalid_cnpjs}"""
