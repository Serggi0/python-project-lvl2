from gendiff import differ


def test_gendiff():
    file_result = open('tests/fixtures/file_result_plain_simple.txt')
    my_string = file_result.read()
    path_file1 = 'tests/fixtures/file1_simple.yaml'
    path_file2 = 'tests/fixtures/file2_simple.yaml'
    x = differ.generate_diff(path_file1, path_file2, format_name='plain')
    assert my_string == x
    file_result.close()
