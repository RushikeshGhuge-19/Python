#calculator program

operator = input("Select one of the following output (+ - * /):  ")
Num1 = float(input("Enter the first number: "))
Num2 = float(input("Enter the second number: "))

if operator == '+':
    result = Num1 + Num2
    print(round(result))
elif operator == '-':
    result = Num1 - Num2
    print(round(result))
elif operator == '*':
    result = Num1 * Num2
    print(round(result))
elif operator == '/':
    result = Num1 / Num2
    print(round(result))
else:
    print(f"{operator} Doesnt exist in calci")