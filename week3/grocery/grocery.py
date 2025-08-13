# Its a grocery list, just enter a grocery item

# dict to store all the items
items = {}

# Add items list to dictionary
while True:
    try:
        item = input().upper()
    except EOFError:
        break
    if item in items:
        items[item] += 1
    else:
        items.update({item: 1})

# sort the dictionary alphabetically
# print the dictionary in formatted way "Quantity Item"
for item in sorted(items):
    print(f"{items[item]} {item}")
