


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

def mod(n1, n2):
    return n1 % n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": mod
}

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for op in operations:
    print(op)

operation_symbol = input("Pick an operation from the line above: ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")