txt = input("Input: ")
out = ""

for c in txt:
    if c.lower() != "a" and c.lower() != "e" and c.lower() != "i" and c.lower() != "o" and c.lower() != "u":
        out += c
    else:
        pass

print(out)

