import math

def fact(a):
    ans = 1
    if a == 0:
        return 1
    else:
        for i in range(1,a+1):
            ans *= i
        return ans

x = eval(input("Enter any Value for X: "))
n = int(input("Enter how many iterations: "))

result = 0

for i in range(0,n+1):
    result += math.e ** x / fact(i)

msg = round(result,4)

print(msg)