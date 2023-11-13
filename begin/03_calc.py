def main():
    print("Enter two integers followed by matematical operation ")
    n1 = int(input("What is the first number? "))
    n2 = int(input("What is the second number? "))
    operation = input("What is the operation? ")
    calculate(n1, n2, operation)


def calculate(n1, n2, operation):
    operators = ["+", "-", "/", "*"]
    if operation in operators:
        if operation == "+":
            print("addtion")
            print(add(n1, n2))
        elif operation == "-":
            print("subtract")
            print(subtract(n1, n2))
        elif operation == "/":
            print("divide")
            print(divide(n1, n2))
        else:
            print("multiply")
            print(multiply(n1, n2))
    else:
        print("select another operation!")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


main()
