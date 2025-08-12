print("What is the Answer to the Great Question of Life, the Universe, and Everything? ", end="")

question = input().strip()

if question == "42" or question.lower() == "forty two" or question.lower() == "forty-two":
    print("Yes")
else:
    print("No")



