import pytest
from gendiff.differ import generate_diff, read_file
import json


@pytest.mark.parametrize(
    'path_file1, path_file2, path_file_result, format_name',
    [
        ('tests/fixtures/file1_simple.json', 'tests/fixtures/file2_simple.json',
            'tests/fixtures/file_result_simple.txt', 'stylish'),
        ('tests/fixtures/file1_simple.yaml', 'tests/fixtures/file2_simple.yaml',
            'tests/fixtures/file_result_simple.txt', 'stylish'),
        ('tests/fixtures/file1_recurs.json', 'tests/fixtures/file2_recurs.json',
            'tests/fixtures/file_result_recurs.txt', 'stylish'),
        ('tests/fixtures/file1_recurs.yaml', 'tests/fixtures/file2_recurs.yaml',
            'tests/fixtures/file_result_recurs.txt', 'stylish'),
        ('tests/fixtures/file1_simple.json', 'tests/fixtures/file2_simple.json',
            'tests/fixtures/file_result_plain_simple.txt', 'plain'),
        ('tests/fixtures/file1_simple.yaml', 'tests/fixtures/file2_simple.yaml',
            'tests/fixtures/file_result_plain_simple.txt', 'plain'),
        ('tests/fixtures/file1_recurs.json', 'tests/fixtures/file2_recurs.json',
            'tests/fixtures/file_result_plain_recurs.txt', 'plain'),
        ('tests/fixtures/file1_recurs.yaml', 'tests/fixtures/file2_recurs.yaml',
            'tests/fixtures/file_result_plain_recurs.txt', 'plain'),
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
    'path_file1, path_file2, path_file_result, format_name',
    [
        ('tests/fixtures/file1_recurs.json', 'tests/fixtures/file2_recurs.json',
            'tests/fixtures/file_result_recurs.json', 'json'),
        ('tests/fixtures/file1_simple.json', 'tests/fixtures/file2_simple.json',
            'tests/fixtures/file_result_simple.json', 'json'),
    ]
)
def test_diff_json(path_file1, path_file2, path_file_result, format_name):
    file_res = read_file(path_file_result)
    res1 = json.loads(file_res)
    result = generate_diff(path_file1, path_file2, format_name='json')
    assert res1 == json.loads(result)


@pytest.mark.parametrize(
    "extention",
    [
        ('tests/fixtures/file_result_simple.txt'),
    ]
)
def test_unknown_format(extention):
    with pytest.raises(Exception) as err:
        raise Exception('Unsupported file format')
    assert err.value.args[0] == 'Unsupported file format'
