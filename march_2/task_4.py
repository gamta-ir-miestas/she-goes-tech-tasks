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


# or... as mentioned in a lesson

year2 = int(input("Please write a year:"))
leapyear = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
print("Leap year: ", leapyear)