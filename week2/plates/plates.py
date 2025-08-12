def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # max characters = 6  min characters= 2
    if 2 <= len(s) <= 6:
        # No periods, spaces, or punctuation marks are allowed
        if s.isalnum() == True:
            # plates must start with at least two letters
            if s[0:2].isalpha() == True:
                # Numbers cannot be used in the middle of a plate
                firstnum = True
                flag = False
                for c in s[2:]:
                    if c.isdigit() == True:
                        while firstnum == True:
                            if c == "0":
                                return False
                            else:
                                firstnum = False
                        flag = True
                    if flag == True and (c.isalpha() == True):
                        return False
                return True
    else:
        return False

if __name__ == "__main__":
    main()
