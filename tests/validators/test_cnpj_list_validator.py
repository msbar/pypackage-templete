import pytest

from package.validators.cnpj_validator import CnpjListValidator


@pytest.fixture
def valid_cnpj_list():
    """Lista de CNPJs para teste."""
    return ["00.394.460/0058-87", "18.727.053/0001-74", "00.000.000/0001-91", "42.498.733/0001-48"]


@pytest.fixture
def invalid_cnpj_list():
    """Lista de CNPJs para teste."""
    return ["00.394.460/0058-88", "00.394.460/0058-89", "00.394.460/0058-90", "00.394.460/0058-91"]


@pytest.fixture
def valid_invalid_cnpj_list(valid_cnpj_list, invalid_cnpj_list):
    """Lista de CNPJs para teste."""
    return valid_cnpj_list + invalid_cnpj_list


def test_cnpj_list_validate_help():
    """Testa o método validate da classe CnpjListValidator com uma lista vazia."""
    assert CnpjListValidator(cnpj_list=[]).help() == "Valida uma lista de CNPJs."


def test_cnpj_list_validator_empty():
    """Testa o método validate da classe CnpjListValidator com uma lista vazia."""
    assert CnpjListValidator(cnpj_list=[]).validate() == False


def test_cnpj_list_validator_validate_valid(valid_cnpj_list):
    """Testa o método validate da classe CnpjListValidator com uma lista valida."""
    assert CnpjListValidator(cnpj_list=valid_cnpj_list).validate() == True


def test_cnpj_list_validator_validate_invalid(invalid_cnpj_list):
    """Testa o método validate da classe CnpjListValidator com uma lista inválida."""
    assert CnpjListValidator(cnpj_list=invalid_cnpj_list).validate() == False


def test_cnpj_list_validator_valid_cnpjs(valid_invalid_cnpj_list, valid_cnpj_list):
    """Testa o método get_valid_cnpjs da classe CnpjListValidator com uma lista de CNPJs válidos."""
    cnpj_list_validator = CnpjListValidator(cnpj_list=valid_invalid_cnpj_list, sanitize=False)
    assert set(cnpj_list_validator.get_valid_cnpjs()) == set(valid_cnpj_list)


def test_cnpj_list_validator_invalid_cnpjs(valid_invalid_cnpj_list, invalid_cnpj_list):
    """Testa o método get_invalid_cnpjs da classe CnpjListValidator com uma lista de CNPJs inválidos."""
    cnpj_list_validator = CnpjListValidator(cnpj_list=valid_invalid_cnpj_list, sanitize=False)
    assert set(cnpj_list_validator.get_invalid_cnpjs()) == set(invalid_cnpj_list)


def test_cnpj_list_validator_sanitized(valid_invalid_cnpj_list):
    """Testa o método validate da classe CnpjListValidator com uma lista de CNPJs válidos."""
    cnpj_list_validator = CnpjListValidator(cnpj_list=valid_invalid_cnpj_list, sanitize=True)
    valid_cnpj_list_sanitized = ["18727053000174", "42498733000148", "00394460005887", "00000000000191"]
    assert set(cnpj_list_validator.get_valid_cnpjs()) == set(valid_cnpj_list_sanitized)
