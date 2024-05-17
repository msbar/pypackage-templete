import pytest

from package.validators.cpf_validator import CpfValidator


@pytest.fixture
def cpf_validator():
    """Create an instance of the CpfValidator class for testing."""
    return CpfValidator()


def test_validate_invalid_length(cpf_validator):
    """Test the validate method of the CpfValidator class with an invalid length."""
    assert cpf_validator.validate("123") == False


def test_validate_invalid_blacklist(cpf_validator):
    """Test the validate method of the CpfValidator class with an invalid blacklist."""
    assert cpf_validator.validate("00000000000") == False


def test_validate_ivalid(cpf_validator):
    """Test the validate method of the CpfValidator class with a valid CPF."""
    assert cpf_validator.validate("243.801.080-08") == False


def test_validate_valid(cpf_validator):
    """Test the validate method of the CpfValidator class with a valid CPF."""
    assert cpf_validator.validate("243.801.080-07") == True


def test_sanitize_cpf(cpf_validator):
    """Test the sanitize_cpf method of the CpfValidator class."""
    assert cpf_validator.sanitize_cpf("243.801.080-07") == "24380108007"


def test_calculate_first_digit(cpf_validator):
    """Test the _calculate_first_digit method of the CpfValidator class."""
    cpf = "24380108007"
    digits = [int(digit) for digit in cpf]
    assert cpf_validator._calculate_first_digit(digits) == 0


def test_calculate_second_digit(cpf_validator):
    """Test the _calculate_second_digit method of the CpfValidator class."""
    cpf = "24380108007"
    digits = [int(digit) for digit in cpf]
    assert cpf_validator._calculate_second_digit(digits) == 7


def test_help(cpf_validator):
    """Test the help method of the CpfValidator class."""
    assert cpf_validator.help() == "Valida um CPF."
