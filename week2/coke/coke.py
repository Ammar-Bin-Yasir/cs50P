# tell user the price of coke as amount due = 50 cents
coke = 50
while coke > 0:
    print(f"Amount Due: {coke}")

    # ask user to insert coin: 25 or 10 or 5 repeatedly until you get 50
    while True:
        money = int(input("Insert coin: "))
        if money == 5 or money == 10 or money == 25:
            break
        else:
            print(f"Amount Due: {coke}")

    coke -= money

# change = positive value of coke
change = abs(coke)

print(f"Change Owed: {change}")
