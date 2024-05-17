import pytest

from package.validators.cpf_validator import CpfListValidator


@pytest.fixture
def valid_cpf_list():
    """Lista de CPFs para teste."""
    return ["243.801.080-07", "627.270.300-70", "832.029.310-32", "730.046.010-01"]


@pytest.fixture
def invalid_cpf_list():
    """Lista de CPFs para teste."""
    return ["243.801.080-08", "627.270.310-70", "853.029.310-36", "111.111.111-11"]


@pytest.fixture
def valid_invalid_cpf_list(valid_cpf_list, invalid_cpf_list):
    """Lista de CPFs para teste."""
    return valid_cpf_list + invalid_cpf_list


def test_cpf_list_validate_help():
    """Testa o método validate da classe CpfListValidator com uma lista vazia."""
    assert CpfListValidator(cpf_list=[]).help() == "Valida uma lista de CPFs."


def test_cpf_list_validator_empty():
    """Testa o método validate da classe CpfListValidator com uma lista vazia."""
    assert CpfListValidator(cpf_list=[]).validate() == False


def test_cpf_list_validator_validate_valid(valid_cpf_list):
    """Testa o método validate da classe CpfListValidator com uma lista valida."""
    assert CpfListValidator(cpf_list=valid_cpf_list).validate() == True


def test_cpf_list_validator_validate_invalid(invalid_cpf_list):
    """Testa o método validate da classe CpfListValidator com uma lista inválida."""
    assert CpfListValidator(cpf_list=invalid_cpf_list).validate() == False


def test_cpf_list_validator_get_valid_cpfs(valid_invalid_cpf_list, valid_cpf_list):
    """Testa o método get_valid_cpfs da classe CpfListValidator com uma lista de CPFs válidos."""
    cpf_list_validator = CpfListValidator(cpf_list=valid_invalid_cpf_list, sanitize=False)
    assert set(cpf_list_validator.get_valid_cpfs()) == set(valid_cpf_list)


def test_cpf_list_validator_get_invalid_cpfs(valid_invalid_cpf_list, invalid_cpf_list):
    """Testa o método get_invalid_cpfs da classe CpfListValidator com uma lista de CPFs inválidos."""
    cpf_list_validator = CpfListValidator(cpf_list=valid_invalid_cpf_list, sanitize=False)
    assert set(cpf_list_validator.get_invalid_cpfs()) == set(invalid_cpf_list)


def test_cpf_list_validator_sanitized(valid_invalid_cpf_list):
    """Testa o método validate da classe CpfListValidator com uma lista de CPFs válidos."""
    cpf_list_validator = CpfListValidator(cpf_list=valid_invalid_cpf_list, sanitize=True)
    valid_cpf_list_sanitized = ["73004601001", "83202931032", "62727030070", "24380108007"]
    assert set(cpf_list_validator.get_valid_cpfs()) == set(valid_cpf_list_sanitized)
