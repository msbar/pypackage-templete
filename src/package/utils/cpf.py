from package.validators.cpf_validator import CpfValidator


class Cpf:
    """Classe para processamento de CPF."""

    def __init__(self, cpf) -> None:
        """
        Inicializa a classe.

        Args:
            cpf: CPF
        """
        self.validator = CpfValidator()
        self._cpf = cpf
        self.__sanitized_cpf = self.sanitized

    @property
    def cpf(self) -> str:
        """Retorna CPF"""
        return self.__sanitized_cpf

    @cpf.setter
    def cpf(self, cpf) -> None:
        """
        Define CPF.

        Args:
            cpf: CPF
        """
        self._cpf = cpf
        self.__sanitized_cpf = self.sanitized

    @property
    def cpf_basico(self) -> str:
        """Retorna CPF sem formatação"""
        return self.cpf[0:9]

    @property
    def digitos_verificadores(self) -> str:
        """Retorna dígitos verificadores do CPF"""
        return self.cpf[9:]

    @property
    def digito_verificador_1(self) -> str:
        """Retorna primeiro dígito verificador do CPF"""
        return self.cpf[9]

    @property
    def digito_verificador_2(self) -> str:
        """Retorna segundo dígito verificador do CPF"""
        return self.cpf[10]

    @property
    def sanitized(self) -> str:
        """Remove caracteres não numéricos do CPF"""
        return self.validator.sanitize_cpf(self._cpf)

    @property
    def formatado(self) -> str:
        """Aplica máscara ao CPF"""
        mask = "###.###.###-##"
        format = ""
        cpf = self.__sanitized_cpf
        for i in range(len(mask)):
            if mask[i] == "#":
                format += cpf[0]
                cpf = cpf[1:]
            else:
                format += mask[i]
        return format

    @property
    def anonimizado(self) -> str:
        """Retorna CPF anonimizado"""
        return "**" + self.cpf_basico[2:] + "**"

    @property
    def int(self) -> int:
        """Retorna CPF como inteiro"""
        return int(self.__sanitized_cpf)

    def is_valid(self) -> bool:
        """Valida CPF"""
        return self.validator.validate(self.__sanitized_cpf)

    def __str__(self) -> str:
        """Retorna a representação do CPF como string"""
        return self.__sanitized_cpf

    def __repr__(self) -> str:
        """Retorna a representação do CPF como string"""
        return f"cpf(cpf='{self.__sanitized_cpf}')"

    def __len__(self) -> int:
        """Retorna o tamanho do CPF"""
        return len(self.__sanitized_cpf)

    def __hash__(self) -> int:
        """Retorna o hash do CPF"""
        return hash(self.__sanitized_cpf)

    def __eq__(self, other) -> bool:
        """
        Retorna se o CPF é igual a outro CPF

        Args:
            other: CPF ou string a ser comparado
        """
        if isinstance(other, Cpf):
            return self.__sanitized_cpf == other.cpf
        elif isinstance(other, str):
            return self.__sanitized_cpf == other
        else:
            return False
