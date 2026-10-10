#Python program to find roots of ax^2 + bx + c = 0
import math

a= int(input("Enter the coefficient 'a': "))
b= int(input("Enter the coefficient 'b': "))
c= int(input("Enter the coefficient 'c': "))

D = (b**2 - 4*a*c)

if D > 0:
    root1 = (-b + math.sqrt(D)) / 2*a
    root2 = (-b - math.sqrt(D)) / 2*a

    print(f"Both roots have two distinct real values: {root1} and {root2}")

elif D == 0:
    eq_root = (-b / 2*a)

    print(f"Both roots are real and equal in value: {eq_root}")

else:
    real_part = -b / 2*a
    img_part = math.sqrt(-D) / 2*a

    print(f"Both roots are imaginary and have two complex values: {real_part} + {img_part}i and {real_part} - {img_part}i")
