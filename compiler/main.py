import argparse
from parser_ import *

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("-v", "--verbose", action='store_true', help="Verbose mode")
argument_parser.add_argument("input_file", help="Input file")
args = argument_parser.parse_args()

VERBOSE_MODE = args.verbose

def main():
   with open(args.input_file) as file:
       content = file.read()
   root = Parser.run(content)
   root.Evaluate()
   if VERBOSE_MODE:
      print("\nSprint ended")

if __name__ == "__main__":
   main()


    # employee_array_json = json.dumps(employee_array, indent=2)
    # squads_table_json = json.dumps(squads_table, indent=2)

    # print(employee_array_json)
    # print(squads_table_json)
