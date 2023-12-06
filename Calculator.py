def addition(first_digit, second_digit):
    return first_digit + second_digit

def subtraction(first_digit, second_digit):
    return first_digit - second_digit

def multiplication(first_digit, second_digit):
    return first_digit * second_digit

def division(first_digit, second_digit):
    if second_digit != 0:
        return first_digit / second_digit
    else:
        return "Cannot divide by zero."

def start():
    print("\n******************* Simple Calculator in Python *******************")
    print("\n The mathematical operations are: ")
    print("\n 1 - Addition / 2 - Subtraction / 3 - Multiplication / 4 - Division")

    a = input("\n Choose the math operation (1/2/3/4): ")

    if a in ['1', '2', '3', '4']:
        first_digit = int(input("\n Write the first number to calculate: "))
        second_digit = int(input("\n Write the second number to calculate: "))
        result = comparison(a, first_digit, second_digit)
        print(f"\n Result: {result}")
    else:
        print("Incorrect digit...")
        start()

def comparison(a, first_digit, second_digit):
    if a == '1':
        return addition(first_digit, second_digit)
    elif a == '2':
        return subtraction(first_digit, second_digit)
    elif a == '3':
        return multiplication(first_digit, second_digit)
    elif a == '4':
        return division(first_digit, second_digit)

    return None

start()