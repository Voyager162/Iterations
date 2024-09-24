# Looping with range

print("Example 1")
for x in range(3):
    print(x)

# Gives a range of numbers for the loop to go through

# The last number is not included (range(4) would be 0-3)

print("Example 2")
for x in range(2, 5):
    print(x)

# Added a start to the range

# Starts at 2 instead of 0 and ends at 5

print("Example 3")
for x in range(1, 10, 2):
    print(x)

# Adds a step

# Starts at 1 and goes 2 forward instead of 1 (1, 3, 5, 7, 9)


# Looping through a list with index variable

list = [1, 2, 5, "James", 7.0, "Adam"]

for item in range(len(list)):
    print(f"Index: {item}")
    print(f"Element: {list[item]}")

# Creates a list

# Creates a for loop having as many iterations as the length of the list

# Each iteration is an index which correlates to a value in the list