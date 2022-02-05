#very basic calculator
number1 = float(input("Please enter your first number: "))
operation = input("Please enter an operator")
number2 = float(input("Please enter your second number"))
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("something went wrong! Try again.")