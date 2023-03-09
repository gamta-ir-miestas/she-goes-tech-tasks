number = int(input("Please write an integer:"))
i = 1
print("Here are the factors of " + str(number) + ":")
while number + 1> i:
    if number % i == 0:
        print(i)
    i += 1
    