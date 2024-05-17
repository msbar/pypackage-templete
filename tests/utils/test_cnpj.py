import pytest

from package.utils.cnpj import Cnpj


@pytest.fixture
def valid_cnpj():
    """CNPJ válido para teste."""
    return "00.394.460/0058-87"


@pytest.fixture
def invalid_cnpj():
    """CNPJ inválido para teste."""
    return "00.394.460/0058-88"


def test_cnpj_is_valid(valid_cnpj):
    """Test the is_valid method of the Cnpj class."""
    assert Cnpj(cnpj=valid_cnpj).is_valid() == True


def test_cnpj_is_invalid(invalid_cnpj):
    """Testa o método validate da classe Cnpj com um CNPJ inválido."""
    assert Cnpj(cnpj=invalid_cnpj).is_valid() == False


def test_cnpj_basico(valid_cnpj):
    """Testa o método cnpj_basico da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert cnpj.cnpj_basico == "00394460"


def test_cnpj_ordem(valid_cnpj):
    """Testa o método cnpj_ordem da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert cnpj.cnpj_ordem == "0058"


def test_cnpj_digitos_verificadores(valid_cnpj):
    """Testa o método digitos_verificadores da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert cnpj.digitos_verificadores == "87"


def test_cnpj_digito_verificador_1(valid_cnpj):
    """Testa o método digito_verificador_1 da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert cnpj.digito_verificador_1 == "8"


def test_cnpj_digito_verificador_2(valid_cnpj):
    """Testa o método digito_verificador_2 da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert cnpj.digito_verificador_2 == "7"


def test_cnpj_sanitized(valid_cnpj):
    """Testa o método sanitized da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert cnpj.sanitized == "00394460005887"


def test_cnpj_formatado():
    """Testa o método formatado da classe Cnpj."""
    cnpj = Cnpj("00394460005887")
    assert cnpj.formatado == "00.394.460/0058-87"


def test_cnpj_anonimizado(valid_cnpj):
    """Testa o método anonimizado da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert cnpj.anonimizado == "00394460******"


def test_cnpj_int(valid_cnpj):
    """Testa o método int da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert cnpj.int == 394460005887


def test_cnpj_matriz(valid_cnpj):
    """Testa o método matriz da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert Cnpj("18.727.053/0001-74").matriz() == True
    assert cnpj.matriz() == False


def test_cnpj_filial(valid_cnpj):
    """Testa o método filial da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert cnpj.filial() == True
    assert Cnpj("18.727.053/0001-74").filial() == False


def test__str__(valid_cnpj):
    """Testa o método __str__ da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert str(cnpj) == "00394460005887"


def test__repr__(valid_cnpj):
    """Testa o método __repr__ da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert repr(cnpj) == "Cnpj(cnpj='00394460005887')"


def test__eq__(valid_cnpj):
    """Testa o método __eq__ da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert cnpj == Cnpj("00.394.460/0058-87")


def test__len__(valid_cnpj):
    """Testa o método __len__ da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert len(cnpj) == 14


def test__hash__(valid_cnpj):
    """Testa o método __hash__ da classe Cnpj."""
    cnpj = Cnpj(valid_cnpj)
    assert hash(cnpj) == hash("00394460005887")
