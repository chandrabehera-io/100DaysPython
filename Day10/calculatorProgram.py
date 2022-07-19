# calclulator program

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


num1 = int(input("Enter first number: "))
num2 = int(input("Enter next number: "))
operator = input("Enter operator: ")

# check if the operator is in the dictionary

for key in operations:
    if key == operator:
        print(operations[key](num1, num2))
        break
    else:
        print("Invalid operator")
        break
