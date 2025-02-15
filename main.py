"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""

# ORLANDO MARIN
# Software Design and Development - CSC 330
# March 2, 20255


def main():
    running_total()


def running_total():
    # error fix #1: initialize total to 0
    total = 0

    for i in range(5):
        # ask user to input a number
        # error fix #2: convert user input to an integer
        number = int(input("Enter a number: "))
        total += number
    
    # error fix #3: add a comma after the string so the running total appears
    print("The running total is: ",  total)


if __name__ == "__main__":
    main()