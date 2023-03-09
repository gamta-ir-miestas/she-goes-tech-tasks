for number in range(1, 101):
    word = ''
    if number % 3 == 0:
        word += 'Fizz'
    if number % 5 == 0:
        word += 'Buzz'
    elif number % 3 != 0 and number % 5 != 0:
        word += str(number)
    print(word)