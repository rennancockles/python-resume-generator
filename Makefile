.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")

.PHONY: fmt
fmt:            ## Format code using ruff formatter.
	$(ENV_PREFIX)ruff format .

.PHONY: lint
lint:        	  ## Run ruff and mypy linters.
	$(ENV_PREFIX)ruff check .
	$(ENV_PREFIX)ruff format . --check
	$(ENV_PREFIX)mypy

.PHONY: ruff
ruff:           ## Run ruff checks.
	$(ENV_PREFIX)ruff check .
	$(ENV_PREFIX)ruff format . --check

.PHONY: mypy
mypy:           ## Run mypy checks.
	$(ENV_PREFIX)mypy

.PHONY: test
test:        	  ## Run tests
	$(ENV_PREFIX)pytest

.PHONY: test_cov
test_cov:       ## Run tests with coverage
	$(ENV_PREFIX)pytest --cov --cov-report=html
