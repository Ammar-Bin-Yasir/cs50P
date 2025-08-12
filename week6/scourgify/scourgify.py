import csv
import sys

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

elif sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):

    # Read the file into a list
    contents = []

    try:
        with open(sys.argv[1]) as before:
            # Read the file
            reader = csv.DictReader(before)
            # Seperate the columns form name, house to first, last, house
            for row in reader:
                last, first = row['name'].split(", ")
                contents.append({'first': first, 'last': last, 'house': row['house']})

    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    else:
        # Write the contents into a new csv file
        with open(sys.argv[2], 'w', newline='') as after:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(after, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contents)
