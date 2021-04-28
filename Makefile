install:
	poetry install

gendiff_json:
	poetry run gendiff tests/fixtures/file1_simple.json tests/fixtures/file2_simple.json

gendiff_yaml:
	poetry run gendiff tests/fixtures/file1_simple.yaml tests/fixtures/file2_simple.yaml

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

.PHONY: install build package-install lint gendiff test gendiff_json gendiff_json2 gendiff_yaml gendiff_yaml2