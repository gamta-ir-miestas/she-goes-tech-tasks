date = input("Please write a date: (YYYY-MM-DD)")
datelist = date.split('-')
if 0 < int(datelist[1]) < 13:
    valid_month = True
else:
    valid_month = False

if int(datelist[1]) in [1, 3, 5, 7, 8, 10, 12]:
    if 0 < int(datelist[2]) < 32:
        valid_day = True
    else:
        valid_day = False
elif int(datelist[1]) == 2:
    if int(datelist[0]) % 4 == 0:
        if int(datelist[0]) % 400 == 0:
            if 0 < int(datelist[2]) < 30:
                valid_day = True
            else:
                valid_day = False
        
        elif int(datelist[0]) % 100 != 0:
            if 0 < int(datelist[2]) < 30:
                valid_day = True
            else:
                valid_day = False
        
    else:
        if 0 < int(datelist[2]) < 29:
            valid_day = True
        else:
            valid_day = False
else:
    if 0 < int(datelist[2]) < 31:
        valid_day = True
    else:
        valid_day = False 

if valid_month == True and valid_day == True:
    print("Date valid: " + str(valid_month))
else:
    print("Date valid: " + str(False))