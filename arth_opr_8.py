def arithmetic_operation(s):
    for i in s:
        if not i.isdigit():
            op=i
            break
    num1,num2 = s.split(op)
    num1, num2 = float(num1), float(num2)

    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return num1 / num2
    else:
        raise ValueError("Invalid operator. Must be one of (+, -, *, /).")
s=input("enter string")
print(arithmetic_operation(s))
 
