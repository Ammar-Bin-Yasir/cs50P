# gets the percentage of fuel in a tank

# Prompt user for a fraction (X/Y)
# Keep prompting of invalid value
while True:
    try:
        frac = input("Fraction: ")
        x, y = frac.split("/")
        x, y = int(x), int(y)
        if x > y:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

percentage = (x / y) * 100

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{round(percentage)}%")

