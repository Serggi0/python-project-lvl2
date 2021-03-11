install:
	poetry install

gendiff_json:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

gendiff_yaml:
	poetry run gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml

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