from gendiff import generate_diff

diff = generate_diff('tests/test_data/file1.yml', 'tests/test_data/file2.yml')
print(diff)
