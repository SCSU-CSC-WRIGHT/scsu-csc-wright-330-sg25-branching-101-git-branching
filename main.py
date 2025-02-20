"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""
total = 0 # Error 1: Added total = 0

for i in range(5):
    number = int(input("Enter a number: ")) # Error 2: Added int
    total += number

print("The running total is:  "+ str(total)) # Error 3: Added str()
