def main():
    txt = input("Input: ")
    print(shorten(txt))


def shorten(txt):

    out = ""

    for c in txt:
        if c.lower() != "a" and c.lower() != "e" and c.lower() != "i" and c.lower() != "o" and c.lower() != "u":
            out += c
        else:
            pass

    return out

if __name__ == "__main__":
    main()

