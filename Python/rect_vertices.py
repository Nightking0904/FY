# Very Simple vertices Calculator of a rectangle

x1 = int(input("Enter the Coordinate x1: "))
y1 = int(input("Enter the Coordinate y1: "))
print("======================================")
x2 = int(input("Enter the Coordinate x2: "))
y2 = int(input("Enter the Coordinate y2: "))
print("======================================")
x3 = int(input("Enter the Coordinate x3: "))
y3 = int(input("Enter the Coordinate y3: "))

if x1 == x2:
    print(f"The value of x4 is {x3}")

elif x1 == x3:
    print(f"The value of x4 is {x2}")

else:
    print("Your Entered x-Coordinates are not of a Rectangle\n")

if y1 == y2:
    print(f"The value of y4 is {y3}")

elif y1 == y3:
    print(f"The value of y4 is {y2}")

else:
    print("Your Entered y-Coordinates are not of a Rectangle")