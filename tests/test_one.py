from gendiff import engine


def test_get_diff():
    file_result = open('tests/fixtures/file_result.txt')
    assert engine.get_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json'
    ) == file_result.read()
    file_result.close()
