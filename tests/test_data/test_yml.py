from gendiff import generate_diff

diff = generate_diff('test/test_data/file1.yml', 'test/test_data/file2.yml')
print(diff)