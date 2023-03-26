def even_values(dict):
    list_of_keys = []
    for key in dict:
        if dict[key] % 2 == 0:
            list_of_keys.append(key)
    return list_of_keys

#test
keyvalue = {"one": 1, "two": 2, "three": 3, "four" : 4, "twoagain": 2}
result = print(even_values(keyvalue))