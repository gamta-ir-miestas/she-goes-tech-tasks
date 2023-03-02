year = input("Please write a year:")
num_year = int(year)
result = "Leap year: "
end = False
if num_year % 4 == 0:
    if num_year % 400 == 0:
        end = True
        print(result + str(end))
    elif num_year % 100 != 0:
        end = True
        print(result + str(end))
    else:
        print(result + str(end))
else:
    print(result + str(end))
