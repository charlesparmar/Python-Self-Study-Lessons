import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# multiplication1 = operation["*"](3,5)
# print(multiplication1)

def calculator():
    print(art.logo)
    accumulate = True
    num1 = float(input("Enter first number: "))

    while accumulate:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Enter operation: ")
        numb2 = float(input("Enter second number: "))
        answer = operation[operation_symbol](num1, numb2)
        print(f"{num1} {operation_symbol} {numb2} = {answer}")

        choice = input(f"Do you want to continue further operations with the {answer}? (y/n): ")
        if choice == "y":
            num1 = answer
        else:
            accumulate = False
            print("\n" * 20)
            calculator()

calculator()
