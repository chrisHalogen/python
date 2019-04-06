import math

x = eval(input("Enter radius of Circle:\t"))
y = eval(input("Enter angle made by joining both ends of the chord to the center:\t"))

area = y * math.pi * x * x / 360
area = round(area,3)

print("The length is ", area ," units or cm")
