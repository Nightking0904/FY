# -------------------------------------------------- 
# Method 1: Swap two values using a temporary variable
# -------------------------------------------------- 
# This approach works in all programming languages.
# We store one value in a temporary variable before reassigning both values.

a = input("Enter the value of 'a': ")
b = input("Enter the value of 'b': ")

temp = a
a = b
b = temp

print(f"The new value of 'a' is: {a}")
print(f"The new value of 'b' is: {b}")


# -------------------------------------------------- 
# Method 2: Python-only swap without a temporary variable
# -------------------------------------------------- 
# Python supports multiple assignment in a single line.
# This directly swaps the values of 'a' and 'b' without creating an extra variable.

a, b = b, a

print(f"The new value of 'a' is: {a}")
print(f"The new value of 'b' is: {b}")