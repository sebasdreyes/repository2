import math

def scientific_calculator():
    print("Select operation:")
    print("1. Sin")
    print("2. Cos")
    print("3. Tan")
    print("4. Logarithm (base 10)")
    print("5. Square Root")
    print("6. Power")
    print("7. Factorial")
    print("8. Exit")

    while True:
        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Exiting the calculator.")
            break

        if choice in {'1', '2', '3', '4', '5', '6', '7'}:
            if choice in {'1', '2', '3'}:  # Trigonometric functions
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)  # Convert to radians

                if choice == '1':
                    result = math.sin(radians)
                elif choice == '2':
                    result = math.cos(radians)
                elif choice == '3':
                    result = math.tan(radians)

            elif choice == '4':  # Logarithm
                num = float(input("Enter number: "))
                if num <= 0:
                    result = "Logarithm is not defined for non-positive numbers."
                else:
                    result = math.log10(num)

            elif choice == '5':  # Square Root
                num = float(input("Enter number: "))
                if num < 0:
                    result = "Square root is not defined for negative numbers."
                else:
                    result = math.sqrt(num)

            elif choice == '6':  # Power
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                result = math.pow(base, exponent)

            elif choice == '7':  # Factorial
                num = int(input("Enter a non-negative integer: "))
                if num < 0:
                    result = "Factorial is not defined for negative numbers."
                else:
                    result = math.factorial(num)

            print(f"Result: {result}")
        else:
            print("Invalid choice. Please try again.")

# Run the calculator
scientific_calculator()
