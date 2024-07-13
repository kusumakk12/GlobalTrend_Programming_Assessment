def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("enter number"))
print(f"The {n}th Fibonacci number is:(not counting o)", fibonacci(n))

def fibonacci1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("enter number"))
print(f"The {n}th Fibonacci number is(o as first number):", fibonacci1(n-1))#fabinacci start from 0 as 1st element.



