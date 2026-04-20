from gendiff import generate_diff

diff = generate_diff('gendiff/json/file1.json', 'gendiff/json/file2.json')
print(diff)