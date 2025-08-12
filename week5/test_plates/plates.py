from sys import exit

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        exit(0)
    else:
        print("Invalid")
        exit(1)


def is_valid(s):
    # Check length constraints
    if not (2 <= len(s) <= 6):
        return False

    # Ensure all characters are alphanumeric
    if not s.isalnum():
        return False

    # Ensure the plate starts with at least two letters
    if not s[:2].isalpha():
        return False

    # Numbers cannot be used in the middle of the plate
    has_number = False
    for char in s[2:]:
        if char.isdigit():
            if not has_number and char == "0":
                # Numbers cannot start with '0'
                return False
            has_number = True
        elif has_number:
            # A letter appears after a number
            return False

    return True

if __name__ == "__main__":
    main()
