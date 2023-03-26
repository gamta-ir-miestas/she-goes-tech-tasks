def vowel(string):
    counter = 0
    for char in string:
        if char in "aeiou":
            counter += 1
    return print(counter)
