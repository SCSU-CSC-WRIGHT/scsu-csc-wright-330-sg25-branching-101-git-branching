"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""

# Fix 1: Initialize variable `total`
total = 0

for i in range(5):
    # Fix 2: Convert input into an integer
    number = int(input("Enter a number: "))
    total += number

# Fix 3: Add comma to separate arguments to print function
print("The running total is: ", total)
