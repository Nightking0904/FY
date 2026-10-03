# Script for Convertion of Kilometer to Mile and Mile to Kilometer

kms = float(input("Enter distance in kilometers: "))

miles = 0.621371 * kms

print(f"{kms} kilometers is equal to {miles.__round__(3)} miles. and {kms * 1000} meters ")

miles = float(input("Enter distance in miles: "))

kms = miles / 0.621371

print(f"{miles} miles is equal to {kms.__round__(3)} kilometers and {kms * 1000} meters ")
