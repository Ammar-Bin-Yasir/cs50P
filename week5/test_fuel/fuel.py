import sys

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            value = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass

    result = gauge(value)
    print(result)


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        if y == 0:  # Check for division by zero
            raise ZeroDivisionError
        if x > y:  # Invalid fraction
            raise ValueError
        return round((x / y) * 100)
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
