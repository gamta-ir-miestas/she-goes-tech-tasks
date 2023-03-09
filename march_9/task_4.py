while True:
    num1, operator, num2 = input("Ask computer to do some aritmetics, like 2 + 2: ").split(' ')
    nu1 = int(num1) 
    nu2 = int(num2)
    if operator == '+':
        print(nu1 + nu2)
        break
    elif operator == '-':
        print(nu1 - nu2)
        break
    elif operator == '*':
        print(nu1 * nu2)
        break
    elif operator == '/':
        print(nu1 / nu2)
        break
    elif operator == '%':
        print(nu1 % nu2)
        break
    else:
        print("Operation provided isn't valid, please,try again")
