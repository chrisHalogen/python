def factoria(n):
    x = 1
    for i in range(1,n+1):
        x = x * i
    return x
x = int(input("Enter first nos: "))
y = int(input("Enter second nos: "))

result = factoria(x)/(factoria(x-y)*factoria(y))
print(result)