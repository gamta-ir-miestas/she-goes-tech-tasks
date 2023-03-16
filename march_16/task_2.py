#this part of code creates a list that contains random strings :)
#the list changes during every run

import numpy as np

choices = [i for i in range(300)] #first 300 characters in unicode should be enough, can change the number for fun
#if the number in choices is higher than 2000, then I recommend to change the character encoding for better compatibility

the_list = np.random.choice(choices, size = (10, 15)).tolist()

#changing from list of lists of numbers to list of strings
for j, word in enumerate(the_list):
    for i, char in enumerate(word):
        word[i] = str(chr(char))
    the_list[j] = ''.join(word)

#changing from list of lists of numbers to list of numbers
#if you uncomment this, comment the string one
# for i, number in enumerate(the_list):
#     total = sum(number) ** 2
#     the_list[i] = total


for i in the_list:
    print(i)
print("\n")

# THE TASK 


#the algorithm basically compares 2 items which is bigger, works just like sort function
#computationally more expensive than sort function

for index in range(len(the_list)):
    min_index = index
    for next_index in range(min_index + 1, len(the_list)):
        if the_list[next_index] < the_list[min_index]:
            min_index = next_index
        else:
            continue
    the_list[index], the_list[min_index] = the_list[min_index], the_list[index]

for i in the_list:
    print(i)