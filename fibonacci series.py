#The fibonacci series

x = int(input("Enter first number of the sequence:\t"))
y = int(input("Enter Second number of the sequence:\t"))
z = int(input("Enter how many terms should be printed:\t"))

q = z-2

print("Having first and second term of ", x," and ",y," respectively, The next ", q, " terms of the fibonacci series are")

for n in range(1,z-1):
    p = x + y
    print(p)
    x = y
    y = p

    


