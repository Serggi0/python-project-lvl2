install:
	poetry install

gendiff_json:
	poetry run gendiff tests/fixtures/file1_plain.json tests/fixtures/file2_plain.json

gendiff_yaml:
	poetry run gendiff tests/fixtures/file1_plain.yaml tests/fixtures/file2_plain.yaml

gendiff_json2:
	poetry run gendiff tests/fixtures/file1_recurs.json tests/fixtures/file2_recurs.json

gendiff_yaml2:
	poetry run gendiff tests/fixtures/file1_recurs.yaml tests/fixtures/file2_recurs.yaml

build:
	poetry build

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest -vv --cov=gendiff tests/ --cov-report xml

.PHONY: install build package-install lint gendiff test