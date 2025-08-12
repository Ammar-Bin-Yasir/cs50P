import random


def main():
    n = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        error = 1

        question = int(input(f"{x} + {y} = "))
        if (x + y) == question:
            score += 1
        else:
            print("EEE")
            while error != 3:
                question = int(input(f"{x} + {y} = "))
                if (x + y) == question:
                    break
                else:
                    error += 1

            print(f"{x} + {y} = {(x + y)}")

    print(f"Score: {score}")


# Returns an int LEVEL 1-3
def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 0 < n < 4:
                return n


# Generate numbers based on the level
def generate_integer(level):
    if level == 1:
        num = random.randint(0, 9)
        return num
    elif level == 2:
        num = random.randint(10, 99)
        return num
    elif level == 3:
        num = random.randint(100, 999)
        return num

if __name__ == "__main__":
    main()
