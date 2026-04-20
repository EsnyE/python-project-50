from gendiff import generate_diff

diff = generate_diff('test/test_data/file1.json', 'test/test_data/file2.json')
print(diff)