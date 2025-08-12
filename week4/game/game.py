import random

# Prompt user for a positive number
while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        if n > 0:
            break

# Generate a random number 1-n
num = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess > 0:
            if guess > num:
                print("Too large!")
            elif guess < num:
                print("Too small!")
            else:
                print("Just right!")
                break
