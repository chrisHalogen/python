numbers = [2,2,3,3,4,44,6,3,1,0,88]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
print(uniques)