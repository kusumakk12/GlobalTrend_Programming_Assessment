def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
a = int(input("enter dividend"))
b = int(input("enter divisor"))
print(f"{a} divided by {b} is:", divide_numbers(a, b))
