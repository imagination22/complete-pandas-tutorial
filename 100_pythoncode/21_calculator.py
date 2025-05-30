print("Calculator")
a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
operation = input("Enter the operation (+, -, *, /): ")
match operation:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Error: Invalid operation.")
