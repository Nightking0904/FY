# Script for comparing tow numbers and printing the result

a = float(input("Enter the first number: "))

b = float(input("Enter the second number: "))

if a > b:
    print(f"{a} is greater than {b}")

elif a < b:
    print(f"{a} is less than {b}")

else:
    print(f"{a} is equal to {b}")
