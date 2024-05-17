.PHONY: format lint test sec

format:
	@black src/package/
	@black tests/
	@isort -m 3 src/package/
	@isort -m 3 tests/

lint:
	@black src/package/ --check
	@black tests/ --check
	@flake8 src/package/
	@flake8 tests/
	@isort -m 3 src/package/ --check
	@isort -m 3 tests/ --check


test:
	@pytest -v
	
sec:
	@pip-audit