import math

x = eval(input("Enter radius of Circle:\t"))
y = eval(input("Enter angle made by joining both ends of the chord to the center:\t"))

y = math.radians(y)
y = y / 2
l = 2 * x * math.sin(y)
l = round(l,3)

print("The length is ", l ," units or cm")
