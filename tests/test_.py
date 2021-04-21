import pytest
from gendiff.differ import generate_diff, get_format


file1_simple_json = 'tests/fixtures/file1_simple.json'
file2_simple_json = 'tests/fixtures/file2_simple.json'
file1_recurs_json = 'tests/fixtures/file1_recurs.json'
file2_recurs_json = 'tests/fixtures/file2_recurs.json'
file1_simple_yaml = 'tests/fixtures/file1_simple.yaml'
file2_simple_yaml = 'tests/fixtures/file2_simple.yaml'
file1_recurs_yaml = 'tests/fixtures/file1_recurs.yaml'
file2_recurs_yaml = 'tests/fixtures/file2_recurs.yaml'
file_result_simple = 'tests/fixtures/file_result_simple.txt'
file_result_recurs = 'tests/fixtures/file_result_recurs.txt'
file_result_plain_simple = 'tests/fixtures/file_result_plain_simple.txt'
file_result_plain_recurs = 'tests/fixtures/file_result_plain_recurs.txt'
file_result_json_recurs = 'tests/fixtures/file_result_json_recurs.txt'


@pytest.mark.parametrize(
    'path_file1, path_file2, path_file_result, format_name',
    [
        (file1_simple_json, file2_simple_json,
            file_result_simple, 'stylish'),
        (file1_simple_yaml, file2_simple_yaml,
            file_result_simple, 'stylish'),
        (file1_recurs_json, file2_recurs_json,
            file_result_recurs, 'stylish'),
        (file1_recurs_yaml, file2_recurs_yaml,
            file_result_recurs, 'stylish'),
        (file1_simple_json, file2_simple_json,
            file_result_plain_simple, 'plain'),
        (file1_simple_yaml, file2_simple_yaml,
            file_result_plain_simple, 'plain'),
        (file1_recurs_json, file2_recurs_json,
            file_result_plain_recurs, 'plain'),
        (file1_recurs_yaml, file2_recurs_yaml,
            file_result_plain_recurs, 'plain'),
        (file1_recurs_json, file2_recurs_json,
            file_result_json_recurs, 'json')
    ]
)
def test_gendiff(path_file1, path_file2, path_file_result, format_name):
    file_result = open(path_file_result)
    my_string = file_result.read()
    path_file1 = path_file1
    path_file2 = path_file2
    x = generate_diff(path_file1, path_file2, format_name)
    assert my_string == x
    file_result.close()


@pytest.mark.parametrize(
    "extention",
    [
        ('tests/fixtures/file_result_simple.txt'),
        ('tests/fixtures/file_'),
        ('tests/fixtures/file_.md')
    ]
)
def test_unknown_format(extention):
    assert get_format(extention) == 0
