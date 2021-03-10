install:
	poetry install

gendiff:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

build:
	poetry build

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests


test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

.PHONY: install build package-install lint gendiff test