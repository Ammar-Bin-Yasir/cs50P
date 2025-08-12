ctxt = input("camelCase: ")

stxt = ""
for c in ctxt:
    if c.isupper():
        stxt += "_" + c.lower()
    else:
        stxt += c

print(stxt)
