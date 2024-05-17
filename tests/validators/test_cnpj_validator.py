import pytest

from package.validators.cnpj_validator import CnpjValidator


@pytest.fixture
def cnpj_validator():
    """Create an instance of the CnpjValidator class for testing."""
    return CnpjValidator()


def test_validate_invalid_length(cnpj_validator):
    """Test the validate method of the CnpjValidator class with an invalid length."""
    assert cnpj_validator.validate("123") == False


def test_validate_invalid_blacklist(cnpj_validator):
    """Test the validate method of the CnpjValidator class with an invalid blacklist."""
    assert cnpj_validator.validate("00000000000000") == False


def test_validate_ivalid(cnpj_validator):
    """Test the validate method of the CnpjValidator class with a valid CNPJ."""
    assert cnpj_validator.validate("00.394.460/0058-86") == False


def test_validate_valid(cnpj_validator):
    """Test the validate method of the CnpjValidator class with a valid CNPJ."""
    assert cnpj_validator.validate("00.394.460/0058-87") == True


def test_sanitize_cnpj(cnpj_validator):
    """Test the sanitize_cnpj method of the CnpjValidator class."""
    assert cnpj_validator.sanitize_cnpj("00.394.460/0058-87") == "00394460005887"


def test_calculate_first_digit(cnpj_validator):
    """Test the _calculate_first_digit method of the CnpjValidator class."""
    cnpj = "00394460005887"
    digits = [int(digit) for digit in cnpj]
    assert cnpj_validator._calculate_first_digit(digits) == 8


def test_calculate_second_digit(cnpj_validator):
    """Test the _calculate_second_digit method of the CnpjValidator class."""
    cnpj = "00394460005887"
    digits = [int(digit) for digit in cnpj]
    assert cnpj_validator._calculate_second_digit(digits) == 7


def test_help(cnpj_validator):
    """Test the help method of the CnpjValidator class."""
    assert cnpj_validator.help() == "Valida um CNPJ."
