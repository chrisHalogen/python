def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
x = eval(input("Enter a number: "))

print(fact(x))