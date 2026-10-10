year = int(input("Enter The Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"The year {year} is a Leap year")

else:
    print(f"The year {year} is Not a Leap year")