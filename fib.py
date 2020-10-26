def fib(b):
    if b == 0:
        return 0
    if b == 1 :
        return 1
    return fib(b-1) + fib(b-1)

b = int(input("Enter a number : "))
print(fib(b))
