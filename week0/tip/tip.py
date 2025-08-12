def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # take the $##.## string and return float ##.##
    n = d.replace("$","")
    return float(n)


def percent_to_float(p):
    # take the ##% string and return float 0.##
    n = p.replace("%","")
    return float(f"0.{n}")


main()
