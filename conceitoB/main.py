import sys

from parser_ import *

def main():
    input_file = sys.argv[1]
    with open(input_file) as file:
        content = file.read()
    root = Parser.run(content)
    root.Evaluate()

if __name__ == "__main__":
    main()
