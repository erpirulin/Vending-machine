products = ["Water", "Chocolate", "Chips", "Soda", "Sandwich"]
choice_index = int(input())

# Write a try-except block to display the selected product
try:
    print(products[choice_index])
# or print "Wrong Index" if the input index is out of range
except IndexError:
    print("Worng Index")
