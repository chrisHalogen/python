#using recursion
def facrecursive(n):
    if n == 0:
        return 1
    else:
        return n * facrecursive(n - 1)
def main():
    n = eval(input("Enter the number:"))
    print("The factorial of", n ,"using decrement", "=", facrecursive(n))
main()