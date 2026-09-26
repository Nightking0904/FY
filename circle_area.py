import math

# Get radius from user
radius = float(input("Enter the radius of the circle: "))

# Get Unit From User 
unit = input("Enter the desired unit: ")

# Calculate area: Area = pi * r^2
area = math.pi * (radius ** 2)

# Print the actual area
print(f"The area of the circle with radius {radius} is: {area} sq {unit}")
