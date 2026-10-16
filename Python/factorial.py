num = int(input("Enter the number: "))

fact = 1
count = 1

while count <= num:
    fact = fact * count
    count += 1

print(f"Factorial of {num} is {fact}")