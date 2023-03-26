def weirdfunc(list_of_dicts):
    keys = [str(x) for x in range(len(list_of_dicts))]
    values = []
    for dictr in list_of_dicts:
        total = []
        for key in dictr:
            total.append(dictr[key])
        values.append(sum(total))
    result = dict(zip(keys, values))
    return result

#test
random_list = [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}, {"a": 7, "b": 8, "c": 9}]

print(weirdfunc(random_list))