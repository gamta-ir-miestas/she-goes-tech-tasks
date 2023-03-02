#If password has to be at least 8 characters long
password = input("Please type your password:")
if len(password) >= 8:
    result = True
    print("Password accepted: " + str(result))
else:
    result = False
    print("Password accepted: " + str(result))

#If password has to be at least 8 characters long, contains
#uppercase, lowercase, digits and special characters

password2 = input("Please type your password:")
if len(password2) >= 8:
    result1 = True
else:
    result1 = False

digit, uppercase, lowercase, specialchar = False, False, False, False
for char in password2:
    if char.isdigit() == True:
        digit = True
    elif char.isupper() == True:
        uppercase = True
    elif char.islower() == True:
        lowercase = True
    else:
        specialchar = True


if result1 and digit and uppercase and lowercase and specialchar == True:
    print("Password accepted: " + str(True))
else:
    print("Password accepted: " + str(False))