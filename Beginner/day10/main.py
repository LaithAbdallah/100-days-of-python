import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return None
    else:
        return n1 / n2

def power(n1, n2):
    return n1 ** n2

# To have cleaner result message
def check_is_integer(number):
    if number.is_integer():
        return int(number)
    return number

def calculator(operations, first_num):
    if first_num is None:
        first_number = float(input("What's the first number?: "))
    else:
        first_number = first_num
    for key in operations:
        print(key)
    operation = input("Pick an operation: ")
    while operation not in  operations:
        operation = input("Please pick either one of the five operations '+', '-', '*', '/', '^': ")
    second_number = float(input("What's the next number?: "))
    result = operations[operation](first_number, second_number)
    if result is None:
        print("Error Occurred, Can't divide by 0!")
        return None
    result = check_is_integer(result)
    first_number = check_is_integer(first_number)
    second_number = check_is_integer(second_number)
    print(f"{first_number} {operation} {second_number} = {result}")
    return result

def main():
    print(art.logo)
    operations_dict = {
        "+": add, "-": subtract, "*": multiply, "/": divide, "^": power
    }
    previous_result = None
    while True:
        output = calculator(operations_dict, previous_result)
        if output is None:
            keep_going = input("Type 'n' to start a new calculation, or 'x' to exit: ")
            while keep_going not in "nx":
                keep_going = input("Please type either 'n' or 'x': ")
        else:
            keep_going = input(f"Type 'y' to continue calculating with {output}, or 'n' to start a new calculation, or 'x' to exit the program:  ")
            while keep_going not in "ynx":
                keep_going = input("Please type either 'y' or 'n' or 'x': ")
        if keep_going == "n":
            print("\n" * 20 + art.logo)
            previous_result = None
        elif keep_going == "y":
            previous_result = output
        else:
            break



if __name__ == "__main__":
    main()