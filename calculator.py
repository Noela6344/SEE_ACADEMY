def calculator():
    print("Welcome to the Full Calculator")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nCalculating...")

        print(f"\nSum: {num1} + {num2} = {num1 + num2}")
        print(f"Difference: {num1} - {num2} = {num1 - num2}")
        print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

        if num2 != 0:
            print(f"Division (Quotient): {num1} / {num2} = {num1 / num2}")
        else:
            print("Division: Error! Cannot divide by zero.")

    except ValueError:
        print("\nError: Please enter valid numbers.")

# Run the calculator
calculator()