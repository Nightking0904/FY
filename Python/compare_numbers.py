num1 = float(input("Enter The First Number: "))
num2 = float(input("Enter The Second Number: "))
num3 = float(input("Enter The Third Number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The Largest of All is {num1}")

elif num2 >= num1 and num2 >= num3:
    print(f"The Largest of All is {num2}")

else:
    print(f"The Largest of All is {num3}")