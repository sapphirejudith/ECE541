print("Biodata form")

name = input("Enter your name ")
age = int(input("Enter your age "))
dept = input("Enter your department ")

def display(name, age, dept):
    print("Name:", name)
    print("Age:", age)
    print("Department:", dept)

display(name, age, dept)