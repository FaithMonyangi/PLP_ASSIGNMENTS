
# Basic Calculator Program

# Get user input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = input("Enter an operator ('+', '-', '*', '/'): ")

# Perform the calculation based on the operator
if c == "+":
    result = a + b
    print(f"{a} + {b} = {result}")
    
elif c == "-":
    result = a - b
    print(f"{a} - {b} = {result}")
elif c == "*":
    result = a * b
    print(f"{a} * {b} = {result}")
elif c == "/":
    if b == 0:
        print("Error! Division by zero is not allowed.")
    else:
        result = a / b
        print(f"{a} / {b} = {result}")
else:
    print("Invalid operator! Please enter '+', '-', '*', or '/'.")
