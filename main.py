"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""

# adjustment 1: create the main method
def main():
    running_total()

# adjustment 2: create a running_total function
# that contains sebastian's original code
def running_total():
    total = 0
    for i in range(5):
        number = int(input("Enter a number: "))
        total += number

    print("The running total is: ", total)

# adjustment 3: call the main method
main()
