from gendiff import generate_diff

diff = generate_diff('tests/test_data/file1.json', 'tests/test_data/file2.json')
print(diff)
