def settoset(sets):
    new_set = set([x for x in sets if x % 3 != 0])
    return new_set

#test
set_ex = {1, 5, 55, 15, 6, 18, 21, 26}
print(settoset(set_ex))
