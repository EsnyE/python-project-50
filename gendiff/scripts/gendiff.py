import argparse
import os
import sys

from gendiff.generate_diff import generate_diff


def find_file(filename):
    if os.path.exists(filename):
        return filename
    
    test_data_path = os.path.join('tests', 'test_data', filename)
    if os.path.exists(test_data_path):
        return test_data_path
    
    return None


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output'
    )
    args = parser.parse_args()
    
    first_file = find_file(args.first_file)
    second_file = find_file(args.second_file)
    
    if not first_file:
        print(
            f"Error: File '{args.first_file}' not found "
            f"in current directory or tests/test_data/"
        )
        return 1
    
    if not second_file:
        print(
            f"Error: File '{args.second_file}' not found "
            f"in current directory or tests/test_data/"
        )
        return 1
    
    diff = generate_diff(first_file, second_file, args.format)
    print(diff)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())