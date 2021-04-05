from gendiff import engine


def test_gendiff():
    file_result = open('tests/fixtures/file_result_plain.txt')
    my_string = file_result.read()
    x = engine.generate_diff(
        'tests/fixtures/file1_plain.json', 'tests/fixtures/file2_plain.json')
    assert my_string == x
    file_result.close()
