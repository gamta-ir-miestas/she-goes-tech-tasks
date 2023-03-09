number = int(input("Please write an integer: "))
answer = []

for i in range(1, number + 1):
    if number % i == 0:
        answer.append(i)

if number < 2:
    print("This number is neither prime nor not prime")
elif len(answer) == 2:
    print("This number is prime")
elif len(answer) > 2:
    print("This number is not prime")

# orrr...

#for i in range(1, number + 1):
#    if number % i == 0:
#        answer.append(i)