int1 = input("Please write first number:" )
int2 = input("Please write second number:") 
num1 = float(int1)
num2 = float(int2)

result1 = "Both numbers are even: "
result2 = "At least one number is even: "


if num1 % 2 == 0 and num2 % 2 == 0:
    print(result1 + str(True))
else:
    print(result1 + str(False))

if num1 % 2 == 0 or num2 % 2 == 0:
    print(result2 + str(True))
else:
    print(result2 + str(False))