from gendiff import engine


def test_gendiff():
    file_result = open('tests/fixtures/file_result_recurs.txt')
    my_string = file_result.read()
    x = engine.generate_diff(
        'tests/fixtures/file1_recurs.json', 'tests/fixtures/file2_recurs.json')
    assert my_string == x
    file_result.close()
