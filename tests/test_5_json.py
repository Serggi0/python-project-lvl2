from gendiff import engine


def test_gendiff():
    file_result = open('tests/fixtures/file_result_json_simple.txt')
    my_string = file_result.read()
    path_file1 = 'tests/fixtures/file1_simple.json'
    path_file2 = 'tests/fixtures/file2_simple.json'
    x = engine.generate_diff(path_file1, path_file2, format_name='json')
    assert my_string == x
    file_result.close()