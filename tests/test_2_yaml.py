from gendiff import engine


def test_gendiff():
    file_result = open('tests/fixtures/file_result_recurs.txt')
    my_string = file_result.read()
    x = engine.generate_diff(
        'tests/fixtures/file1_recurs.yaml', 'tests/fixtures/file2_recurs.yaml')
    assert my_string == x
    file_result.close()
