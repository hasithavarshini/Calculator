import math

def perform_addition(x, y):
    return x + y

def perform_subtraction(x, y):
    return x - y

def perform_multiplication(x, y):
    return x * y

def perform_division(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def power(base, exponent):
    return base ** exponent

def compute_square_root(val):
    if val < 0:
        return "Error: Cannot compute square root of negative number."
    return math.sqrt(val)

def compute_factorial(num):
    if num < 0 or not float(num).is_integer():
        return "Error: Factorial is only defined for non-negative integers."
    return math.factorial(int(num))

def calculate_log10(val):
    if val <= 0:
        return "Error: log10 undefined for non-positive values."
    return math.log10(val)

def calculate_ln(val):
    if val <= 0:
        return "Error: Natural log undefined for non-positive values."
    return math.log(val)

def sine_in_degrees(deg):
    return math.sin(math.radians(deg))

def cosine_in_degrees(deg):
    return math.cos(math.radians(deg))

def tangent_in_degrees(deg):
    return math.tan(math.radians(deg))

while True:
    print("\n==== Advanced Calculator Menu ====")
    print("1. Add         2. Subtract       3. Multiply      4. Divide")
    print("5. Exponent    6. Square Root    7. Factorial     8. Display π")
    print("9. log10       10. ln            11. sin(x°)      12. cos(x°)")
    print("13. tan(x°)    14. Exit")

    option = input("Enter your choice (1 to 14): ")

    if option == '14':
        print("Calculator closed. Goodbye!")
        break

    try:
        if option in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first value: "))
            num2 = float(input("Enter second value: "))

            if option == '1':
                result = perform_addition(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif option == '2':
                result = perform_subtraction(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif option == '3':
                result = perform_multiplication(num1, num2)
                print(f"Result: {num1} × {num2} = {result}")
            elif option == '4':
                result = perform_division(num1, num2)
                print(f"Result: {num1} ÷ {num2} = {result}")
            elif option == '5':
                result = power(num1, num2)
                print(f"Result: {num1} ^ {num2} = {result}")

        elif option == '6':
            val = float(input("Enter value: "))
            result = compute_square_root(val)
            print(f"Result: √{val} = {result}")

        elif option == '7':
            val = float(input("Enter a non-negative integer: "))
            result = compute_factorial(val)
            print(f"Result: {int(val)}! = {result}")

        elif option == '8':
            print(f"Value of π: {math.pi}")

        elif option == '9':
            val = float(input("Enter value: "))
            result = calculate_log10(val)
            print(f"Result: log10({val}) = {result}")

        elif option == '10':
            val = float(input("Enter value: "))
            result = calculate_ln(val)
            print(f"Result: ln({val}) = {result}")

        elif option == '11':
            angle = float(input("Enter angle in degrees: "))
            result = sine_in_degrees(angle)
            print(f"Result: sin({angle}°) = {result}")

        elif option == '12':
            angle = float(input("Enter angle in degrees: "))
            result = cosine_in_degrees(angle)
            print(f"Result: cos({angle}°) = {result}")

        elif option == '13':
            angle = float(input("Enter angle in degrees: "))
            result = tangent_in_degrees(angle)
            print(f"Result: tan({angle}°) = {result}")

        else:
            print("Invalid choice. Please select a number from 1 to 14.")

    except ValueError:
        print("Input error: Please enter valid numerical values.")
