"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""
# Wrap the program in a function
def main():
    total = 0
    for i in range(5):
        number = int(input("Enter a number: "))
        total += number

    print("The running total is: " + str(total))

if __name__ ==  "__main__":
    main() # Run the main() function
