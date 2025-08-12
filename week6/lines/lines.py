import sys

def main():
    # Check for the condition where there is only 1 file provided at command line which is a python file.
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[1].endswith(".py") != True:
        print("Not a python file")
        sys.exit(1)


    elif len(sys.argv) == 2:
        try:
            with open(sys.argv[1]) as file:
                # Count the lines of code in the file
                lines = code_count(file)
                print(lines)

        except FileNotFoundError:
            print("File not found")
            sys.exit(1)


# Function to count the lines of code in the provided python file
def code_count(file):
    count = 0
    # Iterate over the file
    for row in file:
        if row.strip() == "" or "#" in row.strip():
            pass
        else:
            count += 1

    return count

main()

