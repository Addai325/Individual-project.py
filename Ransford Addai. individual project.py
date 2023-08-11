# INDIVIDUAL PROJECT(ARITHMETIC CALCULATOR)
# NAME: Ransford Addai
# TRAINING ID: 32524


#SOLUTION TO PROJECT

def main():
    # Display a welcome message
    print("Welcome to the Basic Arithmetic calculator!👋")
    print()

    # Start an infinite loop for user interaction
    while True:
        try:
            # Get user input for two numbers
            num_one = int(input("Please enter your first number: "))
            num_two = int(input("Please enter your second number: "))
        except ValueError:
            # Handle invalid input by showing an error message
            print("Please enter a valid number.☺️")
            continue

        # Display available arithmetic operations
        print("Select an operation:")
        print("1. Multiplication")
        print("2. Addition")
        print("3. Subtraction")
        your_choice = input("Enter your choice (1/2/3): ")

        # Perform the selected arithmetic operation based on user's choice
        if your_choice == "1":
            result = num_one * num_two
            operator = "*"
        elif your_choice == "2":
            result = num_one + num_two
            operator = "+"
        elif your_choice == "3":
            result = num_one - num_two
            operator = "-"
        else:
            # Handle invalid operation choice
            print("Invalid choice, please choose a valid operation.☺️")
            continue

        # Display the calculated result
        print(f"Result: {num_one} {operator} {num_two} = {result}")

        # Ask if the user wants to perform another calculation
        repeat = input("Do you want to perform another calculation? (yes/no): ").lower()
        print()
        if repeat == "yes":
            continue
        elif repeat == "no":
            # End the loop if the user doesn't want to continue
            print("Thank you for using the Basic Arithmetic Calculator!😇")
            break
        else:
            # Handle invalid input for repeating calculation
            print("Please choose between yes/no.")

# Call the main function to start the program
main()
