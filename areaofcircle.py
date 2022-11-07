
print("Area of Circle Calculator")

while True:
    radius = int(input("Enter Radius "))

    area = 3.142 * (radius**2)

    print("Area of the circle =", round(area, 2))
    print("Would you like to perform another operation?")
    print("1.Yes")
    print("2.No")
    option = int(input("Select option (1-2) "))
    if option == 1:
        continue
    else:
        break
