# prompts the user for mass as an integer (in kilograms)
m = int(input("m: "))

# calculates the energy using the formula E = mc^2
e = m*300000000**2

# outputs the equivalent number of Joules as an integer.
print(f"E: {e}")
