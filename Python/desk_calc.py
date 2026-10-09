a = int(input("The Number of Students in class A: "))

b = int(input("The Number of Students in class B: "))

c = int(input("The Number of Students in class C: "))

desk_a = (a + 1) // 2 
desk_b = (b + 1) // 2 
desk_c = (c + 1) // 2 
total_desks = desk_a + desk_b + desk_c

print(f"The Number of Desks required for class A is: {desk_a}")
print(f"The Number of Desks required for class B is: {desk_b}")
print(f"The Number of Desks required for class C is: {desk_c}")
print(f"The Total Number of Desks required is: {total_desks}")