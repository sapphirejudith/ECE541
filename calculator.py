
#functions

def add(a,b):
    total = a + b
    return total

def subtract(a,b):
    total = a - b
    return total

def multiply(a,b):
    total = a * b
    return total

def divide (a,b):
    total = a / b
    return total
while True:
    print("Select an Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    selection = input("Select an operation (1-4) ")
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    if selection == '1':
        print(a," + ", b, " = ", add(a,b))
    elif selection == '2':
        print(a, " - ", b, " = ", subtract(a,b))
    elif selection == '3':
        print(a," * ", b ," = ", multiply(a,b))
    elif selection == '4':
        print(a ," / ", b ," = ", round(divide(a,b), 2))
    else:
        print("Invalid selection")

    print("Would you like to perform another operation?")
    print("1.Yes")
    print("2.No")
    option = int(input("Select option (1-2) "))
    if option == 1:
        continue
    else:
        break