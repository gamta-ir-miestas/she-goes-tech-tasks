def evenlist(list):
    even = [number for number in list if number % 2 == 0]
    return even

#test
the_list = [2, 0, 8, 9, 5, 15, 97, 50364]
even_list = evenlist(the_list)
print(even_list)