def target(list, sum):
    for num1 in range(len(list)):
        for num2 in range(1, len(list)):
            if list[num1] + list[num2] == sum:
                return [list[num1], list[num2]]

#test
the_list = [i for i in range(1, 12)]
result = target(the_list, 25)
print(result)