import sys
import os
import argparse
from gendiff.generate_diff import generate_diff

def find_file(filename):

    if os.path.exists(filename):
        return filename
 
    test_path = os.path.join('test', 'test_data', filename)
    if os.path.exists(test_path):
        return test_path
    
    return None

def main():
    gendiff_text = '''gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options::
  -h, --help            show this help message and exit
  -f {stylish, plain, json}, --format {stylish, plain, json}
                        set format of output
  Example:
  gendiff file1.json file2.json
  gendiff -f plain file1.yml file2.yml'''
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='output format (default: stylish)'
    )
    
    args = parser.parse_args()
    
    first_file = find_file(args.first_file)
    second_file = find_file(args.second_file)
    
    if not first_file:
        print(f"Error: File '{args.first_file}' not found in current directory or tests/test_data/")
        return 1
    
    if not second_file:
        print(f"Error: File '{args.second_file}' not found in current directory or tests/test_data/")
        return 1
    
    try:
        diff = generate_diff(first_file, second_file, args.format)
        print(diff)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0
if __name__ == "__main__":
    main()