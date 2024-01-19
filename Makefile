install:
	poetry install

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gen_diff --cov-report xml

lint:
	poetry run flake8 gen_diff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build