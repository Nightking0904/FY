t1 = input("Enter the first timestamp (HH:MM:SS): ").split(":")
t2 = input("Enter the second timestamp (HH:MM:SS): ").split(":")

h1 = int(t1[0])
m1 = int(t1[1])
s1 = int(t1[2])

h2 = int(t2[0])
m2 = int(t2[1])
s2 = int(t2[2])

time1 = (h1*3600) + (m1*60) + (s1)
time2 = (h2*3600) + (m2*60) + (s2)

diff = abs((time1) - (time2))
print(f"The Difference Between the two Time Stamps is {diff}s!")