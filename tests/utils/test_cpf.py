import pytest

from package.utils.cpf import Cpf


@pytest.fixture
def valid_cpf():
    """CPF válido para teste."""
    return "243.801.080-07"


@pytest.fixture
def invalid_cpf():
    """CPF inválido para teste."""
    return "243.801.080-08"


def test_cpf_is_valid(valid_cpf):
    """Test the is_valid method of the Cpf class."""
    assert Cpf(cpf=valid_cpf).is_valid() == True


def test_cpf_is_invalid(invalid_cpf):
    """Testa o método validate da classe Cpf com um CPF inválido."""
    assert Cpf(cpf=invalid_cpf).is_valid() == False


def test_cpf_basico(valid_cpf):
    """Testa o método cpf_basico da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert cpf.cpf_basico == "243801080"


def test_cpf_digitos_verificadores(valid_cpf):
    """Testa o método digitos_verificadores da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert cpf.digitos_verificadores == "07"


def test_cpf_digito_verificador_1(valid_cpf):
    """Testa o método digito_verificador_1 da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert cpf.digito_verificador_1 == "0"


def test_cpf_digito_verificador_2(valid_cpf):
    """Testa o método digito_verificador_2 da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert cpf.digito_verificador_2 == "7"


def test_cpf_sanitized(valid_cpf):
    """Testa o método sanitized da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert cpf.sanitized == "24380108007"


def test_cpf_formatado():
    """Testa o método formatado da classe Cpf."""
    cpf = Cpf("24380108007")
    assert cpf.formatado == "243.801.080-07"


def test_cpf_anonimizado(valid_cpf):
    """Testa o método anonimizado da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert cpf.anonimizado == "**3801080**"


def test_cpf_int(valid_cpf):
    """Testa o método int da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert cpf.int == 24380108007


def test__str__(valid_cpf):
    """Testa o método __str__ da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert str(cpf) == "24380108007"


def test__repr__(valid_cpf):
    """Testa o método __repr__ da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert repr(cpf) == "cpf(cpf='24380108007')"


def test__eq__(valid_cpf):
    """Testa o método __eq__ da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert cpf == Cpf("243.801.080-07")


def test__len__(valid_cpf):
    """Testa o método __len__ da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert len(cpf) == 11


def test__hash__(valid_cpf):
    """Testa o método __hash__ da classe Cpf."""
    cpf = Cpf(valid_cpf)
    assert hash(cpf) == hash("24380108007")
