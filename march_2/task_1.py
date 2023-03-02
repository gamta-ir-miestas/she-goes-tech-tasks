age = input("Please write your age:")
license = input("Do you have a driver's licence? (Yes or No)")
if int(age) >= 18 and license == "Yes":
    print("You are able to drive")
else:
    print("You are not able to drive")

#Yes, I know I can write print("You are able to drive: " + str(bool))