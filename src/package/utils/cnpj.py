from package.validators.cnpj_validator import CnpjValidator


class Cnpj:
    """Classe para processamento de CNPJ"""

    def __init__(self, cnpj) -> None:
        """
        Inicializa a classe.

        Args:
            cnpj: CNPJ
        """
        self.validator = CnpjValidator()
        self._cnpj = cnpj
        self.__sanitized_cnpj = self.sanitized

    @property
    def cnpj(self) -> str:
        """Retorna CNPJ"""
        return self.__sanitized_cnpj

    @cnpj.setter
    def cnpj(self, cnpj) -> None:
        """
        Define CNPJ.

        Args:
            cnpj: CNPJ
        """
        self._cnpj = cnpj
        self.__sanitized_cnpj = self.sanitized

    @property
    def cnpj_basico(self) -> str:
        """Retorna CNPJ sem formatação"""
        return self.cnpj[0:8]

    @property
    def cnpj_ordem(self) -> str:
        """Retorna ordem do CNPJ"""
        return self.cnpj[8:12]

    @property
    def digitos_verificadores(self) -> str:
        """Retorna dígitos verificadores do CNPJ"""
        return self.cnpj[12:14]

    @property
    def digito_verificador_1(self) -> str:
        """Retorna primeiro dígito verificador do CNPJ"""
        return self.cnpj[12]

    @property
    def digito_verificador_2(self) -> str:
        """Retorna segundo dígito verificador do CNPJ"""
        return self.cnpj[13]

    @property
    def sanitized(self) -> str:
        """Remove caracteres não numéricos do CNPJ"""
        return self.validator.sanitize_cnpj(self._cnpj)

    @property
    def formatado(self) -> str:
        """Aplica máscara ao CNPJ"""
        mask = "##.###.###/####-##"
        format = ""
        cnpj = self.__sanitized_cnpj
        for i in range(len(mask)):
            if mask[i] == "#":
                format += cnpj[0]
                cnpj = cnpj[1:]
            else:
                format += mask[i]
        return format

    @property
    def anonimizado(self) -> str:
        """Retorna CNPJ anonimizado"""
        return self.cnpj_basico + "******"

    @property
    def int(self) -> int:
        """Retorna CNPJ como inteiro"""
        return int(self.__sanitized_cnpj)

    def matriz(self) -> bool:
        """Verifica se CNPJ é matriz"""
        return self.cnpj[8:12] == "0001"

    def filial(self) -> bool:
        """Verifica se CNPJ é filial"""
        return not self.matriz()

    def is_valid(self) -> bool:
        """Valida CNPJ"""
        return self.validator.validate(self.__sanitized_cnpj)

    def __str__(self) -> str:
        """Retorna a representação do CNPJ como string"""
        return self.__sanitized_cnpj

    def __repr__(self) -> str:
        """Retorna a representação do CNPJ como string"""
        return f"Cnpj(cnpj='{self.__sanitized_cnpj}')"

    def __len__(self) -> int:
        """Retorna o tamanho do CNPJ"""
        return len(self.__sanitized_cnpj)

    def __hash__(self) -> int:
        """Retorna o hash do CNPJ"""
        return hash(self.__sanitized_cnpj)

    def __eq__(self, other) -> bool:
        """
        Verifica se CNPJ é igual a outro CNPJ ou string

        Args:
            other: CNPJ ou string
        """
        if isinstance(other, Cnpj):
            return self.__sanitized_cnpj == other.cnpj
        elif isinstance(other, str):
            return self.__sanitized_cnpj == other
        else:
            return False
