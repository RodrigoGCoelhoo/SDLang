import sys
# import json

from parser_ import *

def main():
    input_file = sys.argv[1]
    with open(input_file) as file:
        content = file.read()
    root = Parser.run(content)
    root.Evaluate()

if __name__ == "__main__":
    main()

    # employee_array_json = json.dumps(employee_array, indent=2)
    # squads_table_json = json.dumps(squads_table, indent=2)

    # print(employee_array_json)
    # print(squads_table_json)
