# Calculator using Functions

def add(a: int, b: int) -> int:  # addition function
    return a + b


def subtract(a: int, b: int) -> int:  # subtract function
    return a - b


def divide(a: int, b: int) -> float:  # divide function
    return a / b


def multiply(a: int, b: int) -> int:  # multiply function
    return a * b


def calculator(num1: int, num2: int, operation: str) -> None:  # calculator function
    if operation == "+":  # returns number inputs added together
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == "-":  # returns number inputs subtracted
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == "/":  # returns number inputs divided
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:  # returns number inputs multiplied
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print("\n")
    main()


def main():
    operations_list = ["+", "-", "/", "*"]
    x = input("Would you like to +,-,/,or *? \n")
    if x in operations_list:  # Input validation so that a real operation can only be entered
        a = int(input("Enter your first number: \n"))
        b = int(input("Enter your second number: \n"))
        calculator(a, b, x)
    else:
        x = input("Would you like to +,-,/,or *")


if __name__ == '__main__':
    main()
