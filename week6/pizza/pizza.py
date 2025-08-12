import sys
import csv
from tabulate import tabulate

def main():
    # Check for the condition where there is only 1 file provided at command line which is a csv file.
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[1].endswith(".csv") != True:
        print("Not a python file")
        sys.exit(1)
    else:
        try:
            with open(sys.argv[1]) as file:
                row = csv.DictReader(file)
                print(tabulate(row, headers="keys",tablefmt="grid"))


        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)

main()

