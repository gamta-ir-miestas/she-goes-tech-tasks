def swaptuple(tuples):
    listt = list(tuples)
    listt[-1], listt[0] = listt[0], listt[-1]
    result = tuple(listt)
    return result

#test
random_tuple = ("abcd", "efg", "hijk", "lmnop", "qrs", "tuv", "wxyz")
print(swaptuple(random_tuple))