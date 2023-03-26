def multiplied(list):
    result = 1
    for number in list:
        result *= number
    return result

#test
the_list = [5, 8, 94, 67, 5]
print(multiplied(the_list))