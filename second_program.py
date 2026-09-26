try:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))

    print(f"The Sum Of Two Numbers is: {a+b}")
    print(f"The Difference Between Two Numbers is: {a-b}")
    print(f"The Product of Two Numbers is: {a*b}")
    print(f"The Division of Two Numbers is: {a/b}")


except ValueError:
    print("Error: Please enter valid integer(s).")