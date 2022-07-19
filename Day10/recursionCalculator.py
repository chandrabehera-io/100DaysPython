
# calculator program
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# create a dictionary named operations
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

# recursion calculator program


def calculator():
    num1 = float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    shouldContinue = True

    while shouldContinue:
        operator_symbol = input("Enter operator: ")
        num2 = float(input("Enter next number: "))
        # get the function from the dictionary
        calculation_function = operations[operator_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1}{operator_symbol}{num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation") == "y":
            num1 = answer
        else:
            shouldContinue = False
            calculator()


calculator()
