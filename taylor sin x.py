import math

def fact(a):
    ans = 1
    for i in range(1,a+1):
        ans *= i
    return ans

x = eval(input("Enter any angle in degrees: "))
n = int(input("Enter how many iterations: "))

result = 0
x = math.radians(x)

for i in range(1,n+1):
    term = 2 * i - 1
    result += ((-1) ** (i+1)) * (x ** (term))/ fact(term)

print(result)