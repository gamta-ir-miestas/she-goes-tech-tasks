text = input("Please write anything: \n")
letter = input("Please write a character that you would like to find: \n")

result = text.count(letter)
print("There are {} occurences of your requested character {} ".format(result, letter))

lst, counts = [], []
for charx in text:
    if charx in lst:
        continue
    else:
        lst.append(charx)
        count = text.count(charx)
        counts.append(count)

for i in range(len(lst)):
    print("There are {} occurences of character {} ".format(counts[i], lst[i]))