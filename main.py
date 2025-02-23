def main():
    """
    Prompts the user to enter five numbers and calculates the running total.
    Prints the final total.
    """
    
    total = 0  # Initialize total to zero

    for _ in range(5):
        number = int(input("Enter a number: "))  # Get user input as integer
        total += number  # Add number to running total

    print("The running total is: " + str(total))  # Print final total


if __name__ == "__main__":
    main()