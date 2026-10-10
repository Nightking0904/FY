# Program to check validation of a date

date = input("Enter the Date in format dd/mm/yyyy: ")
date = date.split("/")

day = int(date[0])
month = int(date[1])
year = int(date[2])
valid = True

if day < 1 or day > 31:
    valid = False

elif month < 1 or month > 12:
    valid = False

elif month in [4, 6, 9, 11] and day > 30:
    valid = False

elif month == 2:
    if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
        if day > 29:
            valid = False
    else:
        if day > 28:
            valid = False

if valid:
    print("The Date is Valid")
else:
    print("The Date is Invalid")