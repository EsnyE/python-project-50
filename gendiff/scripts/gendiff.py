import sys

def main():
    gendiff_text = '''gendiff -h
usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit'''
    if '-h' in sys.argv or '--help' in sys.argv:
      print(gendiff_text)


if __name__ == "__main__":
    main()